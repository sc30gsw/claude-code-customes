# Claude Code 専門家システム

開発プロジェクトにおいて、Claude Codeの様々な専門家があなたの開発をサポートします。

## 基本的な使い方

### Serenaとの連携
常に最新のSerenaとの連携を行い、最適な開発環境を提供します。

### コンテキスト保持
過去の会話のコンテキストを保持し、継続的な開発支援を行います。

### 専門性
それぞれの専門家は特定の技術領域に特化しています。

---

## カテゴリー別専門家

### 開発・設計専門家

#### `/backend-architect` - バックエンド設計者
**役割**: サーバーサイドのAPI設計やマイクロサービス設計を専門とします。

**専門領域**:
- RESTful API設計とベストプラクティス
- GraphQL スキーマ設計と最適化
- WebSocketリアルタイム通信
- gRPCとProtocol Buffersの活用
- メッセージキュー（RabbitMQ、Kafka、SQS）
- アーキテクチャパターン（CQRS、イベント駆動）
- データベース設計とパフォーマンス最適化
- OpenAPI/Swagger仕様書作成

**対応可能な課題**:
- 効率的なバックエンド設計
- APIの性能改善
- マイクロサービス分割
- データベース最適化

**推奨使用場面**: 新規プロジェクト立ち上げ、既存システム改善

**使用例**:
```
# API設計相談
@backend-architect 新しいAPIの設計について相談したい

# マイクロサービス化
@backend-architect 既存システムのマイクロサービス化を検討したい
```

#### `/frontend-developer` - フロントエンド開発者
**役割**: 主にReactを中心としたモダンなフロントエンド開発を専門とします。

**専門領域**:
- React ライブラリ全般（Hooks、Context、パフォーマンス最適化）
- Next.js 14+ App Router、Server Components
- Remix、Astro、SvelteKit等のフレームワーク
- 状態管理（Redux、Zustand、Jotai、Valtio）
- Web Vitals（LCP、INP、CLS）
- PWA、プリロードとキャッシュ戦略
- マイクロフロントエンド設計
- アクセシビリティ（WCAG準拠、ARIA）

**対応可能な課題**:
- UIコンポーネント設計と最適化
- フロントエンドアーキテクチャ検討
- パフォーマンス改善
- アクセシビリティ対応

**使用例**:
```
# コンポーネント設計
@frontend-developer 再利用可能なコンポーネント設計をサポート

# パフォーマンス最適化
@frontend-developer このページの読み込み速度を改善したい
```

#### `/mobile-developer` - モバイル開発者
**役割**: React NativeやFlutterなどのクロスプラットフォーム開発を専門とします。

**専門領域**:
- React Native開発（TypeScript、Navigation、パフォーマンス最適化）
- Flutter開発（Widget状態管理、アニメーション）
- クロスプラットフォーム開発（iOS/Android）
- ネイティブ機能統合
- アプリストア申請とデプロイ
- モバイル固有のUX設計
- プッシュ通知実装

**対応可能な課題**:
- モバイルアプリ開発・最適化
- アプリストア申請支援
- パフォーマンス・UX改善
- クロスプラットフォーム実装

**使用例**:
```
# アプリ開発
@mobile-developer SNSアプリの機能を実装したい

# クロスプラットフォーム実装
@mobile-developer iOS/Android両対応の実装をサポート
```

### インフラ・運用専門家

#### `/cloud-architect` - クラウド設計者
**役割**: AWS/Azure/GCPのクラウド設計と運用最適化を専門とします。

**専門領域**:
- Infrastructure as Code（Terraform、CloudFormation、Pulumi）
- Kubernetes/EKS/GKE/AKS コンテナオーケストレーション
- サーバーレスアーキテクチャ設計
- FinOpsとコスト最適化
- GitOpsワークフロー（ArgoCD、Flux）
- 災害復旧・高可用性設計
- SRE実践（SLO/SLI設定）

**対応可能な課題**:
- クラウド移行設計・最適化
- コスト削減施策
- 可用性向上
- 運用自動化の導入

**使用例**:
```
# インフラ設計
@cloud-architect マイクロサービス向けのKubernetes設計

# コスト最適化
@cloud-architect AWSの月額費用を30%削減したい
```

#### `/terraform-specialist` - Terraform専門家
**役割**: TerraformによるIaC設計とベストプラクティス実装を専門とします。

**専門領域**:
- 大規模Terraformプロジェクト設計
- 状態管理とチーム開発
- Terragruntによる環境管理
- Policy as Code（OPA、Sentinel）
- Infracostによるコスト予測
- Terraform CDK（TypeScript/Python）
- GitOpsワークフローとの統合

**対応可能な課題**:
- Terraformプロジェクト構造設計・改善
- 状態管理・チーム開発
- IaCのベストプラクティス
- 環境管理自動化

**使用例**:
```
# プロジェクト設計
@terraform-specialist EKS環境のプロビジョニング構成を設計

# 状態管理
@terraform-specialist チームでの状態管理戦略を検討
```

#### `/devops-engineer` - DevOps・CI/CD
**役割**: CI/CDパイプライン構築と運用自動化を専門とします。

**専門領域**:
- CI/CDパイプライン設計（GitHub Actions、GitLab CI、Jenkins）
- Docker・Kubernetes コンテナ化
- 監視・ログ（Prometheus、Grafana、ELK）
- デプロイ戦略（Blue-Green、Canary）
- Infrastructure as Code
- セキュリティ・品質ゲート

**対応可能な課題**:
- パイプライン設計・構築
- 自動化・効率化
- 監視体制の構築
- 運用品質の改善

**使用例**:
```
# パイプライン構築
@devops-engineer Node.jsプロジェクトのCI/CDパイプライン設計

# 監視設計
@devops-engineer アプリケーション監視基盤の構築支援
```

### 品質・セキュリティ専門家

#### `/code-reviewer` - コードレビュー専門家
**役割**: コード品質向上とベストプラクティスの推進を専門とします。

**専門領域**:
- 静的解析とコード品質向上
- リンター設定（ESLint、Prettier、SonarQube）
- パフォーマンス・プロファイリング
- 設計パターンとアーキテクチャレビュー
- セキュリティ監査（Snyk、OWASP）
- AI/機械学習モデル評価

**対応可能な課題**:
- コード品質の継続的改善
- セキュリティ脆弱性の検出
- パフォーマンス・アーキテクチャ改善
- コードレビュープロセス改善

**使用例**:
```
# コードレビュー
@code-reviewer この実装のコード品質をレビューして

# セキュリティ監査
@code-reviewer セキュリティ脆弱性を監査して
```

#### `/testing-specialist` - テスト専門家
**役割**: 総合的なテスト戦略とTDD/BDD実践を専門とします。

**専門領域**:
- テスト戦略（Unit、Integration、E2E）
- テストツール（Jest、Vitest、Cypress、Playwright）
- TDD/BDD手法
- パフォーマンステスト設計
- テスト自動化・環境構築
- CI/CD統合テスト

**対応可能な課題**:
- テスト設計・カバレッジ改善
- テストツール導入・設定
- CI/CDテスト統合
- テスト戦略の策定

**使用例**:
```
# テスト設計
@testing-specialist この機能のテスト設計をサポート

# E2Eテスト
@testing-specialist ユーザージャーニーのE2Eテスト設計
```

#### `/security-engineer` - セキュリティ専門家
**役割**: アプリケーションセキュリティ対策とコンプライアンス対応を専門とします。

**専門領域**:
- OWASP Top 10対策
- 脆弱性診断・修正
- 認証・認可システム
- 脆弱性修正と緩和策
- セキュリティヘッダー（CSP等）
- コンプライアンス（GDPR、CCPA）
- インシデント対応

**対応可能な課題**:
- セキュリティ監査・対策
- 脆弱性修正
- コンプライアンス対応
- セキュリティ設計の改善

**使用例**:
```
# セキュリティ監査
@security-engineer このAPIのセキュリティ監査をして

# GDPR対応
@security-engineer GDPR対応のプライバシー設計をサポート
```

### データ・検索専門家

#### `/database-architect` - データベース設計者
**役割**: データベース設計・最適化とデータ管理を専門とします。

**専門領域**:
- SQL/NoSQLデータベース設計
- インデックス設計・最適化
- クエリ最適化とパフォーマンスチューニング
- データマイグレーション戦略
- ETLパイプライン設計
- データレプリケーション
- 大規模データ運用戦略

**対応可能な課題**:
- データベース設計・最適化
- パフォーマンス・スケーラビリティ改善
- 可用性・運用性向上
- データ移行支援

**使用例**:
```
# DB設計
@database-architect ECサイトのデータベース設計

# パフォーマンス最適化
@database-architect このクエリを最適化したい
```

#### `/search-specialist` - 検索・情報収集専門家
**役割**: 大規模検索システムやWeb/ドキュメント情報収集を専門とします。

**専門領域**:
- Web検索・情報収集戦略
- AI/LLM統合検索（RAG、ベクトル検索）
- 検索アルゴリズム・ランキング最適化
- ナレッジベース構築
- リアルタイム検索・推薦システム
- 検索パフォーマンス最適化

**対応可能な課題**:
- 効率的な情報収集
- 検索機能実装
- ナレッジベース構築
- 情報整理

**使用例**:
```
# 情報収集
@search-specialist React 18の新機能について詳しく調べて

# 検索実装
@search-specialist サイト内検索の実装をサポート
```

### UI/UX・デザイン専門家

#### `/ui-ux-designer` - UI/UX設計者
**役割**: ユーザビリティ設計とユーザーエクスペリエンス最適化を専門とします。

**専門領域**:
- ユーザビリティ・情報アーキテクチャ設計
- アクセシビリティとインクルーシブデザイン
- デザインシステム・コンポーネント設計
- A/Bテスト・feature flag統合
- モバイルファーストレスポンシブデザイン
- プロトタイピング・ワイヤーフレーム
- マイクロインタラクション・アニメーション

**対応可能な課題**:
- ユーザビリティ改善
- デザインシステム最適化
- ユーザーエクスペリエンス最適化
- アクセシビリティ改善

**使用例**:
```
# ユーザビリティ改善
@ui-ux-designer この管理画面のユーザビリティを改善

# UX改善
@ui-ux-designer ユーザーフローのUXを改善
```

#### `/react-performance-optimization` - React最適化専門家
**役割**: React アプリケーションのパフォーマンス最適化を専門とします。

**専門領域**:
- レンダリング最適化・メモ化対策
- React Server Components最適化
- バンドルサイズ最適化
- コード分割・遅延読み込み対策
- Core Web Vitals最適化
- Virtual scrolling・windowing
- React Compiler活用

**対応可能な課題**:
- React アプリの改善
- レンダリング最適化
- 読み込み速度向上
- パフォーマンス測定

**使用例**:
```
# パフォーマンス改善
@react-performance-optimization この画面の描画速度を改善

# レンダリング最適化
@react-performance-optimization 不要な再レンダリングを解消
```

### コマンド開発・運用支援

#### `/command-expert` - CLIコマンド設計
**役割**: Claude Code Templatesの CLIコマンド設計・実装を専門とします。

**専門領域**:
- コマンドライン設計・実装
- 自動化CLI ツール開発
- パイプライン・ワークフロー自動化
- 設定管理・環境構築
- 生産性向上ツール
- 運用効率化設計

**対応可能な課題**:
- CLIコマンド設計・実装
- 開発ワークフロー最適化
- 自動化ツール構築
- 環境構築自動化

**使用例**:
```
# コマンド設計
@command-expert 開発用コマンドを設計

# 自動化実装
@command-expert 環境構築自動化コマンドを実装
```

#### `/serena-expert` - Serena連携エキスパート
**役割**: 継続的な会話を通じたスケーラブル開発支援を専門とします。

**専門領域**:
- マルチスケール開発支援・継続
- プロジェクト設計・管理・コンサルティング
- API連携・統合テスト設計
- 運用最適化

**対応可能な課題**:
- 複合的開発スケーラビリティ改善
- プロジェクト継続的コンサルティング
- 運用設計・最適化

---

## 専門家選択ガイド

### 開発フェーズ別おすすめ専門家

| フェーズ | おすすめ専門家 |
|---------|-----------------|
| **要件定義** | search-specialist, ui-ux-designer |
| **設計** | backend-architect, frontend-developer, cloud-architect |
| **実装** | mobile-developer, database-architect, command-expert |
| **テスト** | testing-specialist, react-performance-optimization |
| **運用** | devops-engineer, terraform-specialist |
| **運用・保守** | security-engineer, code-reviewer |

### 課題別おすすめ専門家

| 課題分類 | おすすめ専門家 |
|-----------|-----------------|
| **パフォーマンス課題** | react-performance-optimization, database-architect |
| **セキュリティ課題** | security-engineer, code-reviewer |
| **インフラ課題** | cloud-architect, devops-engineer, terraform-specialist |
| **UI/UX課題** | ui-ux-designer, frontend-developer |
| **テスト課題** | testing-specialist, code-reviewer |

### 技術別おすすめ専門家

| 技術分野 | おすすめ専門家 |
|-------------|-----------------|
| **React/Next.js** | frontend-developer, react-performance-optimization |
| **Node.js/Express** | backend-architect, security-engineer |
| **モバイル** | mobile-developer, ui-ux-designer |
| **AWS/GCP/Azure** | cloud-architect, terraform-specialist, devops-engineer |
| **データベース** | database-architect, backend-architect |

---

## 専門性組み合わせ

### 複合専門性パターン

1. **フルスタック開発**:
   `backend-architect` + `frontend-developer` + `testing-specialist` + `code-reviewer`

2. **インフラ構築**:
   `cloud-architect` + `terraform-specialist` + `devops-engineer` + `security-engineer`

3. **パフォーマンス最適化**:
   `react-performance-optimization` + `database-architect` + `code-reviewer`

4. **セキュリティ強化**:
   `security-engineer` + `code-reviewer` + `testing-specialist`

### 継続的サポート

プロジェクトの各段階で継続的にサポートします。

- **code-reviewer**: コード品質の継続的改善
- **security-engineer**: セキュリティ対策の継続監視
- **react-performance-optimization**: React パフォーマンス最適化の継続改善
- **cloud-architect**: 運用環境最適化の継続改善

---

## 専門家一覧

| 専門家コマンド | カテゴリー | 主要領域 |
|-------------|---------|-------------|
| `/backend-architect` | 開発・設計 | API設計・マイクロサービス |
| `/frontend-developer` | 開発・設計 | React・モダンフロントエンド |
| `/mobile-developer` | 開発・設計 | React Native・Flutter・クロスプラットフォーム |
| `/cloud-architect` | インフラ・運用 | クラウド設計・コスト最適化 |
| `/terraform-specialist` | インフラ・運用 | Terraform・IaC・環境管理 |
| `/devops-engineer` | インフラ・運用 | CI/CD・運用自動化 |
| `/code-reviewer` | 品質・セキュリティ | コード品質・静的解析 |
| `/testing-specialist` | 品質・セキュリティ | テスト戦略・TDD |
| `/security-engineer` | 品質・セキュリティ | セキュリティ・脆弱性・コンプライアンス |
| `/database-architect` | データ・検索 | データベース設計・最適化 |
| `/search-specialist` | データ・検索 | 検索・情報収集・情報整理 |
| `/ui-ux-designer` | UI/UX・デザイン | ユーザビリティ・UX最適化 |
| `/react-performance-optimization` | UI/UX・デザイン | React パフォーマンス最適化 |
| `/command-expert` | コマンド開発・運用支援 | CLI コマンド設計・実装 |
| `/serena-expert` | コマンド開発・運用支援 | マルチスケール開発支援 |