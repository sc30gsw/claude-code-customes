---
allowed-tools: mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_type, mcp__playwright__browser_select_option, mcp__playwright__browser_wait_for, mcp__playwright__browser_evaluate, mcp__playwright__browser_console_messages, mcp__playwright__browser_network_requests, mcp__playwright__browser_handle_dialog, mcp__playwright__browser_close, 
Read, Glob, Grep, Edit, MultiEdit, Write, Bash, TodoWrite, mcp__sequential-thinking__sequentialthinking, mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory
description: E2E testing and application behavior verification command using Playwright MCP (Serena integration)
---

# Playwright E2E Testing & Behavior Verification Command

## Overview

A command that integrates Playwright MCP with Serena tools to automate application behavior testing and specification verification.

## Usage

### Basic Syntax
```bash
/playwright-test <target> [options]
```

### Target Specification

| Target Type | Example | Description |
|-------------|---------|-------------|
| **URL** | `https://example.com` | External website testing |
| **Local URL** | `http://localhost:3000` | Development app testing |
| **Page Path** | `/login`, `/dashboard` | Specific page testing |
| **Feature Name** | `authentication`, `checkout` | Feature flow testing |

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-s, --spec` | Compare with specification files | false |
| `-r, --report` | Generate detailed report | false |
| `-i, --interactive` | Interactive mode execution | false |
| `-w, --wait` | Wait for element display (seconds) | 5 |
| `-d, --device` | Device emulation | desktop |
| `-b, --browser` | Browser specification | chromium |
| `--headless` | Headless mode | true |
| `--record` | Record test execution video | false |
| `--network` | Network monitoring | false |
| `--console` | Capture console logs | false |

### Usage Examples

```bash
# Basic page testing
/playwright-test https://myapp.com/login

# Local development environment testing
/playwright-test http://localhost:3000/dashboard -i -w 10

# Specification verification
/playwright-test /checkout -s -r

# Mobile device testing
/playwright-test https://myapp.com -d mobile -r

# Network monitoring test
/playwright-test /api-heavy-page --network --console -r
```

## Feature Details

### 1. Application Behavior Testing

#### Basic Flow Verification
- Page load time measurement
- Essential element presence verification
- Interactive element behavior confirmation
- Form submission process verification

#### Error Handling Tests
- Invalid input behavior confirmation
- Network error handling
- JavaScript error detection
- 404/500 error display verification

### 2. Serena Tool Integration

#### Codebase Analysis
```bash
# Identify test targets within project
mcp__serena__get_symbols_overview -> component-list
mcp__serena__search_for_pattern -> test-targets
```

#### Test Result Storage and Learning
```bash
# Save test results to Serena memory
mcp__serena__write_memory: test-results-{timestamp}
# Compare with previous test results
mcp__serena__read_memory: previous-test-results
```

### 3. Specification Verification Feature (-s option)

#### Supported Specification File Formats
- **Requirements**: `requirements/*.md`
- **Design Documents**: `docs/design/*.md`
- **API Specifications**: `openapi.yaml`, `swagger.json`
- **User Stories**: `stories/*.md`

#### Verification Items
1. **UI Element Specification Compliance**
   - Button text and placement verification
   - Form field completeness
   - Error message accuracy

2. **Behavior Specification Compliance**
   - Input validation rules
   - Screen transition flows
   - Data processing logic

3. **Performance Specifications**
   - Page load times
   - API response times
   - Resource usage

### 4. Report Generation Feature (-r option)

#### Auto-Generated Report
```markdown
# Test Execution Report - {timestamp}

## Execution Overview
- Target URL: {target-url}
- Execution Time: {duration}
- Browser: {browser-type}
- Device: {device-type}

## Test Results
### ✅ Successful Items ({success-count})
- Page Load: {load-time}ms
- Essential Elements: All present
- Form Submission: Normal operation

### ❌ Failed Items ({failure-count})
- Login Button: Not clickable
- Error Details: {error-message}

## Specification Compliance (-s option)
### 📋 Comparison with Specifications
- UI Specification Compliance: 95.2%
- Behavior Specification Compliance: 88.7%
- Non-compliance Items: 3

## Performance Metrics
- First Contentful Paint: {fcp}ms
- Largest Contentful Paint: {lcp}ms
- Network Requests: {network-requests}

## Recommended Improvements
1. {improvement-1}
2. {improvement-2}
3. {improvement-3}
```

### 5. Interactive Testing Feature (-i option)

#### Combination with Manual Operations
```bash
# Interactive mode test execution example
/playwright-test localhost:3000/app -i

# Interactive prompts during execution:
> Page loaded. Select next operation:
  1. Click element
  2. Enter text
  3. Take screenshot
  4. Check specifications
  5. Complete test
```

## Implementation Workflow

### Step 1: Preparation
```typescript
// Project analysis with Serena
mcp__serena__onboarding()
project_structure = mcp__serena__get_symbols_overview()
test_targets = mcp__serena__search_for_pattern("test-patterns")
```

### Step 2: Browser Launch & Navigation
```typescript
// Browser operations with Playwright
mcp__playwright__browser_navigate(target_url)
await mcp__playwright__browser_wait_for({time: wait_seconds})
```

### Step 3: Basic Operation Verification
```typescript
// Get DOM structure
page_snapshot = mcp__playwright__browser_snapshot()
// Verify essential elements
essential_elements = extract_essential_elements(page_snapshot)
// Identify interactive elements
interactive_elements = find_interactive_elements(page_snapshot)
```

### Step 4: Function Test Execution
```typescript
// Form test example
test_form_submission() {
  mcp__playwright__browser_type("email-input", "test@example.com")
  mcp__playwright__browser_type("password-input", "testpass123")
  mcp__playwright__browser_click("submit-button")
  await mcp__playwright__browser_wait_for({text: "Success"})
}
```

### Step 5: Specification Verification (-s option)
```typescript
// Load specification files
spec_files = find_specification_files()
// Compare actual behavior with specifications
compliance_check = compare_with_specifications(
  actual_behavior, 
  spec_requirements
)
```

### Step 6: Report Generation & Storage
```typescript
// Aggregate test results
test_results = aggregate_test_results()
// Save to Serena memory
mcp__serena__write_memory("test-results", test_results)
// Generate report file
generate_report(test_results, report_format)
```

## Error Handling

### Common Errors and Solutions

#### Page Load Error
```bash
❌ Error: Failed to load page
Solutions:
1. Verify URL accuracy
2. Check network connection
3. Extend wait time with --wait option
```

#### Element Not Found Error
```bash
❌ Error: Specified element not found
Solutions:
1. Verify element selector
2. Wait for page load completion
3. Manual verification with --interactive mode
```

#### JavaScript Execution Error
```bash
❌ Error: Error occurred during JavaScript execution
Solutions:
1. Check logs with --console option
2. Detailed verification with browser dev tools
3. Visual verification with --headless=false
```

## Performance Optimization

### Large-Scale Test Efficiency
- Time reduction through parallel execution
- Redundant processing reduction through cache utilization
- Processing speed improvement through smart element discovery

### Resource Usage Optimization
- Memory usage monitoring
- Proper browser process termination
- Split execution for large data processing

## Integration Features

### CI/CD Pipeline Integration
```yaml
# GitHub Actions example
- name: Playwright E2E Test
  run: /playwright-test ${{ env.STAGING_URL }} -s -r --headless
```

### Integration with Other Commands
```bash
# Complete workflow: Test → Analysis → Report
/playwright-test localhost:3000 -r
/web-analyzer localhost:3000 -r
/visual-regression localhost:3000 -b
```

## Limitations

### Supported
- ✅ Modern browsers (Chrome, Firefox, Safari)
- ✅ Responsive design
- ✅ SPA (Single Page Application)
- ✅ SSR (Server Side Rendering)

### Limitations
- ❌ Legacy technologies (Flash/Silverlight, etc.)
- ❌ Complex authentication flows (OAuth, SAML, etc.)
- ❌ Large data performance testing
- ❌ Complex multi-tab interactions

## Support & Troubleshooting

### Debug Mode
```bash
# Test execution with debug information
/playwright-test target-url -i --console --network --record
```

### Log Files
- Test execution log: `logs/playwright-test-{timestamp}.log`
- Screenshots: `screenshots/test-{timestamp}.png`
- Video recording: `videos/test-{timestamp}.mp4`

### Community Support
- GitHub Issues: Technical problem reporting
- Documentation: Detailed setup and usage
- Samples: Implementation examples and best practices