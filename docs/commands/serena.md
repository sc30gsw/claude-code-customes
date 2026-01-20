# Serena Command

## 概要

Serena MCPを使用したトークン効率の高い構造化アプリ開発コマンド。最小限のトークンで最大の開発効率を実現します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/serena` |
| 引数 | `<task_description>` |
| 用途 | 効率的なアプリ開発、問題解決 |
| 許可ツール | すべてのツール |

## コア機能

### 1. シンボリック操作
- 関数・クラスの検索と編集
- リファクタリング（名前変更、移動）
- 依存関係の追跡

### 2. メモリ管理
- セッション間のコンテキスト保持
- プロジェクト固有の知識蓄積
- 学習した設計パターンの適用

### 3. 構造化開発
- 段階的な実装アプローチ
- テスト駆動開発の支援
- コード品質の維持

## 使用例

```bash
# コンポーネント作成
/serena "create UserProfile component with avatar and bio"

# API実装
/serena "implement REST API for product CRUD"

# リファクタリング
/serena "rename getUserData to fetchUserProfile"
```

## オプションフラグ

| フラグ | 説明 |
|--------|------|
| `-q` | Quick mode（3-5 thoughts） |
| `-c` | Code-focused output |
| `--summary` | Summary only |

## Serena MCPツール

### 検索・分析
- `find_symbol` - シンボル検索
- `find_referencing_symbols` - 参照検索
- `get_symbols_overview` - ファイル概要
- `search_for_pattern` - パターン検索

### 編集
- `replace_symbol_body` - シンボル置換
- `insert_after_symbol` - シンボル後に挿入
- `insert_before_symbol` - シンボル前に挿入
- `rename_symbol` - シンボル名変更

### メモリ
- `write_memory` - 情報保存
- `read_memory` - 情報読み取り
- `list_memories` - メモリ一覧

## ベストプラクティス

1. **明確なタスク記述** - 具体的な目標を指定
2. **段階的な実装** - 小さなステップで進める
3. **メモリの活用** - 重要な決定を記録
4. **シンボリック操作優先** - ファイル全体の読み込みを避ける
