---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_evaluate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_console_messages, mcp__playwright__browser_wait_for
description: Playwright MCPを使用したアクセシビリティテストとWCAG準拠検証コマンド
---

# アクセシビリティテスト - Webアクセシビリティテスト

## 概要

Playwright MCPとSerenaツールを統合し、WCAG 2.1/2.2準拠のアクセシビリティ検証を自動実行するコマンドです。

## 使用方法

### 基本構文
```bash
/accessibility-test <ターゲット> [オプション]
```

### ターゲット指定

| ターゲットタイプ | 例 | 説明 |
|-------------|---------|-------------|
| **URL** | `http://localhost:3000` | 開発アプリのテスト |
| **本番URL** | `https://myapp.com` | 本番環境のテスト |
| **ページパス** | `/form`, `/dashboard` | 特定ページのテスト |
| **コンポーネント** | `Modal`, `Form` | コンポーネントレベルテスト |

### オプション

| オプション | 説明 | デフォルト |
|--------|-------------|---------|
| `-l, --level` | WCAG準拠レベル | AA |
| `-s, --standard` | WCAGバージョン | 2.1 |
| `-k, --keyboard` | キーボードナビゲーションテスト | true |
| `-c, --color` | 色とコントラストテスト | true |
| `-t, --text` | テキストとスクリーンリーダーテスト | true |
| `-f, --focus` | フォーカス管理テスト | true |
| `-a, --aria` | ARIA属性テスト | true |
| `-r, --report` | 詳細レポート生成 | false |
| `-i, --interactive` | インタラクティブ修正モード | false |
| `-m, --mobile` | モバイルアクセシビリティテスト | false |
| `--screen-reader` | スクリーンリーダーシミュレーション | false |
| `--auto-fix` | 自動修正提案 | false |

### 使用例

```bash
# 基本アクセシビリティテスト
/accessibility-test http://localhost:3000

# 厳格なWCAG AAA準拠テスト
/accessibility-test /form -l AAA -s 2.2 -r

# キーボードナビゲーション重視テスト
/accessibility-test /dashboard -k -f --screen-reader

# モバイルアクセシビリティテスト
/accessibility-test https://myapp.com -m -c -t

# インタラクティブ修正モード
/accessibility-test /signup -i --auto-fix -r

# コンポーネントレベルテスト
/accessibility-test /storybook --component=Modal -a -f
```

## 機能詳細

### 1. WCAG準拠チェック

#### 対応標準レベル
```typescript
enum WCAGLevel {
  A = 'A',        // 最低要件
  AA = 'AA',      // 標準要件（推奨）
  AAA = 'AAA'     // 最高レベル要件
}

enum WCAGVersion {
  'WCAG_2_0' = '2.0',
  'WCAG_2_1' = '2.1',  // 推奨
  'WCAG_2_2' = '2.2'   // 最新
}
```

#### 検証カテゴリ
1. **知覚可能**
   - 画像の代替テキスト
   - 動画・音声のキャプションと説明
   - 色だけに依存しない情報提示
   - 適切なコントラスト比

2. **操作可能**
   - キーボードアクセシビリティ
   - 発作を引き起こすコンテンツの回避
   - 適切なタイムアウト設定
   - ナビゲーション支援

3. **理解可能**
   - 読みやすい言語使用
   - 予測可能な機能
   - 入力エラーの特定と修正支援

4. **堅牢**
   - 支援技術との互換性
   - 将来の技術変化への適応

### 2. キーボードナビゲーションテスト（-kオプション）

#### テスト対象操作
```typescript
const keyboardTests = [
  // 基本ナビゲーション
  { key: 'Tab', action: 'フォーカス移動（前方）' },
  { key: 'Shift+Tab', action: 'フォーカス移動（後方）' },
  { key: 'Enter', action: 'アクティベーション' },
  { key: 'Space', action: 'ボタン/チェックボックス操作' },

  // 矢印キーナビゲーション
  { key: 'ArrowUp', action: 'メニュー/リスト上移動' },
  { key: 'ArrowDown', action: 'メニュー/リスト下移動' },
  { key: 'ArrowLeft', action: 'タブ/カルーセル左移動' },
  { key: 'ArrowRight', action: 'タブ/カルーセル右移動' },

  // エスケープと終了操作
  { key: 'Escape', action: 'モーダル/メニューを閉じる' },
  { key: 'Home', action: '最初の要素にジャンプ' },
  { key: 'End', action: '最後の要素にジャンプ' }
]
```

#### フォーカス管理テスト
```typescript
// フォーカストラップ検証
async function testFocusTrap(modalSelector: string) {
  // モーダルを開く
  await mcp__playwright__browser_click(modalSelector)

  // フォーカスが最初の要素にあることを確認
  const firstFocusable = await getFirstFocusableElement()
  expect(document.activeElement).toBe(firstFocusable)

  // Tabで最後の要素に移動
  await navigateToLastElement()

  // Tabで最初の要素に戻ることを確認
  await mcp__playwright__browser_press_key('Tab')
  expect(document.activeElement).toBe(firstFocusable)

  // Escapeでモーダルが閉じることを確認
  await mcp__playwright__browser_press_key('Escape')
  expect(document.querySelector('.modal')).toBeNull()
}
```

### 3. 色とコントラストテスト（-cオプション）

#### コントラスト比計算
```typescript
interface ContrastTest {
  element: Element
  foregroundColor: string
  backgroundColor: string
  ratio: number
  wcagLevel: 'AA' | 'AAA'
  passed: boolean
}

// WCAG標準
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
    AAA: 3.0  // UIコンポーネント、グラフィック要素
  }
}
```

#### 色依存チェック
```typescript
// 色だけに依存した情報提示の検出
const colorDependencyTests = [
  {
    issue: '必須フィールドが赤色のみで表示',
    fix: 'アスタリスク（*）またはaria-required属性を追加'
  },
  {
    issue: 'エラー状態が色変更のみで表示',
    fix: 'エラーアイコンまたはテキストメッセージを追加'
  },
  {
    issue: 'ステータスが色のみで区別',
    fix: 'ラベルテキストまたはアイコンを併用'
  }
]
```

### 4. ARIA属性テスト（-aオプション）

#### 必須ARIA属性チェック
```typescript
const ariaValidationRules = [
  // ランドマーク
  { role: 'main', required: true, unique: true },
  { role: 'navigation', required: false, multiple: true },
  { role: 'banner', required: true, unique: true },
  { role: 'contentinfo', required: true, unique: true },

  // インタラクティブ要素
  { role: 'button', requiredProps: ['aria-label', 'accessible-name'] },
  { role: 'link', requiredProps: ['accessible-name'] },
  { role: 'textbox', requiredProps: ['aria-label'] },

  // 状態管理
  { attribute: 'aria-expanded', validValues: ['true', 'false'] },
  { attribute: 'aria-checked', validValues: ['true', 'false', 'mixed'] },
  { attribute: 'aria-selected', validValues: ['true', 'false'] }
]
```

#### セマンティック構造検証
```typescript
// 見出し階層検証
function validateHeadingHierarchy() {
  const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6')
  const issues: string[] = []

  let previousLevel = 0
  headings.forEach((heading, index) => {
    const currentLevel = parseInt(heading.tagName.charAt(1))

    if (index === 0 && currentLevel !== 1) {
      issues.push('最初の見出しはh1でなければなりません')
    }

    if (currentLevel - previousLevel > 1) {
      issues.push(`見出しレベルがスキップされています: h${previousLevel} → h${currentLevel}`)
    }

    previousLevel = currentLevel
  })

  return issues
}
```

### 5. スクリーンリーダーシミュレーション（--screen-readerオプション）

#### スクリーンリーダーテキスト生成
```typescript
async function generateScreenReaderText(element: Element): Promise<string> {
  const computedName = await mcp__playwright__browser_evaluate(`
    const element = arguments[0];

    // アクセシブル名の計算
    function computeAccessibleName(el) {
      // aria-labelledby優先
      if (el.hasAttribute('aria-labelledby')) {
        const ids = el.getAttribute('aria-labelledby').split(' ');
        return ids.map(id => document.getElementById(id)?.textContent).join(' ');
      }

      // aria-label
      if (el.hasAttribute('aria-label')) {
        return el.getAttribute('aria-label');
      }

      // フォーム要素のラベル
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        const label = document.querySelector(\`label[for="\${el.id}"]\`);
        if (label) return label.textContent;
      }

      // テキストコンテンツ
      return el.textContent || el.alt || '';
    }

    return computeAccessibleName(element);
  `, element)

  return computedName
}
```

### 6. Serena統合機能

#### コンポーネント分析統合
```typescript
// アクセシビリティパターン学習
async function learnAccessibilityPatterns() {
  const components = await mcp__serena__get_symbols_overview()

  // よく使用されるコンポーネントのアクセシビリティパターンを特定
  const patterns = analyzeAccessibilityPatterns(components)

  await mcp__serena__write_memory('accessibility-patterns', {
    common_violations: patterns.violations,
    best_practices: patterns.bestPractices,
    component_templates: patterns.templates
  })
}
```

#### 修正提案生成
```typescript
// Serena知識を使用した修正提案
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

### 7. 自動修正機能（--auto-fixオプション）

#### 自動軽微問題修正
```typescript
const autoFixRules = [
  {
    issue: 'alt属性が欠落',
    fix: (img: HTMLImageElement) => {
      if (img.src.includes('decorative') || img.classList.contains('decoration')) {
        img.alt = '' // 装飾画像
      } else {
        img.alt = generateAltText(img.src) // AI/ルールベース生成
      }
    }
  },
  {
    issue: 'フォームラベルが欠落',
    fix: (input: HTMLInputElement) => {
      if (!input.labels?.length && !input.getAttribute('aria-label')) {
        const label = createLabel(input)
        input.parentNode?.insertBefore(label, input)
      }
    }
  }
]
```

#### インタラクティブ修正モード（-iオプション）
```bash
# インタラクティブ修正提案選択
12件のアクセシビリティ問題が見つかりました:

1. [クリティカル] ボタンにアクセシブル名がありません
   場所: .header .user-menu button
   修正オプション:
   a) aria-label="ユーザーメニュー"を追加
   b) 表示テキストコンテンツを追加
   c) aria-labelledby参照を使用
   選択 [a/b/c/skip]: a

2. [高] 画像にalt属性がありません
   場所: .hero img
   提案alt: "チームコラボレーションダッシュボードのスクリーンショット"
   承認? [y/n/edit]: edit
   altテキストを入力: 私たちのコラボレーションプラットフォームを使用するプロフェッショナルチーム
```

## 実装ワークフロー

### ステップ1: 初期分析とセットアップ
```typescript
// Serenaでプロジェクト分析
await mcp__serena__onboarding()
const projectStructure = await mcp__serena__get_symbols_overview()

// アクセシビリティテスト対象を特定
const testTargets = await mcp__serena__search_for_pattern('accessibility-critical')
```

### ステップ2: ページアクセスと初期評価
```typescript
// ページアクセス
await mcp__playwright__browser_navigate(targetUrl)
await mcp__playwright__browser_wait_for({time: 3})

// axe-coreライブラリを注入
await mcp__playwright__browser_evaluate(`
  const script = document.createElement('script');
  script.src = 'https://unpkg.com/axe-core@latest/axe.min.js';
  document.head.appendChild(script);
`)

// 初期アクセシビリティ検査
const snapshot = await mcp__playwright__browser_snapshot()
```

### ステップ3: カテゴリ別テスト実行
```typescript
// キーボードナビゲーションテスト
if (options.keyboard) {
  const keyboardResults = await runKeyboardTests()
}

// 色とコントラストテスト
if (options.color) {
  const colorResults = await runColorContrastTests()
}

// ARIA属性テスト
if (options.aria) {
  const ariaResults = await runAriaTests()
}
```

### ステップ4: 包括的分析とレポート生成
```typescript
// 結果統合
const comprehensiveResults = {
  summary: generateSummary(allResults),
  violations: categorizeViolations(allResults),
  recommendations: generateRecommendations(allResults),
  fixSuggestions: await generateFixSuggestions(violations)
}

// Serenaメモリに保存
await mcp__serena__write_memory('accessibility-test-results', {
  url: targetUrl,
  timestamp: Date.now(),
  results: comprehensiveResults
})
```

## レポート生成機能（-rオプション）

### 詳細レポート構造
```markdown
# アクセシビリティテストレポート

## 📊 テスト概要
- ターゲットURL: {target-url}
- WCAG標準: {wcag-version} レベル{level}
- テスト日時: {timestamp}
- 総合スコア: {score}/100

## 🎯 テスト結果サマリー
- 🔴 クリティカル問題: {critical-count}
- 🟡 重大問題: {serious-count}
- 🔵 軽微問題: {moderate-count}
- ✅ 準拠項目: {passed-count}

## 🔥 クリティカル問題

### 1. キーボードでアクセスできない
**問題**: メインナビゲーションがキーボードでアクセスできません
**場所**: `.main-nav .dropdown`
**WCAG**: 2.1.1 キーボード（レベルA）
**修正方法**:
```html
<!-- 修正前 -->
<div class="dropdown" onclick="toggleMenu()">

<!-- 修正後 -->
<button class="dropdown" onclick="toggleMenu()"
        onkeydown="handleKeyDown(event)"
        aria-expanded="false"
        aria-haspopup="true">
```

### 2. コントラスト比が不十分
**問題**: テキストと背景のコントラスト比が3.2:1で、標準の4.5:1を下回っています
**場所**: `.secondary-text`
**WCAG**: 1.4.3 コントラスト（レベルAA）
**修正方法**: テキスト色を#666666から#484848に変更

## 🛠️ 自動修正された項目
{auto-fixed-items}

## 📋 実装チェックリスト
- [ ] すべての画像にalt属性を追加
- [ ] フォーム要素にラベルを関連付け
- [ ] 見出し階層を修正（h2→h3→h4）
- [ ] フォーカス表示を改善
- [ ] aria-liveリージョンでステータス更新を通知

## 📈 改善傾向
{improvement-trends}
```

### スコアリングシステム
```typescript
interface AccessibilityScore {
  overall: number          // 0-100 総合スコア
  keyboard: number         // キーボードアクセシビリティ
  visual: number          // 視覚的アクセシビリティ
  cognitive: number       // 認知的アクセシビリティ
  technical: number       // 技術的実装品質
}

// スコア計算
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

## CI/CD統合

### GitHub Actions統合
```yaml
name: アクセシビリティテスト
on: [push, pull_request]

jobs:
  a11y-test:
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

      - name: アクセシビリティテスト実行
        run: /accessibility-test http://localhost:3000 -l AA -r

      - name: アクセシビリティレポートアップロード
        uses: actions/upload-artifact@v3
        with:
          name: accessibility-report
          path: accessibility-report.html

      - name: PRに結果をコメント
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

### 品質ゲート設定
```yaml
# 最低品質基準
accessibility_gates:
  min_score: 85
  max_critical_issues: 0
  max_serious_issues: 2
  required_wcag_level: AA
```

## 制限事項と考慮事項

### テスト可能範囲
- ✅ 静的HTMLとCSS
- ✅ JavaScript動的コンテンツ
- ✅ フォームとインタラクション
- ⚠️ 複雑なカスタムウィジェット

### 検出が困難な問題
- ❌ 認知負荷の問題
- ❌ 主観的な読みやすさ評価
- ❌ 複雑なワークフローのユーザビリティ
- ❌ 実デバイス支援技術の動作

## ベストプラクティス

### 継続的改善
1. **定期的なテスト実行**
   - CI/CDパイプラインへの統合
   - リリース前の必須チェック
   - 定期的なフルページスキャン

2. **チーム教育**
   - アクセシビリティガイドラインの共有
   - 修正のための知識ベース構築
   - 内部ベストプラクティスの標準化

3. **ユーザーテスト**
   - 実際の支援技術ユーザーとのテスト
   - 多様性を考慮したユーザビリティテスト
   - 継続的なフィードバック統合
