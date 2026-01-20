# Kiro Steering Custom Command

## 概要

特殊なプロジェクトコンテキストのためのカスタムKiro steeringドキュメントを作成するコマンド。3つの基本ファイル（product.md, tech.md, structure.md）を補完します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:steering-custom` |
| 用途 | カスタムSteeringドキュメントの作成 |
| 許可ツール | Bash, Read, Write, Edit, MultiEdit, Glob, Grep, LS |

## 一般的なカスタムSteeringタイプ

### 1. API Standards (`api-standards.md`)
- REST/GraphQL規約
- エラーハンドリングパターン
- 認証/認可アプローチ
- APIバージョニング戦略

### 2. Testing Approach (`testing.md`)
- テストファイル構成
- テストの命名規則
- モッキング戦略
- カバレッジ要件
- E2E vs ユニット vs 統合テスト

### 3. Code Style Guidelines (`code-style.md`)
- 言語固有の規約
- リンター以上のフォーマットルール
- コメント基準
- 関数/変数の命名パターン
- コード構成原則

### 4. Security Policies (`security.md`)
- 入力バリデーション要件
- 認証パターン
- シークレット管理
- OWASPコンプライアンスガイドライン
- セキュリティレビューチェックリスト

### 5. Database Conventions (`database.md`)
- スキーマ設計パターン
- マイグレーション戦略
- クエリ最適化ガイドライン
- コネクションプール設定
- バックアップ・リカバリ手順

### 6. Performance Standards (`performance.md`)
- 読み込み時間要件
- メモリ使用量制限
- 最適化テクニック
- キャッシング戦略
- モニタリングとプロファイリング

### 7. Deployment Workflow (`deployment.md`)
- CI/CDパイプラインステージ
- 環境設定
- リリース手順
- ロールバック戦略
- ヘルスチェック要件

## インクルージョンモード選択

### 1. Always Included（カスタムファイルには控えめに使用）
- **使用時期**: すべてのコードに適用される普遍的な標準
- **例**: `security-standards.md`
- **推奨**: 真に普遍的なガイドラインのみ

### 2. Conditional Inclusion（ほとんどのカスタムファイルに推奨）
- **使用時期**: 特定のファイルタイプやディレクトリ向け
- **パターン**: `"*.test.js"`, `"src/api/**/*"`, `"**/auth/*"`
- **例**: `testing-approach.md`はテストファイル編集時のみ読み込み

### 3. Manual Inclusion（特殊なコンテキストに最適）
- **使用時期**: 時々必要な専門知識
- **使用法**: `@filename.md`構文で参照
- **例**: `deployment-runbook.md`

## ドキュメント構造ガイドライン

1. **明確なタイトルと目的**
2. **具体的なガイドライン**
3. **コード例**
4. **統合ポイント**

## 使用例

```bash
# カスタムsteeringドキュメントを作成
/kiro:steering-custom

# 対話形式で以下を指定:
# - ドキュメント名
# - トピック/目的
# - インクルージョンモード
# - 条件付きインクルージョンのパターン（該当する場合）
```

## ファイルヘッダー形式

```markdown
<!-- Inclusion Mode: Always | Conditional: "pattern" | Manual -->

# [Document Title]

[Content...]
```
