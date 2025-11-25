---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_snapshot, mcp__playwright__browser_wait_for, Glob, Grep
description: Visual regression testing and UI change detection command using Playwright MCP
---

# Visual Regression Test - Visual Regression Testing

## Overview

A visual regression testing command that integrates Playwright MCP with Serena tools to detect visual changes in UI and prevent unintended modifications.

## Usage

### Basic Syntax
```bash
/visual-regression <target> [options]
```

### Target Specification

| Target Type | Example | Description |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | Development app testing |
| **Production URL** | `https://myapp.com` | Production environment comparison |
| **Page Path** | `/dashboard`, `/profile` | Specific page testing |
| **Component** | `Button`, `Modal` | Component-level testing |

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-b, --baseline` | Create baseline images | false |
| `-c, --compare` | Compare with existing baseline | true |
| `-f, --full-page` | Full page screenshot | false |
| `-m, --mobile` | Test mobile version simultaneously | false |
| `-d, --devices` | Multiple device testing | desktop |
| `-t, --threshold` | Difference tolerance threshold (%) | 0.2 |
| `-i, --ignore-regions` | Specify regions to ignore | none |
| `-r, --report` | Generate detailed report | false |
| `-a, --auto-update` | Auto-update confirmation on differences | false |
| `--animations` | Disable animations | true |
| `--wait-for` | Wait for element display | 2 seconds |

### Usage Examples

```bash
# Create initial baseline images
/visual-regression http://localhost:3000 -b -f

# Comparison test after changes
/visual-regression http://localhost:3000 -c -r

# Multi-device testing
/visual-regression /dashboard -m -d "desktop,tablet,mobile"

# Comparison with specific threshold
/visual-regression /profile -c -t 0.5

# Production environment comparison
/visual-regression https://staging.myapp.com -c --baseline-url=https://myapp.com

# Component-level testing
/visual-regression /storybook -c --component=Button --states=all
```

## Feature Details

### 1. Baseline Management (-b option)

#### Initial Baseline Creation
```bash
# Create baseline for entire project
/visual-regression http://localhost:3000 -b -f
```

#### Baseline Image Structure
```
visual-tests/
├── baselines/
│   ├── desktop/
│   │   ├── home-page.png
│   │   ├── dashboard.png
│   │   └── profile.png
│   ├── tablet/
│   │   └── home-page.png
│   └── mobile/
│       └── home-page.png
├── current/
└── diffs/
```

#### Version Control
- Git integration for baseline history management
- Branch-specific baseline settings
- Tag-based baseline fixing

### 2. Difference Detection & Comparison (-c option)

#### Image Comparison Algorithm
```typescript
interface ComparisonResult {
  similarity: number        // Similarity (0-100%)
  pixelDifference: number   // Number of different pixels
  regions: DiffRegion[]     // Detailed difference regions
  severity: 'minor' | 'major' | 'breaking'
}

interface DiffRegion {
  x: number
  y: number
  width: number
  height: number
  significance: number  // Importance (0-1)
}
```

#### Difference Visualization
- Highlight display of difference areas
- Pixel-level change detection
- Color change analysis
- Layout shift detection

### 3. Multi-Device Support (-d option)

#### Supported Devices
```typescript
const DevicePresets = {
  desktop: { width: 1920, height: 1080 },
  laptop: { width: 1366, height: 768 },
  tablet: { width: 768, height: 1024 },
  mobile: { width: 375, height: 667 },
  'mobile-landscape': { width: 667, height: 375 }
}
```

#### Responsive Testing
- Breakpoint-specific screenshots
- Cross-device consistency checks
- Screen rotation support verification

### 4. Ignore Region Settings (-i option)

#### Dynamic Content Exclusion
```json
{
  "ignoreRegions": [
    {
      "selector": ".timestamp",
      "reason": "Dynamic time display"
    },
    {
      "selector": ".user-avatar",
      "reason": "User-specific image"
    },
    {
      "coordinates": { "x": 0, "y": 0, "width": 100, "height": 50 },
      "reason": "Advertisement area"
    }
  ]
}
```

#### Exclusion Setting Patterns
- Element exclusion by selector specification
- Region exclusion by coordinate specification
- Text exclusion by regular expressions
- Automatic detection of dynamic content

### 5. Serena Integration Features

#### Component Analysis Integration
```typescript
// Get component structure and identify test targets
const components = await mcp__serena__get_symbols_overview()
const testTargets = identifyVisualTestTargets(components)

// Compare with past test results
const previousResults = await mcp__serena__read_memory('visual-test-history')
const trendAnalysis = analyzeTrends(previousResults, currentResults)
```

#### Learning & Improvement Features
```typescript
// Learn frequently false-positive areas
await mcp__serena__write_memory('false-positive-patterns', {
  selector: '.dynamic-element',
  frequency: falsePositiveCount,
  recommendations: ['ignore', 'mask', 'stabilize']
})
```

### 6. Auto-Update Feature (-a option)

#### Intelligent Updates
```bash
# Auto-update confirmation for intentional changes
Visual diff detected in login-page.png
Changes appear to be intentional (UI redesign)
Update baseline? [y/N/review]: review

Showing differences:
- Button color changed: #007bff → #28a745
- Spacing increased: 16px → 20px
- New icon added to header

Confirm update? [y/N]: y
```

#### Update Policies
- Automatic design change detection
- Mandatory team review settings
- Gradual updates (partial approval)
- Rollback functionality

## Implementation Workflow

### Step 1: Environment Preparation & Setup
```typescript
// Project structure analysis with Serena
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// Identify pages and components
const testTargets = await mcp__serena__search_for_pattern('visual-test-targets')
```

### Step 2: Baseline Creation (Initial)
```typescript
for (const device of targetDevices) {
  // Device configuration
  await mcp__playwright__browser_resize(device.width, device.height)
  
  // Page access
  await mcp__playwright__browser_navigate(targetUrl)
  await mcp__playwright__browser_wait_for({time: waitTime})
  
  // Disable animations
  if (options.disableAnimations) {
    await mcp__playwright__browser_evaluate(`
      document.querySelectorAll('*').forEach(el => {
        el.style.animationDuration = '0s';
        el.style.transitionDuration = '0s';
      });
    `)
  }
  
  // Take screenshot
  const screenshot = await mcp__playwright__browser_take_screenshot({
    fullPage: options.fullPage,
    filename: `baseline-${device.name}-${pageName}.png`
  })
}
```

### Step 3: Comparison Test Execution
```typescript
// Capture current screen
const currentScreenshot = await captureCurrentState(targetUrl, device)

// Compare with baseline
const comparisonResult = await compareImages(
  baselineImage,
  currentScreenshot,
  {
    threshold: options.threshold,
    ignoreRegions: options.ignoreRegions
  }
)

// Analyze differences
const diffAnalysis = await analyzeDifferences(comparisonResult)
```

### Step 4: Result Analysis & Report Generation
```typescript
// Aggregate test results
const testResults = {
  totalTests: testCount,
  passed: passedCount,
  failed: failedCount,
  differences: detectedDiffs,
  severity: calculateSeverity(detectedDiffs)
}

// Save to Serena memory
await mcp__serena__write_memory('visual-regression-results', {
  timestamp: Date.now(),
  results: testResults,
  baseline: baselineVersion
})
```

## Report Generation Feature (-r option)

### Detailed Report Structure
```markdown
# Visual Regression Test Report

## 📊 Test Overview
- Execution Date: {timestamp}
- Target URLs: {target-urls}
- Test Devices: {device-list}
- Baseline: {baseline-version}

## 🎯 Test Results Summary
- Total Tests: {total-tests}
- Passed: {passed-tests} ✅
- Failed: {failed-tests} ❌
- Differences Detected: {detected-diffs} ⚠️

## 📸 Difference Details

### Breaking Changes
1. **Login Page** - Desktop
   - Difference Rate: 15.2%
   - Impact: Layout breakdown
   - 📷 [Comparison Image](./diffs/login-desktop-diff.png)

### Minor Changes
1. **Dashboard** - Mobile
   - Difference Rate: 2.1%
   - Impact: Color changes
   - 📷 [Comparison Image](./diffs/dashboard-mobile-diff.png)

## 🔧 Recommended Actions
{recommendations}

## 📈 Trend Analysis
{trend-analysis}
```

### Image-Included Reports
- Before/After side-by-side display
- Difference highlight images
- Pixel-level change maps
- Regional impact analysis

## CI/CD Integration

### GitHub Actions Integration
```yaml
name: Visual Regression Test
on: [push, pull_request]

jobs:
  visual-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Start application
        run: npm start &
        
      - name: Wait for application
        run: npx wait-on http://localhost:3000
      
      - name: Run visual tests
        run: /visual-regression http://localhost:3000 -c -r
      
      - name: Upload test results
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: visual-test-results
          path: visual-tests/
```

### Automation Policies
- Mandatory checks before PR merge
- Automatic blocking on failure
- Required review flag settings
- Slack/Teams notification integration

## Advanced Features

### 1. Component Isolation Testing
```bash
# Storybook integration
/visual-regression http://localhost:6006 --storybook --component=Button --states=all

# Generated test cases:
# - Button/Default
# - Button/Primary
# - Button/Secondary
# - Button/Disabled
# - Button/Loading
```

### 2. Animation Support
```typescript
// Animation completion waiting
const animationSettings = {
  disableAnimations: true,
  waitForAnimations: false,
  captureAnimationFrames: false,  // Video capture
  animationTimeout: 5000
}
```

### 3. Dynamic Content Normalization
```typescript
// Dynamic element masking
const normalizationRules = [
  { selector: '.timestamp', replacement: 'MOCKED_TIME' },
  { selector: '.user-id', replacement: 'USER_123' },
  { selector: '.random-uuid', pattern: /[0-9a-f-]{36}/, replacement: 'UUID' }
]
```

## Performance Optimization

### Image Processing Optimization
- Use of compression algorithms
- Acceleration through parallel processing
- Cache feature utilization
- Comparison of difference regions only

### Storage Management
- Automatic deletion of old screenshots
- Space saving through compression
- Cloud storage integration
- Synchronization with version control

## Error Handling

### Common Errors and Solutions

#### Baseline Mismatch Error
```bash
❌ Error: Baseline image not found
Solutions:
1. Create baseline with -b option
2. Check file paths
3. Verify branch settings
```

#### Threshold Exceeded Error
```bash
❌ Error: Difference exceeds threshold (0.2%)
Solutions:
1. Adjust threshold with -t option
2. Update with -a for intentional changes
3. Consider adding ignore regions
```

#### Rendering Error
```bash
❌ Error: Page rendering incomplete
Solutions:
1. Extend wait time with --wait-for option
2. Verify required element loading
3. Investigate JavaScript errors
```

## Limitations & Considerations

### Test Targets
- ✅ Static content
- ✅ CSS/layout changes
- ✅ Responsive design
- ⚠️ Dynamic content (requires configuration)

### Limitations
- ❌ Video/GIF animations
- ❌ Detailed Canvas element comparison
- ❌ 3D/WebGL elements
- ❌ Non-deterministic rendering

## Best Practices

### Effective Test Design
1. **Priority Important Pages**
   - Landing pages
   - Payment/login pages
   - Dashboard screens

2. **Appropriate Threshold Settings**
   - Strict: 0.1-0.2% (important pages)
   - Standard: 0.5-1.0% (general pages)
   - Relaxed: 2.0-5.0% (with dynamic elements)

3. **Maintenance Strategy**
   - Regular baseline updates
   - Delete unnecessary screenshots
   - Analyze and improve test results

### Team Operations
- Baseline update flow for design changes
- Establish review processes
- False positive learning & improvement cycles
- Test expansion when adding new features