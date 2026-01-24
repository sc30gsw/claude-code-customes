# Test Skill

## 概要

ユニット/E2Eサポート、自動実行、スマート修正機能を備えた高度なテスト実装コマンド。Serena MCPを活用してコード分析を行い、包括的なテストを生成します。

## アクティベーショントリガー

- 新しいコンポーネントや関数のテストが必要な時
- テストカバレッジを向上させたい時
- E2Eテストを追加したい時
- テストの自動修正が必要な時

## 使用方法

```bash
/test <target> [options]
```

## ターゲット指定

| ターゲットタイプ | 例 | 説明 |
|------------------|-----|------|
| コンポーネント名 | `LoginForm`, `UserProfile` | React/Vue/Angularコンポーネント |
| ファイルパス | `utils/validation`, `hooks/useAuth` | モジュールとユーティリティ |
| 関数名 | `calculateTotal`, `formatDate` | 特定の関数 |
| 機能名 | `authentication`, `payment` | 機能領域全体 |

## オプション

| オプション | 説明 | デフォルト |
|------------|------|-----------|
| `-u` | ユニットテストモード | ✅ |
| `-e` | E2Eテストモード + アクセシビリティ注入 | - |
| `-r` | 自動実行とスマート修正 | - |
| `-v` | 詳細出力モード | - |
| `-c` | カバレッジフォーカスモード（90%+目標） | - |
| `-p` | パフォーマンステストモード | - |
| `-w` | ウォッチモード | - |
| `-f` | ファストモード（並列 + キャッシュ） | - |
| `--files=PATTERN` | globでファイル指定 | - |
| `--exclude=PATTERN` | globでファイル除外 | - |
| `--include-deps` | 依存ファイルを含める | - |
| `--dry-run` | テスト設計のみ | - |

## Serena MCP ツール優先

### ファイル操作
- `mcp__serena__find_file` → `Read`（フォールバック）
- `mcp__serena__search_for_pattern` → `Grep`（フォールバック）
- `mcp__serena__find_symbol` → `Glob`（フォールバック）

### コード分析
- `mcp__serena__get_symbols_overview` - シンボル概要
- `mcp__serena__find_referencing_symbols` - シンボル参照
- `mcp__serena__replace_symbol_body` → `Edit`（フォールバック）

## 使用例

```bash
# 基本的な使用
/test LoginComponent -e -r          # E2Eテスト、実行と修正
/test utils/auth -u -r -c           # 高カバレッジユニットテスト
/test PaymentForm -e -v             # E2Eと詳細出力

# ファイルパターン指定
/test components --files="Button*" -u -r
/test src --files="**/*.hook.ts" -u -c
/test api --files="**/*Controller.ts" --include-deps -u -r

# パフォーマンスフォーカス
/test heavyComponent -u -p -f --parallel=8
/test api/bulk -u -p --timeout=60
```

## テスト実装フロー

### ユニットテストモード (-u)
1. Serena MCPでターゲットコード分析
2. テストフレームワーク検出（Jest, Vitest, Mocha）
3. テストケース作成: ハッピーパス、エラーケース、エッジケース

### E2Eテストモード (-e)
1. インタラクティブ要素のコンポーネント分析
2. E2Eフレームワーク検出（Cypress, Playwright）
3. アクセシビリティ属性の注入（data-testid, aria-label）
4. E2Eテストケース作成: ページロード、ユーザー操作、フォーム

### スマート修正 (-r オプション)
1. エラー出力を解析
2. エラー分類: 構文、アサーション、非同期、モック、E2E固有
3. 適切な修正戦略を適用
4. 再実行と反復（最大10回）

## 出力レポート

```
📁 Created/Updated Files:
- src/components/LoginForm.test.tsx
- cypress/e2e/user-authentication.cy.ts

🧪 Implemented Test Cases:
[Unit Tests]
✓ LoginForm happy path tests (3 cases)
✓ LoginForm error handling tests (2 cases)

🚀 Test Execution Results:
[1st Run] ❌ 2 failures
[Auto-Fix Applied] ✅
[2nd Run] ✅ All passed (9 tests)
Coverage: 95.2%
```

## テストパターン

### ハッピーパス
- 正常なユーザーフロー
- 期待される入力と出力
- 成功シナリオ

### エラーハンドリング
- 無効な入力
- ネットワークエラー
- 認証エラー

### エッジケース
- 空の入力
- 極端な値
- 境界条件
- 特殊文字

## 成功指標

- ターゲットカバレッジ達成（80%+または指定値）
- すべてのテストがパス
- エッジケースがカバーされている
- E2Eテストが主要フローを検証
- 自動修正が機能している
