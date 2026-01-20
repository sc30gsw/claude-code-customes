# Kiro Spec Design Command

## 概要

仕様に対する包括的な技術設計ドキュメントを作成するコマンド。アーキテクチャ、コンポーネント、インターフェース、データモデルを定義します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:spec-design` |
| 引数 | `<feature-name> [-y]` |
| 用途 | 技術設計ドキュメントの生成 |
| 許可ツール | Bash, Glob, Grep, LS, Read, Write, Edit, MultiEdit, Update, WebSearch, WebFetch |

## 前提条件

- 要件が承認されていること
- `-y`フラグで要件を自動承認可能

## フィーチャー分類

| タイプ | プロセス範囲 |
|--------|------------|
| New Feature（新規） | 完全なプロセス（技術選定、アーキテクチャ決定） |
| Extension（拡張） | 統合分析にフォーカス |
| Simple Addition（CRUD等） | 合理化されたプロセス |
| Complex Integration | 包括的な分析とリスク評価 |

## 設計ドキュメント構造

### コアセクション
- **Overview** - 目的、ユーザー、影響
- **Goals/Non-Goals** - スコープの明確化
- **Architecture** - 高レベル設計とMermaid図
- **Components and Interfaces** - 詳細なコンポーネント定義
- **Data Models** - ドメイン/論理/物理モデル
- **Error Handling** - エラー戦略と監視
- **Testing Strategy** - テスト計画

### 条件付きセクション
- Security Considerations
- Performance & Scalability
- Migration Strategy

## 使用例

```bash
# 設計を生成（要件は事前承認必要）
/kiro:spec-design user-authentication

# 要件を自動承認して設計を生成
/kiro:spec-design user-authentication -y

# 既存の設計がある場合の選択肢
# [o] Overwrite - 新規生成
# [m] Merge - 既存を参照して生成
# [c] Cancel - 手動レビュー
```

## Discovery & Analysis Phase

1. **要件からコンポーネントへのマッピング**
2. **既存実装の分析**（拡張の場合）
3. **Steeringアライメントチェック**
4. **技術・代替案の分析**（新機能の場合）
5. **外部依存の調査**
6. **技術リスク評価**

## 次のフェーズ

設計生成後：
- `/kiro:validate-design <feature-name>` - 設計のレビュー
- `/kiro:spec-tasks <feature-name> -y` - タスクの生成
