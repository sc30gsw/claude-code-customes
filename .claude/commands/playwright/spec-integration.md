---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_console_messages, mcp__playwright__browser_network_requests, Glob, Grep
description: Integration specification and usage guide for Playwright MCP integrated command system
---

# Playwright MCP Integration System - Integration Specification

## Overview

This is the comprehensive integration specification for a complete web application testing and analysis system that integrates Playwright MCP with Serena tools.

## System Architecture

### Command List
```
/Users/kakikaito/.claude/commands/playwright/
├── e2e.md                   # E2E testing & behavior verification
├── web-analyzer.md          # Website analysis & specification extraction
├── visual-regression.md     # Visual regression testing
├── accessibility-test.md    # Accessibility testing
└── performance-monitor.md   # Performance monitoring

/Users/kakikaito/.claude/commands/spec/
└── playwright-integration.md # Integration specification (this file)
```

### Feature Matrix

| Feature Category | e2e | web-analyzer | visual-regression | accessibility-test | performance-monitor |
|-----------------|-----|--------------|------------------|-------------------|-------------------|
| **E2E Automation** | ✅ Primary | ❌ | ❌ | ❌ | ❌ |
| **UI/UX Analysis** | ❌ | ✅ Primary | ❌ | ❌ | ❌ |
| **Visual Change Detection** | ❌ | ❌ | ✅ Primary | ❌ | ❌ |
| **Accessibility** | ⚠️ Basic check | ⚠️ Basic analysis | ❌ | ✅ Primary | ❌ |
| **Performance** | ⚠️ Basic measurement | ❌ | ❌ | ❌ | ✅ Primary |
| **Specification Comparison** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Competitive Analysis** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Report Generation** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CI/CD Integration** | ✅ | ⚠️ | ✅ | ✅ | ✅ |

## Technical Integration Specification

### Playwright MCP Integration

#### Common Tool Utilization
```typescript
// Common Playwright MCP tools for all commands
const commonPlaywrightTools = [
  'mcp__playwright__browser_navigate',      // Page navigation
  'mcp__playwright__browser_snapshot',      // DOM structure retrieval
  'mcp__playwright__browser_take_screenshot', // Screenshots
  'mcp__playwright__browser_wait_for',      // Wait processing
  'mcp__playwright__browser_evaluate',      // JavaScript execution
  'mcp__playwright__browser_close'          // Browser termination
]

// Command-specific tools
const specializedTools = {
  'e2e': [
    'mcp__playwright__browser_click',
    'mcp__playwright__browser_type',
    'mcp__playwright__browser_select_option',
    'mcp__playwright__browser_handle_dialog'
  ],
  'performance-monitor': [
    'mcp__playwright__browser_network_requests',
    'mcp__playwright__browser_console_messages'
  ],
  'accessibility-test': [
    'mcp__playwright__browser_press_key'
  ]
}
```

#### Unified Browser Configuration
```typescript
// Common browser settings for all commands
const browserConfig = {
  headless: true,
  viewport: { width: 1920, height: 1080 },
  timeout: 30000,
  ignoreHTTPSErrors: true,
  userAgent: 'Claude-Code-Playwright-Integration/1.0'
}

// Device-specific settings
const deviceConfigs = {
  desktop: { width: 1920, height: 1080 },
  laptop: { width: 1366, height: 768 },
  tablet: { width: 768, height: 1024 },
  mobile: { width: 375, height: 667 }
}
```

### Serena Integration Specification

#### Common Memory Structure
```typescript
// Unified Serena memory structure
interface SerenaMemoryStructure {
  // Basic project information
  project_info: {
    name: string
    structure: ProjectStructure
    tech_stack: TechStack
    last_updated: number
  }
  
  // Test result history
  test_results: {
    e2e_tests: E2ETestResult[]
    visual_regression: VisualTestResult[]
    accessibility: AccessibilityTestResult[]
    performance: PerformanceTestResult[]
  }
  
  // Analysis results
  analysis_results: {
    web_analysis: WebAnalysisResult[]
    competitor_analysis: CompetitorAnalysisResult[]
    ux_patterns: UXPatternLibrary
  }
  
  // Learning data
  learning_data: {
    optimization_patterns: OptimizationPattern[]
    best_practices: BestPractice[]
    common_issues: CommonIssue[]
  }
}
```

#### Inter-Command Data Collaboration
```typescript
// Data sharing patterns between commands
class PlaywrightIntegration {
  // web-analyzer → e2e collaboration
  async analyzeAndTest(competitorUrl: string, localUrl: string) {
    // 1. Competitor site analysis
    const analysis = await this.runWebAnalyzer(competitorUrl)
    
    // 2. Save analysis results to Serena memory
    await mcp__serena__write_memory('competitor_patterns', analysis.patterns)
    
    // 3. Execute tests referencing patterns
    const testResults = await this.runE2ETest(localUrl, {
      referencePatterns: analysis.patterns
    })
    
    return { analysis, testResults }
  }
  
  // visual-regression → accessibility-test collaboration
  async comprehensiveQualityCheck(url: string) {
    // 1. Visual regression testing
    const visualResults = await this.runVisualRegression(url)
    
    // 2. Accessibility testing
    const a11yResults = await this.runAccessibilityTest(url)
    
    // 3. Integrate results and generate report
    return this.generateQualityReport(visualResults, a11yResults)
  }
}
```

## Workflow Integration

### Development Lifecycle Integration

#### 1. Requirements Definition & Design Phase
```bash
# Requirements clarification through competitive analysis
/web-analyzer https://competitor1.com -d -u -x -t -c -r
/web-analyzer https://competitor2.com -d -u -x -t -c -r

# Generate comparison report from analysis results
/web-analyzer --compare competitor1.com competitor2.com
```

#### 2. Development Phase
```bash
# Continuous E2E testing
/e2e http://localhost:3000 -i -w 10

# Real-time performance monitoring
/performance-monitor http://localhost:3000 -v -n --alerts
```

#### 3. Testing & Quality Assurance Phase
```bash
# Comprehensive quality check
/e2e http://staging.myapp.com -s -r
/visual-regression http://staging.myapp.com -c -m -r
/accessibility-test http://staging.myapp.com -l AA -r
/performance-monitor http://staging.myapp.com -v -l --baseline
```

#### 4. Release & Monitoring Phase
```bash
# Production environment monitoring
/performance-monitor https://myapp.com --alerts --baseline
/accessibility-test https://myapp.com -l AAA --alerts
```

### Team Collaboration Workflows

#### For Designers & UX Designers
```bash
# Design research
/web-analyzer https://inspirational-site.com -u -c -s
# Component specification extraction
/web-analyzer https://design-system.com -c --components
```

#### For Frontend Developers
```bash
# Post-implementation behavior verification
/e2e http://localhost:3000/new-feature -r
# Visual regression testing
/visual-regression http://localhost:3000 -c -m
```

#### For QA Engineers
```bash
# Overall quality check
/accessibility-test http://staging.myapp.com -l AA -r
/performance-monitor http://staging.myapp.com -v -l -n -j
```

#### For DevOps Engineers
```bash
# CI/CD integration
/e2e $STAGING_URL -s -r --ci-mode
/performance-monitor $PRODUCTION_URL --alerts --ci-mode
```

## CI/CD Integration Specification

### GitHub Actions Integration Template
```yaml
name: Comprehensive Web Testing
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM

jobs:
  setup:
    runs-on: ubuntu-latest
    outputs:
      staging-url: ${{ steps.deploy.outputs.url }}
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Staging
        id: deploy
        run: |
          # Staging environment deployment
          echo "url=https://staging-${{ github.sha }}.myapp.com" >> $GITHUB_OUTPUT

  e2e-testing:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: E2E Testing
        run: |
          /e2e ${{ needs.setup.outputs.staging-url }} \
            -s -r --ci-mode --report-format=json
      
      - name: Upload E2E Results
        uses: actions/upload-artifact@v3
        with:
          name: e2e-results
          path: e2e-test-results.json

  visual-regression:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: Visual Regression Testing
        run: |
          /visual-regression ${{ needs.setup.outputs.staging-url }} \
            -c -m -d "desktop,tablet,mobile" --report

  accessibility-testing:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: Accessibility Testing
        run: |
          /accessibility-test ${{ needs.setup.outputs.staging-url }} \
            -l AA -s 2.1 -r --ci-mode

  performance-monitoring:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: Performance Monitoring
        run: |
          /performance-monitor ${{ needs.setup.outputs.staging-url }} \
            -v -l -n -j --baseline --alerts

  quality-gate:
    needs: [e2e-testing, visual-regression, accessibility-testing, performance-monitoring]
    runs-on: ubuntu-latest
    steps:
      - name: Quality Gate Check
        run: |
          # Quality standard check
          python check_quality_gates.py \
            --e2e-results=e2e-results.json \
            --visual-results=visual-results.json \
            --a11y-results=accessibility-results.json \
            --perf-results=performance-results.json

  reporting:
    needs: quality-gate
    runs-on: ubuntu-latest
    steps:
      - name: Generate Comprehensive Report
        run: |
          python generate_comprehensive_report.py \
            --output=comprehensive-quality-report.html
      
      - name: Comment PR with Results
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('quality-summary.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: report
            });
```

### Quality Gate Configuration
```yaml
# .github/quality-gates.yml
quality_gates:
  e2e_tests:
    min_pass_rate: 95
    max_critical_failures: 0
    
  visual_regression:
    max_diff_percentage: 2.0
    critical_pages: ["home", "login", "checkout"]
    
  accessibility:
    min_score: 85
    wcag_level: "AA"
    max_critical_issues: 0
    
  performance:
    lighthouse_score: 80
    lcp_threshold: 2500
    cls_threshold: 0.1
    
blocking_conditions:
  - critical_e2e_failure
  - visual_regression_critical_pages
  - accessibility_critical_issues
  - performance_below_threshold
```

## Report Integration System

### Comprehensive Report Generation
```typescript
class ComprehensiveReportGenerator {
  async generateReport(testResults: AllTestResults): Promise<ComprehensiveReport> {
    return {
      summary: this.generateSummary(testResults),
      e2eResults: this.formatE2EResults(testResults.e2e),
      visualResults: this.formatVisualResults(testResults.visual),
      accessibilityResults: this.formatA11yResults(testResults.accessibility),
      performanceResults: this.formatPerfResults(testResults.performance),
      recommendations: await this.generateRecommendations(testResults),
      trends: await this.analyzeTrends(testResults)
    }
  }
  
  private async generateRecommendations(results: AllTestResults): Promise<Recommendation[]> {
    // Reference past patterns from Serena memory
    const pastPatterns = await mcp__serena__read_memory('optimization_patterns')
    
    // Cross-functional improvement suggestions
    return [
      ...this.analyzeE2EIssues(results.e2e, pastPatterns),
      ...this.analyzePerformanceBottlenecks(results.performance, pastPatterns),
      ...this.analyzeAccessibilityIssues(results.accessibility, pastPatterns),
      ...this.analyzeVisualInconsistencies(results.visual, pastPatterns)
    ]
  }
}
```

### Dashboard Integration
```html
<!-- Integrated dashboard HTML -->
<div class="quality-dashboard">
  <div class="summary-cards">
    <div class="card e2e">
      <h3>E2E Tests</h3>
      <div class="score">{e2e_pass_rate}%</div>
    </div>
    <div class="card visual">
      <h3>Visual Quality</h3>
      <div class="score">{visual_score}</div>
    </div>
    <div class="card accessibility">
      <h3>Accessibility</h3>
      <div class="score">{a11y_score}/100</div>
    </div>
    <div class="card performance">
      <h3>Performance</h3>
      <div class="score">{lighthouse_score}/100</div>
    </div>
  </div>
  
  <div class="detailed-results">
    <!-- Detailed results display -->
  </div>
  
  <div class="trends-chart">
    <!-- Trend chart -->
  </div>
</div>
```

## Learning & Optimization System

### Serena Learning Patterns
```typescript
// Continuous learning system
class PlaywrightLearningSystem {
  async learnFromResults(results: TestResults) {
    // Pattern analysis
    const patterns = this.analyzePatterns(results)
    
    // Learn success patterns
    const successPatterns = patterns.filter(p => p.success)
    await mcp__serena__write_memory('success_patterns', successPatterns)
    
    // Learn failure patterns
    const failurePatterns = patterns.filter(p => !p.success)
    await mcp__serena__write_memory('failure_patterns', failurePatterns)
    
    // Generate optimization suggestions
    const optimizations = this.generateOptimizations(patterns)
    await mcp__serena__write_memory('optimization_suggestions', optimizations)
  }
  
  async predictIssues(projectStructure: ProjectStructure): Promise<PredictedIssue[]> {
    const knownPatterns = await mcp__serena__read_memory('failure_patterns')
    
    return this.matchPatternsToProject(knownPatterns, projectStructure)
  }
}
```

### Automatic Improvement Suggestions
```typescript
// Automatic improvement suggestion system
interface ImprovementSuggestion {
  category: 'performance' | 'accessibility' | 'visual' | 'e2e'
  priority: 'critical' | 'high' | 'medium' | 'low'
  issue: string
  solution: string
  codeExample?: string
  estimatedImpact: string
  implementationTime: string
}

async function generateImprovementSuggestions(
  allResults: AllTestResults
): Promise<ImprovementSuggestion[]> {
  const suggestions: ImprovementSuggestion[] = []
  
  // Performance improvement suggestions
  if (allResults.performance.lighthouse.score < 80) {
    suggestions.push({
      category: 'performance',
      priority: 'high',
      issue: 'Lighthouse score is below 80',
      solution: 'Remove unused JavaScript and optimize images',
      estimatedImpact: '20% improvement in page load speed',
      implementationTime: '2-3 days'
    })
  }
  
  // Accessibility improvement suggestions
  if (allResults.accessibility.score < 85) {
    suggestions.push({
      category: 'accessibility',
      priority: 'critical',
      issue: 'Does not meet WCAG AA standards',
      solution: 'Add alt attributes and improve keyboard navigation',
      codeExample: '<img src="..." alt="Product image" />',
      estimatedImpact: 'Reach accessibility score of 95',
      implementationTime: '1-2 days'
    })
  }
  
  return suggestions
}
```

## Security & Privacy Considerations

### Data Protection
```typescript
// Confidential data protection
const securityConfig = {
  // Remove sensitive information from screenshots
  screenshot_masking: {
    selectors: ['.personal-info', '.credit-card', '.ssn'],
    mask_type: 'blur' | 'black-box' | 'remove'
  },
  
  // Filter sensitive information from network data
  network_filtering: {
    exclude_headers: ['authorization', 'cookie', 'x-api-key'],
    exclude_body_patterns: [/password/i, /token/i, /secret/i]
  },
  
  // Serena memory encryption
  memory_encryption: {
    enabled: true,
    key_rotation: '30d',
    pii_detection: true
  }
}
```

### GDPR/Privacy Compliance
```typescript
// Privacy compliance settings
const privacyConfig = {
  data_retention: {
    test_results: '90d',
    screenshots: '30d',
    network_logs: '7d',
    user_data: '0d'  // Delete immediately
  },
  
  consent_management: {
    require_explicit_consent: true,
    data_minimization: true,
    right_to_erasure: true
  },
  
  geographic_restrictions: {
    eu_data_protection: true,
    ccpa_compliance: true
  }
}
```

## Extensibility & Customization

### Plugin System
```typescript
// Plugin development interface
interface PlaywrightPlugin {
  name: string
  version: string
  
  // Lifecycle hooks
  beforeTest?(context: TestContext): Promise<void>
  afterTest?(context: TestContext, results: TestResults): Promise<void>
  
  // Custom analysis
  analyze?(page: Page): Promise<AnalysisResult>
  
  // Report extension
  extendReport?(report: Report): Promise<ExtendedReport>
}

// Plugin example: Custom metrics collection
class CustomMetricsPlugin implements PlaywrightPlugin {
  name = 'custom-metrics'
  version = '1.0.0'
  
  async analyze(page: Page): Promise<CustomMetrics> {
    return await page.evaluate(() => {
      // Custom metrics collection logic
      return {
        customLoadTime: performance.now(),
        userInteractionCount: window.userInteractions || 0,
        errorCount: window.errorLog?.length || 0
      }
    })
  }
}
```

### Configuration Customization
```json
{
  "playwright_integration_config": {
    "default_options": {
      "headless": true,
      "timeout": 30000,
      "retries": 3
    },
    
    "command_specific": {
      "e2e": {
        "auto_retry": true,
        "screenshot_on_failure": true
      },
      "performance-monitor": {
        "measurement_runs": 5,
        "warmup_runs": 2
      }
    },
    
    "team_settings": {
      "notification_channels": ["slack", "email"],
      "report_recipients": ["team@example.com"],
      "escalation_rules": {
        "critical_failures": "immediate",
        "performance_degradation": "daily_summary"
      }
    }
  }
}
```

## Troubleshooting & Support

### Integrated Debugging
```bash
# Overall diagnostic command
/playwright-integration --diagnose

# Execution content:
# 1. Verify operation of each command
# 2. Check Playwright MCP connection
# 3. Serena memory integrity check
# 4. Configuration file validation
# 5. Permission & security check
```

### Common Issues and Solutions

#### Browser Launch Error
```bash
# Diagnosis
/playwright-integration --check-browser

# Solutions
# 1. Reinstall Playwright browser
# 2. Check permission settings
# 3. Check system resources
```

#### Serena Integration Error
```bash
# Diagnosis
/playwright-integration --check-serena

# Solutions
# 1. Re-run Serena onboarding
# 2. Re-analyze project structure
# 3. Repair memory integrity
```

#### Performance Issues
```bash
# Diagnosis
/playwright-integration --performance-debug

# Optimization suggestions
# 1. Adjust parallel execution count
# 2. Review cache settings
# 3. Narrow down measurement targets
```

## Future Extension Plans

### Phase 2 Feature Additions
- **Enhanced AI Analysis**: Advanced analysis using LLMs
- **Cross-Browser Testing**: Firefox, Safari support
- **Mobile App Testing**: React Native, Flutter support
- **Security Testing**: OWASP-compliant vulnerability testing

### Phase 3 Ecosystem Integration
- **Third-Party Tool Integration**: Jira, Slack, Confluence integration
- **Cloud Support**: AWS, Azure, GCP execution
- **Enterprise Features**: RBAC, audit logs, compliance

### Long-Term Vision
- Fully automated quality assurance platform
- Predictive quality management system
- AI assistant integration for development teams

## Licensing & Compliance

### Open Source Licenses
- Playwright: Apache License 2.0
- Integration System: MIT License

### Enterprise Support
- Commercial use licensing
- Premium support
- Customization services

---

**Playwright MCP Integration System v1.0**  
**Created**: 2025  
**Last Updated**: Auto-updated