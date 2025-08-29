# SuperClaude 実践ワークフローガイド

## 概要
このガイドでは、実際の開発シナリオでSuperClaudeを効果的に活用するための実践的なワークフローパターンを紹介します。

## 🚀 プロジェクトタイプ別ワークフロー

### 1. 新規Webアプリケーション開発

#### フェーズ1: 要件定義・設計
```bash
# Step 1: アイデアの構造化
/sc:brainstorm "タスク管理アプリ" --strategy systematic

# Step 2: 技術スタック決定
/sc:workflow "React + Node.js + PostgreSQL" --c7 --seq

# Step 3: アーキテクチャ設計
/sc:analyze "システム設計" --think-hard --seq
```

#### フェーズ2: フロントエンド実装
```bash
# Step 1: UIコンポーネント設計
/sc:ui "ダッシュボードレイアウト" --magic --c7 --focus accessibility

# Step 2: 状態管理実装
/sc:implement "Redux Toolkit状態管理" --c7 --focus performance

# Step 3: 認証フロー実装
/sc:implement "JWT認証システム" --magic --c7 --focus security
```

#### フェーズ3: バックエンド実装
```bash
# Step 1: API設計
/sc:implement "RESTful API" --c7 --focus architecture

# Step 2: データベース設計
/sc:implement "PostgreSQL スキーマ" --c7 --think

# Step 3: セキュリティ実装
/sc:secure --scan vulnerabilities --focus security
```

#### フェーズ4: テスト・検証
```bash
# Step 1: 単体テスト
/sc:test --type unit --coverage --fix

# Step 2: E2Eテスト
/sc:test "ユーザーフロー" --play --type e2e

# Step 3: パフォーマンステスト
/sc:analyze --focus performance --seq
```

### 2. レガシーシステム現代化

#### フェーズ1: 現状分析
```bash
# Step 1: 包括的分析
/sc:analyze legacy/ --ultrathink --serena --all-mcp

# Step 2: 技術的負債評価
/sc:analyze "技術的負債" --focus quality --seq

# Step 3: 移行戦略立案
/sc:workflow "段階的移行計画" --strategy agile --think-hard
```

#### フェーズ2: 段階的現代化
```bash
# Step 1: 依存関係分析
/sc:analyze dependencies/ --serena --seq

# Step 2: 一括リファクタリング
/sc:improve legacy/ --morph --type modernization --preview

# Step 3: 新技術統合
/sc:implement "モダンフレームワーク統合" --c7 --seq
```

#### フェーズ3: 品質向上・検証
```bash
# Step 1: セキュリティ強化
/sc:secure --scan all --focus security

# Step 2: パフォーマンス最適化
/sc:optimize --target performance --focus scalability

# Step 3: 総合テスト
/sc:test --type integration --coverage --play
```

### 3. APIファースト開発

#### フェーズ1: API設計
```bash
# Step 1: 要件分析
/sc:brainstorm "RESTful API仕様" --strategy systematic

# Step 2: OpenAPI仕様作成
/sc:document --type api --format openapi

# Step 3: モックサーバー構築
/sc:implement "モックAPI" --c7 --type backend
```

#### フェーズ2: 実装・テスト
```bash
# Step 1: API実装
/sc:implement "Express.js API" --c7 --focus performance

# Step 2: バリデーション実装
/sc:implement "入力検証システム" --focus security

# Step 3: API テスト
/sc:test "API エンドポイント" --type integration
```

## 🎯 シナリオ別最適パターン

### A. 緊急バグ修正

#### 超高速デバッグフロー
```bash
# Step 1: 問題の迅速な特定
/sc:troubleshoot "本番エラー: 500" --seq --urgent

# Step 2: 根本原因分析
/sc:analyze error-logs/ --focus security --seq

# Step 3: 最小限の修正
/sc:implement "hotfix" --focus reliability --preview

# Step 4: 緊急テスト
/sc:test --type smoke --quick
```

### B. パフォーマンス改善

#### 体系的最適化フロー
```bash
# Step 1: ベンチマーク取得
/sc:analyze performance/ --focus performance --think

# Step 2: ボトルネック特定
/sc:troubleshoot "遅いクエリ" --seq --focus performance

# Step 3: 最適化実装
/sc:optimize database-queries/ --target performance

# Step 4: 効果測定
/sc:test "パフォーマンステスト" --type performance
```

### C. セキュリティ監査

#### 包括的セキュリティレビュー
```bash
# Step 1: 脆弱性スキャン
/sc:secure --scan vulnerabilities --all-mcp

# Step 2: コードレビュー
/sc:analyze auth/ --focus security --think-hard

# Step 3: セキュリティ強化
/sc:implement "セキュリティ改善" --focus security

# Step 4: ペネトレーションテスト
/sc:test --type security --comprehensive
```

## 🔄 継続的改善ワークフロー

### 週次品質向上サイクル

#### 月曜日: 分析・計画
```bash
# 週次コード品質レポート
/sc:analyze . --focus quality --uc --save "週次レポート"

# 改善項目の優先順位付け
/sc:workflow "品質改善計画" --strategy agile
```

#### 水曜日: 実装・改善
```bash
# 優先度の高い改善実装
/sc:improve src/ --type quality --preview
/sc:implement "改善案" --focus maintainability
```

#### 金曜日: テスト・検証
```bash
# 包括的テスト実行
/sc:test --type all --coverage

# パフォーマンス確認
/sc:analyze --focus performance --compare
```

## 🛠️ チーム開発パターン

### コードレビュー最適化

#### レビュー前準備
```bash
# 自動品質チェック
/sc:analyze pull-request/ --focus quality --uc

# セキュリティレビュー
/sc:secure --scan code-changes --focus security

# テストカバレッジ確認
/sc:test --coverage --report
```

### オンボーディング支援

#### 新メンバー向けガイド生成
```bash
# プロジェクト概要生成
/sc:document --type onboarding --comprehensive

# アーキテクチャ図作成
/sc:analyze architecture/ --visual --think

# セットアップガイド作成
/sc:document --type setup-guide --detailed
```

## 🎨 専門的ワークフロー

### フロントエンド特化

#### React開発最適化
```bash
# コンポーネント設計
/sc:ui "デザインシステム" --magic --c7

# パフォーマンス最適化
/sc:optimize "React バンドル" --target bundle

# アクセシビリティ確保
/sc:test --focus accessibility --play
```

### バックエンド特化

#### Node.js API開発
```bash
# Express.js アーキテクチャ
/sc:implement "マイクロサービス" --c7 --think

# データベース最適化
/sc:optimize database/ --target performance

# API ドキュメンテーション
/sc:document --type api --format swagger
```

### DevOps特化

#### CI/CD パイプライン構築
```bash
# パイプライン設計
/sc:workflow "CI/CD戦略" --think-hard

# Docker化
/sc:implement "コンテナ化" --c7 --focus scalability

# デプロイメント自動化
/sc:implement "自動デプロイ" --focus reliability
```

## 🚨 緊急事態対応プロトコル

### 本番障害対応

#### レベル1: 緊急対応（5分以内）
```bash
# 即座の状況把握
/sc:troubleshoot "本番障害" --urgent --uc

# 緊急回復手順
/sc:implement "ホットフィックス" --safe-mode
```

#### レベル2: 根本対応（30分以内）
```bash
# 詳細な原因分析
/sc:analyze incident/ --seq --think-hard

# 恒久対策実装
/sc:implement "根本修正" --focus reliability
```

#### レベル3: 再発防止（1日以内）
```bash
# 事後分析レポート
/sc:document --type incident-report

# 監視・アラート改善
/sc:implement "予防システム" --focus monitoring
```

## 📊 生産性測定・改善

### 開発効率メトリクス

#### 週次効率レポート
```bash
# 開発速度分析
/sc:analyze commits/ --focus productivity --time-series

# コード品質トレンド
/sc:analyze quality-metrics/ --trend --visual

# チームパフォーマンス評価
/sc:analyze team-metrics/ --comprehensive
```

### プロセス改善

#### 継続的プロセス最適化
```bash
# ワークフロー分析
/sc:analyze workflow/ --focus efficiency

# ボトルネック特定
/sc:troubleshoot "開発プロセス遅延" --seq

# 改善案実装
/sc:implement "プロセス改善" --focus productivity
```

## 🎯 成功指標とベストプラクティス

### KPI追跡
- **開発速度**: 機能実装時間の短縮（目標: 30%削減）
- **コード品質**: バグ発生率の低下（目標: 50%削減）
- **テストカバレッジ**: 自動テスト率向上（目標: 90%以上）
- **セキュリティ**: 脆弱性検出・修正速度（目標: 24時間以内）

### 継続的学習
```bash
# 定期的なスキルアップ
/sc:learn "新技術トレンド" --c7 --comprehensive

# チーム知識共有
/sc:document --type knowledge-base --collaborative

# ベストプラクティス更新
/sc:improve workflows/ --type optimization --continuous
```

このワークフローガイドを活用することで、SuperClaudeの真の力を発揮し、開発プロジェクトを成功に導くことができます。各パターンは実際のプロジェクト状況に応じて調整・組み合わせて使用してください。