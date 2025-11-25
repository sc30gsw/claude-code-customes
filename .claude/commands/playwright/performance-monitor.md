---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_evaluate, mcp__playwright__browser_network_requests, mcp__playwright__browser_console_messages, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_wait_for
description: Performance monitoring and Core Web Vitals measurement command using Playwright MCP
---

# Performance Monitor - Performance Monitoring

## Overview

A command that integrates Playwright MCP with Serena tools to automatically perform web application performance measurement and optimization suggestions.

## Usage

### Basic Syntax
```bash
/performance-monitor <target> [options]
```

### Target Specification

| Target Type | Example | Description |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | Test development app |
| **Production URL** | `https://myapp.com` | Production environment monitoring |
| **Page Path** | `/dashboard`, `/checkout` | Specific page measurement |
| **User Flow** | `login-flow`, `purchase-flow` | Complete flow measurement |

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-v, --vitals` | Core Web Vitals measurement | true |
| `-l, --lighthouse` | Run Lighthouse audit | false |
| `-n, --network` | Detailed network analysis | false |
| `-j, --javascript` | JavaScript execution time analysis | false |
| `-m, --memory` | Memory usage monitoring | false |
| `-c, --cpu` | CPU usage measurement | false |
| `-r, --runs` | Number of measurement runs | 3 |
| `-d, --device` | Device condition setting | desktop |
| `-t, --throttling` | Network/CPU throttling | none |
| `--report` | Generate detailed report | false |
| `--baseline` | Baseline comparison | false |
| `--alerts` | Threshold alert settings | false |

### Usage Examples

```bash
# Basic performance measurement
/performance-monitor http://localhost:3000

# Core Web Vitals + Lighthouse audit
/performance-monitor /dashboard -v -l --report

# Detailed performance analysis
/performance-monitor /checkout -n -j -m -c

# Mobile environment measurement
/performance-monitor https://myapp.com -d mobile -t "slow-3g"

# Multiple runs for reliability
/performance-monitor /api-heavy-page -r 10 --baseline

# Monitoring with alerts
/performance-monitor https://production.com --alerts --report
```

## Feature Details

### 1. Core Web Vitals Measurement (-v option)

#### Measurement Metrics
```typescript
interface CoreWebVitals {
  // Page load performance
  LCP: number      // Largest Contentful Paint (ms)
  
  // Interactivity
  FID: number      // First Input Delay (ms)
  INP: number      // Interaction to Next Paint (ms)
  
  // Visual stability
  CLS: number      // Cumulative Layout Shift (score)
  
  // Loading speed
  FCP: number      // First Contentful Paint (ms)
  TTFB: number     // Time to First Byte (ms)
}
```

#### Evaluation by Google Standards
```typescript
const webVitalsThresholds = {
  LCP: { good: 2500, needsImprovement: 4000 },
  FID: { good: 100, needsImprovement: 300 },
  INP: { good: 200, needsImprovement: 500 },
  CLS: { good: 0.1, needsImprovement: 0.25 },
  FCP: { good: 1800, needsImprovement: 3000 },
  TTFB: { good: 800, needsImprovement: 1800 }
}

function evaluateScore(metric: string, value: number): 'good' | 'needs-improvement' | 'poor' {
  const threshold = webVitalsThresholds[metric]
  if (value <= threshold.good) return 'good'
  if (value <= threshold.needsImprovement) return 'needs-improvement'
  return 'poor'
}
```

### 2. Lighthouse Audit (-l option)

#### Audit Categories
```typescript
interface LighthouseAudit {
  performance: {
    score: number    // 0-100 performance score
    metrics: {
      firstContentfulPaint: number
      largestContentfulPaint: number
      firstMeaningfulPaint: number
      speedIndex: number
      totalBlockingTime: number
    }
  }
  accessibility: {
    score: number
    violations: AccessibilityViolation[]
  }
  bestPractices: {
    score: number
    issues: BestPracticeIssue[]
  }
  seo: {
    score: number
    recommendations: SEORecommendation[]
  }
}
```

#### Identifying Optimization Opportunities
```typescript
const optimizationOpportunities = [
  {
    audit: 'unused-css-rules',
    impact: 'high',
    description: 'Removing unused CSS can reduce ~500KB'
  },
  {
    audit: 'efficient-animated-content',
    impact: 'medium',
    description: 'Animation optimization reduces rendering load'
  },
  {
    audit: 'offscreen-images',
    impact: 'high',
    description: 'Lazy loading can reduce initial load by ~2 seconds'
  }
]
```

### 3. Network Analysis (-n option)

#### Resource Analysis
```typescript
interface NetworkAnalysis {
  totalRequests: number
  totalBytes: number
  requestsByType: {
    document: ResourceMetrics
    stylesheet: ResourceMetrics
    script: ResourceMetrics
    image: ResourceMetrics
    font: ResourceMetrics
    xhr: ResourceMetrics
  }
  waterfall: RequestWaterfall[]
  criticalPath: CriticalPathAnalysis
}

interface ResourceMetrics {
  count: number
  size: number
  loadTime: number
  cacheHitRate: number
}
```

#### Bottleneck Identification
```typescript
// Identify slow requests
function identifySlowRequests(requests: NetworkRequest[]): SlowRequest[] {
  return requests
    .filter(req => req.duration > 1000)
    .sort((a, b) => b.duration - a.duration)
    .map(req => ({
      url: req.url,
      duration: req.duration,
      size: req.responseBodySize,
      recommendation: generateRecommendation(req)
    }))
}
```

### 4. JavaScript Execution Analysis (-j option)

#### Performance Profiling
```typescript
interface JavaScriptAnalysis {
  mainThreadBlocking: number
  scriptEvaluationTime: number
  parseTime: number
  executeTime: number
  heavyTasks: HeavyTask[]
  memoryUsage: MemoryProfile
}

interface HeavyTask {
  function: string
  duration: number
  category: 'parsing' | 'compilation' | 'execution' | 'gc'
  recommendation: string
}
```

#### Performance Bottleneck Detection
```typescript
// Detect heavy JavaScript processing
async function analyzeJavaScriptPerformance() {
  const performanceEntries = await mcp__playwright__browser_evaluate(`
    // Performance Observer for Long Tasks
    const longTasks = [];
    
    new PerformanceObserver((list) => {
      list.getEntries().forEach((entry) => {
        if (entry.duration > 50) {
          longTasks.push({
            name: entry.name,
            duration: entry.duration,
            startTime: entry.startTime
          });
        }
      });
    }).observe({entryTypes: ['longtask', 'measure']});
    
    // Memory usage
    const memoryInfo = performance.memory ? {
      used: performance.memory.usedJSHeapSize,
      total: performance.memory.totalJSHeapSize,
      limit: performance.memory.jsHeapSizeLimit
    } : null;
    
    return { longTasks, memoryInfo };
  `)
  
  return performanceEntries
}
```

### 5. Memory Usage Monitoring (-m option)

#### Memory Profile
```typescript
interface MemoryProfile {
  heapUsed: number
  heapTotal: number
  heapLimit: number
  external: number
  arrayBuffers: number
  
  // Garbage collection information
  gcEvents: GCEvent[]
  memoryLeaks: MemoryLeak[]
}

interface MemoryLeak {
  type: 'event-listener' | 'dom-reference' | 'closure' | 'timer'
  description: string
  impact: 'low' | 'medium' | 'high'
  recommendation: string
}
```

#### Memory Leak Detection
```typescript
// Detect memory leaks
async function detectMemoryLeaks() {
  const initialMemory = await measureMemoryUsage()
  
  // Execute user actions
  await simulateUserInteractions()
  
  const finalMemory = await measureMemoryUsage()
  
  // Analyze memory growth
  const memoryGrowth = finalMemory.heapUsed - initialMemory.heapUsed
  
  if (memoryGrowth > MEMORY_LEAK_THRESHOLD) {
    return analyzeMemoryGrowth(initialMemory, finalMemory)
  }
}
```

### 6. Serena Integration Features

#### Codebase Analysis Integration
```typescript
// Identify performance-critical components
async function identifyPerformanceCriticalComponents() {
  const components = await mcp__serena__get_symbols_overview()
  
  // Search for heavy component patterns
  const heavyComponents = await mcp__serena__search_for_pattern([
    'useState.*array.*length.*1000',
    'useEffect.*dependencies.*length.*10',
    'heavy.*computation',
    'large.*data.*processing'
  ])
  
  return analyzeComponentPerformanceImpact(components, heavyComponents)
}
```

#### Optimization Suggestion Generation
```typescript
// Generate optimization suggestions using Serena knowledge
async function generateOptimizationSuggestions(performanceData: PerformanceMetrics) {
  const pastOptimizations = await mcp__serena__read_memory('performance-optimizations')
  
  const suggestions = analyzeOptimizationOpportunities(performanceData, pastOptimizations)
  
  // Save as learning data
  await mcp__serena__write_memory('performance-analysis', {
    timestamp: Date.now(),
    metrics: performanceData,
    suggestions: suggestions,
    context: await mcp__serena__get_symbols_overview()
  })
  
  return suggestions
}
```

### 7. Baseline Comparison (--baseline option)

#### Continuous Performance Monitoring
```typescript
interface PerformanceBaseline {
  timestamp: number
  version: string
  metrics: CoreWebVitals
  environment: {
    device: string
    network: string
    location: string
  }
}

// Performance trend analysis
function analyzePerformanceTrends(current: PerformanceMetrics, baselines: PerformanceBaseline[]) {
  const trends = {
    LCP: calculateTrend(baselines.map(b => b.metrics.LCP), current.LCP),
    FID: calculateTrend(baselines.map(b => b.metrics.FID), current.FID),
    CLS: calculateTrend(baselines.map(b => b.metrics.CLS), current.CLS)
  }
  
  return {
    improving: trends.filter(t => t.direction === 'improving'),
    degrading: trends.filter(t => t.direction === 'degrading'),
    stable: trends.filter(t => t.direction === 'stable')
  }
}
```

### 8. Alert Features (--alerts option)

#### Threshold Monitoring
```typescript
interface PerformanceAlert {
  metric: string
  currentValue: number
  threshold: number
  severity: 'warning' | 'critical'
  message: string
  recommendations: string[]
}

const alertRules = [
  {
    metric: 'LCP',
    warningThreshold: 2500,
    criticalThreshold: 4000,
    message: 'Page load speed is degrading'
  },
  {
    metric: 'CLS',
    warningThreshold: 0.1,
    criticalThreshold: 0.25,
    message: 'Layout shift is occurring'
  }
]
```

## Implementation Workflow

### Step 1: Environment Setup and Preparation
```typescript
// Project analysis with Serena
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// Identify performance measurement targets
const criticalPaths = await mcp__serena__search_for_pattern('performance-critical')
```

### Step 2: Page Access and Initial Measurement
```typescript
// Page access
await mcp__playwright__browser_navigate(targetUrl)

// Performance Observer setup
await mcp__playwright__browser_evaluate(`
  window.performanceMetrics = {};
  
  // Web Vitals measurement
  new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
      window.performanceMetrics[entry.name] = entry.value;
    });
  }).observe({entryTypes: ['paint', 'navigation', 'measure']});
  
  // Layout Shift measurement
  new PerformanceObserver((list) => {
    let cls = 0;
    list.getEntries().forEach((entry) => {
      if (!entry.hadRecentInput) {
        cls += entry.value;
      }
    });
    window.performanceMetrics.CLS = cls;
  }).observe({entryTypes: ['layout-shift']});
`)
```

### Step 3: Detailed Metrics Collection
```typescript
// Core Web Vitals measurement
const webVitals = await measureCoreWebVitals()

// Network analysis
if (options.network) {
  const networkData = await mcp__playwright__browser_network_requests()
  const networkAnalysis = analyzeNetworkPerformance(networkData)
}

// JavaScript analysis
if (options.javascript) {
  const jsAnalysis = await analyzeJavaScriptPerformance()
}

// Memory analysis
if (options.memory) {
  const memoryProfile = await profileMemoryUsage()
}
```

### Step 4: Lighthouse Audit Execution (-l option)
```typescript
// Execute Lighthouse audit
const lighthouseResult = await runLighthouseAudit(targetUrl, {
  device: options.device,
  throttling: options.throttling,
  categories: ['performance', 'accessibility', 'best-practices', 'seo']
})
```

### Step 5: Data Analysis and Optimization Suggestions
```typescript
// Comprehensive analysis
const comprehensiveAnalysis = {
  coreWebVitals: webVitals,
  lighthouse: lighthouseResult,
  network: networkAnalysis,
  javascript: jsAnalysis,
  memory: memoryProfile
}

// Optimization suggestions using Serena
const optimizationSuggestions = await generateOptimizationSuggestions(comprehensiveAnalysis)

// Save results
await mcp__serena__write_memory('performance-monitoring', {
  url: targetUrl,
  timestamp: Date.now(),
  analysis: comprehensiveAnalysis,
  suggestions: optimizationSuggestions
})
```

## Report Generation Feature (--report option)

### Detailed Report Structure
```markdown
# Performance Monitoring Report

## 📊 Overview
- Target: {target-url}
- Measurement Date: {timestamp}
- Device: {device-type}
- Network: {network-condition}

## 🚀 Core Web Vitals

### Largest Contentful Paint (LCP)
- **Current Value**: 1,847ms ✅ Good
- **Target**: < 2,500ms
- **Improvement**: -340ms from previous

### First Input Delay (FID)
- **Current Value**: 12ms ✅ Good
- **Target**: < 100ms

### Cumulative Layout Shift (CLS)
- **Current Value**: 0.06 ✅ Good
- **Target**: < 0.1

## ⚡ Lighthouse Scores
- **Performance**: 89/100 ✅
- **Accessibility**: 92/100 ✅
- **Best Practices**: 87/100 ⚠️
- **SEO**: 100/100 ✅

## 🔍 Detailed Analysis

### Network Optimization
- Total requests: 47
- Total data size: 1.2MB
- **Improvement Suggestions**:
  1. Image optimization can reduce 500KB
  2. Unused CSS removal can reduce 200KB

### JavaScript Performance
- Main thread blocking time: 230ms
- **Heavy Processing**:
  1. Data processing library (120ms)
  2. Chart rendering (85ms)

### Memory Usage
- Heap usage: 45MB / 128MB
- **Memory Leaks**: None detected ✅

## 🎯 Optimization Recommendations

### High Priority
1. **Implement Image Lazy Loading**
   - Effect: -800ms LCP reduction
   - Implementation difficulty: Low
   
2. **Remove Unused JavaScript**
   - Effect: -400ms FCP reduction
   - Implementation difficulty: Medium

### Medium Priority
3. **Consider CDN Implementation**
   - Effect: -200ms TTFB reduction
   - Implementation difficulty: Medium

## 📈 Trend Analysis
{performance-trends}

## 🔧 Code Improvement Suggestions
{code-optimization-suggestions}
```

### Graphical Reports
```typescript
// Performance chart generation
const performanceChart = {
  type: 'line',
  data: {
    labels: timestamps,
    datasets: [
      {
        label: 'LCP',
        data: lcpValues,
        borderColor: 'rgb(75, 192, 192)'
      },
      {
        label: 'FID',
        data: fidValues,
        borderColor: 'rgb(255, 99, 132)'
      }
    ]
  }
}
```

## Continuous Monitoring and CI/CD Integration

### GitHub Actions Integration
```yaml
name: Performance Monitoring
on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  push:
    branches: [main]

jobs:
  performance-test:
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
      
      - name: Run performance monitoring
        run: |
          /performance-monitor http://localhost:3000 \
            -v -l -n -j --report --baseline --alerts
      
      - name: Performance Budget Check
        run: |
          if [ $(cat performance-report.json | jq '.lighthouse.performance.score') -lt 80 ]; then
            echo "Performance score below threshold"
            exit 1
          fi
      
      - name: Upload performance report
        uses: actions/upload-artifact@v3
        with:
          name: performance-report
          path: performance-report.html
      
      - name: Slack notification
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: custom
          custom_payload: |
            {
              text: "Performance regression detected",
              attachments: [{
                color: "danger",
                fields: [{
                  title: "Performance Score",
                  value: "${{ env.PERFORMANCE_SCORE }}",
                  short: true
                }]
              }]
            }
```

### Performance Budget
```json
{
  "budget": {
    "lcp": 2500,
    "fid": 100,
    "cls": 0.1,
    "lighthouse_performance": 80,
    "bundle_size": 1048576,
    "requests_count": 50
  },
  "alerts": {
    "slack_webhook": "https://hooks.slack.com/...",
    "email": ["team@example.com"],
    "pagerduty": "integration-key"
  }
}
```

## Advanced Features

### 1. User Flow Measurement
```typescript
// Performance measurement across multiple pages
async function measureUserJourney(flowSteps: FlowStep[]) {
  let journeyMetrics = []
  
  for (const step of flowSteps) {
    await mcp__playwright__browser_navigate(step.url)
    
    if (step.interactions) {
      await performInteractions(step.interactions)
    }
    
    const stepMetrics = await measureStepPerformance()
    journeyMetrics.push({
      step: step.name,
      metrics: stepMetrics,
      timestamp: Date.now()
    })
  }
  
  return analyzeJourneyPerformance(journeyMetrics)
}
```

### 2. Real User Monitoring (RUM)
```typescript
// RUM data collection setup
const rumScript = `
(function() {
  // Navigation Timing
  window.addEventListener('load', function() {
    const navigation = performance.getEntriesByType('navigation')[0];
    
    // Real User Metrics
    const rumData = {
      loadTime: navigation.loadEventEnd - navigation.fetchStart,
      domComplete: navigation.domComplete - navigation.fetchStart,
      firstByte: navigation.responseStart - navigation.fetchStart,
      userAgent: navigator.userAgent,
      timestamp: Date.now()
    };
    
    // Send data
    fetch('/api/rum', {
      method: 'POST',
      body: JSON.stringify(rumData)
    });
  });
})();
`
```

### 3. A/B Test Performance Comparison
```typescript
// Compare A/B test performance
async function compareABTestPerformance(variantA: string, variantB: string) {
  const resultA = await measurePerformance(variantA)
  const resultB = await measurePerformance(variantB)
  
  return {
    winner: determinePerformanceWinner(resultA, resultB),
    improvements: calculateImprovements(resultA, resultB),
    significance: calculateStatisticalSignificance(resultA, resultB)
  }
}
```

## Performance Optimization

### Batch Processing and Parallel Execution
```typescript
// Parallel measurement of multiple pages
async function measureMultiplePages(urls: string[]) {
  const batchSize = 3
  const results = []
  
  for (let i = 0; i < urls.length; i += batchSize) {
    const batch = urls.slice(i, i + batchSize)
    const batchResults = await Promise.all(
      batch.map(url => measurePerformance(url))
    )
    results.push(...batchResults)
  }
  
  return results
}
```

### Cache Optimization
```typescript
// Cache measurement results
const performanceCache = new Map()

async function cachedPerformanceMeasurement(url: string, options: MeasureOptions) {
  const cacheKey = `${url}-${JSON.stringify(options)}`
  
  if (performanceCache.has(cacheKey)) {
    const cached = performanceCache.get(cacheKey)
    if (Date.now() - cached.timestamp < CACHE_TTL) {
      return cached.data
    }
  }
  
  const result = await measurePerformance(url, options)
  performanceCache.set(cacheKey, {
    data: result,
    timestamp: Date.now()
  })
  
  return result
}
```

## Error Handling

### Common Errors and Solutions

#### Measurement Timeout Error
```bash
❌ Error: Performance measurement timed out
Solutions:
1. Extend time with --timeout option
2. Check network environment
3. Execute measurements in stages
```

#### Memory Shortage Error
```bash
❌ Error: Measurement failed due to memory shortage
Solutions:
1. Reduce number of runs (-r option)
2. Disable detailed analysis
3. Reduce batch size
```

#### Lighthouse Execution Error
```bash
❌ Error: Lighthouse audit failed
Solutions:
1. Check Chrome version
2. Run in headless mode
3. Limit audit categories
```

## Limitations and Considerations

### Measurement Environment Considerations
- Network environment variations
- System resource impact
- Browser cache state
- External service response times

### Improving Measurement Accuracy
- Ensure reliability through multiple measurements
- Measure under consistent environment conditions
- Eliminate external factors
- Analysis using statistical methods

## Best Practices

### Effective Measurement Strategy
1. **Priority Measurement of Important Pages**
   - Landing pages
   - Conversion pages
   - Key feature pages

2. **Implement Continuous Monitoring**
   - CI/CD pipeline integration
   - Regular automated measurements
   - Set performance budgets

3. **Establish Improvement Cycle**
   - Measure → Analyze → Improve → Re-measure
   - Implement optimizations gradually
   - Measure and verify effectiveness

### Team Operations
- Share performance standards
- Hold regular review meetings
- Prioritize improvement suggestions
- Accumulate knowledge and expertise