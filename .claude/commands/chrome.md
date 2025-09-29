---
allowed-tools: Read, Glob, Grep, Edit, MultiEdit, Write, Bash, TodoWrite, mcp__chrome-devtools__click, mcp__chrome-devtools__drag, mcp__chrome-devtools__fill, mcp__chrome-devtools__fill_form, mcp__chrome-devtools__hover, mcp__chrome-devtools__upload_file, mcp__chrome-devtools__close_page, mcp__chrome-devtools__list_pages, mcp__chrome-devtools__navigate_page, mcp__chrome-devtools__navigate_page_history, mcp__chrome-devtools__new_page, mcp__chrome-devtools__select_page, mcp__chrome-devtools__wait_for, mcp__chrome-devtools__emulate_cpu, mcp__chrome-devtools__emulate_network, mcp__chrome-devtools__resize_page, mcp__chrome-devtools__performance_analyze_insight, mcp__chrome-devtools__performance_start_trace, mcp__chrome-devtools__performance_stop_trace, mcp__chrome-devtools__get_network_request, mcp__chrome-devtools__list_network_requests, mcp__chrome-devtools__evaluate_script, mcp__chrome-devtools__list_console_messages, mcp__chrome-devtools__take_screenshot, mcp__chrome-devtools__take_snapshot, mcp__chrome-devtools__handle_dialog
description: Comprehensive Chrome DevTools development system with native Chrome capabilities for debugging, E2E testing, performance analysis, and browser automation
---

## Context

- Browser status: !`ps aux | grep chrome | wc -l | xargs echo "Chrome processes:"`
- Page count: Available pages via Chrome DevTools MCP
- Performance state: Active traces and monitoring status
- Network activity: Request monitoring and analysis
- Console state: Message count and error levels
- Project context: @package.json for web application type
- **Revolutionary DOM Analysis**: AI can directly observe rendered screens and understand visual issues programmatically
- **UI-Code Bridge**: Direct connection between abstract UI experience and concrete implementation problems
- **Visual Verification**: AI performs human-level observational actions with browser developer tools

## Tool Usage Priorities

**ALWAYS prioritize Chrome DevTools MCP for all browser operations:**

### Chrome DevTools MCP (Primary Browser Control)
- **Visual DOM Analysis**: Use `mcp__chrome-devtools__take_snapshot` for complete DOM structure analysis and visual debugging
- **UI Problem Diagnosis**: Translate visual issues ("button not visible") into technical causes ("hidden attribute applied")
- **Performance Analysis**: Use `mcp__chrome-devtools__performance_start_trace`, `performance_stop_trace`, `performance_analyze_insight`
- **Browser Automation**: Use `mcp__chrome-devtools__click`, `fill`, `navigate_page`, `take_screenshot`
- **Debugging**: Use `mcp__chrome-devtools__list_console_messages`, `evaluate_script`, `take_snapshot`
- **Network Monitoring**: Use `mcp__chrome-devtools__list_network_requests`, `get_network_request`
- **Emulation**: Use `mcp__chrome-devtools__emulate_cpu`, `emulate_network`, `resize_page`
- **Page Management**: Use `mcp__chrome-devtools__list_pages`, `new_page`, `select_page`, `close_page`

### Fallback Tools (Standard)
- **File Operations**: Use Read, Glob, Grep when Chrome DevTools unavailable
- **Build & Test**: Use Bash for non-browser commands
- **Documentation**: Use Write, Edit for creating reports

# Chrome: Complete Chrome DevTools Integration System

Advanced browser development support system utilizing Chrome DevTools MCP's native capabilities for debugging, E2E testing, performance analysis, and comprehensive browser automation.

## Usage Guide

### Basic Syntax
```bash
/chrome [action] [target] [options]
```

### Available Actions

| Action | Description | Example |
|--------|-------------|---------|
| `logs` | View/analyze console messages | `/chrome logs --filter "ERROR"` |
| `errors` | Analyze console errors | `/chrome errors --last 10` |
| `debug` | Debug specific issues | `/chrome debug "login fails"` |
| `eval` | Execute JavaScript | `/chrome eval "document.title"` |
| `test` | E2E testing scenarios | `/chrome test --scenario login` |
| `navigate` | Page navigation | `/chrome navigate "https://example.com"` |
| `click` | Element interaction | `/chrome click "#submit-btn"` |
| `fill` | Form input | `/chrome fill "#email" "test@example.com"` |
| `form` | Multi-field form handling | `/chrome form --auto-fill` |
| `screenshot` | Capture screenshots | `/chrome screenshot --full-page` |
| `snapshot` | DOM/accessibility capture | `/chrome snapshot --analyze` |
| `perf` | Performance analysis | `/chrome perf start --trace` |
| `network` | Network monitoring | `/chrome network list --filter "api"` |
| `emulate` | Browser emulation | `/chrome emulate device mobile` |
| `pages` | Multi-page management | `/chrome pages list` |
| `history` | Navigation history | `/chrome history back` |
| `dialog` | Dialog handling | `/chrome dialog accept` |
| `monitor` | Real-time monitoring | `/chrome monitor --performance` |
| `record` | Session recording | `/chrome record start` |
| `report` | Generate reports | `/chrome report --comprehensive` |
| `workflow` | Integrated workflows | `/chrome workflow debug --full` |

### Core Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--headless` | `-h` | Headless mode | `/chrome test -h` |
| `--isolated` | `-i` | Isolated profile | `/chrome debug -i` |
| `--channel` | `-c` | Chrome channel | `/chrome perf -c canary` |
| `--verbose` | `-v` | Detailed output | `/chrome debug -v` |
| `--analyze` | `-a` | Auto-analysis | `/chrome perf -a` |
| `--auto-fix` | `-f` | Auto-fix issues | `/chrome debug -f` |
| `--record` | `-r` | Session recording | `/chrome test -r` |
| `--filter` | | Content filtering | `/chrome logs --filter "ERROR"` |
| `--threshold` | `-t` | Performance thresholds | `/chrome monitor -t high` |
| `--compare` | | Comparison analysis | `/chrome perf --compare baseline` |

## Quick Examples

### Debugging & Console Analysis
```bash
# View recent console messages with filtering
/chrome logs --filter "ERROR|WARN" --last 50

# Analyze specific error patterns
/chrome errors --analyze --context 5

# Execute debugging JavaScript
/chrome eval "console.log(performance.getEntries())"

# Debug specific issues with auto-fix
/chrome debug "form validation not working" --auto-fix
```

### E2E Testing & Automation
```bash
# Navigate to page and take screenshot
/chrome navigate "http://localhost:3000"
/chrome screenshot --full-page --save "homepage.png"

# Complete form interaction
/chrome fill "#email" "test@example.com"
/chrome fill "#password" "password123"
/chrome click "#login-button"
/chrome wait_for "Welcome"

# Multi-field form automation
/chrome form --fields "email:test@example.com,password:secret"

# E2E test scenario execution
/chrome test --scenario user-registration --record
```

### Performance Analysis
```bash
# Start performance tracing
/chrome perf start --insights

# Navigate and interact
/chrome navigate "https://myapp.com/dashboard"
/chrome click "#heavy-operation"

# Stop trace and analyze
/chrome perf stop --analyze

# Get specific performance insights
/chrome perf insights "LCPBreakdown"
```

### Network Monitoring
```bash
# List all network requests
/chrome network list --type "fetch"

# Get specific request details
/chrome network get "https://api.myapp.com/users"

# Monitor API calls in real-time
/chrome network monitor --filter "api" --watch
```

### Browser Emulation
```bash
# Mobile device emulation
/chrome emulate device mobile
/chrome emulate network "Slow 3G"
/chrome emulate cpu --throttle 4

# Test different viewport sizes
/chrome emulate device --width 375 --height 667

# Offline mode testing
/chrome emulate network offline
```

### Multi-Page Management
```bash
# List all open pages/tabs
/chrome pages list

# Open new page in tab
/chrome pages new "https://example.com"

# Switch between tabs
/chrome pages select 2

# Close specific tab
/chrome pages close 1

# Navigation history
/chrome history back
/chrome history forward
```

## Advanced Workflows

### Complete Debugging Workflow
```bash
# 1. Initial error investigation
/chrome logs --analyze --filter "ERROR"

# 2. Console state capture
/chrome snapshot --accessibility

# 3. Network analysis
/chrome network list --errors

# 4. JavaScript debugging
/chrome eval "window.onerror = (msg,url,line) => console.log({msg,url,line})"

# 5. Screenshot evidence
/chrome screenshot --error-state

# 6. Comprehensive debug report
/chrome workflow debug --full --report
```

### Performance Optimization Workflow
```bash
# 1. Baseline performance measurement
/chrome perf start --baseline

# 2. Navigate to target page
/chrome navigate "https://myapp.com/slow-page"

# 3. Stop trace and analyze
/chrome perf stop --analyze --compare baseline

# 4. CPU throttling test
/chrome emulate cpu --throttle 4
/chrome perf start
/chrome navigate "https://myapp.com/slow-page"
/chrome perf stop --analyze

# 5. Network limitation test
/chrome emulate network "Slow 3G"
/chrome perf start
/chrome navigate "https://myapp.com/slow-page"
/chrome perf stop --analyze

# 6. Optimization recommendations
/chrome report --performance --suggestions
```

### E2E Testing Workflow
```bash
# 1. Start test session recording
/chrome record start --session "user-journey-test"

# 2. Test scenario execution
/chrome test --scenario complete-purchase --steps:
#    - Navigate to product page
#    - Add to cart
#    - Proceed to checkout
#    - Fill payment form
#    - Complete purchase

# 3. Visual validation
/chrome screenshot --compare --baseline checkout-flow

# 4. Performance validation during test
/chrome monitor --performance --budget

# 5. Test report generation
/chrome record stop --analyze
/chrome report --test-results --comprehensive
```

## Advanced Features

### 🧠 AI-Assisted Development
```bash
# AI-powered debugging
/chrome ai debug --analyze-errors --suggest-fixes

# Smart test generation
/chrome ai test --generate-from-usage

# Performance optimization AI
/chrome ai perf --analyze-bottlenecks --recommend-fixes

# Code quality analysis
/chrome ai code --analyze-patterns --best-practices
```

### 📊 Real-time Monitoring
```bash
# Comprehensive monitoring
/chrome monitor --all --dashboard

# Performance budget monitoring
/chrome monitor --performance --budget --alerts

# Memory leak detection
/chrome monitor --memory --leak-detection

# Network bottleneck monitoring
/chrome monitor --network --slow-requests
```

### 🔄 Session Management
```bash
# Start comprehensive monitoring session
/chrome session start --name "feature-development" --record-all

# Resume previous session
/chrome session resume "feature-development"

# Save current browser state
/chrome session save --state "before-refactor"

# Restore browser state
/chrome session restore "before-refactor"
```

### 📈 Advanced Reporting
```bash
# Comprehensive development report
/chrome report --comprehensive --include-all

# Performance-focused report
/chrome report --performance --metrics --insights

# Accessibility compliance report
/chrome report --accessibility --wcag --remediation

# Security analysis report
/chrome report --security --vulnerabilities --recommendations
```

## Integration Patterns

### With Development Workflow
```bash
# Development debugging cycle
/chrome workflow dev-debug --watch:
#  1. Monitor console/network in real-time
#  2. Auto-capture errors with context
#  3. Generate fix suggestions
#  4. Validate fixes with tests

# Pre-deployment validation
/chrome workflow pre-deploy --comprehensive:
#  1. Performance analysis
#  2. Accessibility testing
#  3. Cross-device emulation
#  4. Network condition testing
#  5. Security validation
```

### Chrome DevTools Specific Features

#### Performance Insights Integration
```bash
# Core Web Vitals analysis
/chrome perf vitals --lcp --fid --cls

# JavaScript performance profiling
/chrome perf profile --javascript --heap

# Network performance analysis
/chrome perf network --waterfall --timing
```

#### Native Chrome Emulation
```bash
# CPU throttling (1-20x slowdown)
/chrome emulate cpu --factor 1    # No throttling
/chrome emulate cpu --factor 4    # 4x slower
/chrome emulate cpu --factor 20   # 20x slower

# Network presets
/chrome emulate network "No emulation"
/chrome emulate network "Slow 3G"
/chrome emulate network "Fast 3G"
/chrome emulate network "Slow 4G"
/chrome emulate network "Fast 4G"

# Custom network conditions
/chrome emulate network --download 1000 --upload 500 --latency 100
```

#### Browser Context Management
```bash
# Multi-page debugging
/chrome pages debug --all-tabs

# Page isolation testing
/chrome pages isolate --test-independence

# Cross-tab communication testing
/chrome pages communicate --test-messaging
```

## Configuration & Settings

### Chrome Channel Selection
```bash
# Use different Chrome versions
/chrome --channel stable    # Default stable
/chrome --channel beta      # Beta channel
/chrome --channel dev       # Dev channel
/chrome --channel canary    # Canary channel
```

### Profile Management
```bash
# Isolated testing profile
/chrome --isolated --clean-slate

# Persistent profile for session
/chrome --profile dev-testing

# Custom executable path
/chrome --executable "/path/to/chrome"
```

### Debugging & Logging
```bash
# Enable verbose logging
/chrome --log-file debug.log --verbose

# Debug specific subsystems
/chrome --debug network,performance,console
```

## Best Practices

### Effective Chrome DevTools Usage
1. **Start with Console Analysis**: Use `list_console_messages` first for error investigation
2. **Performance Baseline**: Always measure before optimizing with `performance_start_trace`
3. **Network First**: Check network requests before blaming code performance
4. **Emulation Testing**: Test under realistic conditions with CPU/network throttling
5. **Visual Validation**: Use screenshots for UI regression detection

### Browser State Management
1. **Clean State**: Use `--isolated` for reproducible testing
2. **Page Management**: Properly close unused pages to prevent resource leaks
3. **Session Recording**: Record important debugging sessions for replay
4. **State Snapshots**: Capture DOM snapshots before making changes
5. **Dialog Handling**: Always handle browser dialogs to prevent blocking

### Performance Optimization
1. **Trace Everything**: Use comprehensive tracing for bottleneck identification
2. **Emulate Real Conditions**: Test with throttled CPU and network
3. **Monitor Continuously**: Use real-time monitoring during development
4. **Compare Baselines**: Always compare against performance baselines
5. **Actionable Insights**: Focus on Chrome's native performance insights

## Requirements

### Prerequisites
- Chrome DevTools MCP server configured and running
- Chrome browser (stable/beta/dev/canary)
- Node.js 22.12.0+ for MCP server

### Chrome DevTools MCP Configuration
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}
```

## Error Handling

- **Chrome Startup Issues**: Automatic retry with different configurations
- **Page Load Failures**: Graceful fallback with error context capture
- **Performance Analysis Errors**: Partial results with diagnostic information
- **Network Request Failures**: Comprehensive error reporting with retry logic

## Chrome DevTools Advantages

### Over Other Browser Automation Tools
1. **Native Chrome Integration**: Direct DevTools Protocol access
2. **Performance Insights**: Built-in Chrome performance analysis
3. **Real Browser Context**: Actual Chrome rendering and JavaScript engine
4. **Advanced Emulation**: Native CPU and network throttling
5. **Debugging Depth**: Full access to Chrome's debugging capabilities

### Unique Chrome DevTools Features
1. **Performance Tracing**: Industry-standard browser performance analysis
2. **Network Throttling**: Realistic connection simulation
3. **CPU Emulation**: Hardware constraint testing
4. **DevTools Integration**: Access to Chrome's full developer toolkit
5. **Cross-Platform**: Consistent behavior across operating systems

This command provides complete Chrome DevTools integration, offering native browser capabilities that surpass traditional automation tools while providing comprehensive debugging, testing, and performance analysis features.