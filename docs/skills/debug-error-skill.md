# Debug Error Skill

## 概要

Serena MCPを活用した高度なデバッグシステム。インテリジェントなコードベース分析と効率的なエラー解決を提供します。

## アクティベーショントリガー

- エラーが発生した時
- バグの調査が必要な時
- 問題の根本原因を特定したい時
- 複雑なデバッグセッションが必要な時

## 使用方法

```bash
/debug-error "<error_description>" [options]
```

## オプション

| オプション | 説明 | 例 |
|-----------|------|-----|
| `--analyze`, `-a` | 深いSerena分析を有効化 | `/debug-error "crash" -a` |
| `--trace`, `-t` | コードフロートレーシング | `/debug-error "logic error" -t` |
| `--serena-deep`, `-s` | 完全なSerenaツールキット使用 | `/debug-error "complex bug" -s` |
| `--pattern-search`, `-p` | 類似エラーパターン検索 | `/debug-error "timeout" -p` |
| `--memory`, `-m` | デバッグメモリを使用 | `/debug-error "recurring issue" -m` |
| `--interactive`, `-i` | ステップバイステップガイダンス | `/debug-error "unknown issue" -i` |
| `--implement` | 自動的に修正を実装 | `/debug-error "known solution" --implement` |

## ワークフロー

### Step 1: エラー情報収集
- エラーメッセージ、スタックトレース、エラーコードを収集
- タイミング、発生場所、頻度を記録
- `mcp__serena__search_for_pattern`で関連パターンを検索

### Step 2: エラーの再現
- 最小限のテストケースを作成
- 正確な手順を文書化

### Step 3: スタックトレース分析
- 下から上へ読む
- 正確な失敗行を特定
- 実行パスをトレース

### Step 4: コードコンテキスト調査
- `mcp__serena__find_symbol`で位置コンテキストを取得
- `mcp__serena__find_referencing_symbols`で依存関係を確認
- git履歴と最近の変更をチェック

### Step 5: 仮説形成
- 一般的な原因を考慮: null参照、型不一致、レース条件

### Step 6: 系統的調査
- Serenaを使用したインテリジェントなテスト
- `mcp__serena__insert_after_symbol`でターゲットログを追加

### Step 7: ソリューション実装
- `mcp__serena__replace_symbol_body`で対象修正
- 包括的なエラーハンドリングを追加

### Step 8: テストと予防
- 元のエラーに対して修正をテスト
- ユニットテストとインテグレーションテストを追加
- エラーハンドリングとロギングを改善

## ベストプラクティス

1. **パターン検索から開始** - 類似の問題がないか最初にチェック
2. **メモリを活用** - 過去のデバッグセッションを活用
3. **依存関係をトレース** - エラー伝播を理解
4. **ソリューションを文書化** - 将来の参照のために成功したアプローチを保存

## 成功指標

- 根本原因が特定される
- エラーが再現可能
- 修正が適用され検証済み
- 同様のエラーを防ぐテストが追加される
