# Kiro Spec Init Command

## 概要

詳細なプロジェクト記述と要件に基づいて新しい仕様を初期化するコマンド。Kiroのspec-driven development（仕様駆動開発）の起点となります。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:spec-init` |
| 引数 | `<project-description>` |
| 用途 | 仕様ディレクトリの初期化 |
| 許可ツール | Bash, Read, Write, Glob |

## 実行内容

### 1. フィーチャー名の生成
- プロジェクト記述から簡潔で説明的な名前を生成
- 既存の`.kiro/specs/`と重複しないことを確認
- 重複がある場合は番号サフィックスを追加

### 2. Specディレクトリの作成
```
.kiro/specs/[generated-feature-name]/
├── spec.json       # メタデータと承認追跡
└── requirements.md # プロジェクト記述を含むテンプレート
```

### 3. spec.jsonの初期化
```json
{
  "feature_name": "[generated-feature-name]",
  "created_at": "current_timestamp",
  "updated_at": "current_timestamp",
  "language": "ja",
  "phase": "initialized",
  "approvals": {
    "requirements": { "generated": false, "approved": false },
    "design": { "generated": false, "approved": false },
    "tasks": { "generated": false, "approved": false }
  },
  "ready_for_implementation": false
}
```

## 使用例

```bash
# 新しい仕様を初期化
/kiro:spec-init "ユーザー認証システムの実装。JWT認証、ソーシャルログイン対応"

# E-commerce機能の仕様
/kiro:spec-init "商品カタログと検索機能。フィルタリング、ソート、ページネーション対応"
```

## 次のステップ

初期化後、以下の順序で進めます：

1. **`/kiro:spec-requirements <feature-name>`** - 要件の生成
2. **`/kiro:spec-design <feature-name>`** - 技術設計の作成
3. **`/kiro:spec-tasks <feature-name>`** - 実装タスクの生成

## 出力

- 生成されたフィーチャー名とその根拠
- プロジェクトの簡潔な概要
- 作成されたspec.jsonのパス
- 次のステップへの明確なガイダンス
