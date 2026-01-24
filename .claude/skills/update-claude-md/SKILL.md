---
name: update-claude-md
description: Intelligent command for automatically generating and updating project-specific CLAUDE.md (Serena + Sequential Thinking integration)
---

# Update CLAUDE.md

Automatically generate and update project-specific CLAUDE.md with intelligent analysis.

## Quick Reference

```bash
/update-claude-md                    # Basic update with auto-detection
/update-claude-md --auto --backup    # Auto-detection + backup
/update-claude-md --files README.md COMMANDS.md  # Specific files
/update-claude-md --preview          # Preview only
/update-claude-md --template kiro    # Use Kiro template
```

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--files` | `-f` | Specify files | Auto-detect |
| `--auto` | `-a` | Auto-detect MD files | true |
| `--backup` | `-b` | Backup existing CLAUDE.md | false |
| `--preview` | `-p` | Show preview before update | false |
| `--include-docs` | `-d` | Include docs directory | false |
| `--structure` | `-s` | Analyze project structure | false |
| `--template` | `-t` | Specify template | auto |
| `--merge` | `-m` | Merge with existing content | false |
| `--output` | `-o` | Output filename | CLAUDE.md |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ for codebase analysis and mcp__sequential-thinking__ for complex reasoning:**

### Primary Analysis Engine (Serena MCP)
- **Project Structure**: Use `mcp__serena__list_dir`
- **File Discovery**: Use `mcp__serena__find_file`
- **Content Analysis**: Use `mcp__serena__search_for_pattern`
- **Memory Integration**: Use `mcp__serena__write_memory` / `read_memory`

### Strategic Thinking Engine (Sequential Thinking MCP)
- Use `mcp__sequential-thinking__sequentialthinking` for CLAUDE.md structure planning
- Integration strategy for merging document sources

## Available Templates

### Kiro Template (`--template kiro`)
- Steering vs Specification explanation
- Phase-based workflow
- Kiro command integration

### Standard Template (`--template standard`)
- Project overview and context
- Development guidelines
- Available commands and agents

### Minimal Template (`--template minimal`)
- Basic project information only
- Minimal framework references

## Workflow

1. **Project Analysis**: Serena MCP analyzes project structure
2. **Content Integration**: Sequential Thinking plans merge strategy
3. **CLAUDE.md Generation**: Framework integration + project context
4. **Quality Assurance**: Validation of generated content

## Generated Structure

```markdown
# What I want you to do
[User-specific instructions]

# Framework Components
@FLAGS.md
@PRINCIPLES.md
@RULES.md

# MCP Documentation
@MCP_Context7.md
@MCP_Playwright.md
@MCP_Sequential.md
@MCP_Serena.md

# [Project Name]
[Auto-generated project description]

## Project Context
[Auto-detected sections]

## Development Guidelines
[Project-specific guidelines]
```

## Success Metrics

- ✅ Complete framework integration
- ✅ Accurate project-specific information
- ✅ Information integration from existing documents
- ✅ Adaptability to future updates
