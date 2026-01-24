# Chrome Skill

## 概要

Chrome DevTools MCPを活用した包括的なブラウザ開発サポートシステム。デバッグ、E2Eテスト、パフォーマンス分析、ブラウザ自動化を提供します。

## アクティベーショントリガー

- ブラウザでのデバッグが必要な時
- E2Eテストの実行・作成時
- パフォーマンス分析が必要な時
- UI/UXの検証時
- スクリーンショットの撮影時

## コア機能

### 1. AI駆動ページ分析
- DOM + コンソール + ネットワーク + パフォーマンスの統合分析
- セキュリティ＆アクセシビリティ分析
- コンテンツ要約と構造分析

### 2. デバッグ＆コンソール分析
- コンソールメッセージのフィルタリング表示
- 特定のエラーパターン分析
- デバッグ用JavaScript実行

### 3. E2Eテスト＆自動化
- フォーム操作の完全自動化
- マルチフィールドフォーム自動化
- E2Eテストシナリオ実行

### 4. パフォーマンス分析
- パフォーマンストレーシング
- Core Web Vitals分析
- ネットワークパフォーマンス分析

## 使用方法

```bash
/chrome [action] [target] [options]
```

### 利用可能なアクション

| アクション | 説明 | 例 |
|-----------|------|-----|
| `analyze` | 包括的なページ分析 | `/chrome analyze --full` |
| `summarize` | コンテンツ要約 | `/chrome summarize --structure` |
| `extract` | データ抽出 | `/chrome extract --metadata` |
| `logs` | コンソールメッセージ表示 | `/chrome logs --filter "ERROR"` |
| `debug` | 特定問題のデバッグ | `/chrome debug "login fails"` |
| `test` | E2Eテストシナリオ | `/chrome test --scenario login` |
| `perf` | パフォーマンス分析 | `/chrome perf start --trace` |
| `network` | ネットワークモニタリング | `/chrome network list` |
| `screenshot` | スクリーンショット撮影 | `/chrome screenshot --full-page` |

### オプション

| オプション | 説明 |
|-----------|------|
| `--headless` | ヘッドレスモード |
| `--verbose` | 詳細出力 |
| `--analyze` | 自動分析 |
| `--filter` | コンテンツフィルタリング |

## ツール優先度

Chrome DevTools MCPを全てのブラウザ操作で優先:

- **Visual DOM分析**: `mcp__chrome-devtools__take_snapshot`
- **パフォーマンス分析**: `mcp__chrome-devtools__performance_start_trace`
- **ブラウザ自動化**: `mcp__chrome-devtools__click`, `fill`, `navigate_page`
- **デバッグ**: `mcp__chrome-devtools__list_console_messages`

## 要件

- Chrome DevTools MCPサーバーが設定・起動済み
- Chromeブラウザ（stable/beta/dev/canary）
- Node.js 22.12.0+

## 成功指標

- ページ分析が正常に完了
- パフォーマンスメトリクスが収集される
- E2Eテストが期待通りに動作
- スクリーンショットが正常に撮影される
