---
name: test
description: Advanced test implementation command with unit/E2E support, auto-execution, and smart fixing capabilities
---

# Test Command

Implement comprehensive tests with optional test execution and intelligent failure fixing.

## Usage

```bash
/test <target> [options]
```

## Target Specification

| Target Type | Examples | Description |
|-------------|----------|-------------|
| Component Name | `LoginForm`, `UserProfile` | React/Vue/Angular components |
| File Path | `utils/validation`, `hooks/useAuth` | Module and utility files |
| Function Name | `calculateTotal`, `formatDate` | Specific functions |
| Feature Name | `authentication`, `payment` | Entire feature areas |

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `-u` | Unit test mode | ✅ |
| `-e` | E2E test mode + accessibility injection | - |
| `-r` | Auto-run tests with smart fixing | - |
| `-v` | Verbose output mode | - |
| `-c` | Coverage-focused mode (target 90%+) | - |
| `-p` | Performance test mode | - |
| `-w` | Watch mode | - |
| `-f` | Fast mode (parallel + caching) | - |
| `--files=PATTERN` | Specify files by glob | - |
| `--exclude=PATTERN` | Exclude files by glob | - |
| `--include-deps` | Include dependency files | - |
| `--dry-run` | Test design only | - |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools:**

### File Operations (Serena MCP First)
- **Reading files**: Use `mcp__serena__find_file` → `Read` (fallback)
- **Searching patterns**: Use `mcp__serena__search_for_pattern` → `Grep` (fallback)
- **Finding symbols**: Use `mcp__serena__find_symbol` → `Glob` (fallback)

### Code Analysis (Serena MCP)
- **Symbol overview**: Use `mcp__serena__get_symbols_overview`
- **Symbol references**: Use `mcp__serena__find_referencing_symbols`
- **Code replacement**: Use `mcp__serena__replace_symbol_body` → `Edit` (fallback)

## Examples

```bash
# Basic Usage
/test LoginComponent -e -r          # E2E tests, run & fix
/test utils/auth -u -r -c           # High-coverage unit tests
/test PaymentForm -e -v             # E2E with verbose output

# File Pattern Specification
/test components --files="Button*" -u -r
/test src --files="**/*.hook.ts" -u -c
/test api --files="**/*Controller.ts" --include-deps -u -r

# Performance-Focused
/test heavyComponent -u -p -f --parallel=8
/test api/bulk -u -p --timeout=60
```

## Test Implementation Flow

### Unit Test Mode (-u)
1. Target code analysis with Serena MCP
2. Test framework detection (Jest, Vitest, Mocha)
3. Test case creation: happy path, error cases, edge cases

### E2E Test Mode (-e)
1. Component analysis for interactive elements
2. E2E framework detection (Cypress, Playwright)
3. Accessibility attribute injection (data-testid, aria-label)
4. E2E test case creation: page loading, user interactions, forms

### Smart Fixing (-r option)
1. Parse error output
2. Classify errors: syntax, assertion, async, mock, E2E-specific
3. Apply appropriate fixing strategy
4. Re-run and iterate (max 10 attempts)

## Output Report

```
📁 Created/Updated Files:
- src/components/LoginForm.test.tsx
- cypress/e2e/user-authentication.cy.ts

🧪 Implemented Test Cases:
[Unit Tests]
✓ LoginForm happy path tests (3 cases)
✓ LoginForm error handling tests (2 cases)

🚀 Test Execution Results:
[1st Run] ❌ 2 failures
[Auto-Fix Applied] ✅
[2nd Run] ✅ All passed (9 tests)
Coverage: 95.2%
```
