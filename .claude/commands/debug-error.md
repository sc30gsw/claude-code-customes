---
allowed-tools: Read, Write, Bash, Grep, Glob, mcp__serena__search_for_pattern, mcp__serena__find_symbol, mcp__serena__find_referencing_symbols, mcp__serena__read_memory, mcp__serena__write_memory
description: Advanced debugging system with Serena MCP integration for intelligent codebase analysis and error resolution
---

## Context

- Current error status: !`grep -r "ERROR\|error" . --include="*.log" | head -5 2>/dev/null || echo "No error logs found"`
- Recent failures: !`git log --oneline --grep="fix\|bug" -5 2>/dev/null || echo "No recent fixes"`
- Test failures: !`npm test 2>/dev/null | grep -i "fail\|error" | head -3 || echo "No test output"`
- System errors: !`dmesg | tail -3 2>/dev/null || echo "No system errors"`
- Project type: @package.json
- Debug configuration: !`ls -la .vscode/launch.json tsconfig.json webpack.config.* 2>/dev/null || echo "No debug config"`

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools when available:**

### Error Analysis (Serena MCP First)
- **Pattern Search**: Use `mcp__serena__search_for_pattern` to find error patterns and similar issues
- **Symbol Analysis**: Use `mcp__serena__find_symbol` to understand error location context
- **Reference Tracking**: Use `mcp__serena__find_referencing_symbols` to trace error propagation
- **Code Overview**: Use `mcp__serena__get_symbols_overview` for architectural understanding

### Memory & Learning (Serena MCP Only)
- **Previous Solutions**: Use `mcp__serena__read_memory` to recall similar debugging sessions
- **Pattern Storage**: Use `mcp__serena__write_memory` to store successful debugging approaches
- **Information Analysis**: Use `mcp__serena__think_about_collected_information` to categorize findings
- **Progress Tracking**: Use `mcp__serena__think_about_task_adherence` for debugging quality

### Code Modification (Serena MCP First)
- **Targeted Fixes**: Use `mcp__serena__replace_symbol_body` for precise code fixes
- **Pattern Replacement**: Use `mcp__serena__replace_regex` for systematic fixes
- **Strategic Insertion**: Use `mcp__serena__insert_before_symbol` / `mcp__serena__insert_after_symbol` for logging

### Fallback Tools (Standard)
- **File Operations**: Use Read, Glob, Grep when Serena tools unavailable
- **Build & Test**: Use Bash for running tests, builds, and debugging commands
- **Documentation**: Use Write, Edit for creating debug documentation

# Intelligent Debug and Fix Errors

Systematic debugging with Serena MCP for smart codebase analysis and efficient error resolution

## Usage Guide

### Basic Syntax
```bash
/debug-error "<error_description>" [options]
```

### Available Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--analyze` | `-a` | Enable deep Serena analysis | `/debug-error "crash" -a` |
| `--trace` | `-t` | Code flow tracing | `/debug-error "logic error" -t` |
| `--serena-deep` | `-s` | Full Serena toolkit usage | `/debug-error "complex bug" -s` |
| `--pattern-search` | `-p` | Find similar error patterns | `/debug-error "timeout" -p` |
| `--memory` | `-m` | Use debugging memory | `/debug-error "recurring issue" -m` |
| `--interactive` | `-i` | Step-by-step guidance | `/debug-error "unknown issue" -i` |
| `--impact` | | Analyze fix impact | `/debug-error "critical bug" --impact` |
| `--quick` | `-q` | Fast error assessment | `/debug-error "simple bug" -q` |
| `--implement` | | Implement fix automatically | `/debug-error "known solution" --implement` |
| `--document` | `-d` | Document debugging process | `/debug-error "complex issue" -d` |
| `--memory-store` | | Store solution for future | `/debug-error "solved issue" --memory-store` |

### Quick Examples

```bash
# Basic debugging with pattern search
/debug-error "NullPointerException in UserService" --pattern-search

# Deep analysis with Serena
/debug-error "performance degradation" --analyze --serena-deep

# Code flow tracing
/debug-error "auth flow broken" --trace --memory

# Interactive debugging for complex issues
/debug-error "mysterious crash" --interactive --step-by-step

# Quick triage for simple bugs
/debug-error "typo in function" --quick --implement
```

## Workflow Process

Follow this enhanced debugging methodology with Serena MCP integration to resolve: **$ARGUMENTS**

1. **Error Information Gathering** (Enhanced with Serena)
   - **Complete Error Context**: Collect error message, stack trace, and error code
   - **Timing Analysis**: Note when, where, and how frequently the error occurs
   - **Environment Context**: Identify environment (dev, staging, prod) and configuration
   - **Log Analysis**: Gather relevant logs with Serena pattern recognition
   - **🔧 Serena Integration**: Use `mcp__serena__search_for_pattern` to find related error patterns
   - **Semantic Search**: Find similar error patterns across the codebase

2. **Reproduce the Error**
   - Create a minimal test case that reproduces the error consistently
   - Document the exact steps needed to trigger the error
   - Test in different environments if possible
   - Note any patterns or conditions that affect error occurrence

3. **Stack Trace Analysis**
   - Read the stack trace from bottom to top to understand the call chain
   - Identify the exact line where the error originates
   - Trace the execution path leading to the error
   - Look for any obvious issues in the failing code

4. **Code Context Investigation** (Serena-Enhanced)
   - **🔧 Symbol Analysis**: Use `mcp__serena__find_symbol` to understand error location context
   - **🔧 Reference Mapping**: Use `mcp__serena__find_referencing_symbols` to trace dependencies
   - **🔧 Code Overview**: Use `mcp__serena__get_symbols_overview` for architectural understanding
   - **Recent Changes**: Check git history and recent modifications
   - **State Analysis**: Review variable values and function parameters
   - **🔧 Pattern Search**: Use `mcp__serena__search_for_pattern` for similar code patterns

5. **Hypothesis Formation**
   - Based on evidence, form hypotheses about the root cause
   - Consider common causes:
     - Null pointer/undefined reference
     - Type mismatches
     - Race conditions
     - Resource exhaustion
     - Logic errors
     - External dependency failures

6. **Debugging Tools Setup**
   - Set up appropriate debugging tools for the technology stack
   - Use debugger, profiler, or logging as needed
   - Configure breakpoints at strategic locations
   - Set up monitoring and alerting if not already present

7. **Systematic Investigation** (Serena-Powered)
   - **🔧 Intelligent Testing**: Use Serena to identify key test points
   - **🔧 Symbol Tracking**: Use `mcp__serena__find_referencing_symbols` for data flow analysis
   - **Binary Search**: Isolate problems with Serena-guided code navigation
   - **🔧 Strategic Instrumentation**: Use `mcp__serena__insert_after_symbol` for targeted logging
   - **🔧 Memory Analysis**: Use `mcp__serena__read_memory` to recall similar issues
   - **Data Flow Tracing**: Step-by-step transformation analysis with semantic understanding

8. **Data Validation**
   - Verify input data format and validity
   - Check for edge cases and boundary conditions
   - Validate assumptions about data state
   - Test with different data sets to isolate patterns

9. **Dependency Analysis**
   - Check external dependencies and their versions
   - Verify network connectivity and API availability
   - Review configuration files and environment variables
   - Test database connections and query execution

10. **Memory and Resource Analysis**
    - Check for memory leaks or excessive memory usage
    - Monitor CPU and I/O resource consumption
    - Analyze garbage collection patterns if applicable
    - Check for resource deadlocks or contention

11. **Concurrency Issues Investigation**
    - Look for race conditions in multi-threaded code
    - Check synchronization mechanisms and locks
    - Analyze async operations and promise handling
    - Test under different load conditions

12. **Root Cause Identification**
    - Once the cause is identified, understand why it happened
    - Determine if it's a logic error, design flaw, or external issue
    - Assess the scope and impact of the problem
    - Consider if similar issues exist elsewhere

13. **Solution Implementation** (Serena-Assisted)
    - **🔧 Root Cause Targeting**: Use Serena analysis to design precise fixes
    - **Solution Alternatives**: Generate multiple approaches with trade-off analysis
    - **🔧 Intelligent Implementation**: Use `mcp__serena__replace_symbol_body` for targeted fixes
    - **🔧 Context-Aware Insertion**: Use `mcp__serena__insert_before_symbol` for validation
    - **Error Handling**: Add comprehensive error handling with pattern recognition
    - **🔧 Impact Analysis**: Use Serena to assess fix impact across codebase

14. **Testing the Fix**
    - Test the fix against the original error case
    - Test edge cases and related scenarios
    - Run regression tests to ensure no new issues
    - Test under various load and stress conditions

15. **Prevention Measures**
    - Add appropriate unit and integration tests
    - Improve error handling and logging
    - Add input validation and defensive checks
    - Update documentation and code comments

16. **Monitoring and Alerting**
    - Set up monitoring for similar issues
    - Add metrics and health checks
    - Configure alerts for error thresholds
    - Implement better observability

17. **Documentation**
    - Document the error, investigation process, and solution
    - Update troubleshooting guides
    - Share learnings with the team
    - Update code comments with context

18. **Post-Resolution Review**
    - Analyze why the error wasn't caught earlier
    - Review development and testing processes
    - Consider improvements to prevent similar issues
    - Update coding standards or guidelines if needed

## Serena MCP Integration Features

### Intelligent Code Analysis
- **Symbol-Level Understanding**: Deep analysis of functions, classes, and dependencies
- **Pattern Recognition**: Identifies similar bugs and solutions across the codebase
- **Context Mapping**: Understands code relationships and potential impact areas
- **Memory Integration**: Remembers previous debugging sessions and solutions

### Advanced Debugging Capabilities
- **Semantic Search**: Find related code patterns and potential bug sources
- **Reference Tracing**: Track how errors propagate through the codebase
- **Intelligent Instrumentation**: Add targeted logging and debugging code
- **Solution Templates**: Learn from past fixes and apply similar patterns

## Enhanced Debugging Options

```bash
# Basic debugging with Serena
/debug-error "NullPointerException in UserService"

# Deep analysis mode
/debug-error "performance degradation" --analyze --serena-deep

# Code flow tracing
/debug-error "auth flow broken" --trace --memory

# Pattern-based debugging
/debug-error "memory leak" --pattern-search --similar-issues

# Interactive debugging
/debug-error "complex bug" --interactive --step-by-step
```

## Advanced Options

| Option | Description | Use Case |
|--------|-------------|-----------|
| `--analyze` | Deep Serena analysis | Complex issues |
| `--trace` | Code flow tracing | Logic errors |
| `--serena-deep` | Full Serena toolkit | Unknown issues |
| `--pattern-search` | Find similar patterns | Recurring bugs |
| `--memory` | Use debugging memory | Learning from past |
| `--interactive` | Step-by-step guidance | Complex debugging |
| `--impact` | Analyze fix impact | Critical systems |

## Workflow Integration

### 1. Quick Triage
```bash
# Fast error assessment
/debug-error "error message" --quick --pattern-search
```

### 2. Deep Investigation
```bash
# Comprehensive analysis
/debug-error "complex issue" --serena-deep --trace --memory
```

### 3. Solution Development
```bash
# Intelligent fix implementation
/debug-error "root cause identified" --implement --impact
```

### 4. Learning Integration
```bash
# Remember solution for future
/debug-error "solved issue" --document --memory-store
```

## Serena MCP Integration Features

### Intelligent Error Analysis
- **Pattern Recognition**: Automatically identifies similar error patterns across codebase
- **Symbol-Level Tracking**: Understands functions, classes, and dependencies involved in errors
- **Context Mapping**: Maps error context to broader system architecture
- **Memory Integration**: Learns from previous debugging sessions and solutions

### Advanced Debugging Capabilities
- **Semantic Search**: Finds related code patterns and potential error sources
- **Reference Tracing**: Tracks how errors propagate through the codebase
- **Intelligent Instrumentation**: Adds targeted logging and debugging code
- **Solution Templates**: Applies learned patterns from past successful fixes

### Code Repair Intelligence
- **Precision Targeting**: Makes exact fixes without affecting surrounding code
- **Impact Assessment**: Understands broader implications of proposed fixes
- **Pattern-Based Solutions**: Applies proven solutions to similar problems
- **Regression Prevention**: Considers potential side effects of fixes

## Requirements

### Prerequisites
- Codebase with clear error symptoms or stack traces
- Serena MCP integration available
- Optional: Test suite for validation
- Optional: Logging and monitoring tools

### Dependencies
- **Serena MCP**: For intelligent code analysis and pattern recognition
- **Build Tools**: For testing fixes and validation
- **Version Control**: For tracking changes and rollback capability
- **Debug Tools** (optional): For runtime analysis and profiling

## Best Practices with Serena

1. **Start with Pattern Search**: Always check for similar issues first using `mcp__serena__search_for_pattern`
2. **Use Memory**: Leverage past debugging sessions with `mcp__serena__read_memory`
3. **Trace Dependencies**: Use `mcp__serena__find_referencing_symbols` to understand error propagation
4. **Document Solutions**: Store successful approaches with `mcp__serena__write_memory`
5. **Impact Analysis**: Always assess broader impact before implementing fixes
6. **Progressive Debugging**: Start simple, then use deeper Serena analysis for complex issues

## Usage Examples

### Quick Debugging Scenarios

```bash
# Simple error with known patterns
/debug-error "TypeError: Cannot read property" --pattern-search --quick

# API endpoint returning 500 error
/debug-error "API 500 error on /users endpoint" --trace --analyze

# Performance issue identification
/debug-error "page load time increased" --serena-deep --impact

# Memory leak investigation
/debug-error "memory usage growing" --analyze --memory --document
```

### Complex Problem Solving

```bash
# Mysterious production bug
/debug-error "intermittent crashes in production" --serena-deep --interactive --memory

# Integration failure
/debug-error "third-party API integration failing" --trace --pattern-search --impact

# Database performance degradation
/debug-error "query performance decreased" --analyze --serena-deep --implement

# Security vulnerability discovered
/debug-error "SQL injection vulnerability" --serena-deep --impact --document --memory-store
```

### Learning and Improvement

```bash
# Document successful fix for future reference
/debug-error "authentication token refresh issue" --implement --memory-store --document

# Build on previous debugging session
/debug-error "similar caching issue as before" --memory --pattern-search --quick

# Complex architectural debugging
/debug-error "microservice communication failure" --serena-deep --trace --interactive
```

## Integration Patterns

### With Other Commands
```bash
# Research → Debug → Think → Fix workflow
/tech-research "common React performance issues" --serena
/debug-error "React app slow rendering" --serena-deep --memory
/smart-think "optimization strategy" --serena --use-debug-findings
/serena "implement performance optimizations" --use-solution

# Commit integration
/debug-error "memory leak in auth service" --implement --document
/commit --scope=fix --analyze --serena-context
```

### Error Recovery

- **Fix Validation**: Automatic testing and validation of proposed fixes
- **Rollback Capability**: Safe rollback if fixes introduce new issues
- **Progressive Enhancement**: Iterative improvement based on testing results
- **Memory Update**: Continuous learning from both successes and failures

Remember to maintain detailed notes throughout the debugging process and leverage Serena's memory system to build debugging expertise over time.