---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_console_messages, mcp__playwright__browser_network_requests, Glob, Grep
description: Playwright MCP統合コマンドシステムの統合仕様と使用ガイド
---

# Playwright MCP統合システム - 統合仕様

## 概要

Playwright MCPとSerenaツールを統合した、完全なWebアプリケーションテストと分析システムの包括的な統合仕様です。

## システムアーキテクチャ

### コマンド一覧
```
/Users/kakikaito/.claude/commands/playwright/
├── e2e.md                   # E2Eテスト・動作検証
├── web-analyzer.md          # ウェブサイト分析・仕様抽出
├── visual-regression.md     # ビジュアルリグレッションテスト
├── accessibility-test.md    # アクセシビリティテスト
└── performance-monitor.md   # パフォーマンス監視

/Users/kakikaito/.claude/commands/spec/
└── playwright-integration.md # 統合仕様（このファイル）
```

### 機能マトリックス

| 機能カテゴリ | e2e | web-analyzer | visual-regression | accessibility-test | performance-monitor |
|------------|-----|--------------|------------------|-------------------|-------------------|
| **E2E自動化** | ✅ 主機能 | ❌ | ❌ | ❌ | ❌ |
| **UI/UX分析** | ❌ | ✅ 主機能 | ❌ | ❌ | ❌ |
| **ビジュアル変更検出** | ❌ | ❌ | ✅ 主機能 | ❌ | ❌ |
| **アクセシビリティ** | ⚠️ 基本チェック | ⚠️ 基本分析 | ❌ | ✅ 主機能 | ❌ |
| **パフォーマンス** | ⚠️ 基本計測 | ❌ | ❌ | ❌ | ✅ 主機能 |
| **仕様比較** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **競合分析** | ❌ | ✅ | ❌ | ❌ | ❌ |
| **レポート生成** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CI/CD統合** | ✅ | ⚠️ | ✅ | ✅ | ✅ |

## 技術的統合仕様

### Playwright MCP統合

#### 共通ツール利用
```typescript
// 全コマンド共通のPlaywright MCPツール
const commonPlaywrightTools = [
  'mcp__playwright__browser_navigate',      // ページナビゲーション
  'mcp__playwright__browser_snapshot',      // DOM構造取得
  'mcp__playwright__browser_take_screenshot', // スクリーンショット
  'mcp__playwright__browser_wait_for',      // 待機処理
  'mcp__playwright__browser_evaluate',      // JavaScript実行
  'mcp__playwright__browser_close'          // ブラウザ終了
]

// コマンド固有ツール
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

#### 統一ブラウザ設定
```typescript
// 全コマンド共通のブラウザ設定
const browserConfig = {
  headless: true,
  viewport: { width: 1920, height: 1080 },
  timeout: 30000,
  ignoreHTTPSErrors: true,
  userAgent: 'Claude-Code-Playwright-Integration/1.0'
}

// デバイス固有設定
const deviceConfigs = {
  desktop: { width: 1920, height: 1080 },
  laptop: { width: 1366, height: 768 },
  tablet: { width: 768, height: 1024 },
  mobile: { width: 375, height: 667 }
}
```

### Serena統合仕様

#### 共通メモリ構造
```typescript
// Serena統一メモリ構造
interface SerenaMemoryStructure {
  // 基本プロジェクト情報
  project_info: {
    name: string
    structure: ProjectStructure
    tech_stack: TechStack
    last_updated: number
  }

  // テスト結果履歴
  test_results: {
    e2e_tests: E2ETestResult[]
    visual_regression: VisualTestResult[]
    accessibility: AccessibilityTestResult[]
    performance: PerformanceTestResult[]
  }

  // 分析結果
  analysis_results: {
    web_analysis: WebAnalysisResult[]
    competitor_analysis: CompetitorAnalysisResult[]
    ux_patterns: UXPatternLibrary
  }

  // 学習データ
  learning_data: {
    optimization_patterns: OptimizationPattern[]
    best_practices: BestPractice[]
    common_issues: CommonIssue[]
  }
}
```

#### コマンド間データ連携
```typescript
// コマンド間でのデータ共有パターン
class PlaywrightIntegration {
  // web-analyzer → e2e の連携
  async analyzeAndTest(competitorUrl: string, localUrl: string) {
    // 1. 競合サイト分析
    const analysis = await this.runWebAnalyzer(competitorUrl)

    // 2. 分析結果をSerenaメモリに保存
    await mcp__serena__write_memory('competitor_patterns', analysis.patterns)

    // 3. パターンを参照してテスト実行
    const testResults = await this.runE2ETest(localUrl, {
      referencePatterns: analysis.patterns
    })

    return { analysis, testResults }
  }

  // visual-regression → accessibility-test の連携
  async comprehensiveQualityCheck(url: string) {
    // 1. ビジュアルリグレッションテスト
    const visualResults = await this.runVisualRegression(url)

    // 2. アクセシビリティテスト
    const a11yResults = await this.runAccessibilityTest(url)

    // 3. 結果を統合してレポート生成
    return this.generateQualityReport(visualResults, a11yResults)
  }
}
```

## ワークフロー統合

### 開発ライフサイクル統合

#### 1. 要件定義・設計フェーズ
```bash
# 競合分析による要件明確化
/web-analyzer https://competitor1.com -d -u -x -t -c -r
/web-analyzer https://competitor2.com -d -u -x -t -c -r

# 分析結果から比較レポート生成
/web-analyzer --compare competitor1.com competitor2.com
```

#### 2. 開発フェーズ
```bash
# 継続的なE2Eテスト
/e2e http://localhost:3000 -i -w 10

# リアルタイムパフォーマンス監視
/performance-monitor http://localhost:3000 -v -n --alerts
```

#### 3. テスト・品質保証フェーズ
```bash
# 包括的な品質チェック
/e2e http://staging.myapp.com -s -r
/visual-regression http://staging.myapp.com -c -m -r
/accessibility-test http://staging.myapp.com -l AA -r
/performance-monitor http://staging.myapp.com -v -l --baseline
```

#### 4. リリース・監視フェーズ
```bash
# 本番環境監視
/performance-monitor https://myapp.com --alerts --baseline
/accessibility-test https://myapp.com -l AAA --alerts
```

### チームコラボレーションワークフロー

#### デザイナー・UXデザイナー向け
```bash
# デザインリサーチ
/web-analyzer https://inspirational-site.com -u -c -s
# コンポーネント仕様抽出
/web-analyzer https://design-system.com -c --components
```

#### フロントエンド開発者向け
```bash
# 実装後の動作確認
/e2e http://localhost:3000/new-feature -r
# ビジュアルリグレッションテスト
/visual-regression http://localhost:3000 -c -m
```

#### QAエンジニア向け
```bash
# 総合品質チェック
/accessibility-test http://staging.myapp.com -l AA -r
/performance-monitor http://staging.myapp.com -v -l -n -j
```

#### DevOpsエンジニア向け
```bash
# CI/CD統合
/e2e $STAGING_URL -s -r --ci-mode
/performance-monitor $PRODUCTION_URL --alerts --ci-mode
```

## CI/CD統合仕様

### GitHub Actions統合テンプレート
```yaml
name: 包括的Webテスト
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * *'  # 毎日6時

jobs:
  setup:
    runs-on: ubuntu-latest
    outputs:
      staging-url: ${{ steps.deploy.outputs.url }}
    steps:
      - uses: actions/checkout@v3
      - name: ステージングにデプロイ
        id: deploy
        run: |
          # ステージング環境へのデプロイ
          echo "url=https://staging-${{ github.sha }}.myapp.com" >> $GITHUB_OUTPUT

  e2e-testing:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: E2Eテスト
        run: |
          /e2e ${{ needs.setup.outputs.staging-url }} \
            -s -r --ci-mode --report-format=json

      - name: E2E結果をアップロード
        uses: actions/upload-artifact@v3
        with:
          name: e2e-results
          path: e2e-test-results.json

  visual-regression:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: ビジュアルリグレッションテスト
        run: |
          /visual-regression ${{ needs.setup.outputs.staging-url }} \
            -c -m -d "desktop,tablet,mobile" --report

  accessibility-testing:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: アクセシビリティテスト
        run: |
          /accessibility-test ${{ needs.setup.outputs.staging-url }} \
            -l AA -s 2.1 -r --ci-mode

  performance-monitoring:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - name: パフォーマンス監視
        run: |
          /performance-monitor ${{ needs.setup.outputs.staging-url }} \
            -v -l -n -j --baseline --alerts

  quality-gate:
    needs: [e2e-testing, visual-regression, accessibility-testing, performance-monitoring]
    runs-on: ubuntu-latest
    steps:
      - name: 品質ゲートチェック
        run: |
          # 品質基準チェック
          python check_quality_gates.py \
            --e2e-results=e2e-results.json \
            --visual-results=visual-results.json \
            --a11y-results=accessibility-results.json \
            --perf-results=performance-results.json

  reporting:
    needs: quality-gate
    runs-on: ubuntu-latest
    steps:
      - name: 包括的レポート生成
        run: |
          python generate_comprehensive_report.py \
            --output=comprehensive-quality-report.html

      - name: PRに結果をコメント
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

### 品質ゲート設定
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

## レポート統合システム

### 包括的レポート生成
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
    // Serenaメモリから過去のパターンを参照
    const pastPatterns = await mcp__serena__read_memory('optimization_patterns')

    // 横断的な改善提案を生成
    return [
      ...this.analyzeE2EIssues(results.e2e, pastPatterns),
      ...this.analyzePerformanceBottlenecks(results.performance, pastPatterns),
      ...this.analyzeAccessibilityIssues(results.accessibility, pastPatterns),
      ...this.analyzeVisualInconsistencies(results.visual, pastPatterns)
    ]
  }
}
```

### ダッシュボード統合
```html
<!-- 統合ダッシュボードHTML -->
<div class="quality-dashboard">
  <div class="summary-cards">
    <div class="card e2e">
      <h3>E2Eテスト</h3>
      <div class="score">{e2e_pass_rate}%</div>
    </div>
    <div class="card visual">
      <h3>ビジュアル品質</h3>
      <div class="score">{visual_score}</div>
    </div>
    <div class="card accessibility">
      <h3>アクセシビリティ</h3>
      <div class="score">{a11y_score}/100</div>
    </div>
    <div class="card performance">
      <h3>パフォーマンス</h3>
      <div class="score">{lighthouse_score}/100</div>
    </div>
  </div>

  <div class="detailed-results">
    <!-- 詳細結果表示 -->
  </div>

  <div class="trends-chart">
    <!-- トレンドチャート -->
  </div>
</div>
```

## 学習・最適化システム

### Serena学習パターン
```typescript
// 継続的学習システム
class PlaywrightLearningSystem {
  async learnFromResults(results: TestResults) {
    // パターン分析
    const patterns = this.analyzePatterns(results)

    // 成功パターンを学習
    const successPatterns = patterns.filter(p => p.success)
    await mcp__serena__write_memory('success_patterns', successPatterns)

    // 失敗パターンを学習
    const failurePatterns = patterns.filter(p => !p.success)
    await mcp__serena__write_memory('failure_patterns', failurePatterns)

    // 最適化提案を生成
    const optimizations = this.generateOptimizations(patterns)
    await mcp__serena__write_memory('optimization_suggestions', optimizations)
  }

  async predictIssues(projectStructure: ProjectStructure): Promise<PredictedIssue[]> {
    const knownPatterns = await mcp__serena__read_memory('failure_patterns')

    return this.matchPatternsToProject(knownPatterns, projectStructure)
  }
}
```

### 自動改善提案
```typescript
// 自動改善提案システム
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

  // パフォーマンス改善提案
  if (allResults.performance.lighthouse.score < 80) {
    suggestions.push({
      category: 'performance',
      priority: 'high',
      issue: 'Lighthouseスコアが80未満です',
      solution: '未使用のJavaScriptを削除し、画像を最適化してください',
      estimatedImpact: 'ページ読み込み速度が20%改善',
      implementationTime: '2-3日'
    })
  }

  // アクセシビリティ改善提案
  if (allResults.accessibility.score < 85) {
    suggestions.push({
      category: 'accessibility',
      priority: 'critical',
      issue: 'WCAG AA基準を満たしていません',
      solution: 'alt属性を追加し、キーボードナビゲーションを改善してください',
      codeExample: '<img src="..." alt="商品画像" />',
      estimatedImpact: 'アクセシビリティスコア95達成',
      implementationTime: '1-2日'
    })
  }

  return suggestions
}
```

## セキュリティとプライバシーの考慮事項

### データ保護
```typescript
// 機密データ保護
const securityConfig = {
  // スクリーンショットから機密情報を削除
  screenshot_masking: {
    selectors: ['.personal-info', '.credit-card', '.ssn'],
    mask_type: 'blur' | 'black-box' | 'remove'
  },

  // ネットワークデータから機密情報をフィルタ
  network_filtering: {
    exclude_headers: ['authorization', 'cookie', 'x-api-key'],
    exclude_body_patterns: [/password/i, /token/i, /secret/i]
  },

  // Serenaメモリ暗号化
  memory_encryption: {
    enabled: true,
    key_rotation: '30d',
    pii_detection: true
  }
}
```

### GDPR/プライバシー準拠
```typescript
// プライバシー準拠設定
const privacyConfig = {
  data_retention: {
    test_results: '90d',
    screenshots: '30d',
    network_logs: '7d',
    user_data: '0d'  // 即時削除
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

## 拡張性とカスタマイズ

### プラグインシステム
```typescript
// プラグイン開発インターフェース
interface PlaywrightPlugin {
  name: string
  version: string

  // ライフサイクルフック
  beforeTest?(context: TestContext): Promise<void>
  afterTest?(context: TestContext, results: TestResults): Promise<void>

  // カスタム分析
  analyze?(page: Page): Promise<AnalysisResult>

  // レポート拡張
  extendReport?(report: Report): Promise<ExtendedReport>
}

// プラグイン例: カスタムメトリクス収集
class CustomMetricsPlugin implements PlaywrightPlugin {
  name = 'custom-metrics'
  version = '1.0.0'

  async analyze(page: Page): Promise<CustomMetrics> {
    return await page.evaluate(() => {
      // カスタムメトリクス収集ロジック
      return {
        customLoadTime: performance.now(),
        userInteractionCount: window.userInteractions || 0,
        errorCount: window.errorLog?.length || 0
      }
    })
  }
}
```

### 設定カスタマイズ
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

## トラブルシューティングとサポート

### 統合デバッグ
```bash
# 全体診断コマンド
/playwright-integration --diagnose

# 実行内容:
# 1. 各コマンドの動作確認
# 2. Playwright MCP接続チェック
# 3. Serenaメモリ整合性確認
# 4. 設定ファイルの検証
# 5. 権限・セキュリティチェック
```

### よくある問題と解決策

#### ブラウザ起動エラー
```bash
# 診断
/playwright-integration --check-browser

# 解決策
# 1. Playwrightブラウザを再インストール
# 2. 権限設定を確認
# 3. システムリソースを確認
```

#### Serena統合エラー
```bash
# 診断
/playwright-integration --check-serena

# 解決策
# 1. Serenaオンボーディングを再実行
# 2. プロジェクト構造を再分析
# 3. メモリ整合性を修復
```

#### パフォーマンス問題
```bash
# 診断
/playwright-integration --performance-debug

# 最適化提案
# 1. 並列実行数を調整
# 2. キャッシュ設定を見直し
# 3. 計測対象を絞り込み
```

## 将来の拡張計画

### フェーズ2 機能追加
- **AI強化分析**: LLMを活用した高度な分析
- **クロスブラウザテスト**: Firefox、Safari対応
- **モバイルアプリテスト**: React Native、Flutter対応
- **セキュリティテスト**: OWASP準拠の脆弱性テスト

### フェーズ3 エコシステム統合
- **サードパーティツール統合**: Jira、Slack、Confluence連携
- **クラウドサポート**: AWS、Azure、GCPでの実行
- **エンタープライズ機能**: RBAC、監査ログ、コンプライアンス

### 長期ビジョン
- 完全自動化された品質保証プラットフォーム
- 予測的品質管理システム
- 開発チーム向けAIアシスタント統合

## ライセンスとコンプライアンス

### オープンソースライセンス
- Playwright: Apache License 2.0
- 統合システム: MIT License

### エンタープライズサポート
- 商用利用ライセンス
- プレミアムサポート
- カスタマイズサービス

---

**Playwright MCP統合システム v1.0**
**作成日**: 2025年
**最終更新**: 自動更新
