---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_click, mcp__playwright__browser_type, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_wait_for
description: Playwright MCPを使用したE2Eテストとアプリケーション動作検証コマンド
---

# Playwright E2Eテスト＆動作検証コマンド

## 概要

Playwright MCPとSerenaツールを統合し、アプリケーション動作テストと仕様検証を自動化するコマンドです。

## 使用方法

### 基本構文
```bash
/playwright-test <ターゲット> [オプション]
```

### ターゲット指定

| ターゲットタイプ | 例 | 説明 |
|-------------|---------|-------------|
| **URL** | `https://example.com` | 外部ウェブサイトテスト |
| **ローカルURL** | `http://localhost:3000` | 開発アプリテスト |
| **ページパス** | `/login`, `/dashboard` | 特定ページテスト |
| **機能名** | `authentication`, `checkout` | 機能フローテスト |

### オプション

| オプション | 説明 | デフォルト |
|--------|-------------|---------|
| `-s, --spec` | 仕様ファイルと比較 | false |
| `-r, --report` | 詳細レポート生成 | false |
| `-i, --interactive` | インタラクティブモード実行 | false |
| `-w, --wait` | 要素表示待機時間（秒） | 5 |
| `-d, --device` | デバイスエミュレーション | desktop |
| `-b, --browser` | ブラウザ指定 | chromium |
| `--headless` | ヘッドレスモード | true |
| `--record` | テスト実行動画記録 | false |
| `--network` | ネットワーク監視 | false |
| `--console` | コンソールログキャプチャ | false |

### 使用例

```bash
# 基本ページテスト
/playwright-test https://myapp.com/login

# ローカル開発環境テスト
/playwright-test http://localhost:3000/dashboard -i -w 10

# 仕様検証
/playwright-test /checkout -s -r

# モバイルデバイステスト
/playwright-test https://myapp.com -d mobile -r

# ネットワーク監視テスト
/playwright-test /api-heavy-page --network --console -r
```

## 機能詳細

### 1. アプリケーション動作テスト

#### 基本フロー検証
- ページ読み込み時間測定
- 必須要素の存在確認
- インタラクティブ要素の動作確認
- フォーム送信プロセス検証

#### エラーハンドリングテスト
- 不正入力動作確認
- ネットワークエラー処理
- JavaScriptエラー検出
- 404/500エラー表示検証

### 2. Serenaツール統合

#### コードベース分析
```bash
# プロジェクト内のテスト対象を特定
mcp__serena__get_symbols_overview -> component-list
mcp__serena__search_for_pattern -> test-targets
```

#### テスト結果保存と学習
```bash
# テスト結果をSerenaメモリに保存
mcp__serena__write_memory: test-results-{timestamp}
# 過去のテスト結果と比較
mcp__serena__read_memory: previous-test-results
```

### 3. 仕様検証機能（-sオプション）

#### 対応仕様ファイル形式
- **要件**: `requirements/*.md`
- **設計ドキュメント**: `docs/design/*.md`
- **API仕様**: `openapi.yaml`, `swagger.json`
- **ユーザーストーリー**: `stories/*.md`

#### 検証項目
1. **UI要素仕様準拠**
   - ボタンテキストと配置の検証
   - フォームフィールドの完全性
   - エラーメッセージの正確性

2. **動作仕様準拠**
   - 入力検証ルール
   - 画面遷移フロー
   - データ処理ロジック

3. **パフォーマンス仕様**
   - ページ読み込み時間
   - APIレスポンス時間
   - リソース使用量

### 4. レポート生成機能（-rオプション）

#### 自動生成レポート
```markdown
# テスト実行レポート - {timestamp}

## 実行概要
- ターゲットURL: {target-url}
- 実行時間: {duration}
- ブラウザ: {browser-type}
- デバイス: {device-type}

## テスト結果
### ✅ 成功項目 ({success-count})
- ページ読み込み: {load-time}ms
- 必須要素: すべて存在
- フォーム送信: 正常動作

### ❌ 失敗項目 ({failure-count})
- ログインボタン: クリック不可
- エラー詳細: {error-message}

## 仕様準拠状況（-sオプション）
### 📋 仕様との比較
- UI仕様準拠率: 95.2%
- 動作仕様準拠率: 88.7%
- 非準拠項目: 3件

## パフォーマンスメトリクス
- First Contentful Paint: {fcp}ms
- Largest Contentful Paint: {lcp}ms
- ネットワークリクエスト: {network-requests}

## 改善推奨事項
1. {improvement-1}
2. {improvement-2}
3. {improvement-3}
```

### 5. インタラクティブテスト機能（-iオプション）

#### 手動操作との組み合わせ
```bash
# インタラクティブモードテスト実行例
/playwright-test localhost:3000/app -i

# 実行中のインタラクティブプロンプト:
> ページが読み込まれました。次の操作を選択:
  1. 要素をクリック
  2. テキストを入力
  3. スクリーンショットを撮る
  4. 仕様をチェック
  5. テストを完了
```

## 実装ワークフロー

### ステップ1: 準備
```typescript
// Serenaでプロジェクト分析
mcp__serena__onboarding()
project_structure = mcp__serena__get_symbols_overview()
test_targets = mcp__serena__search_for_pattern("test-patterns")
```

### ステップ2: ブラウザ起動＆ナビゲーション
```typescript
// Playwrightでブラウザ操作
mcp__playwright__browser_navigate(target_url)
await mcp__playwright__browser_wait_for({time: wait_seconds})
```

### ステップ3: 基本操作検証
```typescript
// DOM構造を取得
page_snapshot = mcp__playwright__browser_snapshot()
// 必須要素を検証
essential_elements = extract_essential_elements(page_snapshot)
// インタラクティブ要素を特定
interactive_elements = find_interactive_elements(page_snapshot)
```

### ステップ4: 機能テスト実行
```typescript
// フォームテスト例
test_form_submission() {
  mcp__playwright__browser_type("email-input", "test@example.com")
  mcp__playwright__browser_type("password-input", "testpass123")
  mcp__playwright__browser_click("submit-button")
  await mcp__playwright__browser_wait_for({text: "Success"})
}
```

### ステップ5: 仕様検証（-sオプション）
```typescript
// 仕様ファイルを読み込み
spec_files = find_specification_files()
// 実際の動作と仕様を比較
compliance_check = compare_with_specifications(
  actual_behavior,
  spec_requirements
)
```

### ステップ6: レポート生成＆保存
```typescript
// テスト結果を集計
test_results = aggregate_test_results()
// Serenaメモリに保存
mcp__serena__write_memory("test-results", test_results)
// レポートファイルを生成
generate_report(test_results, report_format)
```

## エラーハンドリング

### 一般的なエラーと解決策

#### ページ読み込みエラー
```bash
❌ エラー: ページの読み込みに失敗
解決策:
1. URLの正確性を確認
2. ネットワーク接続をチェック
3. --waitオプションで待機時間を延長
```

#### 要素が見つからないエラー
```bash
❌ エラー: 指定された要素が見つからない
解決策:
1. 要素セレクターを確認
2. ページ読み込み完了を待機
3. --interactiveモードで手動確認
```

#### JavaScript実行エラー
```bash
❌ エラー: JavaScript実行中にエラー発生
解決策:
1. --consoleオプションでログをチェック
2. ブラウザ開発ツールで詳細確認
3. --headless=falseで目視確認
```

## パフォーマンス最適化

### 大規模テストの効率化
- 並列実行による時間短縮
- キャッシュ活用による冗長処理削減
- スマート要素検出による処理速度向上

### リソース使用量最適化
- メモリ使用量モニタリング
- ブラウザプロセスの適切な終了
- 大量データ処理の分割実行

## 統合機能

### CI/CDパイプライン統合
```yaml
# GitHub Actions例
- name: Playwright E2Eテスト
  run: /playwright-test ${{ env.STAGING_URL }} -s -r --headless
```

### 他コマンドとの連携
```bash
# 完全ワークフロー: テスト → 分析 → レポート
/playwright-test localhost:3000 -r
/web-analyzer localhost:3000 -r
/visual-regression localhost:3000 -b
```

## 制限事項

### 対応範囲
- ✅ モダンブラウザ（Chrome、Firefox、Safari）
- ✅ レスポンシブデザイン
- ✅ SPA（シングルページアプリケーション）
- ✅ SSR（サーバーサイドレンダリング）

### 制限事項
- ❌ レガシー技術（Flash/Silverlight等）
- ❌ 複雑な認証フロー（OAuth、SAML等）
- ❌ 大量データパフォーマンステスト
- ❌ 複雑なマルチタブインタラクション

## サポート＆トラブルシューティング

### デバッグモード
```bash
# デバッグ情報付きテスト実行
/playwright-test target-url -i --console --network --record
```

### ログファイル
- テスト実行ログ: `logs/playwright-test-{timestamp}.log`
- スクリーンショット: `screenshots/test-{timestamp}.png`
- 動画記録: `videos/test-{timestamp}.mp4`

### コミュニティサポート
- GitHub Issues: 技術的問題の報告
- ドキュメント: 詳細なセットアップと使用方法
- サンプル: 実装例とベストプラクティス
