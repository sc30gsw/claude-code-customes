---
allowed-tools: mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, Read, Glob, Grep, Edit, MultiEdit, Write, Bash, mcp__context7__resolve-library-id, mcp__context7__get-library-docs
description: Advanced test implementation command with unit/E2E support, auto-execution, and smart fixing capabilities
---

## Context

- Project package.json: @package.json
- Current file structure: !`find . -type f -name "*.ts" -o -name "*.tsx" -o -name "*.js" -o -name "*.jsx" | head -20`
- Existing test files: !`find . -type f \( -name "*.test.*" -o -name "*.spec.*" \) | head -10`
- Test configuration files: !`find . -maxdepth 2 -name "jest.config.*" -o -name "vitest.config.*" -o -name "cypress.config.*" -o -name "playwright.config.*" -o -name "*.config.ts" | grep -E "(test|spec)" | head -5`
- Test scripts in package.json: !`cat package.json | jq -r '.scripts | to_entries[] | select(.key | test("test|spec|e2e|unit")) | "\(.key): \(.value)"' 2>/dev/null || echo "No test scripts found"`

## Usage Guide

### Basic Syntax
```bash
/test <target> [options]
```

### Target Specification

| Target Type | Examples | Description |
|-------------|----------|-------------|
| **Component Name** | `LoginForm`, `UserProfile` | React/Vue/Angular components |
| **File Path** | `utils/validation`, `hooks/useAuth` | Module and utility files |
| **Function Name** | `calculateTotal`, `formatDate` | Specific functions |
| **Feature Name** | `authentication`, `payment` | Entire feature areas |

### File Pattern Specification

When using `--files` option, you can specify glob patterns to target multiple files:

| Pattern Type | Examples | Matches |
|-------------|----------|---------|
| **Wildcards** | `Button*` | `Button.tsx`, `ButtonGroup.ts`, `ButtonIcon.vue` |
| **Extensions** | `**/*.hook.ts` | All `.hook.ts` files in any subdirectory |
| **Directories** | `components/**/*.tsx` | All `.tsx` files in components and subdirectories |
| **Multiple patterns** | `{*.ts,*.tsx}` | Files with either `.ts` or `.tsx` extension |
| **Negation with exclude** | `--files="src/**/*.ts" --exclude="**/*.test.*"` | All `.ts` files except test files |

### Dependency Inclusion

With `--include-deps` option:
- Automatically analyzes `import` and `require` statements
- Includes imported local files in testing scope
- Excludes node_modules dependencies (focus on local code)
- Useful for comprehensive feature testing

### Available Options

| Option | Description | Default |
|--------|-------------|---------|
| **-u** | Unit test mode | ✅ |
| **-e** | E2E test mode + accessibility attribute injection | - |
| **-r** | Auto-run tests with smart fixing (up to 10 attempts) | - |
| **-v** | Verbose output mode (show implementation process) | - |
| **-c** | Coverage-focused mode (target 90%+ coverage) | - |
| **-p** | Performance test mode (execution time & memory profiling) | - |
| **-w** | Watch mode (auto-rerun on file changes) | - |
| **-f** | Fast mode (parallel execution & caching) | - |
| **--skip-lint** | Skip linter execution | - |
| **--dry-run** | Test design only (no file writes) | - |
| **--parallel=N** | Specify parallel execution count (default: CPU count) | - |
| **--timeout=N** | Specify timeout in seconds (default: 30s) | - |
| **--files=PATTERN** | Specify files by glob pattern (e.g., `src/**/*.ts`, `components/Button*`) | - |
| **--exclude=PATTERN** | Exclude files by glob pattern | - |
| **--include-deps** | Include dependency files in testing scope | - |

### Option Combination Examples

```bash
# Basic Usage
/test LoginComponent -e -r          # Create, run, and fix E2E tests
/test utils/auth -u -r -c          # High-coverage unit tests with execution
/test PaymentForm -e -v            # E2E test creation with verbose output
/test validateEmail --dry-run      # Test design verification only

# File Pattern Specification
/test components --files="Button*" -u -r      # Test all Button components
/test src --files="**/*.hook.ts" -u -c        # Test all custom hooks with coverage
/test . --files="utils/**/*.ts" --exclude="*.test.*" -u -r    # Test utils, exclude existing tests
/test api --files="**/*Controller.ts" --include-deps -u -r    # Test controllers with their dependencies

# Advanced Usage
/test UserDashboard -e -r -v -c    # Full-featured E2E testing
/test api/users -u -r --skip-lint  # Unit tests without linting
/test . --files="src/**/*.tsx" --exclude="**/*.stories.*" -e -r    # E2E test all components, exclude stories

# Performance-Focused
/test heavyComponent -u -p -f --parallel=8    # Fast parallel performance tests
/test api/bulk -u -p --timeout=60            # Long-running performance tests
/test . --files="**/*Heavy*.ts" -u -p --parallel=4    # Performance test heavy components

# Development Efficiency
/test ActiveComponent -u -w -f                # Watch mode + fast execution
/test utils/helpers -u -r -f --parallel=4    # Fast test execution with fixing
/test . --files="src/components/**/*.tsx" -u -w -f    # Watch all components for changes
```

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools when available:**

### File Operations (Use Serena MCP First)
- **Reading files**: Use `mcp__serena__find_file` → `Read` (fallback)
- **Searching patterns**: Use `mcp__serena__search_for_pattern` → `Grep` (fallback)
- **Directory listing**: Use `mcp__serena__list_dir` → `LS` (fallback)
- **Finding symbols**: Use `mcp__serena__find_symbol` → `Glob` (fallback)

### Code Analysis (Serena MCP Exclusive)
- **Symbol overview**: Use `mcp__serena__get_symbols_overview`
- **Symbol references**: Use `mcp__serena__find_referencing_symbols`
- **Code replacement**: Use `mcp__serena__replace_symbol_body` → `Edit` (fallback)
- **Pattern replacement**: Use `mcp__serena__replace_regex` → `MultiEdit` (fallback)

### Memory & Context (Serena MCP Only)
- **Task tracking**: Use `mcp__serena__think_about_task_adherence`
- **Progress checking**: Use `mcp__serena__think_about_whether_you_are_done`
- **Information analysis**: Use `mcp__serena__think_about_collected_information`
- **Memory operations**: Use `mcp__serena__write_memory`, `mcp__serena__read_memory`

## Your Task

Implement comprehensive tests for the specified feature, file, or function, with optional test execution and intelligent failure fixing based on the provided options.

### Execution Flow

#### 1. Pre-execution Setup
1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. Read package.json using `mcp__serena__find_file` to identify available testing libraries and frameworks
3. Verify existing test configurations and scripts using `mcp__serena__list_dir`
4. **File Discovery & Filtering**:
   - Parse target argument and file specification options
   - Use `mcp__serena__search_for_pattern` with `--files` pattern → `Glob` (fallback)
   - Apply `--exclude` pattern to filter out unwanted files
   - If `--include-deps` is set, use `mcp__serena__find_referencing_symbols` to analyze imports
   - Validate that discovered files exist using `mcp__serena__find_file`
5. **Progress Tracking**: Use `mcp__serena__think_about_task_adherence` to verify setup completion

#### 2. Mode-Specific Test Implementation

##### Unit Test Mode (-u)
1. **Target Code Analysis**:
   - Identify and read specified files/functions using `mcp__serena__find_file` → `Read` (fallback)
   - Get symbol overview using `mcp__serena__get_symbols_overview`
   - Find symbol definitions using `mcp__serena__find_symbol`
   - Analyze dependencies and imports using `mcp__serena__find_referencing_symbols`
   - Determine function parameters, return values, and side effects

2. **Test Framework Detection**:
   - Identify Jest, Vitest, Mocha, etc. from package.json
   - Reference official documentation via Context7 MCP
   - Analyze existing test file patterns (naming conventions, directory structure)

3. **Test Case Creation**:
   - **Happy Path**: Normal operation with expected inputs
   - **Error Cases**: Invalid inputs and error conditions
   - **Edge Cases**: Min/max values, null, undefined, etc.
   - **Side Effects**: API calls, state changes, file operations with proper mocking
   - **Async Operations**: Promises, async/await, callbacks

4. **Implementation Details**:
   - Test file naming: `{targetFile}.test.{extension}` or `{targetFile}.spec.{extension}`
   - Proper setup/teardown procedures
   - Appropriate mock and spy configuration with cleanup

##### E2E Test Mode (-e)
1. **Target Component Analysis**:
   - Identify and read component files using `mcp__serena__find_file` → `Read` (fallback)
   - Search for interactive elements using `mcp__serena__search_for_pattern`
   - Get component symbol overview using `mcp__serena__get_symbols_overview`
   - Analyze rendered content, props, and state
   - Identify user interaction elements

2. **E2E Framework Detection**:
   - Identify Cypress, Playwright, Puppeteer, etc. from package.json
   - Reference official documentation via Context7 MCP
   - Analyze existing E2E test patterns

3. **Accessibility Attribute Check & Injection**:
   - Search for buttons, forms, and interactive elements in components
   - Verify existence of aria-label and data-testid attributes
   - Add appropriate attributes when missing:
     ```tsx
     // Example: Adding test ID to button
     <button onClick={handleClick} data-testid="submit-button" aria-label="Submit form">
       Submit
     </button>
     ```

4. **E2E Test Case Creation**:
   - **Page Loading**: Initial display verification
   - **User Interactions**: Clicks, inputs, drag & drop, etc.
   - **Form Operations**: Input, validation, submission
   - **Navigation**: Routing, modal displays, etc.
   - **Data Display**: API responses, real-time updates
   - **Error Handling**: Network errors, validation errors

5. **Implementation Details**:
   - Test file naming: `{feature}.e2e.{extension}` or `cypress/e2e/{feature}.cy.{extension}`
   - Apply Page Object pattern (for large-scale tests)
   - Proper wait conditions and timeout settings

#### 3. Test Execution & Smart Fixing (-r option)

##### Test Execution Flow
1. **Identify Appropriate Test Commands**:
   - Unit test mode: `npm test`, `npm run test:unit`, `yarn test`, etc.
   - E2E test mode: `npm run test:e2e`, `npm run cypress:run`, `npm run playwright`, etc.
   - Auto-detect relevant scripts from package.json

2. **Test Execution**:
   ```bash
   # Run only the implemented test file
   npm test -- --testPathPattern={createdTestFile}
   # or
   npx jest {createdTestFile}
   ```

3. **Result Analysis**:
   - Parse execution output
   - Determine success/failure status
   - Extract error messages

##### Intelligent Auto-Fixing on Failures

1. **Error Classification**:
   - **Syntax Errors**: TypeScript type errors, import errors
   - **Assertion Errors**: Expected vs actual value mismatches
   - **Async Errors**: Unresolved promises, timeouts
   - **Mock Errors**: Improper mock configurations
   - **E2E-Specific Errors**: Selector mismatches, element not found

2. **Fixing Strategies**:
   - **Syntax Errors**:
     - Verify and add TypeScript definition files
     - Fix import paths
     - Add type annotations
   
   - **Assertion Errors**:
     - Review expected values
     - Verify implementation code behavior
     - Adjust test data
   
   - **Async Errors**:
     - Add missing `await` keywords
     - Use proper wait utilities like `waitFor`, `eventually`
     - Adjust timeout values
   
   - **Mock Errors**:
     - Adjust mock function return values
     - Add proper cleanup like `jest.clearAllMocks()`
     - Review mock scope and configuration
   
   - **E2E-Specific Errors**:
     - Update selectors (prioritize data-testid)
     - Add element visibility waits
     - Add page transition waits

3. **Fix Execution**:
   ```bash
   # Re-run after fixes
   npm test -- --testPathPattern={testFile} --verbose
   ```

4. **Iterative Process**:
   - Use `mcp__serena__think_about_whether_you_are_done` to check completion status
   - Attempt fixes up to 10 times maximum
   - Apply different fixing approaches each iteration using `mcp__serena__replace_regex` or `mcp__serena__replace_symbol_body`
   - Continue until all tests pass or fix limit reached
   - Use `mcp__serena__write_memory` to store fix patterns for future reference

##### Fix Result Reporting
- Detailed fix descriptions
- Before/after error message comparisons
- Final test execution results
- Recommended actions for unfixable issues

### Context7 MCP Integration

#### 1. Automatic Library Detection & Documentation Reference

Auto-detect the following from package.json dependencies and reference documentation via Context7 MCP:

##### Testing Frameworks
- **Jest**: `resolve-library-id: "jest"` → Basic test syntax, mocking, async testing
- **Vitest**: `resolve-library-id: "vitest"` → Vite-specific configuration, snapshot testing
- **Mocha**: `resolve-library-id: "mocha"` → describe/it syntax, hook functions
- **Jasmine**: `resolve-library-id: "jasmine"` → Spies, custom matchers

##### E2E Testing Frameworks
- **Cypress**: `resolve-library-id: "cypress"` → Commands, custom commands, plugins
- **Playwright**: `resolve-library-id: "playwright"` → Browser contexts, page objects
- **Puppeteer**: `resolve-library-id: "puppeteer"` → Page manipulation, screenshots

##### Testing Libraries
- **React Testing Library**: `resolve-library-id: "testing-library"` → render, fireEvent, waitFor
- **Vue Testing Library**: `resolve-library-id: "vue-testing-library"` → mount, wrapper operations
- **Angular Testing Utilities**: `resolve-library-id: "@angular/core/testing"` → TestBed, ComponentFixture

##### Mock & Assertion Libraries
- **MSW**: `resolve-library-id: "msw"` → Handler configuration, server setup
- **Sinon**: `resolve-library-id: "sinon"` → Spies, stubs, fakes
- **Chai**: `resolve-library-id: "chai"` → Assertion syntax, plugins

#### 2. Context-Specific Documentation Reference

##### During Test Implementation
```typescript
// Example: Implementing async tests with Jest
// Context7 MCP query: "jest async testing promises" for latest syntax reference
```

##### During Error Resolution
```typescript
// Example: Cypress E2E test selector not found error
// Context7 MCP query: "cypress element not found wait" for solution reference
```

##### During Optimization
```typescript
// Example: Improving Jest test execution speed
// Context7 MCP query: "jest performance optimization parallel" for optimization techniques
```

#### 3. Framework-Specific Reference Examples

- **Jest + React Testing Library**:
  - Topic: "testing hooks", "mocking modules", "snapshot testing"
- **Cypress + TypeScript**:
  - Topic: "typescript configuration", "custom commands", "plugins"
- **Playwright + Page Object Model**:
  - Topic: "page object pattern", "fixtures", "parallel testing"

### Practical Usage Examples

#### 1. Frontend Development Patterns

##### React Component Testing
```bash
# Comprehensive login form testing
/test LoginForm -e -r -c
# → Create E2E tests, add accessibility attributes, run & fix, high coverage

# Custom hook unit testing
/test hooks/useAuth -u -r -v
# → Create useAuth hook tests, run & fix, verbose output

# State management library testing
/test store/userSlice -u -c
# → Redux/Zustand slice tests with high coverage
```

##### Vue.js Usage Examples
```bash
# Vue component E2E testing
/test components/ProductCard -e -r
# → Vue Testing Library + Cypress/Playwright integration

# Composables testing
/test composables/useApi -u -r -c
# → Vue Composition API testing with coverage
```

#### 2. Backend API Testing

```bash
# Express.js route handlers
/test routes/auth -u -r
# → API endpoint unit testing

# Database models
/test models/User -u -c
# → Mongoose/Sequelize model testing

# Middleware functions
/test middleware/auth -u -r -v
# → Authentication middleware testing
```

#### 3. Utility Function Testing

```bash
# Validation functions
/test utils/validation -u -r -c
# → High-coverage unit tests including edge cases

# Date processing utilities
/test utils/dateHelpers -u -r
# → Various date pattern testing

# API client
/test api/httpClient -u -r -v
# → HTTP request mocking tests
```

#### 4. Large-Scale Feature E2E Testing

```bash
# E-commerce checkout flow
/test features/checkout -e -r -v -c
# → Multi-page E2E testing

# Admin panel CRUD operations
/test admin/userManagement -e -r
# → Complete admin interface testing

# Real-time features (WebSocket, etc.)
/test features/chat -e -r -v
# → Chat functionality E2E testing
```

#### 5. Performance-Oriented Testing

```bash
# Bulk data processing functions
/test utils/dataProcessor -u -c -r
# → Memory usage & execution time focused tests

# Virtual scroll components
/test components/VirtualList -e -c -r
# → Performance-focused E2E testing
```

#### 6. Development Stage-Specific Usage

##### Early Development (Design Verification)
```bash
# Test design verification
/test NewFeature --dry-run -v
# → Implementation approach verification, no file creation

# Prototype simple testing
/test prototype/newComponent -u
# → Basic functionality verification only
```

##### During Development (Continuous Testing)
```bash
# Immediate post-modification verification
/test ModifiedComponent -u -r
# → Immediate impact checking after changes

# Regression testing on feature additions
/test existingFeature -e -r --skip-lint
# → Verify impact on existing functionality
```

##### Pre-Release (Quality Assurance)
```bash
# Final quality check
/test criticalFeature -e -r -v -c
# → Comprehensive testing with all options

# Performance verification
/test performance/heavyOperation -u -c -r
# → Production-equivalent load testing
```

### Team Development Best Practices

#### New Feature Development
1. **Design Phase**: `/test newFeature --dry-run -v`
2. **Implementation Phase**: `/test newFeature -u -r`
3. **Integration Phase**: `/test newFeature -e -r -c`

#### Pre-Code Review
```bash
# Create comprehensive test suite for review
/test reviewTarget -u -e -r -c -v
# → Implement tests in reviewer-friendly format
```

#### Development Workflow Integration
```bash
# Lightweight tests for rapid feedback
/test module -u -r --skip-lint

# Comprehensive E2E testing (staging environment)
/test e2eFlow -e -r -c
```

### E2E Accessibility Attribute Injection

#### 1. Target Element Detection

Prioritize detection and add test attributes to the following elements:

##### Interactive Elements
- **Buttons**: `<button>`, `<input type="button|submit|reset">`
- **Links**: `<a href="...">`
- **Form Elements**: `<input>`, `<select>`, `<textarea>`
- **Custom Components**: Elements with event handlers like `onClick`, `onSubmit`

##### Display Elements
- **Headings**: `<h1>` ~ `<h6>`
- **Lists**: `<ul>`, `<ol>`, `<li>`
- **Tables**: `<table>`, `<th>`, `<td>`
- **Media**: `<img>`, `<video>`, `<audio>`

#### 2. Attribute Addition Rules

##### data-testid Addition
```tsx
// Before
<button onClick={handleSubmit}>Submit</button>

// After  
<button onClick={handleSubmit} data-testid="submit-button">Submit</button>
```

**Naming Conventions**:
- Function-based: `{function}-{elementType}` (e.g., `login-button`, `search-input`)
- Hierarchy-based: `{parent}-{child}` (e.g., `header-nav-menu`, `sidebar-user-profile`)
- Semantic-based: `{meaningful-name}` (e.g., `error-message`, `loading-spinner`)

##### aria-label Addition
```tsx
// Before
<button onClick={handleDelete}>🗑️</button>

// After
<button onClick={handleDelete} data-testid="delete-button" aria-label="Delete item">🗑️</button>
```

**Addition Conditions**:
- No text content (icon-only elements)
- Unclear text ("OK", "Details", etc.)
- Context information needed

##### role Addition
```tsx
// Before
<div onClick={handleClick}>Clickable area</div>

// After
<div onClick={handleClick} role="button" data-testid="clickable-area" aria-label="Execute special operation">
  Clickable area
</div>
```

#### 3. Framework-Specific Implementation

##### React/Next.js
```tsx
// Functional component
const LoginForm = () => (
  <form data-testid="login-form">
    <input 
      type="email" 
      data-testid="email-input"
      aria-label="Email address"
    />
    <button 
      type="submit" 
      data-testid="login-submit"
      aria-label="Execute login"
    >
      Login
    </button>
  </form>
);
```

##### Vue
```vue
<template>
  <form data-testid="login-form">
    <input 
      type="email" 
      data-testid="email-input"
      aria-label="Email address"
    />
    <button 
      type="submit" 
      data-testid="login-submit"
      aria-label="Execute login"
    >
      Login
    </button>
  </form>
</template>
```

#### 4. Automatic Addition Process Flow

1. **Component File Analysis**:
   - Read JSX/TSX/Vue file contents
   - Detect interactive elements using regex patterns
   - Check for existing attributes

2. **Attribute Generation**:
   - Generate appropriate `data-testid` from element type and function
   - Add `aria-label` when needed
   - Add `role` when semantics are unclear

3. **Code Updates**:
   - Batch add multiple attributes using `mcp__serena__replace_regex` → `MultiEdit` (fallback)
   - Use `mcp__serena__insert_after_symbol` or `mcp__serena__insert_before_symbol` for precise placement
   - Preserve formatting and indentation
   - Avoid TypeScript type errors

4. **Addition Result Reporting**:
   - Display list of added attributes
   - Provide test usage examples

### Output Format

#### Execution Completion Report

1. **Implemented Test Files**:
   ```
   📁 Created/Updated Files:
   - src/components/LoginForm.test.tsx
   - cypress/e2e/user-authentication.cy.ts
   ```

2. **Test Case Summary**:
   ```
   🧪 Implemented Test Cases:
   [Unit Tests]
   ✓ LoginForm happy path tests (3 cases)
   ✓ LoginForm error handling tests (2 cases) 
   ✓ LoginForm validation tests (4 cases)
   
   [E2E Tests]  
   ✓ Complete login flow test (1 case)
   ✓ Error handling tests (2 cases)
   ```

3. **Detected Frameworks & Libraries**:
   ```
   🛠️ Detected Test Environment:
   - Test Framework: Jest 29.5.0
   - Testing Library: @testing-library/react 13.4.0
   - E2E Framework: Cypress 12.17.0
   - Mock Library: MSW 1.2.1
   ```

4. **Execution Results (-r option)**:
   ```
   🚀 Test Execution Results:
   
   [1st Run] ❌ 2 failures
   - TypeError: Cannot read property 'value' of null
   - ReferenceError: 'mockApi' is not defined
   
   [Auto-Fix Applied]
   ✅ Added null checks
   ✅ Properly configured mock API
   
   [2nd Run] ✅ All passed (9 tests)
   
   Execution time: 2.3s
   Coverage: 95.2%
   ```

5. **Accessibility Attributes Added (-e option)**:
   ```
   ♿ Added Accessibility Attributes:
   
   src/components/LoginForm.tsx:
   - <input type="email"> → data-testid="email-input", aria-label="Email input"
   - <input type="password"> → data-testid="password-input", aria-label="Password input" 
   - <button type="submit"> → data-testid="login-button", aria-label="Execute login"
   - <div class="error"> → data-testid="error-message", role="alert"
   
   Total attributes added: 4
   ```

6. **Additional Information**:
   ```
   📚 Referenced Documentation:
   - Jest Official Docs: Testing Asynchronous Code
   - React Testing Library: Common mistakes
   - Cypress Best Practices: Selecting Elements
   
   💡 Recommendations:
   - Run npm run lint before test execution
   - Consider E2E tests in CI/CD pipeline integration
   ```

#### Error Reporting

Detailed report for unfixable issues:
```
❌ Unresolved Issues:

Issue: TypeError: Cannot resolve module '@/utils/api'
Cause: TypeScript path configuration problem
Recommended Actions:
1. Check tsconfig.json paths configuration
2. Add moduleNameMapper to jest.config.js
3. Change to relative import paths

Reference Documentation: Jest Configuration - moduleNameMapper
```

### Error Handling & Limitations

#### 1. Common Error Situations & Solutions

##### File/Module Not Found
```
❌ Error: Specified file 'components/NonExistent' not found

Solutions:
1. Verify file path accuracy
2. Search files with Glob tool: find . -name "*NonExistent*"
3. Check for typos
```

##### Dependency Issues
```
❌ Error: Test framework not detected

Solutions:
1. Verify Jest/Vitest etc. are installed in package.json
2. Run npm install or yarn install
3. Reference framework setup docs via Context7 MCP
```

##### TypeScript Configuration Errors
```
❌ Error: Failed to resolve paths in TypeScript configuration

Solutions:
1. Check tsconfig.json paths configuration
2. Add moduleNameMapper to jest.config.js
3. Temporarily bypass with --skip-lint option
```

#### 2. Test Execution Limitations

##### Runtime Environment Limitations
- **Node.js Version**: 16.0.0+ recommended
- **Memory Usage**: Minimum 4GB recommended for E2E test execution
- **Parallel Execution**: Cypress limited to 5 concurrent instances max
- **Timeouts**: Unit tests 10s, E2E tests 60s

##### Unsupported Frameworks
```
⚠️ Limited Support:
- Selenium WebDriver (manual configuration required)
- AVA (basic functionality only)
- Tape (assertion conversion required)

❌ Not Supported:
- QUnit (legacy versions)
- Karma (non-Angular projects)
```

#### 3. Auto-Fix Limitations

##### Fixable Errors
- ✅ Import path corrections
- ✅ Basic type errors
- ✅ Simple assertion fixes
- ✅ Mock configuration adjustments
- ✅ Async operation wait fixes

##### Difficult-to-Fix Errors
- ❌ Complex business logic errors
- ❌ Environment-dependent configuration issues
- ❌ External service integration errors
- ❌ Custom test runner problems
- ❌ Circular dependency resolution

#### 4. Performance Limitations

##### Large File Processing
```
Limitations:
- Files > 10MB: Significant processing time increase
- Components > 1000 lines: Attribute addition processing delays
- Test files > 500 cases: Extended execution times

Recommended Actions:
- Consider file splitting
- Implement tests incrementally
- Use --dry-run for pre-verification
```

##### Parallel Execution Limitations
- **Unit Tests**: Parallel execution up to CPU count
- **E2E Tests**: Limited by browser resources
- **Context7 MCP**: Sequential execution due to API limits

#### 5. Security Restrictions

##### Access Limitations
- Cannot fetch documentation from private repositories
- API endpoints requiring authentication need manual mock setup
- Cannot auto-read local environment variables

##### Data Protection
- No automatic generation of test data containing sensitive information
- Manual creation recommended for tests with PII (Personally Identifiable Information)
- Production database connections are prohibited

#### 6. Troubleshooting

##### Common Issues & Solutions

1. **Test Execution Infinite Loop**
   ```bash
   # Force terminate process
   Ctrl+C or killall node
   
   # Cause: Async operation wait mistakes
   # Solution: Review timeout settings
   ```

2. **Memory Shortage Errors**
   ```bash
   # Expand Node.js memory limit
   export NODE_OPTIONS="--max-old-space-size=8192"
   
   # Split test execution
   /test largeComponent -u --dry-run  # Design verification
   /test largeComponent -u -r        # Actual execution
   ```

3. **Unstable E2E Tests**
   ```bash
   # Stability-focused configuration
   /test flakeyComponent -e -r -v    # Identify causes with verbose output
   
   # Manual retry settings adjustment required for persistent issues
   ```

#### 7. Support & Help

##### Troubleshooting Order
1. **--dry-run -v** for test design verification
2. **Context7 MCP** for official documentation reference
3. **Existing test files** pattern analysis
4. **Incremental implementation**: Execute in order -u → -e → -r
5. **Community**: GitHub Issues or Stack Overflow

##### Logging & Diagnostics
```bash
# Detailed log output
/test problematicComponent -u -r -v

# Error diagnostic information collection
- package.json contents
- tsconfig.json configuration
- Existing test file structure
- Complete error messages
```

### Performance Optimization Features

#### 1. Fast Mode (-f) Details

##### Parallel Execution Optimization
```bash
# Maximize CPU utilization
/test largeProject -u -f --parallel=8

# Auto-determine parallel count
/test components/* -u -f    # Auto-adjust based on CPU count
```

**Optimization Features:**
- Parallel test file execution
- Dependency analysis-based scheduling
- Memory-efficient process management
- Cache functionality utilization

##### Caching Strategy
```typescript
// Test result caching
- No file changes → Use previous results
- Dependency changes → Re-run related tests only
- package.json changes → Re-run all tests
```

#### 2. Performance Test Mode (-p) Features

##### Execution Time Measurement
```bash
/test computeHeavyTask -u -p -r

# Example output:
🚀 Performance Measurement Results:
- Test execution time: 1.234s
- Memory usage: 45.2MB (peak)
- CPU utilization: 78% (average)
- Test execution count: 100 runs (benchmark)
```

##### Memory Leak Detection
- Memory monitoring before/after garbage collection
- Memory growth pattern analysis during long-running execution
- Identification of memory-inefficient test sections

#### 3. Watch Mode (-w) Utilization

##### File Monitoring Setup
```bash
# Monitor specific file
/test LoginComponent -u -w

# Execution result:
👀 Monitoring started: src/components/LoginComponent.tsx
📝 Change detected → Auto test execution
✅ Test completed (0.8s)

👀 Re-monitoring...
```

##### Smart Re-execution
- Execute only tests related to changed files
- Impact scope analysis based on dependency graph
- Full test re-execution on configuration file changes

#### 4. Large-Scale Project Optimization

##### Phased Test Execution
```bash
# Phase 1: Fast smoke tests
/test criticalPath -u -f --timeout=5

# Phase 2: Comprehensive tests (only on success)
/test fullSuite -u -r -c --parallel=12

# Phase 3: E2E tests (only on unit test success)
/test e2eFlow -e -r -p
```

##### Resource Management
```bash
# Memory-constrained environment execution
export NODE_OPTIONS="--max-old-space-size=4096"
/test memoryIntensive -u -f --parallel=2

# CPU-constrained environment execution
/test cpuBound -u --parallel=1 --timeout=120
```

#### 5. Debugging & Profiling

##### Detailed Profiling
```bash
# Detailed performance analysis
/test slowTest -u -p -v --timeout=300

# Example output:
🔍 Detailed Profile:
┌─────────────────┬──────────┬────────────┬─────────────┐
│ Test Case       │ Exec Time│ Memory     │ CPU Usage   │
├─────────────────┼──────────┼────────────┼─────────────┤
│ should validate │ 0.045s   │ 2.1MB      │ 15%        │
│ should handle   │ 0.123s   │ 4.7MB      │ 45%        │
│ should process  │ 1.234s   │ 15.2MB     │ 85% ⚠️     │
└─────────────────┴──────────┴────────────┴─────────────┘
⚠️ Performance improvement suggestion: Optimize 'should process'
```

##### Bottleneck Identification
- Identify long-running test cases
- Warning for high memory usage tests
- Detect abnormal CPU usage spikes

### Metrics Collection

#### Structured Test Result Output
```bash
# Save test results in JSON format
/test src/ -u -r -v | tee test-results.json

# Continuous performance monitoring
/test performance/ -u -p --timeout=300 >> perf-history.log

# Coverage data output
/test components/ -u -c -r > coverage-report.json
```

#### Metrics Analysis Examples
```bash
# Execution time trend analysis
/test utils/ -u -p -v | grep "execution time" >> execution-times.log

# Memory usage monitoring
/test heavyComponents/ -u -p | grep "memory usage" >> memory-usage.log

# Failure rate tracking
/test src/ -u -r | grep -E "(✅|❌)" >> test-results-history.log
```