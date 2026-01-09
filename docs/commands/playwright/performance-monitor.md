---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_evaluate, mcp__playwright__browser_network_requests, mcp__playwright__browser_console_messages, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_wait_for
description: Playwright MCPを使用したパフォーマンスモニタリングとCore Web Vitals測定コマンド
---

# パフォーマンスモニター - パフォーマンス監視

## 概要

Playwright MCPとSerenaツールを統合し、Webアプリケーションのパフォーマンス測定と最適化提案を自動実行するコマンドです。

## 使用方法

### 基本構文
```bash
/performance-monitor <ターゲット> [オプション]
```

### ターゲット指定

| ターゲットタイプ | 例 | 説明 |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | 開発アプリのテスト |
| **本番URL** | `https://myapp.com` | 本番環境のモニタリング |
| **ページパス** | `/dashboard`, `/checkout` | 特定ページの測定 |
| **ユーザーフロー** | `login-flow`, `purchase-flow` | 完全なフローの測定 |

### オプション

| オプション | 説明 | デフォルト |
|--------|-------------|---------|
| `-v, --vitals` | Core Web Vitals測定 | true |
| `-l, --lighthouse` | Lighthouse監査実行 | false |
| `-n, --network` | 詳細ネットワーク分析 | false |
| `-j, --javascript` | JavaScript実行時間分析 | false |
| `-m, --memory` | メモリ使用量モニタリング | false |
| `-c, --cpu` | CPU使用量測定 | false |
| `-r, --runs` | 測定実行回数 | 3 |
| `-d, --device` | デバイス条件設定 | desktop |
| `-t, --throttling` | ネットワーク/CPUスロットリング | none |
| `--report` | 詳細レポート生成 | false |
| `--baseline` | ベースライン比較 | false |
| `--alerts` | しきい値アラート設定 | false |

### 使用例

```bash
# 基本パフォーマンス測定
/performance-monitor http://localhost:3000

# Core Web Vitals + Lighthouse監査
/performance-monitor /dashboard -v -l --report

# 詳細パフォーマンス分析
/performance-monitor /checkout -n -j -m -c

# モバイル環境測定
/performance-monitor https://myapp.com -d mobile -t "slow-3g"

# 信頼性向上のための複数回測定
/performance-monitor /api-heavy-page -r 10 --baseline

# アラート付きモニタリング
/performance-monitor https://production.com --alerts --report
```

## 機能詳細

### 1. Core Web Vitals測定（-vオプション）

#### 測定メトリクス
```typescript
interface CoreWebVitals {
  // ページ読み込みパフォーマンス
  LCP: number      // Largest Contentful Paint (ms)

  // インタラクティビティ
  FID: number      // First Input Delay (ms)
  INP: number      // Interaction to Next Paint (ms)

  // 視覚的安定性
  CLS: number      // Cumulative Layout Shift (スコア)

  // 読み込み速度
  FCP: number      // First Contentful Paint (ms)
  TTFB: number     // Time to First Byte (ms)
}
```

#### Google標準による評価
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

### 2. Lighthouse監査（-lオプション）

#### 監査カテゴリ
```typescript
interface LighthouseAudit {
  performance: {
    score: number    // 0-100 パフォーマンススコア
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

#### 最適化機会の特定
```typescript
const optimizationOpportunities = [
  {
    audit: 'unused-css-rules',
    impact: 'high',
    description: '未使用CSSの削除により約500KB削減可能'
  },
  {
    audit: 'efficient-animated-content',
    impact: 'medium',
    description: 'アニメーション最適化によりレンダリング負荷を軽減'
  },
  {
    audit: 'offscreen-images',
    impact: 'high',
    description: '遅延読み込みにより初期読み込みを約2秒短縮可能'
  }
]
```

### 3. ネットワーク分析（-nオプション）

#### リソース分析
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

#### ボトルネック特定
```typescript
// 遅いリクエストの特定
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

### 4. JavaScript実行分析（-jオプション）

#### パフォーマンスプロファイリング
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

#### パフォーマンスボトルネック検出
```typescript
// 重いJavaScript処理の検出
async function analyzeJavaScriptPerformance() {
  const performanceEntries = await mcp__playwright__browser_evaluate(`
    // Long TasksのPerformance Observer
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

    // メモリ使用量
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

### 5. メモリ使用量モニタリング（-mオプション）

#### メモリプロファイル
```typescript
interface MemoryProfile {
  heapUsed: number
  heapTotal: number
  heapLimit: number
  external: number
  arrayBuffers: number

  // ガベージコレクション情報
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

#### メモリリーク検出
```typescript
// メモリリークの検出
async function detectMemoryLeaks() {
  const initialMemory = await measureMemoryUsage()

  // ユーザーアクションの実行
  await simulateUserInteractions()

  const finalMemory = await measureMemoryUsage()

  // メモリ増加の分析
  const memoryGrowth = finalMemory.heapUsed - initialMemory.heapUsed

  if (memoryGrowth > MEMORY_LEAK_THRESHOLD) {
    return analyzeMemoryGrowth(initialMemory, finalMemory)
  }
}
```

### 6. Serena統合機能

#### コードベース分析統合
```typescript
// パフォーマンスクリティカルなコンポーネントの特定
async function identifyPerformanceCriticalComponents() {
  const components = await mcp__serena__get_symbols_overview()

  // 重いコンポーネントパターンの検索
  const heavyComponents = await mcp__serena__search_for_pattern([
    'useState.*array.*length.*1000',
    'useEffect.*dependencies.*length.*10',
    'heavy.*computation',
    'large.*data.*processing'
  ])

  return analyzeComponentPerformanceImpact(components, heavyComponents)
}
```

#### 最適化提案生成
```typescript
// Serena知識を使用した最適化提案の生成
async function generateOptimizationSuggestions(performanceData: PerformanceMetrics) {
  const pastOptimizations = await mcp__serena__read_memory('performance-optimizations')

  const suggestions = analyzeOptimizationOpportunities(performanceData, pastOptimizations)

  // 学習データとして保存
  await mcp__serena__write_memory('performance-analysis', {
    timestamp: Date.now(),
    metrics: performanceData,
    suggestions: suggestions,
    context: await mcp__serena__get_symbols_overview()
  })

  return suggestions
}
```

### 7. ベースライン比較（--baselineオプション）

#### 継続的パフォーマンスモニタリング
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

// パフォーマンストレンド分析
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

### 8. アラート機能（--alertsオプション）

#### しきい値モニタリング
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
    message: 'ページ読み込み速度が低下しています'
  },
  {
    metric: 'CLS',
    warningThreshold: 0.1,
    criticalThreshold: 0.25,
    message: 'レイアウトシフトが発生しています'
  }
]
```

## 実装ワークフロー

### ステップ1: 環境準備とセットアップ
```typescript
// Serenaでプロジェクト分析
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// パフォーマンス測定対象の特定
const criticalPaths = await mcp__serena__search_for_pattern('performance-critical')
```

### ステップ2: ページアクセスと初期測定
```typescript
// ページアクセス
await mcp__playwright__browser_navigate(targetUrl)

// Performance Observerのセットアップ
await mcp__playwright__browser_evaluate(`
  window.performanceMetrics = {};

  // Web Vitals測定
  new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
      window.performanceMetrics[entry.name] = entry.value;
    });
  }).observe({entryTypes: ['paint', 'navigation', 'measure']});

  // Layout Shift測定
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

### ステップ3: 詳細メトリクス収集
```typescript
// Core Web Vitals測定
const webVitals = await measureCoreWebVitals()

// ネットワーク分析
if (options.network) {
  const networkData = await mcp__playwright__browser_network_requests()
  const networkAnalysis = analyzeNetworkPerformance(networkData)
}

// JavaScript分析
if (options.javascript) {
  const jsAnalysis = await analyzeJavaScriptPerformance()
}

// メモリ分析
if (options.memory) {
  const memoryProfile = await profileMemoryUsage()
}
```

### ステップ4: Lighthouse監査実行（-lオプション）
```typescript
// Lighthouse監査の実行
const lighthouseResult = await runLighthouseAudit(targetUrl, {
  device: options.device,
  throttling: options.throttling,
  categories: ['performance', 'accessibility', 'best-practices', 'seo']
})
```

### ステップ5: データ分析と最適化提案
```typescript
// 包括的分析
const comprehensiveAnalysis = {
  coreWebVitals: webVitals,
  lighthouse: lighthouseResult,
  network: networkAnalysis,
  javascript: jsAnalysis,
  memory: memoryProfile
}

// Serenaを使用した最適化提案
const optimizationSuggestions = await generateOptimizationSuggestions(comprehensiveAnalysis)

// 結果の保存
await mcp__serena__write_memory('performance-monitoring', {
  url: targetUrl,
  timestamp: Date.now(),
  analysis: comprehensiveAnalysis,
  suggestions: optimizationSuggestions
})
```

## レポート生成機能（--reportオプション）

### 詳細レポート構造
```markdown
# パフォーマンスモニタリングレポート

## 📊 概要
- ターゲット: {target-url}
- 測定日時: {timestamp}
- デバイス: {device-type}
- ネットワーク: {network-condition}

## 🚀 Core Web Vitals

### Largest Contentful Paint (LCP)
- **現在値**: 1,847ms ✅ 良好
- **目標**: < 2,500ms
- **改善**: 前回より-340ms

### First Input Delay (FID)
- **現在値**: 12ms ✅ 良好
- **目標**: < 100ms

### Cumulative Layout Shift (CLS)
- **現在値**: 0.06 ✅ 良好
- **目標**: < 0.1

## ⚡ Lighthouseスコア
- **パフォーマンス**: 89/100 ✅
- **アクセシビリティ**: 92/100 ✅
- **ベストプラクティス**: 87/100 ⚠️
- **SEO**: 100/100 ✅

## 🔍 詳細分析

### ネットワーク最適化
- 総リクエスト数: 47
- 総データサイズ: 1.2MB
- **改善提案**:
  1. 画像最適化により500KB削減可能
  2. 未使用CSS削除により200KB削減可能

### JavaScriptパフォーマンス
- メインスレッドブロッキング時間: 230ms
- **重い処理**:
  1. データ処理ライブラリ (120ms)
  2. チャートレンダリング (85ms)

### メモリ使用量
- ヒープ使用量: 45MB / 128MB
- **メモリリーク**: 検出されず ✅

## 🎯 最適化推奨事項

### 高優先度
1. **画像遅延読み込みの実装**
   - 効果: LCP -800ms改善
   - 実装難易度: 低

2. **未使用JavaScriptの削除**
   - 効果: FCP -400ms改善
   - 実装難易度: 中

### 中優先度
3. **CDN導入の検討**
   - 効果: TTFB -200ms改善
   - 実装難易度: 中

## 📈 トレンド分析
{performance-trends}

## 🔧 コード改善提案
{code-optimization-suggestions}
```

### グラフィカルレポート
```typescript
// パフォーマンスチャート生成
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

## 継続的モニタリングとCI/CD統合

### GitHub Actions統合
```yaml
name: パフォーマンスモニタリング
on:
  schedule:
    - cron: '0 */6 * * *'  # 6時間ごと
  push:
    branches: [main]

jobs:
  performance-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Node.jsセットアップ
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: 依存関係インストール
        run: npm ci

      - name: アプリケーション起動
        run: npm start &

      - name: アプリケーション待機
        run: npx wait-on http://localhost:3000

      - name: パフォーマンスモニタリング実行
        run: |
          /performance-monitor http://localhost:3000 \
            -v -l -n -j --report --baseline --alerts

      - name: パフォーマンス予算チェック
        run: |
          if [ $(cat performance-report.json | jq '.lighthouse.performance.score') -lt 80 ]; then
            echo "パフォーマンススコアがしきい値を下回っています"
            exit 1
          fi

      - name: パフォーマンスレポートアップロード
        uses: actions/upload-artifact@v3
        with:
          name: performance-report
          path: performance-report.html

      - name: Slack通知
        if: failure()
        uses: 8398a7/action-slack@v3
        with:
          status: custom
          custom_payload: |
            {
              text: "パフォーマンス低下を検出しました",
              attachments: [{
                color: "danger",
                fields: [{
                  title: "パフォーマンススコア",
                  value: "${{ env.PERFORMANCE_SCORE }}",
                  short: true
                }]
              }]
            }
```

### パフォーマンス予算
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

## 高度な機能

### 1. ユーザーフロー測定
```typescript
// 複数ページにわたるパフォーマンス測定
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
// RUMデータ収集セットアップ
const rumScript = `
(function() {
  // Navigation Timing
  window.addEventListener('load', function() {
    const navigation = performance.getEntriesByType('navigation')[0];

    // リアルユーザーメトリクス
    const rumData = {
      loadTime: navigation.loadEventEnd - navigation.fetchStart,
      domComplete: navigation.domComplete - navigation.fetchStart,
      firstByte: navigation.responseStart - navigation.fetchStart,
      userAgent: navigator.userAgent,
      timestamp: Date.now()
    };

    // データ送信
    fetch('/api/rum', {
      method: 'POST',
      body: JSON.stringify(rumData)
    });
  });
})();
`
```

### 3. A/Bテストパフォーマンス比較
```typescript
// A/Bテストのパフォーマンス比較
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

## パフォーマンス最適化

### バッチ処理と並列実行
```typescript
// 複数ページの並列測定
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

### キャッシュ最適化
```typescript
// 測定結果のキャッシュ
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

## エラーハンドリング

### 一般的なエラーと解決策

#### 測定タイムアウトエラー
```bash
❌ エラー: パフォーマンス測定がタイムアウトしました
解決策:
1. --timeoutオプションで時間を延長
2. ネットワーク環境を確認
3. 段階的に測定を実行
```

#### メモリ不足エラー
```bash
❌ エラー: メモリ不足により測定に失敗
解決策:
1. 測定回数（-rオプション）を減らす
2. 詳細分析を無効化
3. バッチサイズを縮小
```

#### Lighthouse実行エラー
```bash
❌ エラー: Lighthouse監査に失敗
解決策:
1. Chromeのバージョンを確認
2. ヘッドレスモードで実行
3. 監査カテゴリを制限
```

## 制限事項と考慮事項

### 測定環境の考慮
- ネットワーク環境の変動
- システムリソースの影響
- ブラウザキャッシュの状態
- 外部サービスの応答時間

### 測定精度の向上
- 複数回測定による信頼性確保
- 一貫した環境条件での測定
- 外部要因の排除
- 統計的手法による分析

## ベストプラクティス

### 効果的な測定戦略
1. **重要ページの優先測定**
   - ランディングページ
   - コンバージョンページ
   - 主要機能ページ

2. **継続的モニタリングの実装**
   - CI/CDパイプライン統合
   - 定期的な自動測定
   - パフォーマンス予算の設定

3. **改善サイクルの確立**
   - 測定 → 分析 → 改善 → 再測定
   - 段階的な最適化の実施
   - 効果の測定と検証

### チーム運用
- パフォーマンス基準の共有
- 定期的なレビュー会議の開催
- 改善提案の優先順位付け
- 知識とノウハウの蓄積
