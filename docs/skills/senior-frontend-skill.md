---
name: senior-frontend
description: ReactJS、NextJS、TypeScript、Tailwind CSSを使用した最新のパフォーマンスに優れたWebアプリケーション構築のための包括的なフロントエンド開発スキル。コンポーネントのスキャフォールディング、パフォーマンス最適化、バンドル分析、UIベストプラクティスを含む。フロントエンド機能の開発、パフォーマンス最適化、UI/UXデザインの実装、状態管理、フロントエンドコードのレビュー時に使用。
---

# シニアフロントエンド

モダンなツールとベストプラクティスを備えたシニアフロントエンド向けの完全なツールキット。

## クイックスタート

### 主要機能

このスキルは自動化スクリプトを通じて3つのコア機能を提供:

```bash
# スクリプト1: コンポーネントジェネレータ
python scripts/component_generator.py [options]

# スクリプト2: バンドルアナライザ
python scripts/bundle_analyzer.py [options]

# スクリプト3: フロントエンドスキャフォールダー
python scripts/frontend_scaffolder.py [options]
```

## コア機能

### 1. コンポーネントジェネレータ

コンポーネント生成タスクのための自動化ツール。

**特徴:**
- 自動スキャフォールディング
- ベストプラクティス組み込み
- 設定可能なテンプレート
- 品質チェック

**使用方法:**
```bash
python scripts/component_generator.py <project-path> [options]
```

### 2. バンドルアナライザ

包括的な分析と最適化ツール。

**特徴:**
- 深い分析
- パフォーマンスメトリクス
- 推奨事項
- 自動修正

**使用方法:**
```bash
python scripts/bundle_analyzer.py <target-path> [--verbose]
```

### 3. フロントエンドスキャフォールダー

専門的なタスク用の高度なツール。

**特徴:**
- エキスパートレベルの自動化
- カスタム設定
- 統合対応
- プロダクショングレードの出力

**使用方法:**
```bash
python scripts/frontend_scaffolder.py [arguments] [options]
```

## リファレンスドキュメント

### Reactパターン

`references/react_patterns.md`で利用可能な包括的なガイド:

- 詳細なパターンとプラクティス
- コード例
- ベストプラクティス
- 避けるべきアンチパターン
- 実世界のシナリオ

### Next.js最適化ガイド

`references/nextjs_optimization_guide.md`の完全なワークフロードキュメント:

- ステップバイステップのプロセス
- 最適化戦略
- ツール統合
- パフォーマンスチューニング
- トラブルシューティングガイド

### フロントエンドベストプラクティス

`references/frontend_best_practices.md`のテクニカルリファレンスガイド:

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
python scripts/bundle_analyzer.py .

# 推奨事項をレビュー
# 修正を適用
```

### 3. ベストプラクティスの実装

以下にドキュメント化されたパターンとプラクティスに従う:
- `references/react_patterns.md`
- `references/nextjs_optimization_guide.md`
- `references/frontend_best_practices.md`

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
python scripts/bundle_analyzer.py .
python scripts/frontend_scaffolder.py --analyze

# デプロイ
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/
```

## トラブルシューティング

### よくある問題

`references/frontend_best_practices.md`の包括的なトラブルシューティングセクションを確認。

### ヘルプの取得

- リファレンスドキュメントをレビュー
- スクリプト出力メッセージを確認
- テックスタックのドキュメントを参照
- エラーログをレビュー

## リソース

- パターンリファレンス: `references/react_patterns.md`
- ワークフローガイド: `references/nextjs_optimization_guide.md`
- テクニカルガイド: `references/frontend_best_practices.md`
- ツールスクリプト: `scripts/`ディレクトリ
