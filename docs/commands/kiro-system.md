# Kiroコマンドシステム

Kiroは、仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポートする包括的なコマンドシステムです。

## コマンド一覧

### 🏗️ プロジェクト初期化・ステアリング

#### `/kiro:steering` - プロジェクトステアリング
プロジェクトのステアリングドキュメントを生成/更新。プロジェクト概要、技術スタック、構造を文書化。

**機能**:
- プロダクト概要ドキュメントの生成
- 技術スタック・アーキテクチャの文書化
- プロジェクト構造の定義
- 既存プロジェクトの分析と文書化

#### `/kiro:steering-custom` - カスタムステアリング
プロジェクト固有のステアリング文書を作成・管理。

**機能**:
- 専門ドメイン固有の文書作成
- チーム固有の開発ルール定義
- カスタム設計パターンの文書化

### 📋 仕様開発フェーズ

#### `/kiro:spec-init [詳細な機能説明]` - 仕様初期化
機能の詳細説明から仕様ディレクトリを作成し、開発プロセスを開始。

**機能**:
- 機能説明の自動解析
- 仕様ディレクトリ構造の作成
- 初期メタデータの生成

#### `/kiro:spec-requirements [機能名]` - 要件定義
EARS形式（Easy Approach to Requirements Syntax）で要件とユーザーストーリーを作成。

**機能**:
- EARS形式での機能要件定義
- 非機能要件の分析
- ユーザーストーリーとアクセプタンス基準の生成
- プロダクトバックログ形式での出力

#### `/kiro:validate-gap [機能名]` - 実装ギャップ分析
既存コードベースと要件間のギャップを分析し、実装戦略を提案。

**機能**:
- 既存コードベースの分析
- 実装可能性の評価
- 複数の実装アプローチの提示
- 技術リサーチ要件の特定
- 実装複雑度の評価（S/M/L/XL）

#### `/kiro:spec-design [機能名]` - 技術設計
アーキテクチャ、データモデル、APIを含む包括的な技術設計を作成。

**機能**:
- アーキテクチャ設計
- データモデル設計
- API設計とインターフェース定義
- セキュリティとパフォーマンスの考慮
- 実装ガイドラインの作成

#### `/kiro:validate-design [機能名]` - 設計品質レビュー
技術設計の品質を対話的にレビューし、GO/NO-GO判定を行う。

**機能**:
- 既存アーキテクチャとの整合性チェック
- 設計一貫性・標準準拠の確認
- 拡張性・保守性の評価
- 型安全性・インターフェース設計の検証
- 最大3つの重要課題に焦点を当てたレビュー

### 🧪 テスト・実装フェーズ

#### `/kiro:spec-tasks [機能名]` - 実装タスク生成
技術設計を基に詳細な実装ステップとTDDタスクを生成。

**機能**:
- 設計から実装タスクへの自動変換
- TDDサイクルでの実装ステップ定義
- 依存関係の考慮した実装順序
- 各タスクの完了基準定義

#### `/kiro:spec-impl [機能名] [タスク番号]` - 実装実行
TDD手法を使用して仕様からタスクを実装。

**引数**:
- `機能名` - 実装する機能名
- `タスク番号` - 実行するタスク（例: `1.1`, `1,2,3`, `--all`）

**機能**:
- Red-Green-Refactorサイクルの実行
- テストファーストでの実装
- コードレビュー品質の自動チェック

**例**:
```bash
/kiro:spec-impl auth-system 1.1            # タスク1.1を実行
/kiro:spec-impl auth-system 1,2,3          # タスク1, 2, 3を実行
/kiro:spec-impl auth-system --all          # 全ての未完了タスクを実行
```

### 📊 監視・管理

#### `/kiro:spec-status [機能名]` - 進捗状況確認
各フェーズの完了状況と次のステップを確認。

**機能**:
- 全フェーズの進捗状況表示
- 承認待ちタスクの確認
- 次に実行すべきコマンドの提案
- 実装完了度の可視化

## TDDワークフロー

1. **Red Phase** - 失敗するテストを先に書く
2. **Green Phase** - テストを通す最小限のコードを実装
3. **Refactor Phase** - テストを維持しながらコードを改善

## ディレクトリ構造

```
.kiro/
├── steering/              # プロジェクト全体の方針・ガイドライン
│   ├── product.md        # 製品概要・ビジネス要件
│   ├── tech.md          # 技術スタック・アーキテクチャ方針
│   ├── structure.md     # プロジェクト構造・組織
│   └── [custom].md      # カスタムステアリング（チーム固有ルール）
└── specs/               # 機能別仕様ディレクトリ
    └── [feature-name]/
        ├── spec.json         # メタデータ（言語設定、承認状態、進捗等）
        ├── requirements.md   # EARS形式要件定義・ユーザーストーリー
        ├── gap-analysis.md   # 実装ギャップ分析結果（validate-gap出力）
        ├── design.md         # 技術設計・アーキテクチャ
        ├── design-review.md  # 設計品質レビュー結果（validate-design出力）
        ├── tasks.md          # 実装タスク・TDDステップ
        ├── implementation/   # 実装進捗・メモ
        │   ├── progress.md   # 実装進捗状況
        │   └── notes.md      # 実装メモ・課題
        └── tests/            # テスト仕様・実装
            ├── test-spec.md  # 包括的テスト戦略
            ├── unit/         # 単体テスト仕様・実装
            ├── component/    # コンポーネントテスト仕様
            ├── hook/         # カスタムフックテスト
            ├── api/          # APIテスト仕様
            ├── e2e/          # E2Eテスト仕様
            ├── mocks/        # モック仕様・テストデータ
            └── ci/           # CI/CD設定（GitHub Actions等）
```

### ファイル説明

#### steering/ - プロジェクト全体方針
- **product.md**: ビジネス要件、ユーザー、市場分析
- **tech.md**: 技術スタック、アーキテクチャ原則、制約
- **structure.md**: ディレクトリ構造、命名規則、組織方針
- **[custom].md**: チーム固有のルール、専門ドメイン知識

#### specs/[feature-name]/ - 機能別管理
- **spec.json**: メタデータ（言語、承認状態、バージョン）
- **requirements.md**: EARS形式要件、アクセプタンス基準
- **gap-analysis.md**: 既存コードとの分析、実装戦略
- **design.md**: 技術設計書、API仕様、データモデル
- **design-review.md**: 設計レビュー結果、改善提案
- **tasks.md**: 実装タスク、TDDステップ、完了基準

#### tests/ - テスト管理
- **test-spec.md**: テスト戦略、カバレッジ目標
- **unit/**: 単体テスト仕様、ビジネスロジック
- **component/**: UIコンポーネントテスト
- **hook/**: カスタムフックテスト
- **api/**: エンドポイントテスト
- **e2e/**: ユーザージャーニーテスト
- **mocks/**: テストデータ、サービスモック
- **ci/**: 自動化設定（GitHub Actions）

## 開発ワークフロー

### 基本ワークフロー（標準的な開発プロセス）

```bash
# 1. プロジェクト初期化
/kiro:steering

# 2. 新機能の仕様作成
/kiro:spec-init "ユーザー認証機能を実装したい。メールアドレスとパスワードでログインできるようにする"

# 3. 要件定義
/kiro:spec-requirements user-authentication

# 4. 実装ギャップ分析（推奨）
/kiro:validate-gap user-authentication

# 5. 技術設計
/kiro:spec-design user-authentication

# 6. 設計品質レビュー（推奨）
/kiro:validate-design user-authentication

# 7. テスト仕様生成（TDD）
/kiro:spec-test user-authentication --test-lib=vitest --e2e-lib=playwright

# 8. 実装タスク生成
/kiro:spec-tasks user-authentication

# 9. 実装実行（TDD）
/kiro:spec-impl user-authentication --all

# 10. 進捗確認
/kiro:spec-status user-authentication
```

### 高速開発ワークフロー（自動承認付き）

```bash
# 1. プロジェクト準備
/kiro:steering

# 2. 機能仕様の自動生成（要件→設計を一括実行）
/kiro:spec-init "eコマース購入機能。カート追加、決済処理、注文確認を含む"
/kiro:spec-requirements ecommerce-purchase
/kiro:spec-design ecommerce-purchase -y  # 自動承認で要件をスキップして設計へ

# 3. 実装準備（設計→タスクを一括実行）
/kiro:spec-tasks ecommerce-purchase -y   # 自動承認で設計をスキップしてタスク生成

# 4. 実装実行
/kiro:spec-impl ecommerce-purchase --all
```

### 品質重視ワークフロー（全レビュー付き）

```bash
# 1. プロジェクト準備
/kiro:steering

# 2. 詳細分析フェーズ
/kiro:spec-init "複雑なリアルタイム通知システム"
/kiro:spec-requirements realtime-notifications
/kiro:validate-gap realtime-notifications     # 既存コードベースとの分析

# 3. 設計・レビューフェーズ
/kiro:spec-design realtime-notifications
/kiro:validate-design realtime-notifications  # 設計品質レビュー

# 4. テスト計画フェーズ
/kiro:spec-test realtime-notifications --coverage=90 --e2e-lib=playwright

# 5. 実装フェーズ
/kiro:spec-tasks realtime-notifications
/kiro:spec-impl realtime-notifications 1     # タスクを段階的に実行
/kiro:spec-status realtime-notifications     # 進捗確認
/kiro:spec-impl realtime-notifications 2
# ... 継続
```

### 既存機能拡張ワークフロー

```bash
# 1. 既存システム分析
/kiro:validate-gap user-profile-enhancement

# 2. 要件定義（既存との整合性を考慮）
/kiro:spec-requirements user-profile-enhancement

# 3. 設計（既存アーキテクチャとの統合を重視）
/kiro:spec-design user-profile-enhancement
/kiro:validate-design user-profile-enhancement

# 4. 段階的実装
/kiro:spec-tasks user-profile-enhancement
/kiro:spec-impl user-profile-enhancement --all
```

### チーム開発ワークフロー

```bash
# 1. チームリーダー：プロジェクトステアリング設定
/kiro:steering
/kiro:steering-custom  # チーム固有ルールの設定

# 2. 開発者A：機能仕様作成
/kiro:spec-init "ユーザー管理機能"
/kiro:spec-requirements user-management

# 3. アーキテクト：設計レビュー
/kiro:validate-gap user-management
/kiro:spec-design user-management
/kiro:validate-design user-management

# 4. 開発者B：実装タスク実行
/kiro:spec-tasks user-management
/kiro:spec-impl user-management 1,2,3

# 5. 進捗管理
/kiro:spec-status user-management
```

## 他のコマンドとの連携パターン

### デバッグ・品質保証連携

```bash
# Kiro仕様作成 → デバッグコマンドでの検証
/kiro:spec-init "APIエラーハンドリング改善"
/kiro:spec-requirements api-error-handling
/debug-error "API timeout errors" --pattern-search --memory

# Kiro実装 → テストコマンドでの自動テスト生成
/kiro:spec-impl auth-system 1.1
/test AuthService -u -r -c  # 単体テスト生成・実行・修正
```

### 開発支援コマンド連携

```bash
# Kiro設計 → dev3000での統合デバッグ
/kiro:spec-design payment-system
/dev debug "payment integration" --analyze --e2e-verify

# Kiro実装 → smart-thinkでの最適化検討
/kiro:spec-impl dashboard-optimization --all
/smart-think "React performance optimization strategy" --serena --use-implementation-context
```

### Git・バージョン管理連携

```bash
# Kiro実装完了後の自動コミット
/kiro:spec-impl user-authentication --all
/commit --scope=feature --analyze --include-kiro-context

# 仕様変更の追跡
/kiro:spec-requirements user-auth-enhancement
/commit --scope=spec --message="Update auth requirements per security review"
```

## ベストプラクティス

### 🎯 効果的な仕様作成
1. **詳細な初期説明**: `/kiro:spec-init`では具体的で詳しい機能説明を提供
2. **段階的レビュー**: 各フェーズで`validate`コマンドを活用して品質確保
3. **既存コード分析**: `validate-gap`で既存システムとの整合性を事前確認
4. **対話的改良**: レビューコマンドでは積極的に対話して改善

### ⚡ 効率的な開発プロセス
1. **自動承認の活用**: 信頼できるプロセスでは`-y`フラグで高速化
2. **段階的実装**: 大きな機能は`spec-impl`でタスク単位での実装
3. **定期的な進捗確認**: `spec-status`で進捗を可視化
4. **パターンの再利用**: 成功した仕様パターンをテンプレート化

### 🔄 品質管理
1. **設計品質の徹底**: `validate-design`でアーキテクチャ整合性を確認
2. **TDDの実践**: テストファーストでの実装を徹底
3. **コードレビュー統合**: 他の品質管理コマンドとの連携活用
4. **継続的改善**: 実装完了後の振り返りと仕様更新

### 👥 チーム開発
1. **ステアリング共有**: チーム共通のプロジェクト方針を文書化
2. **役割分担**: 仕様作成者と実装者の明確な分離
3. **知識共有**: `steering-custom`でチーム固有の知見を蓄積
4. **進捗の透明化**: `spec-status`での進捗共有

## 使用場面・ユースケース

### 🏗️ プロジェクト初期化・ステアリングのユースケース

#### `/kiro:steering` を使う場面
- **新規プロジェクト開始時**: チーム全体でプロジェクト方針を共有したい
- **技術スタック変更時**: フレームワーク移行やアーキテクチャ変更
- **チームメンバー追加時**: 新メンバーへのプロジェクト概要説明
- **定期見直し**: 四半期や年次でのプロジェクト方針再評価

**具体例**:
```bash
# 新規Reactプロジェクトの開始
/kiro:steering  # → product.md, tech.md, structure.md が生成される

# レガシーシステムのモダナイゼーション開始
/kiro:steering  # → 既存システム分析と移行方針の文書化
```

#### `/kiro:steering-custom` を使う場面
- **特殊ドメインプロジェクト**: 金融、医療、IoTなど専門知識が必要
- **企業固有ルール**: セキュリティ要件、コンプライアンス対応
- **チーム固有パターン**: 独自のコーディング規約、デザインパターン
- **マイクロサービス**: サービス間通信、データ整合性ルール

**具体例**:
```bash
# 金融システム開発時
/kiro:steering-custom  # → PCI DSS対応、金融規制要件を文書化

# AIプロジェクト開始時
/kiro:steering-custom  # → ML pipeline、データ処理方針を定義
```

### 📋 仕様開発フェーズのユースケース

#### `/kiro:spec-init` を使う場面
- **新機能開発開始**: まず何を作るかを明確化したい
- **要件が曖昧**: ステークホルダーからの要望をまとめたい
- **アイデア段階**: 頭の中にあるアイデアを構造化したい
- **プロトタイプ前**: 開発前に方向性を確認したい

**具体例**:
```bash
# 曖昧な要求から開始
/kiro:spec-init "顧客がもっと使いやすいダッシュボードが欲しいと言っている"
# → user-friendly-dashboard/ ディレクトリと初期構造が作成

# アイデア段階から
/kiro:spec-init "AIチャットボットでカスタマーサポートを自動化したい。24時間対応で、よくある質問に答えられるようにしたい"
# → ai-chatbot-support/ ディレクトリが作成される
```

#### `/kiro:spec-requirements` を使う場面
- **仕様書作成**: 開発チームが実装に必要な詳細を整理したい
- **ステークホルダー確認**: 要件を文書化して関係者に確認してもらいたい
- **見積もり作成**: 正確な工数見積もりのために詳細要件が必要
- **外部委託**: 外部開発者に渡す仕様書が必要

**適用場面**:
```bash
# B2Bダッシュボード機能
/kiro:spec-requirements analytics-dashboard
# → EARS形式の要件、ユーザーストーリー、アクセプタンス基準を生成

# API開発
/kiro:spec-requirements user-api
# → RESTful API要件、エンドポイント仕様、認証要件を定義
```

#### `/kiro:validate-gap` を使う場面
- **既存システム拡張**: 現在のコードベースとの整合性を確認したい
- **技術調査必要**: 実装可能性やリスクを事前に把握したい
- **工数見積もり**: 実装の複雑度を正確に評価したい
- **アーキテクチャ影響**: 新機能が既存システムに与える影響を知りたい

**実際の使用例**:
```bash
# レガシーシステムに新機能追加
/kiro:validate-gap payment-gateway-integration
# → 既存決済システムとの統合可能性、必要な変更点を分析

# パフォーマンス要件がある機能
/kiro:validate-gap realtime-notifications
# → WebSocket実装の難易度、既存インフラとの互換性を評価
```

#### `/kiro:spec-design` を使う場面
- **複雑な機能実装前**: アーキテクチャ設計が重要な機能
- **チーム開発**: 複数人で作業するために設計書が必要
- **外部連携**: API設計やデータモデル設計を事前に確定したい
- **パフォーマンス重視**: 最適化を考慮した設計が必要

**活用場面**:
```bash
# マイクロサービス設計
/kiro:spec-design order-processing-service
# → サービス境界、API契約、データ整合性を設計

# 大規模フロントエンド機能
/kiro:spec-design admin-panel
# → コンポーネント設計、状態管理、ルーティング設計
```

#### `/kiro:validate-design` を使う場面
- **重要な機能**: ビジネスクリティカルな機能の設計品質を保証したい
- **複雑なアーキテクチャ**: 設計の妥当性を第三者視点でチェック
- **チームレビュー**: 設計をチームで議論する前の品質確保
- **リスク軽減**: 実装前に設計上の問題を発見したい

**適用例**:
```bash
# 決済システム設計のレビュー
/kiro:validate-design payment-processing
# → セキュリティ、パフォーマンス、拡張性の観点でレビュー

# 認証システムの設計検証
/kiro:validate-design oauth-integration
# → セキュリティベストプラクティスとの整合性確認
```

### 🧪 テスト・実装フェーズのユースケース

#### `/kiro:spec-test` を使う場面
- **TDD開始前**: テスト戦略を明確化してから実装を始めたい
- **品質重視**: 高いテストカバレッジが求められる機能
- **チーム開発**: テストの書き方・方針を統一したい
- **CI/CD整備**: 自動テストパイプラインを構築したい

**使用例**:
```bash
# 金融システムの厳格なテスト要件
/kiro:spec-test transaction-processing --coverage=95 --test-lib=jest
# → 高カバレッジテスト戦略、モック戦略、CI設定を生成

# フロントエンド機能のE2Eテスト
/kiro:spec-test user-onboarding --e2e-lib=playwright --ui-lib=testing-library
# → ユーザージャーニーテスト、アクセシビリティテストを計画
```

#### `/kiro:spec-tasks` を使う場面
- **大きな機能**: 実装ステップを細分化して管理したい
- **チーム分担**: タスクを複数人で分担して開発
- **進捗管理**: 実装進捗を細かく追跡したい
- **品質保証**: 各ステップでレビューポイントを設けたい

**実践例**:
```bash
# ECサイト機能の段階的実装
/kiro:spec-tasks shopping-cart
# → カート追加、数量変更、削除、計算など細かいタスクに分解

# 複雑なAPI実装
/kiro:spec-tasks user-management-api
# → エンドポイント毎、バリデーション毎にタスク分割
```

#### `/kiro:spec-impl` を使う場面
- **TDD実践**: テストファーストで確実に実装したい
- **品質重視**: コードレビュー基準を満たしながら実装
- **段階的開発**: 大きな機能を安全に実装したい
- **学習目的**: TDDやベストプラクティスを学びながら実装

**活用方法**:
```bash
# 重要機能の慎重な実装
/kiro:spec-impl authentication-system 1.1  # 一つずつ慎重に
/kiro:spec-impl authentication-system 1.2
# → 各ステップでテスト→実装→リファクタリング

# プロトタイプの高速実装
/kiro:spec-impl dashboard-prototype --all  # 全タスク一括実行
# → MVP作成、デモ用プロトタイプの迅速な構築
```

### 📊 監視・管理のユースケース

#### `/kiro:spec-status` を使う場面
- **プロジェクト管理**: 現在の開発フェーズと進捗を把握したい
- **チーム報告**: ステークホルダーへの進捗報告
- **ブロッカー特定**: 次に何をすべきかを明確化
- **品質チェック**: 承認待ちタスクの確認

**使用シーン**:
```bash
# スプリント終了時の進捗確認
/kiro:spec-status user-profile-enhancement
# → 完了率、残タスク、ブロッカーを可視化

# 毎朝のスタンドアップ前
/kiro:spec-status payment-integration
# → 昨日の進捗、今日のタスクを確認
```

## 実際のプロジェクト別使用パターン

### 🚀 スタートアップ・MVP開発
```bash
# 高速プロトタイプ開発
/kiro:steering                           # プロジェクト方針を短時間で設定
/kiro:spec-init "ユーザー登録とログイン"    # 最小機能から開始
/kiro:spec-requirements user-auth -y      # 自動承認で高速化
/kiro:spec-design user-auth -y           # 設計レビューをスキップ
/kiro:spec-impl user-auth --all          # 一括実装でMVP完成
```

### 🏢 企業システム・厳格な開発
```bash
# コンプライアンス重視の開発
/kiro:steering-custom                     # 企業固有ルール設定
/kiro:spec-init "個人情報管理システム"      # 慎重な仕様策定
/kiro:spec-requirements pii-management    # 詳細要件定義
/kiro:validate-gap pii-management         # リスクアセスメント
/kiro:spec-design pii-management          # セキュリティ設計
/kiro:validate-design pii-management      # 設計レビュー必須
/kiro:spec-test pii-management --coverage=95  # 厳格なテスト要件
/kiro:spec-impl pii-management 1.1        # 段階的な慎重実装
```

### 🛠️ レガシーシステム改善
```bash
# 既存システムの段階的モダナイゼーション
/kiro:validate-gap legacy-modernization   # 現状分析から開始
/kiro:spec-requirements api-migration     # 移行要件の明確化
/kiro:validate-design api-migration       # 既存システムとの整合性確認
/kiro:spec-impl api-migration 1,2,3       # リスクの低い部分から段階実装
```

### 👥 大規模チーム開発
```bash
# 役割分担での効率的開発
# アーキテクト
/kiro:steering && /kiro:steering-custom
/kiro:validate-gap microservice-api

# プロダクトマネージャー
/kiro:spec-requirements microservice-api

# シニア開発者
/kiro:spec-design microservice-api
/kiro:validate-design microservice-api

# 開発チーム
/kiro:spec-impl microservice-api 1,2      # 並列実装
/kiro:spec-impl microservice-api 3,4      # タスク分担
```

## 特徴

- **仕様駆動開発**: 要件から実装まで体系的に管理
- **TDD対応**: テストファーストアプローチをサポート
- **品質レビュー**: 設計品質とギャップ分析による品質保証
- **自動承認**: インタラクティブな承認プロセス
- **多言語対応**: 日本語/英語での仕様生成
- **柔軟な設定**: プロジェクトに合わせてカスタマイズ可能
- **コマンド連携**: 他の開発支援コマンドとのシームレスな統合