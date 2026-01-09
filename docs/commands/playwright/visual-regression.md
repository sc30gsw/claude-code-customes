---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_snapshot, mcp__playwright__browser_wait_for, Glob, Grep
description: Playwright MCPを使用したビジュアルリグレッションテストとUI変更検出コマンド
---

# Visual Regression Test - ビジュアルリグレッションテスト

## 概要

Playwright MCPとSerenaツールを統合し、UIのビジュアル変更を検出して意図しない修正を防止するビジュアルリグレッションテストコマンドです。

## 使用方法

### 基本構文
```bash
/visual-regression <target> [options]
```

### ターゲット指定

| ターゲットタイプ | 例 | 説明 |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | 開発アプリのテスト |
| **本番URL** | `https://myapp.com` | 本番環境との比較 |
| **ページパス** | `/dashboard`, `/profile` | 特定ページのテスト |
| **コンポーネント** | `Button`, `Modal` | コンポーネントレベルテスト |

### オプション

| オプション | 説明 | デフォルト |
|--------|-------------|---------|
| `-b, --baseline` | ベースライン画像を作成 | false |
| `-c, --compare` | 既存ベースラインと比較 | true |
| `-f, --full-page` | フルページスクリーンショット | false |
| `-m, --mobile` | モバイル版も同時テスト | false |
| `-d, --devices` | 複数デバイステスト | desktop |
| `-t, --threshold` | 差分許容閾値 (%) | 0.2 |
| `-i, --ignore-regions` | 無視する領域を指定 | none |
| `-r, --report` | 詳細レポート生成 | false |
| `-a, --auto-update` | 差分時の自動更新確認 | false |
| `--animations` | アニメーション無効化 | true |
| `--wait-for` | 要素表示待機時間 | 2秒 |

### 使用例

```bash
# 初期ベースライン画像を作成
/visual-regression http://localhost:3000 -b -f

# 変更後の比較テスト
/visual-regression http://localhost:3000 -c -r

# マルチデバイステスト
/visual-regression /dashboard -m -d "desktop,tablet,mobile"

# 特定閾値での比較
/visual-regression /profile -c -t 0.5

# 本番環境との比較
/visual-regression https://staging.myapp.com -c --baseline-url=https://myapp.com

# コンポーネントレベルテスト
/visual-regression /storybook -c --component=Button --states=all
```

## 機能詳細

### 1. ベースライン管理 (-b オプション)

#### 初期ベースライン作成
```bash
# プロジェクト全体のベースラインを作成
/visual-regression http://localhost:3000 -b -f
```

#### ベースライン画像構造
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

#### バージョン管理
- ベースライン履歴管理のためのGit統合
- ブランチ固有のベースライン設定
- タグベースのベースライン固定

### 2. 差分検出と比較 (-c オプション)

#### 画像比較アルゴリズム
```typescript
interface ComparisonResult {
  similarity: number        // 類似度 (0-100%)
  pixelDifference: number   // 差分ピクセル数
  regions: DiffRegion[]     // 詳細差分領域
  severity: 'minor' | 'major' | 'breaking'
}

interface DiffRegion {
  x: number
  y: number
  width: number
  height: number
  significance: number  // 重要度 (0-1)
}
```

#### 差分可視化
- 差分エリアのハイライト表示
- ピクセルレベルの変更検出
- 色変更分析
- レイアウトシフト検出

### 3. マルチデバイス対応 (-d オプション)

#### サポートデバイス
```typescript
const DevicePresets = {
  desktop: { width: 1920, height: 1080 },
  laptop: { width: 1366, height: 768 },
  tablet: { width: 768, height: 1024 },
  mobile: { width: 375, height: 667 },
  'mobile-landscape': { width: 667, height: 375 }
}
```

#### レスポンシブテスト
- ブレークポイント固有のスクリーンショット
- クロスデバイス整合性チェック
- 画面回転対応検証

### 4. 無視領域設定 (-i オプション)

#### 動的コンテンツ除外
```json
{
  "ignoreRegions": [
    {
      "selector": ".timestamp",
      "reason": "動的な時刻表示"
    },
    {
      "selector": ".user-avatar",
      "reason": "ユーザー固有の画像"
    },
    {
      "coordinates": { "x": 0, "y": 0, "width": 100, "height": 50 },
      "reason": "広告エリア"
    }
  ]
}
```

#### 除外設定パターン
- セレクタ指定による要素除外
- 座標指定による領域除外
- 正規表現によるテキスト除外
- 動的コンテンツの自動検出

### 5. Serena統合機能

#### コンポーネント分析統合
```typescript
// コンポーネント構造を取得してテスト対象を特定
const components = await mcp__serena__get_symbols_overview()
const testTargets = identifyVisualTestTargets(components)

// 過去のテスト結果と比較
const previousResults = await mcp__serena__read_memory('visual-test-history')
const trendAnalysis = analyzeTrends(previousResults, currentResults)
```

#### 学習・改善機能
```typescript
// 頻繁に誤検出される領域を学習
await mcp__serena__write_memory('false-positive-patterns', {
  selector: '.dynamic-element',
  frequency: falsePositiveCount,
  recommendations: ['ignore', 'mask', 'stabilize']
})
```

### 6. 自動更新機能 (-a オプション)

#### インテリジェント更新
```bash
# 意図的な変更に対する自動更新確認
Visual diff detected in login-page.png
Changes appear to be intentional (UI redesign)
Update baseline? [y/N/review]: review

Showing differences:
- Button color changed: #007bff → #28a745
- Spacing increased: 16px → 20px
- New icon added to header

Confirm update? [y/N]: y
```

#### 更新ポリシー
- 自動デザイン変更検出
- 必須チームレビュー設定
- 段階的更新（部分承認）
- ロールバック機能

## 実装ワークフロー

### ステップ1: 環境準備とセットアップ
```typescript
// Serenaでプロジェクト構造を分析
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// ページとコンポーネントを特定
const testTargets = await mcp__serena__search_for_pattern('visual-test-targets')
```

### ステップ2: ベースライン作成（初回）
```typescript
for (const device of targetDevices) {
  // デバイス設定
  await mcp__playwright__browser_resize(device.width, device.height)

  // ページアクセス
  await mcp__playwright__browser_navigate(targetUrl)
  await mcp__playwright__browser_wait_for({time: waitTime})

  // アニメーション無効化
  if (options.disableAnimations) {
    await mcp__playwright__browser_evaluate(`
      document.querySelectorAll('*').forEach(el => {
        el.style.animationDuration = '0s';
        el.style.transitionDuration = '0s';
      });
    `)
  }

  // スクリーンショット取得
  const screenshot = await mcp__playwright__browser_take_screenshot({
    fullPage: options.fullPage,
    filename: `baseline-${device.name}-${pageName}.png`
  })
}
```

### ステップ3: 比較テスト実行
```typescript
// 現在の画面をキャプチャ
const currentScreenshot = await captureCurrentState(targetUrl, device)

// ベースラインと比較
const comparisonResult = await compareImages(
  baselineImage,
  currentScreenshot,
  {
    threshold: options.threshold,
    ignoreRegions: options.ignoreRegions
  }
)

// 差分を分析
const diffAnalysis = await analyzeDifferences(comparisonResult)
```

### ステップ4: 結果分析とレポート生成
```typescript
// テスト結果を集計
const testResults = {
  totalTests: testCount,
  passed: passedCount,
  failed: failedCount,
  differences: detectedDiffs,
  severity: calculateSeverity(detectedDiffs)
}

// Serenaメモリに保存
await mcp__serena__write_memory('visual-regression-results', {
  timestamp: Date.now(),
  results: testResults,
  baseline: baselineVersion
})
```

## レポート生成機能 (-r オプション)

### 詳細レポート構造
```markdown
# ビジュアルリグレッションテストレポート

## 📊 テスト概要
- 実行日時: {timestamp}
- 対象URL: {target-urls}
- テストデバイス: {device-list}
- ベースライン: {baseline-version}

## 🎯 テスト結果サマリー
- 総テスト数: {total-tests}
- 合格: {passed-tests} ✅
- 不合格: {failed-tests} ❌
- 差分検出: {detected-diffs} ⚠️

## 📸 差分詳細

### 破壊的変更
1. **ログインページ** - デスクトップ
   - 差分率: 15.2%
   - 影響: レイアウト崩壊
   - 📷 [比較画像](./diffs/login-desktop-diff.png)

### 軽微な変更
1. **ダッシュボード** - モバイル
   - 差分率: 2.1%
   - 影響: 色変更
   - 📷 [比較画像](./diffs/dashboard-mobile-diff.png)

## 🔧 推奨アクション
{recommendations}

## 📈 トレンド分析
{trend-analysis}
```

### 画像付きレポート
- Before/After並列表示
- 差分ハイライト画像
- ピクセルレベル変更マップ
- 領域別影響分析

## CI/CD統合

### GitHub Actions統合
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

### 自動化ポリシー
- PRマージ前の必須チェック
- 失敗時の自動ブロック
- 必須レビューフラグ設定
- Slack/Teams通知統合

## 高度な機能

### 1. コンポーネント分離テスト
```bash
# Storybook統合
/visual-regression http://localhost:6006 --storybook --component=Button --states=all

# 生成されるテストケース:
# - Button/Default
# - Button/Primary
# - Button/Secondary
# - Button/Disabled
# - Button/Loading
```

### 2. アニメーション対応
```typescript
// アニメーション完了待機
const animationSettings = {
  disableAnimations: true,
  waitForAnimations: false,
  captureAnimationFrames: false,  // ビデオキャプチャ
  animationTimeout: 5000
}
```

### 3. 動的コンテンツ正規化
```typescript
// 動的要素のマスキング
const normalizationRules = [
  { selector: '.timestamp', replacement: 'MOCKED_TIME' },
  { selector: '.user-id', replacement: 'USER_123' },
  { selector: '.random-uuid', pattern: /[0-9a-f-]{36}/, replacement: 'UUID' }
]
```

## パフォーマンス最適化

### 画像処理最適化
- 圧縮アルゴリズムの使用
- 並列処理による高速化
- キャッシュ機能の活用
- 差分領域のみの比較

### ストレージ管理
- 古いスクリーンショットの自動削除
- 圧縮によるスペース節約
- クラウドストレージ統合
- バージョン管理との同期

## エラーハンドリング

### よくあるエラーと解決策

#### ベースライン不一致エラー
```bash
❌ Error: Baseline image not found
解決策:
1. -b オプションでベースラインを作成
2. ファイルパスを確認
3. ブランチ設定を検証
```

#### 閾値超過エラー
```bash
❌ Error: Difference exceeds threshold (0.2%)
解決策:
1. -t オプションで閾値を調整
2. 意図的な変更の場合は -a で更新
3. 無視領域の追加を検討
```

#### レンダリングエラー
```bash
❌ Error: Page rendering incomplete
解決策:
1. --wait-for オプションで待機時間を延長
2. 必要な要素の読み込みを確認
3. JavaScriptエラーを調査
```

## 制限事項と考慮点

### テスト対象
- ✅ 静的コンテンツ
- ✅ CSS/レイアウト変更
- ✅ レスポンシブデザイン
- ⚠️ 動的コンテンツ（設定が必要）

### 制限事項
- ❌ ビデオ/GIFアニメーション
- ❌ 詳細なCanvas要素比較
- ❌ 3D/WebGL要素
- ❌ 非決定論的レンダリング

## ベストプラクティス

### 効果的なテスト設計
1. **重要ページを優先**
   - ランディングページ
   - 決済/ログインページ
   - ダッシュボード画面

2. **適切な閾値設定**
   - 厳格: 0.1-0.2%（重要ページ）
   - 標準: 0.5-1.0%（一般ページ）
   - 緩和: 2.0-5.0%（動的要素あり）

3. **メンテナンス戦略**
   - 定期的なベースライン更新
   - 不要なスクリーンショットの削除
   - テスト結果の分析と改善

### チーム運用
- デザイン変更時のベースライン更新フロー
- レビュープロセスの確立
- 誤検出の学習・改善サイクル
- 新機能追加時のテスト拡張
