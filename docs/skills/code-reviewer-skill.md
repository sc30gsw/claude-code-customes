---
name: code-reviewer
description: TypeScript、JavaScript、Python、Swift、Kotlin、Go向けの包括的なコードレビュースキル。自動コード分析、ベストプラクティスチェック、セキュリティスキャン、レビューチェックリスト生成を含む。プルリクエストのレビュー、コードフィードバックの提供、問題の特定、コード品質基準の確保時に使用。
---

# コードレビュアー

モダンなツールとベストプラクティスを備えたコードレビュアー向けの完全なツールキット。

## クイックスタート

### 主要機能

このスキルは自動化スクリプトを通じて3つのコア機能を提供:

```bash
# スクリプト1: PRアナライザ
python scripts/pr_analyzer.py [options]

# スクリプト2: コード品質チェッカー
python scripts/code_quality_checker.py [options]

# スクリプト3: レビューレポートジェネレータ
python scripts/review_report_generator.py [options]
```

## コア機能

### 1. PRアナライザ

PRアナライザタスクのための自動化ツール。

**特徴:**
- 自動スキャフォールディング
- ベストプラクティス組み込み
- 設定可能なテンプレート
- 品質チェック

**使用方法:**
```bash
python scripts/pr_analyzer.py <project-path> [options]
```

### 2. コード品質チェッカー

包括的な分析と最適化ツール。

**特徴:**
- 深い分析
- パフォーマンスメトリクス
- 推奨事項
- 自動修正

**使用方法:**
```bash
python scripts/code_quality_checker.py <target-path> [--verbose]
```

### 3. レビューレポートジェネレータ

専門的なタスク用の高度なツール。

**特徴:**
- エキスパートレベルの自動化
- カスタム設定
- 統合対応
- プロダクショングレードの出力

**使用方法:**
```bash
python scripts/review_report_generator.py [arguments] [options]
```

## リファレンスドキュメント

### コードレビューチェックリスト

`references/code_review_checklist.md`で利用可能な包括的なガイド:

- 詳細なパターンとプラクティス
- コード例
- ベストプラクティス
- 避けるべきアンチパターン
- 実世界のシナリオ

### コーディング規約

`references/coding_standards.md`の完全なワークフロードキュメント:

- ステップバイステップのプロセス
- 最適化戦略
- ツール統合
- パフォーマンスチューニング
- トラブルシューティングガイド

### よくあるアンチパターン

`references/common_antipatterns.md`のテクニカルリファレンスガイド:

- テクノロジースタックの詳細
- 設定例
- 統合パターン
- セキュリティ考慮事項
- スケーラビリティガイドライン

## テックスタック

**言語:** TypeScript、JavaScript、Python、Go、Swift、Kotlin
**フロントエンド:** React、Next.js、React Native、Flutter
**バックエンド:** Node.js、Express、GraphQL、REST API
**データベース:** PostgreSQL、Prisma、NeonDB、Supabase
**DevOps:** Docker、Kubernetes、Terraform、GitHub Actions、CircleCI
**クラウド:** AWS、GCP、Azure

## 開発ワークフロー

### 1. セットアップと設定

```bash
# 依存関係のインストール
npm install
# または
pip install -r requirements.txt

# 環境設定
cp .env.example .env
```

### 2. 品質チェックの実行

```bash
# アナライザスクリプトを使用
python scripts/code_quality_checker.py .

# 推奨事項をレビュー
# 修正を適用
```

### 3. ベストプラクティスの実装

以下にドキュメント化されたパターンとプラクティスに従う:
- `references/code_review_checklist.md`
- `references/coding_standards.md`
- `references/common_antipatterns.md`

## ベストプラクティス概要

### コード品質
- 確立されたパターンに従う
- 包括的なテストを作成
- 決定事項をドキュメント化
- 定期的にレビュー

### パフォーマンス
- 最適化前に測定
- 適切なキャッシュを使用
- クリティカルパスを最適化
- 本番環境でモニタリング

### セキュリティ
- すべての入力を検証
- パラメータ化されたクエリを使用
- 適切な認証を実装
- 依存関係を更新

### 保守性
- 明確なコードを書く
- 一貫した命名を使用
- 有用なコメントを追加
- シンプルに保つ

## よく使うコマンド

```bash
# 開発
npm run dev
npm run build
npm run test
npm run lint

# 分析
python scripts/code_quality_checker.py .
python scripts/review_report_generator.py --analyze

# デプロイ
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/
```

## トラブルシューティング

### よくある問題

`references/common_antipatterns.md`の包括的なトラブルシューティングセクションを確認。

### ヘルプの取得

- リファレンスドキュメントをレビュー
- スクリプト出力メッセージを確認
- テックスタックのドキュメントを参照
- エラーログをレビュー

## リソース

- パターンリファレンス: `references/code_review_checklist.md`
- ワークフローガイド: `references/coding_standards.md`
- テクニカルガイド: `references/common_antipatterns.md`
- ツールスクリプト: `scripts/`ディレクトリ
