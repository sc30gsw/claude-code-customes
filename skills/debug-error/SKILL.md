---
name: debug-error
description: Advanced debugging system with Serena MCP integration for intelligent codebase analysis and error resolution
---

# Debug Error

Systematic debugging with Serena MCP for smart codebase analysis and efficient error resolution.

## Usage

```bash
/debug-error "<error_description>" [options]
```

## Options

| Option | Description | Example |
|--------|-------------|---------|
| `--analyze`, `-a` | Enable deep Serena analysis | `/debug-error "crash" -a` |
| `--trace`, `-t` | Code flow tracing | `/debug-error "logic error" -t` |
| `--serena-deep`, `-s` | Full Serena toolkit usage | `/debug-error "complex bug" -s` |
| `--pattern-search`, `-p` | Find similar error patterns | `/debug-error "timeout" -p` |
| `--memory`, `-m` | Use debugging memory | `/debug-error "recurring issue" -m` |
| `--interactive`, `-i` | Step-by-step guidance | `/debug-error "unknown issue" -i` |
| `--implement` | Implement fix automatically | `/debug-error "known solution" --implement` |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ tools when available:**

### Error Analysis (Serena MCP First)
- **Pattern Search**: Use `mcp__serena__search_for_pattern` to find error patterns
- **Symbol Analysis**: Use `mcp__serena__find_symbol` for error location context
- **Reference Tracking**: Use `mcp__serena__find_referencing_symbols` to trace propagation

### Memory & Learning
- **Previous Solutions**: Use `mcp__serena__read_memory` to recall similar sessions
- **Pattern Storage**: Use `mcp__serena__write_memory` to store approaches

## Workflow

1. **Error Information Gathering**
   - Collect error message, stack trace, and error code
   - Note timing, location, and frequency
   - Use `mcp__serena__search_for_pattern` to find related patterns

2. **Reproduce the Error**
   - Create minimal test case
   - Document exact steps

3. **Stack Trace Analysis**
   - Read from bottom to top
   - Identify exact failing line
   - Trace execution path

4. **Code Context Investigation**
   - Use `mcp__serena__find_symbol` for location context
   - Use `mcp__serena__find_referencing_symbols` for dependencies
   - Check git history and recent modifications

5. **Hypothesis Formation**
   - Consider common causes: null references, type mismatches, race conditions

6. **Systematic Investigation**
   - Use Serena for intelligent testing
   - Use `mcp__serena__insert_after_symbol` for targeted logging

7. **Solution Implementation**
   - Use `mcp__serena__replace_symbol_body` for targeted fixes
   - Add comprehensive error handling

8. **Testing and Prevention**
   - Test fix against original error
   - Add unit and integration tests
   - Improve error handling and logging

## Best Practices

1. **Start with Pattern Search**: Always check for similar issues first
2. **Use Memory**: Leverage past debugging sessions
3. **Trace Dependencies**: Understand error propagation
4. **Document Solutions**: Store successful approaches for future reference
