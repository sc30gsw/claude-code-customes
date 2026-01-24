---
name: git-commit
description: Advanced git commit automation with Serena MCP integration for intelligent change analysis and context-aware commit message generation
---

# Git Commit: Intelligent Git Automation

Advanced git commit automation with Serena MCP for intelligent change analysis, git history learning, and context-aware commit message generation.

## Usage

```bash
/git:commit [options]
```

## Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--no-verify` | | Skip pre-commit checks | `/git:commit --no-verify` |
| `--analyze` | `-a` | Enable deep Serena analysis | `/git:commit -a` |
| `--learning` | `-l` | Learn from git history patterns | `/git:commit -l` |
| `--scope` | `-s` | Set commit scope | `/git:commit -s feature` |
| `--batch` | `-b` | Group multiple related changes | `/git:commit -b` |
| `--interactive` | `-i` | Interactive message refinement | `/git:commit -i` |
| `--template` | `-t` | Use specific commit template | `/git:commit -t refactor` |
| `--dry-run` | `-d` | Show what would be committed | `/git:commit -d` |
| `--impact-analysis` | | Analyze potential change impact | `/git:commit --impact-analysis` |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ tools for code analysis:**

### Code Analysis (Serena MCP First)
- **Change Analysis**: Use `mcp__serena__search_for_pattern` to analyze git diff
- **Symbol Understanding**: Use `mcp__serena__get_symbols_overview` for code context
- **Pattern Recognition**: Use `mcp__serena__find_referencing_symbols` for impact

### Memory & Learning
- **Pattern Storage**: Use `mcp__serena__write_memory` to store commit patterns
- **History Learning**: Use `mcp__serena__read_memory` for previous commit styles

## Workflow

1. **Pre-commit Analysis**: Analyze changes with Serena pattern recognition
2. **Quality Checks**: Run pre-commit hooks (lint, build) unless `--no-verify`
3. **Staging Management**: Auto-stage all changes if none staged
4. **Change Analysis**: Perform git diff analysis
5. **Message Generation**: Generate conventional commit with emoji
6. **Commit Execution**: Execute git commit

## Conventional Commit Format

```
<type>: <description>

<optional body>
```

### Types with Emojis

| Type | Emoji | Description |
|------|-------|-------------|
| `feat` | ✨ | New feature |
| `fix` | 🐛 | Bug fix |
| `docs` | 📝 | Documentation |
| `style` | 💄 | Formatting/style |
| `refactor` | ♻️ | Code refactoring |
| `perf` | ⚡️ | Performance |
| `test` | ✅ | Tests |
| `chore` | 🔧 | Tooling, config |
| `ci` | 🚀 | CI/CD |
| `revert` | 🗑️ | Revert changes |

## Examples

```bash
# Basic feature development
/git:commit --scope=feature --learning

# Bug fix with impact analysis
/git:commit --scope=fix --impact-analysis --analyze

# Refactoring with batch commits
/git:commit --template=refactor --batch

# Quick hotfix
/git:commit --scope=fix --no-verify
```

## Guidelines for Splitting Commits

1. **Different concerns**: Changes to unrelated parts
2. **Different types**: Mixing features, fixes, refactoring
3. **File patterns**: Different types of files
4. **Logical grouping**: Easier to understand separately
5. **Size**: Very large changes broken down
