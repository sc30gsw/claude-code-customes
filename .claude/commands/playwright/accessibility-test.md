---
allowed-tools: mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_type, mcp__playwright__browser_select_option, mcp__playwright__browser_wait_for, mcp__playwright__browser_evaluate, mcp__playwright__browser_console_messages, mcp__playwright__browser_network_requests, mcp__playwright__browser_handle_dialog, mcp__playwright__browser_close, 
Read, Glob, Grep, Edit, MultiEdit, Write, Bash, TodoWrite, mcp__sequential-thinking__sequentialthinking, mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory
description: Accessibility testing and WCAG compliance verification command using Playwright MCP (Serena integration)
---

# Accessibility Test - Web Accessibility Testing

## Overview

A command that integrates Playwright MCP with Serena tools to automatically perform WCAG 2.1/2.2 compliance accessibility verification.

## Usage

### Basic Syntax
```bash
/accessibility-test <target> [options]
```

### Target Specification

| Target Type | Example | Description |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | Test development app |
| **Production URL** | `https://myapp.com` | Test production environment |
| **Page Path** | `/form`, `/dashboard` | Test specific pages |
| **Component** | `Modal`, `Form` | Component-level testing |

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-l, --level` | WCAG compliance level | AA |
| `-s, --standard` | WCAG version | 2.1 |
| `-k, --keyboard` | Keyboard navigation testing | true |
| `-c, --color` | Color and contrast testing | true |
| `-t, --text` | Text and screen reader testing | true |
| `-f, --focus` | Focus management testing | true |
| `-a, --aria` | ARIA attributes testing | true |
| `-r, --report` | Generate detailed report | false |
| `-i, --interactive` | Interactive fix mode | false |
| `-m, --mobile` | Mobile accessibility testing | false |
| `--screen-reader` | Screen reader simulation | false |
| `--auto-fix` | Automatic fix suggestions | false |

### Usage Examples

```bash
# Basic accessibility testing
/accessibility-test http://localhost:3000

# Strict WCAG AAA compliance test
/accessibility-test /form -l AAA -s 2.2 -r

# Keyboard navigation focused test
/accessibility-test /dashboard -k -f --screen-reader

# Mobile accessibility testing
/accessibility-test https://myapp.com -m -c -t

# Interactive fix mode
/accessibility-test /signup -i --auto-fix -r

# Component-level testing
/accessibility-test /storybook --component=Modal -a -f
```

## Feature Details

### 1. WCAG Compliance Check

#### Supported Standard Levels
```typescript
enum WCAGLevel {
  A = 'A',        // Minimum requirements
  AA = 'AA',      // Standard requirements (recommended)
  AAA = 'AAA'     // Highest level requirements
}

enum WCAGVersion {
  'WCAG_2_0' = '2.0',
  'WCAG_2_1' = '2.1',  // Recommended
  'WCAG_2_2' = '2.2'   // Latest
}
```

#### Validation Categories
1. **Perceivable**
   - Alternative text for images
   - Captions and descriptions for videos/audio
   - Information presentation not relying solely on color
   - Adequate contrast ratios

2. **Operable**
   - Keyboard accessibility
   - Avoiding content that causes seizures
   - Appropriate timeout settings
   - Navigation assistance

3. **Understandable**
   - Readable language usage
   - Predictable functionality
   - Input error identification and correction assistance

4. **Robust**
   - Compatibility with assistive technologies
   - Adaptation to future technology changes

### 2. Keyboard Navigation Testing (-k option)

#### Test Target Operations
```typescript
const keyboardTests = [
  // Basic navigation
  { key: 'Tab', action: 'Focus movement (forward)' },
  { key: 'Shift+Tab', action: 'Focus movement (backward)' },
  { key: 'Enter', action: 'Activation' },
  { key: 'Space', action: 'Button/checkbox operation' },
  
  // Arrow key navigation
  { key: 'ArrowUp', action: 'Menu/list up movement' },
  { key: 'ArrowDown', action: 'Menu/list down movement' },
  { key: 'ArrowLeft', action: 'Tab/carousel left movement' },
  { key: 'ArrowRight', action: 'Tab/carousel right movement' },
  
  // Escape and exit operations
  { key: 'Escape', action: 'Close modal/menu' },
  { key: 'Home', action: 'Jump to first element' },
  { key: 'End', action: 'Jump to last element' }
]
```

#### Focus Management Testing
```typescript
// Focus trap validation
async function testFocusTrap(modalSelector: string) {
  // Open modal
  await mcp__playwright__browser_click(modalSelector)
  
  // Verify focus is on first element
  const firstFocusable = await getFirstFocusableElement()
  expect(document.activeElement).toBe(firstFocusable)
  
  // Navigate to last element with Tab
  await navigateToLastElement()
  
  // Verify Tab returns to first element
  await mcp__playwright__browser_press_key('Tab')
  expect(document.activeElement).toBe(firstFocusable)
  
  // Verify Escape closes modal
  await mcp__playwright__browser_press_key('Escape')
  expect(document.querySelector('.modal')).toBeNull()
}
```

### 3. Color and Contrast Testing (-c option)

#### Contrast Ratio Calculation
```typescript
interface ContrastTest {
  element: Element
  foregroundColor: string
  backgroundColor: string
  ratio: number
  wcagLevel: 'AA' | 'AAA'
  passed: boolean
}

// WCAG standards
const contrastRequirements = {
  normalText: {
    AA: 4.5,
    AAA: 7.0
  },
  largeText: {
    AA: 3.0,
    AAA: 4.5
  },
  nonTextElements: {
    AA: 3.0,
    AAA: 3.0  // UI components, graphic elements
  }
}
```

#### Color Dependency Check
```typescript
// Detection of information presentation relying solely on color
const colorDependencyTests = [
  {
    issue: 'Required fields shown only in red color',
    fix: 'Add asterisk (*) or aria-required attribute'
  },
  {
    issue: 'Error state shown only by color change',
    fix: 'Add error icon or text message'
  },
  {
    issue: 'Status distinguished only by color',
    fix: 'Use label text or icons in combination'
  }
]
```

### 4. ARIA Attributes Testing (-a option)

#### Required ARIA Attributes Check
```typescript
const ariaValidationRules = [
  // Landmarks
  { role: 'main', required: true, unique: true },
  { role: 'navigation', required: false, multiple: true },
  { role: 'banner', required: true, unique: true },
  { role: 'contentinfo', required: true, unique: true },
  
  // Interactive elements
  { role: 'button', requiredProps: ['aria-label', 'accessible-name'] },
  { role: 'link', requiredProps: ['accessible-name'] },
  { role: 'textbox', requiredProps: ['aria-label'] },
  
  // State management
  { attribute: 'aria-expanded', validValues: ['true', 'false'] },
  { attribute: 'aria-checked', validValues: ['true', 'false', 'mixed'] },
  { attribute: 'aria-selected', validValues: ['true', 'false'] }
]
```

#### Semantic Structure Validation
```typescript
// Heading hierarchy validation
function validateHeadingHierarchy() {
  const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6')
  const issues: string[] = []
  
  let previousLevel = 0
  headings.forEach((heading, index) => {
    const currentLevel = parseInt(heading.tagName.charAt(1))
    
    if (index === 0 && currentLevel !== 1) {
      issues.push('First heading must be h1')
    }
    
    if (currentLevel - previousLevel > 1) {
      issues.push(`Heading level skipped: h${previousLevel} → h${currentLevel}`)
    }
    
    previousLevel = currentLevel
  })
  
  return issues
}
```

### 5. Screen Reader Simulation (--screen-reader option)

#### Screen Reader Text Generation
```typescript
async function generateScreenReaderText(element: Element): Promise<string> {
  const computedName = await mcp__playwright__browser_evaluate(`
    const element = arguments[0];
    
    // Accessible name calculation
    function computeAccessibleName(el) {
      // aria-labelledby priority
      if (el.hasAttribute('aria-labelledby')) {
        const ids = el.getAttribute('aria-labelledby').split(' ');
        return ids.map(id => document.getElementById(id)?.textContent).join(' ');
      }
      
      // aria-label
      if (el.hasAttribute('aria-label')) {
        return el.getAttribute('aria-label');
      }
      
      // Form element labels
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        const label = document.querySelector(\`label[for="\${el.id}"]\`);
        if (label) return label.textContent;
      }
      
      // Text content
      return el.textContent || el.alt || '';
    }
    
    return computeAccessibleName(element);
  `, element)
  
  return computedName
}
```

#### Navigation Experience Simulation
```typescript
// Screen reader page navigation
async function simulateScreenReaderNavigation() {
  const landmarks = await findLandmarks()
  const headings = await findHeadings()
  const links = await findLinks()
  
  return {
    landmarks: landmarks.map(l => ({
      role: l.role,
      label: l.accessibleName,
      position: l.position
    })),
    headingStructure: generateHeadingOutline(headings),
    linkList: links.map(l => ({
      text: l.accessibleName,
      url: l.href,
      context: l.context
    }))
  }
}
```

### 6. Serena Integration Features

#### Component Analysis Integration
```typescript
// Accessibility pattern learning
async function learnAccessibilityPatterns() {
  const components = await mcp__serena__get_symbols_overview()
  
  // Identify accessibility patterns in commonly used components
  const patterns = analyzeAccessibilityPatterns(components)
  
  await mcp__serena__write_memory('accessibility-patterns', {
    common_violations: patterns.violations,
    best_practices: patterns.bestPractices,
    component_templates: patterns.templates
  })
}
```

#### Fix Suggestion Generation
```typescript
// Fix suggestions using Serena knowledge
async function generateFixSuggestions(violations: AccessibilityViolation[]) {
  const knownPatterns = await mcp__serena__read_memory('accessibility-patterns')
  
  return violations.map(violation => ({
    issue: violation.description,
    severity: violation.impact,
    fixSuggestion: generateContextualFix(violation, knownPatterns),
    codeExample: generateCodeExample(violation.type),
    resources: getRelevantResources(violation.wcagRule)
  }))
}
```

### 7. Auto-Fix Feature (--auto-fix option)

#### Automatic Minor Issue Fixes
```typescript
const autoFixRules = [
  {
    issue: 'Missing alt attribute',
    fix: (img: HTMLImageElement) => {
      if (img.src.includes('decorative') || img.classList.contains('decoration')) {
        img.alt = '' // Decorative image
      } else {
        img.alt = generateAltText(img.src) // AI/rule-based generation
      }
    }
  },
  {
    issue: 'Missing form labels',
    fix: (input: HTMLInputElement) => {
      if (!input.labels?.length && !input.getAttribute('aria-label')) {
        const label = createLabel(input)
        input.parentNode?.insertBefore(label, input)
      }
    }
  }
]
```

#### Interactive Fix Mode (-i option)
```bash
# Interactive fix suggestion selection
Found 12 accessibility issues:

1. [CRITICAL] Button missing accessible name
   Location: .header .user-menu button
   Fix options:
   a) Add aria-label="User menu"
   b) Add visible text content
   c) Use aria-labelledby reference
   Choice [a/b/c/skip]: a

2. [HIGH] Image missing alt text
   Location: .hero img
   Suggested alt: "Team collaboration dashboard screenshot"
   Accept? [y/n/edit]: edit
   Enter alt text: Professional team using our collaboration platform
```

## Implementation Workflow

### Step 1: Initial Analysis and Setup
```typescript
// Project analysis with Serena
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// Identify accessibility test targets
const testTargets = await mcp__serena__search_for_pattern('accessibility-critical')
```

### Step 2: Page Access and Initial Evaluation
```typescript
// Page access
await mcp__playwright__browser_navigate(targetUrl)
await mcp__playwright__browser_wait_for({time: 3})

// Inject axe-core library
await mcp__playwright__browser_evaluate(`
  const script = document.createElement('script');
  script.src = 'https://unpkg.com/axe-core@latest/axe.min.js';
  document.head.appendChild(script);
`)

// Initial accessibility inspection
const snapshot = await mcp__playwright__browser_snapshot()
```

### Step 3: Category-based Test Execution
```typescript
// Keyboard navigation testing
if (options.keyboard) {
  const keyboardResults = await runKeyboardTests()
}

// Color and contrast testing
if (options.color) {
  const colorResults = await runColorContrastTests()
}

// ARIA attributes testing
if (options.aria) {
  const ariaResults = await runAriaTests()
}
```

### Step 4: Comprehensive Analysis and Report Generation
```typescript
// Results integration
const comprehensiveResults = {
  summary: generateSummary(allResults),
  violations: categorizeViolations(allResults),
  recommendations: generateRecommendations(allResults),
  fixSuggestions: await generateFixSuggestions(violations)
}

// Save to Serena memory
await mcp__serena__write_memory('accessibility-test-results', {
  url: targetUrl,
  timestamp: Date.now(),
  results: comprehensiveResults
})
```

## Report Generation Feature (-r option)

### Detailed Report Structure
```markdown
# Accessibility Test Report

## 📊 Test Overview
- Target URL: {target-url}
- WCAG Standard: {wcag-version} Level {level}
- Test Date: {timestamp}
- Overall Score: {score}/100

## 🎯 Test Results Summary
- 🔴 Critical Issues: {critical-count}
- 🟡 Serious Issues: {serious-count}
- 🔵 Minor Issues: {moderate-count}
- ✅ Compliant Items: {passed-count}

## 🔥 Critical Issues

### 1. Keyboard Inaccessible
**Issue**: Main navigation is not accessible via keyboard
**Location**: `.main-nav .dropdown`
**WCAG**: 2.1.1 Keyboard (Level A)
**Fix Method**:
```html
<!-- Before -->
<div class="dropdown" onclick="toggleMenu()">

<!-- After -->
<button class="dropdown" onclick="toggleMenu()" 
        onkeydown="handleKeyDown(event)"
        aria-expanded="false"
        aria-haspopup="true">
```

### 2. Insufficient Contrast Ratio
**Issue**: Text contrast ratio with background is 3.2:1, below the standard 4.5:1
**Location**: `.secondary-text`
**WCAG**: 1.4.3 Contrast (Level AA)
**Fix Method**: Change text color from #666666 to #484848

## 🛠️ Auto-Fixed Items
{auto-fixed-items}

## 📋 Implementation Checklist
- [ ] Add alt attributes to all images
- [ ] Associate labels with form elements
- [ ] Fix heading hierarchy (h2→h3→h4)
- [ ] Improve focus indication
- [ ] Notify status updates via aria-live regions

## 📈 Improvement Trends
{improvement-trends}
```

### Scoring System
```typescript
interface AccessibilityScore {
  overall: number          // 0-100 overall score
  keyboard: number         // Keyboard accessibility
  visual: number          // Visual accessibility
  cognitive: number       // Cognitive accessibility
  technical: number       // Technical implementation quality
}

// Score calculation
function calculateScore(results: TestResults): AccessibilityScore {
  const weights = {
    critical: -20,
    serious: -10,
    moderate: -3,
    minor: -1
  }
  
  return {
    overall: Math.max(0, 100 + calculatePenalty(results, weights)),
    keyboard: calculateCategoryScore(results.keyboard),
    visual: calculateCategoryScore(results.visual),
    cognitive: calculateCategoryScore(results.cognitive),
    technical: calculateCategoryScore(results.technical)
  }
}
```

## CI/CD Integration

### GitHub Actions Integration
```yaml
name: Accessibility Test
on: [push, pull_request]

jobs:
  a11y-test:
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
      
      - name: Run accessibility tests
        run: /accessibility-test http://localhost:3000 -l AA -r
      
      - name: Upload accessibility report
        uses: actions/upload-artifact@v3
        with:
          name: accessibility-report
          path: accessibility-report.html
      
      - name: Comment PR with results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('accessibility-summary.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

### Quality Gate Settings
```yaml
# Minimum quality standards
accessibility_gates:
  min_score: 85
  max_critical_issues: 0
  max_serious_issues: 2
  required_wcag_level: AA
```

## Advanced Features

### 1. Dynamic Content Testing
```typescript
// SPA routing accessibility testing
async function testSPAAccessibility(routes: string[]) {
  for (const route of routes) {
    await mcp__playwright__browser_navigate(route)
    
    // Check page change announcements
    const announcements = await checkRouteAnnouncements()
    
    // Check focus management
    const focusManagement = await checkFocusManagement()
    
    // Check live regions
    const liveRegions = await checkLiveRegions()
  }
}
```

### 2. Form Validation Accessibility
```typescript
// Form error accessibility testing
async function testFormAccessibility() {
  // Required field marking
  const requiredFields = await checkRequiredFieldsMarking()
  
  // Error message association
  const errorAssociation = await checkErrorAssociation()
  
  // Validation timing
  const validationTiming = await checkValidationTiming()
  
  // Success state notification
  const successNotification = await checkSuccessNotification()
}
```

### 3. Rich Content Support
```typescript
// Carousel and tab accessibility
const richContentTests = {
  carousel: {
    ariaLive: 'polite',
    controls: ['previous', 'next', 'pause'],
    indicators: 'aria-selected',
    autoplay: 'user-controlled'
  },
  tabs: {
    keyboardNav: 'arrow-keys',
    roving: 'tabindex',
    panels: 'aria-labelledby'
  },
  modal: {
    focusTrap: 'required',
    escapeKey: 'closes',
    returnFocus: 'to-trigger'
  }
}
```

## Performance Considerations

### Test Execution Time Optimization
- Parallel test execution
- Speed improvement through cache utilization
- Selective execution of necessary tests only
- Gradual testing (Critical → Serious → Moderate)

### Resource Usage Management
- Memory-efficient DOM analysis
- Avoiding unnecessary library loading
- Compressed storage of result data

## Limitations and Considerations

### Testable Scope
- ✅ Static HTML and CSS
- ✅ JavaScript dynamic content
- ✅ Forms and interactions
- ⚠️ Complex custom widgets

### Difficult to Detect Issues
- ❌ Cognitive load problems
- ❌ Subjective readability assessment
- ❌ Complex workflow usability
- ❌ Real device assistive technology behavior

## Best Practices

### Continuous Improvement
1. **Regular Test Execution**
   - Integration into CI/CD pipeline
   - Mandatory checks before release
   - Regular full-page scanning

2. **Team Education**
   - Share accessibility guidelines
   - Build knowledge base for fixes
   - Standardize internal best practices

3. **User Testing**
   - Testing with actual assistive technology users
   - Usability testing considering diversity
   - Continuous feedback integration