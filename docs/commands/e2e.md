# /e2e - E2Eテストコマンド

---
description: Playwrightを使用したエンドツーエンドテストの生成と実行。テストジャーニー作成、スクリーンショット/ビデオ/トレースのキャプチャ、アーティファクトのアップロード。
---

## 概要

`/e2e` コマンドは **e2e-runner** エージェントを呼び出し、Playwrightを使用したエンドツーエンドテストの生成、メンテナンス、実行を行います。

## 機能

1. **テストジャーニー生成** - ユーザーフロー用のPlaywrightテストを作成
2. **E2Eテスト実行** - 複数ブラウザでテストを実行
3. **アーティファクトキャプチャ** - 失敗時のスクリーンショット、ビデオ、トレース
4. **結果アップロード** - HTMLレポートとJUnit XML
5. **フレーキーテスト検出** - 不安定なテストを隔離

## 使用タイミング

以下の場合に `/e2e` を使用:
- クリティカルユーザージャーニーのテスト（ログイン、取引、決済）
- マルチステップフローのエンドツーエンド検証
- UIインタラクションとナビゲーションのテスト
- フロントエンドとバックエンド間の統合検証
- 本番デプロイ準備

## 使用例

```
User: /e2e マーケット検索と表示フローをテスト

Agent (e2e-runner):
# E2Eテスト生成: マーケット検索と表示フロー

## テストシナリオ

**ユーザージャーニー:** マーケット検索 → 結果表示 → マーケットクリック → 詳細表示

## 生成されたテストコード

```typescript
// tests/e2e/markets/search-and-view.spec.ts
import { test, expect } from '@playwright/test'
import { MarketsPage } from '../../pages/MarketsPage'

test.describe('Market Search and View Flow', () => {
  test('user can search markets and view details', async ({ page }) => {
    // 1. マーケットページに移動
    const marketsPage = new MarketsPage(page)
    await marketsPage.goto()

    // 2. 検索実行
    await marketsPage.searchMarkets('election')

    // APIレスポンスを待つ
    await page.waitForResponse(resp =>
      resp.url().includes('/api/markets/search') && resp.status() === 200
    )

    // 3. 検索結果を確認
    const marketCards = marketsPage.marketCards
    await expect(marketCards.first()).toBeVisible()

    // スクリーンショット取得
    await page.screenshot({ path: 'artifacts/search-results.png' })

    // 4. 最初の結果をクリック
    await marketCards.first().click()

    // 5. 詳細ページの読み込みを確認
    await expect(page).toHaveURL(/\/markets\/[a-z0-9-]+/)
  })
})
```

## テスト結果

```
╔══════════════════════════════════════════════════════════════╗
║                    E2E Test Results                          ║
╠══════════════════════════════════════════════════════════════╣
║ Status:     ✅ ALL TESTS PASSED                              ║
║ Total:      3 tests                                          ║
║ Passed:     3 (100%)                                         ║
║ Duration:   9.1s                                             ║
╚══════════════════════════════════════════════════════════════╝

Artifacts:
📸 Screenshots: 2 files
📊 HTML Report: playwright-report/index.html
```
```

## テストアーティファクト

**全テストで生成:**
- タイムラインと結果を含むHTMLレポート
- CI統合用JUnit XML

**失敗時のみ:**
- 失敗状態のスクリーンショット
- テストのビデオ録画
- デバッグ用トレースファイル
- ネットワークログ
- コンソールログ

## クイックコマンド

```bash
# すべてのE2Eテストを実行
npx playwright test

# 特定テストファイルを実行
npx playwright test tests/e2e/markets/search.spec.ts

# ヘッドモードで実行（ブラウザ表示）
npx playwright test --headed

# デバッグモード
npx playwright test --debug

# テストコード生成
npx playwright codegen http://localhost:3000

# レポート表示
npx playwright show-report
```

## ベストプラクティス

**DO:**
- ✅ 保守性のためPage Object Modelを使用
- ✅ セレクタにdata-testid属性を使用
- ✅ 任意のタイムアウトでなくAPIレスポンスを待つ
- ✅ クリティカルユーザージャーニーをエンドツーエンドでテスト
- ✅ メインにマージ前にテストを実行
- ✅ テスト失敗時にアーティファクトをレビュー

**DON'T:**
- ❌ 脆弱なセレクタを使用（CSSクラスは変わる可能性）
- ❌ 実装詳細をテスト
- ❌ 本番環境に対してテスト実行
- ❌ フレーキーテストを無視
- ❌ すべてのエッジケースをE2Eでテスト（ユニットテストを使用）

## 他のコマンドとの連携

- `/plan` でテストすべきクリティカルジャーニーを特定
- `/tdd` でユニットテスト（より高速、より詳細）
- `/e2e` で統合とユーザージャーニーテスト
- `/code-review` でテスト品質を確認

## 関連エージェント

このコマンドは以下のエージェントを呼び出します:
`~/.claude/agents/e2e-runner.md`
