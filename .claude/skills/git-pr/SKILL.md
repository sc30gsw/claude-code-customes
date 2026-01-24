---
name: git-pr
description: Generate PR description and automatically create pull request on GitHub
---

# Git PR: Pull Request Automation

Generate PR descriptions and automatically create pull requests on GitHub with Serena MCP integration.

## Usage

```bash
/git:pr [options]
```

## Options

| Option | Description | Example |
|--------|-------------|---------|
| (default) | Generate PR description and create PR | `/git:pr` |
| `-p` | Push current branch and create PR | `/git:pr -p` |
| `-u` | Update existing PR description only | `/git:pr -u` |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ tools for code analysis:**

### File Operations (Serena MCP First)
- **Reading files**: Use `mcp__serena__find_file` → `Bash(git:*)` (fallback)
- **Searching patterns**: Use `mcp__serena__search_for_pattern`
- **Finding symbols**: Use `mcp__serena__find_symbol`

### Code Analysis (Serena MCP)
- **Symbol overview**: Use `mcp__serena__get_symbols_overview`
- **Symbol references**: Use `mcp__serena__find_referencing_symbols`

## Workflow

### Default (no option)
1. Analyze changes with Serena pattern recognition
2. Read PR template from `.github/pull_request_template.md`
3. Create PR description following template format
4. Use Context7 MCP to fetch relevant documentation URLs
5. Add Mermaid diagram visualizing changes
6. Execute `gh pr create --draft`

### With -p option
1. Push current branch: `git push -u origin <current-branch>`
2. Continue with default workflow

### With -u option
1. Analyze changes
2. Read previous PR patterns from Serena memory
3. Update existing PR: `gh pr edit --body <description>`

## Requirements

1. Follow the template structure exactly
2. Use Japanese for all content
3. Include specific implementation details
4. List concrete testing steps
5. Use Context7 MCP for documentation URLs
6. Always include Mermaid diagram

## Mermaid Diagram Guidelines

- Use appropriate diagram types (flowchart, sequence, class)
- Show before/after states if applicable
- Highlight new or modified components
- Use consistent styling and colors

## Context7 Integration

For Reference section, query Context7 MCP for:
- Next.js, React, TanStack Query documentation
- Tailwind CSS, UI library documentation
- Other relevant technologies based on changes
