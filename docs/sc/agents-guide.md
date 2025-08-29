# SuperClaude エージェントガイド

## 概要
SuperClaudeは14個の専門AIエージェントを提供し、各ドメインの専門知識を活用できます。これらは別のAIモデルではなく、Claude Codeの動作を変更するコンテキスト設定です。

## エージェント分類

### 🏗️ アーキテクチャ・システム設計

#### `system-architect`
- **専門分野**: 大規模分散システム設計
- **得意分野**: 
  - マイクロサービスアーキテクチャ
  - スケーラブルシステム設計
  - 技術スタック選択
- **発動キーワード**: "architecture", "system design", "scalability"
- **使用例**: `@system-architect "100万ユーザー対応のEコマースシステム設計"`

#### `backend-architect`
- **専門分野**: サーバーサイドシステムとAPI設計
- **得意分野**: 
  - RESTful API設計
  - データベース設計
  - キャッシュ戦略
- **発動キーワード**: "API", "backend", "server"
- **使用例**: `@backend-architect "GraphQL APIの最適な設計パターン"`

#### `frontend-architect`
- **専門分野**: Webアプリケーション・UI アーキテクチャ
- **得意分野**: 
  - コンポーネント設計
  - 状態管理パターン
  - パフォーマンス最適化
- **発動キーワード**: "frontend", "UI", "component"
- **使用例**: `@frontend-architect "React アプリケーションの状態管理戦略"`

#### `devops-architect`
- **専門分野**: インフラ自動化とデプロイメント
- **得意分野**: 
  - CI/CDパイプライン
  - コンテナオーケストレーション
  - インフラストラクチャ・アズ・コード
- **発動キーワード**: "deployment", "infrastructure", "DevOps"
- **使用例**: `@devops-architect "Kubernetes での Blue-Green デプロイ戦略"`

### 🔍 品質・分析エージェント

#### `security-engineer`
- **専門分野**: アプリケーションセキュリティと脅威モデリング
- **得意分野**: 
  - セキュリティ脆弱性検出
  - 認証・認可設計
  - セキュリティテスト戦略
- **発動キーワード**: "security", "authentication", "vulnerability"
- **使用例**: `@security-engineer "OAuth 2.0 実装のセキュリティレビュー"`

#### `performance-engineer`
- **専門分野**: システム最適化とスケーラビリティ
- **得意分野**: 
  - パフォーマンス測定
  - ボトルネック特定
  - 最適化戦略立案
- **発動キーワード**: "performance", "optimization", "slow"
- **使用例**: `@performance-engineer "Webアプリケーションの読み込み速度改善"`

#### `root-cause-analyst`
- **専門分野**: 体系的問題調査
- **得意分野**: 
  - 複雑な問題の根本原因分析
  - 仮説検証アプローチ
  - 証拠ベースの分析
- **発動キーワード**: "debug", "issue", "problem"
- **使用例**: `@root-cause-analyst "本番環境でのメモリリーク調査"`

#### `quality-engineer`
- **専門分野**: 包括的テスト戦略
- **得意分野**: 
  - テスト計画立案
  - 品質メトリクス定義
  - テスト自動化戦略
- **発動キーワード**: "testing", "quality", "QA"
- **使用例**: `@quality-engineer "E2Eテストスイートの設計と実装"`

#### `refactoring-expert`
- **専門分野**: コード品質改善
- **得意分野**: 
  - レガシーコードの現代化
  - コードの臭い特定
  - リファクタリング戦略
- **発動キーワード**: "refactor", "clean code", "improve"
- **使用例**: `@refactoring-expert "レガシーJavaScriptコードのTypeScript移行"`

### 💻 専門開発エージェント

#### `python-expert`
- **専門分野**: 本番品質Python開発
- **得意分野**: 
  - Pythonic コーディング
  - パフォーマンス最適化
  - ライブラリ選択
- **発動キーワード**: "Python", ".py", "Django", "Flask"
- **使用例**: `@python-expert "FastAPI を使ったマイクロサービス実装"`

#### `requirements-analyst`
- **専門分野**: 要件発見と仕様策定
- **得意分野**: 
  - ステークホルダー分析
  - 機能要件定義
  - 非機能要件特定
- **発動キーワード**: "requirements", "specification", "PRD"
- **使用例**: `@requirements-analyst "モバイルアプリの要件定義と優先順位付け"`

### 📚 コミュニケーション・学習エージェント

#### `technical-writer`
- **専門分野**: 技術ドキュメント設計
- **得意分野**: 
  - API ドキュメンテーション
  - ユーザーガイド作成
  - 技術仕様書作成
- **発動キーワード**: "documentation", "guide", "manual"
- **使用例**: `@technical-writer "開発者向けAPI リファレンス作成"`

#### `learning-guide`
- **専門分野**: 教育コンテンツとスキル開発
- **得意分野**: 
  - 段階的学習設計
  - 実践的演習作成
  - 概念説明の最適化
- **発動キーワード**: "learn", "tutorial", "guide"
- **使用例**: `@learning-guide "React Hooks の実践的チュートリアル"`

### 🔧 その他専門エージェント

#### `terraform-specialist`
- **専門分野**: Infrastructure as Code
- **得意分野**: 
  - Terraform モジュール設計
  - 状態管理
  - インフラ自動化
- **発動キーワード**: "terraform", "infrastructure", "IaC"
- **使用例**: `@terraform-specialist "AWS でのマルチ環境インフラ構築"`

#### `code-reviewer`
- **専門分野**: コードレビューと品質保証
- **得意分野**: 
  - コード品質評価
  - セキュリティレビュー
  - ベストプラクティス確認
- **発動キーワード**: "review", "code quality", "feedback"
- **使用例**: `@code-reviewer "プルリクエストの包括的レビュー"`

## エージェント発動方法

### 手動発動
```bash
# エージェントを直接指定
@agent-security "JWTトークン実装をレビューして"
@agent-performance "このクエリを最適化して"
@agent-frontend "Reactコンポーネントを設計して"
```

### 自動発動
特定のキーワードやコンテキストで自動的に適切なエージェントが選択されます：

```bash
# セキュリティ関連 → security-engineer が自動選択
/sc:implement "JWT認証システム"

# パフォーマンス関連 → performance-engineer が自動選択
/sc:troubleshoot "アプリケーションが遅い"

# UI関連 → frontend-architect が自動選択
/sc:ui "ダッシュボードコンポーネント"
```

## マルチエージェント協調

### 協調パターン
複雑なタスクでは複数のエージェントが連携します：

1. **分析フェーズ**: `requirements-analyst` + `system-architect`
2. **設計フェーズ**: `backend-architect` + `frontend-architect`
3. **実装フェーズ**: 言語別専門エージェント
4. **品質保証**: `security-engineer` + `quality-engineer`
5. **最適化**: `performance-engineer` + `refactoring-expert`

### 実践例

#### Webアプリケーション開発
```bash
/sc:brainstorm "顧客管理システム"
# → requirements-analyst が自動発動

/sc:implement "RESTful API"
# → backend-architect + python-expert が協調

/sc:ui "管理画面"
# → frontend-architect が発動

/sc:test --coverage
# → quality-engineer が包括的テスト戦略を提供

/sc:secure
# → security-engineer がセキュリティ監査実行
```

## エージェント使い分けガイド

### 適切な選択基準

| シナリオ | 推奨エージェント | 理由 |
|---------|----------------|------|
| システム全体の設計 | `system-architect` | 全体最適化の視点 |
| API仕様の検討 | `backend-architect` | サーバーサイド専門知識 |
| UIコンポーネント設計 | `frontend-architect` | フロントエンド専門知識 |
| セキュリティ脆弱性 | `security-engineer` | セキュリティ専門知識 |
| パフォーマンス問題 | `performance-engineer` | 最適化専門知識 |
| 複雑なバグ | `root-cause-analyst` | 体系的分析手法 |
| コード品質改善 | `refactoring-expert` | リファクタリング専門知識 |
| ドキュメント作成 | `technical-writer` | 文書作成専門知識 |

### 避けるべきパターン
- **過剰指定**: 明確な専門分野がある場合の汎用エージェント使用
- **複数同時指定**: 競合する可能性のある複数エージェントの同時指定
- **不適切な選択**: タスクに合わないエージェントの強制使用

## エージェントの学習と最適化

### 適応的学習
- **コンテキスト認識**: プロジェクトの特性に応じた専門知識の調整
- **パターン学習**: 過去の成功例からのパターン抽出
- **継続改善**: フィードバックに基づく推論の最適化

### 品質保証
- **専門知識検証**: 各分野の最新ベストプラクティスとの整合性確認
- **横断的連携**: 異なる専門分野間での知識共有と統合
- **結果検証**: 出力の品質と実用性の継続的評価

このエージェントシステムにより、各技術ドメインで最適化された専門的なサポートを受けることができます。