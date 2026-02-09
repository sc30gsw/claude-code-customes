#!/usr/bin/env python3
"""
Discover all available skills and agents across all scopes.

Scans project, user, global (.agents), plugin marketplaces, and plugin cache
directories to build a complete catalog of available resources.

Usage:
    discover_resources.py [--format json|table] [--scope project|user|global|plugin|all]

Output:
    JSON catalog of agents and skills with scope metadata.
"""

import json
import os
import re
import sys
from pathlib import Path


def get_cwd():
    """Get the current working directory."""
    return Path.cwd()


def get_home():
    """Get the user's home directory."""
    return Path.home()


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file.

    Returns a dict with name, description, tools, model fields if found.
    """
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeDecodeError):
        return None

    if not content.startswith("---"):
        return None

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    frontmatter = match.group(1)
    result = {}

    for field in ("name", "description", "tools", "model"):
        field_match = re.search(rf"^{field}:\s*(.+)$", frontmatter, re.MULTILINE)
        if field_match:
            value = field_match.group(1).strip()
            if field == "tools":
                result[field] = [t.strip() for t in value.split(",")]
            else:
                result[field] = value

    return result if result.get("name") else None


def resolve_path(path):
    """Resolve a path, following symlinks to get the canonical path."""
    try:
        return path.resolve()
    except OSError:
        return path


def scan_agents(base_path, scope):
    """Scan for agent definitions in a directory.

    Looks for *.md files directly in base_path and in sc/ subdirectory.
    """
    agents = []
    seen_resolved = set()

    for search_dir in [base_path, base_path / "sc"]:
        if not search_dir.is_dir():
            continue
        for md_file in sorted(search_dir.glob("*.md")):
            resolved = resolve_path(md_file)
            if resolved in seen_resolved:
                continue
            seen_resolved.add(resolved)

            data = parse_frontmatter(md_file)
            if data:
                entry = {
                    "name": data["name"],
                    "description": data.get("description", ""),
                    "scope": scope,
                }
                if "tools" in data:
                    entry["tools"] = data["tools"]
                if "model" in data:
                    entry["model"] = data["model"]
                agents.append(entry)

    return agents


def scan_skills(base_path, scope):
    """Scan for skill definitions in a directory.

    Looks for */SKILL.md pattern.
    """
    skills = []
    seen_resolved = set()

    if not base_path.is_dir():
        return skills

    for skill_dir in sorted(base_path.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        resolved = resolve_path(skill_md)
        if resolved in seen_resolved:
            continue
        seen_resolved.add(resolved)

        data = parse_frontmatter(skill_md)
        if data:
            skills.append({
                "name": data["name"],
                "description": data.get("description", ""),
                "scope": scope,
            })

    return skills


def scan_plugin_skills(base_path, scope):
    """Scan for skills in plugin directories (recursive).

    Looks for **/skills/*/SKILL.md or **/SKILL.md patterns.
    """
    skills = []
    seen_resolved = set()

    if not base_path.is_dir():
        return skills

    for skill_md in sorted(base_path.rglob("SKILL.md")):
        resolved = resolve_path(skill_md)
        if resolved in seen_resolved:
            continue
        seen_resolved.add(resolved)

        data = parse_frontmatter(skill_md)
        if data:
            skills.append({
                "name": data["name"],
                "description": data.get("description", ""),
                "scope": scope,
            })

    return skills


def discover_all(scope_filter="all"):
    """Discover all agents and skills across all scopes.

    Args:
        scope_filter: One of 'project', 'user', 'global', 'plugin', 'all'

    Returns:
        Dict with 'agents' and 'skills' lists.
    """
    cwd = get_cwd()
    home = get_home()

    all_agents = []
    all_skills = []
    seen_agent_names = set()
    seen_skill_names = set()

    # Scope definitions: (scope_name, agents_paths, skills_paths)
    scopes = []

    if scope_filter in ("all", "project"):
        scopes.append((
            "project",
            [cwd / ".claude" / "agents"],
            [cwd / ".claude" / "skills"],
        ))

    if scope_filter in ("all", "user"):
        scopes.append((
            "user",
            [home / ".claude" / "agents"],
            [home / ".claude" / "skills"],
        ))

    if scope_filter in ("all", "global"):
        scopes.append((
            "global",
            [],
            [home / ".agents" / "skills"],
        ))

    # Agents: scan in priority order, dedup by name
    for scope_name, agent_paths, _ in scopes:
        for agent_path in agent_paths:
            for agent in scan_agents(agent_path, scope_name):
                if agent["name"] not in seen_agent_names:
                    seen_agent_names.add(agent["name"])
                    all_agents.append(agent)

    # Skills: scan in priority order, dedup by name
    for scope_name, _, skill_paths in scopes:
        for skill_path in skill_paths:
            for skill in scan_skills(skill_path, scope_name):
                if skill["name"] not in seen_skill_names:
                    seen_skill_names.add(skill["name"])
                    all_skills.append(skill)

    # Plugin scopes
    if scope_filter in ("all", "plugin"):
        plugin_dirs = [
            home / ".claude" / "plugins" / "marketplaces",
            home / ".claude" / "plugins" / "cache",
        ]
        for plugin_dir in plugin_dirs:
            for skill in scan_plugin_skills(plugin_dir, "plugin"):
                if skill["name"] not in seen_skill_names:
                    seen_skill_names.add(skill["name"])
                    all_skills.append(skill)

    return {"agents": all_agents, "skills": all_skills}


def format_table(catalog):
    """Format catalog as a readable table."""
    lines = []

    if catalog["agents"]:
        lines.append("=== AGENTS ===")
        lines.append(f"{'Name':<25} {'Scope':<10} {'Model':<8} Description")
        lines.append("-" * 80)
        for agent in catalog["agents"]:
            name = agent["name"][:24]
            scope = agent["scope"][:9]
            model = agent.get("model", "-")[:7]
            desc = agent.get("description", "")[:60]
            lines.append(f"{name:<25} {scope:<10} {model:<8} {desc}")

    lines.append("")

    if catalog["skills"]:
        lines.append("=== SKILLS ===")
        lines.append(f"{'Name':<25} {'Scope':<10} Description")
        lines.append("-" * 80)
        for skill in catalog["skills"]:
            name = skill["name"][:24]
            scope = skill["scope"][:9]
            desc = skill.get("description", "")[:60]
            lines.append(f"{name:<25} {scope:<10} {desc}")

    lines.append("")
    lines.append(f"Total: {len(catalog['agents'])} agents, {len(catalog['skills'])} skills")

    return "\n".join(lines)


def main():
    output_format = "json"
    scope_filter = "all"

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--format" and i + 1 < len(args):
            output_format = args[i + 1]
            i += 2
        elif args[i] == "--scope" and i + 1 < len(args):
            scope_filter = args[i + 1]
            i += 2
        else:
            print(f"Unknown argument: {args[i]}", file=sys.stderr)
            print("Usage: discover_resources.py [--format json|table] [--scope project|user|global|plugin|all]", file=sys.stderr)
            sys.exit(1)

    if output_format not in ("json", "table"):
        print(f"Invalid format: {output_format}. Use 'json' or 'table'.", file=sys.stderr)
        sys.exit(1)

    if scope_filter not in ("project", "user", "global", "plugin", "all"):
        print(f"Invalid scope: {scope_filter}. Use 'project', 'user', 'global', 'plugin', or 'all'.", file=sys.stderr)
        sys.exit(1)

    catalog = discover_all(scope_filter)

    if output_format == "json":
        print(json.dumps(catalog, indent=2, ensure_ascii=False))
    else:
        print(format_table(catalog))


if __name__ == "__main__":
    main()
