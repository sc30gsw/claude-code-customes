---
name: chrome
description: Comprehensive Chrome DevTools development system with native Chrome capabilities for debugging, E2E testing, performance analysis, and browser automation
---

# Chrome: Complete Chrome DevTools Integration System

Advanced browser development support system utilizing Chrome DevTools MCP's native capabilities for debugging, E2E testing, performance analysis, and comprehensive browser automation.

## Context

- Browser status: `ps aux | grep chrome | wc -l`
- Page count: Available pages via Chrome DevTools MCP
- Performance state: Active traces and monitoring status
- Network activity: Request monitoring and analysis
- Console state: Message count and error levels

## Tool Priorities

**ALWAYS prioritize Chrome DevTools MCP for all browser operations:**

### Chrome DevTools MCP (Primary Browser Control)
- **Visual DOM Analysis**: Use `mcp__chrome-devtools__take_snapshot` for complete DOM structure analysis
- **UI Problem Diagnosis**: Translate visual issues into technical causes
- **Performance Analysis**: Use `mcp__chrome-devtools__performance_start_trace`, `performance_stop_trace`
- **Browser Automation**: Use `mcp__chrome-devtools__click`, `fill`, `navigate_page`, `take_screenshot`
- **Debugging**: Use `mcp__chrome-devtools__list_console_messages`, `evaluate_script`
- **Network Monitoring**: Use `mcp__chrome-devtools__list_network_requests`

## Usage

```bash
/chrome [action] [target] [options]
```

### Available Actions

| Action | Description | Example |
|--------|-------------|---------|
| `analyze` | Comprehensive page analysis | `/chrome analyze --full` |
| `summarize` | Content summarization | `/chrome summarize --structure` |
| `extract` | Data extraction | `/chrome extract --metadata` |
| `logs` | View console messages | `/chrome logs --filter "ERROR"` |
| `debug` | Debug specific issues | `/chrome debug "login fails"` |
| `test` | E2E testing scenarios | `/chrome test --scenario login` |
| `perf` | Performance analysis | `/chrome perf start --trace` |
| `network` | Network monitoring | `/chrome network list` |
| `screenshot` | Capture screenshots | `/chrome screenshot --full-page` |

### Options

| Option | Description |
|--------|-------------|
| `--headless` | Headless mode |
| `--verbose` | Detailed output |
| `--analyze` | Auto-analysis |
| `--filter` | Content filtering |

## Key Features

### AI-Driven Page Analysis
- DOM + Console + Network + Performance + AI synthesis
- Security & Accessibility analysis
- Content summarization and structure analysis

### Debugging & Console Analysis
- View recent console messages with filtering
- Analyze specific error patterns
- Execute debugging JavaScript

### E2E Testing & Automation
- Complete form interaction
- Multi-field form automation
- E2E test scenario execution

### Performance Analysis
- Performance tracing
- Core Web Vitals analysis
- Network performance analysis

## Requirements

- Chrome DevTools MCP server configured and running
- Chrome browser (stable/beta/dev/canary)
- Node.js 22.12.0+ for MCP server
