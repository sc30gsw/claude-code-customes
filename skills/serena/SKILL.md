---
name: serena
description: Token-efficient Serena MCP command for structured app development and problem-solving
---

# Serena: Intelligent App Development

Token-efficient Serena MCP command for structured app development and problem-solving.

## Quick Reference

```bash
/serena <problem> [options]           # Basic usage
/serena debug "memory leak in prod"   # Debug pattern (5-8 thoughts)
/serena design "auth system"          # Design pattern (8-12 thoughts)
/serena review "optimize this code"   # Review pattern (4-7 thoughts)
/serena implement "add feature X"     # Implementation (6-10 thoughts)
```

## Options

| Option | Description | Example |
|--------|-------------|---------|
| `-q` | Quick mode (3-5 thoughts) | `/serena "fix button" -q` |
| `-d` | Deep mode (10-15 thoughts) | `/serena "architecture design" -d` |
| `-c` | Code-focused analysis | `/serena "optimize performance" -c` |
| `-s` | Step-by-step implementation | `/serena "build dashboard" -s` |
| `-v` | Verbose output | `/serena "debug issue" -v` |
| `-r` | Include research phase | `/serena "choose framework" -r` |
| `-t` | Create implementation todos | `/serena "new feature" -t` |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ tools as the primary development engine:**

### Primary Development Tools (Serena MCP)
- **Project Analysis**: Use `mcp__serena__get_symbols_overview`
- **Code Search**: Use `mcp__serena__search_for_pattern`
- **Symbol Management**: Use `mcp__serena__find_symbol`
- **Code Modification**: Use `mcp__serena__replace_symbol_body`

### Memory & Learning
- **Knowledge Storage**: Use `mcp__serena__write_memory`
- **Experience Retrieval**: Use `mcp__serena__read_memory`
- **Progress Tracking**: Use `mcp__serena__think_about_task_adherence`

## Problem-Specific Templates

### Debug Pattern (5-8 thoughts)
1. Symptom analysis & reproduction
2. Error context & environment check
3. Root cause hypothesis generation
4. Evidence gathering & validation
5. Solution design & risk assessment

### Design Pattern (8-12 thoughts)
1. Requirements clarification
2. Constraints & assumptions
3. Architecture options generation
4. Option evaluation (pros/cons)
5. Technology selection
6. Implementation phases

### Implementation Pattern (6-10 thoughts)
1. Feature specification & scope
2. Technical approach selection
3. Component/module design
4. Dependencies & integration
5. Testing strategy

## Cross-Command Integration

Serena MCP integrates with other commands:

| Command | Integration |
|---------|-------------|
| `/commit` | Git history + change analysis |
| `/debug-error` | Symbol tracking + pattern search |
| `/smart-think` | Codebase context + memory |

## Best Practices

1. Start with problem analysis, end with concrete actions
2. Balance depth with token efficiency
3. Use `-q` for simple problems (saves ~40% tokens)
4. Use `--focus` to avoid irrelevant analysis
