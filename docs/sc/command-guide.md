# SuperClaude コマンドガイド

## 概要
SuperClaudeは21個の専用コマンドを提供し、Claude Codeを構造化された開発プラットフォームに変換します。全コマンドは `/sc:` プレフィックスを使用してコマンド競合を避けています。

## 主要コマンド一覧

### 🎯 プロジェクト開始・計画

#### `/sc:brainstorm`
- **目的**: プロジェクトの要求分析と探索的ディスカバリー
- **使用例**: `/sc:brainstorm "Eコマースプラットフォーム"`
- **フラグ**: `--strategy systematic|creative`
- **動作**: 
  - ソクラテス式質問法でユーザーの曖昧なアイデアを構造化
  - 要件の隠れた側面を発見
  - 実装可能な要件書を生成

#### `/sc:workflow`
- **目的**: 実装計画とワークフロー設計
- **使用例**: `/sc:workflow "ユーザー認証システム"`
- **フラグ**: `--strategy agile|waterfall`, `--format markdown`
- **動作**: 
  - タスクの依存関係を分析
  - 実装フェーズを定義
  - 並列実行可能な操作を特定

### 🔧 開発・実装

#### `/sc:implement`
- **目的**: 機能開発とインテリジェントルーティング
- **使用例**: `/sc:implement "JWTログインシステム"`
- **フラグ**: `--type frontend|backend|fullstack`, `--focus security|performance`
- **動作**: 
  - 適切なエージェントを自動選択
  - セキュリティ要件を考慮
  - 完全な実装を提供（部分実装なし）

#### `/sc:test`
- **目的**: 品質保証とテスト実行
- **使用例**: `/sc:test --coverage`
- **フラグ**: `--type unit|integration|e2e`, `--coverage`, `--fix`
- **動作**: 
  - テスト戦略の立案
  - カバレッジ分析
  - 失敗したテストの自動修正

### 🔍 分析・診断

#### `/sc:analyze`
- **目的**: 包括的なコード評価
- **使用例**: `/sc:analyze .`
- **フラグ**: `--focus quality|security|performance|architecture`
- **動作**: 
  - コードベース全体の構造分析
  - 品質メトリクスの評価
  - 改善提案の生成

#### `/sc:troubleshoot`
- **目的**: 体系的な問題診断
- **使用例**: `/sc:troubleshoot "ログインで500エラー"`
- **フラグ**: `--type build|runtime|performance`
- **動作**: 
  - 根本原因分析
  - 段階的な問題解決
  - 仮説検証アプローチ

### 🚀 最適化・改善

#### `/sc:improve`
- **目的**: コード最適化と品質向上
- **使用例**: `/sc:improve src/`
- **フラグ**: `--type performance|quality|security`, `--preview`
- **動作**: 
  - パフォーマンスボトルネックの特定
  - リファクタリング提案
  - セキュリティ脆弱性の修正

#### `/sc:optimize`
- **目的**: システム全体の最適化
- **使用例**: `/sc:optimize --target performance`
- **フラグ**: `--target performance|memory|bundle`
- **動作**: 
  - システムリソース使用量の最適化
  - バンドルサイズの削減
  - メモリ使用量の改善

### 📚 ドキュメンテーション

#### `/sc:document`
- **目的**: ドキュメント生成と管理
- **使用例**: `/sc:document --type api`
- **フラグ**: `--type api|user-guide|technical`, `--format markdown|html`
- **動作**: 
  - API仕様の自動生成
  - ユーザーガイドの作成
  - 技術ドキュメントの構造化

### 🔒 セキュリティ・品質

#### `/sc:secure`
- **目的**: セキュリティ監査と強化
- **使用例**: `/sc:secure --scan vulnerabilities`
- **フラグ**: `--scan vulnerabilities|dependencies|permissions`
- **動作**: 
  - 脆弱性スキャン
  - 依存関係のセキュリティチェック
  - 権限管理の検証

### 🎨 UI/UX開発

#### `/sc:ui`
- **目的**: UIコンポーネント生成
- **使用例**: `/sc:ui "ダッシュボードレイアウト"`
- **フラグ**: `--framework react|vue|angular`, `--style tailwind|css`
- **動作**: 
  - モダンUIパターンの適用
  - アクセシビリティ準拠
  - レスポンシブデザイン

## 高度なコマンド

### セッション管理
- `/sc:save` - セッション状態の保存
- `/sc:load` - セッション状態の復元
- `/sc:checkpoint` - 中間チェックポイントの作成

### プロジェクト管理
- `/sc:init` - 新規プロジェクトの初期化
- `/sc:migrate` - プロジェクトの移行
- `/sc:deploy` - デプロイメントの実行

## コマンドの動作原理

### 特徴
- **コンテキストトリガー**: ソフトウェアではなく、Claude Codeの動作を変更
- **専用指示ファイル**: 各コマンドは特別な指示ファイルを読み込み
- **チャットインターフェース**: Claude Code内でのみ動作
- **インテリジェント処理**: 適切なエージェントとMCPサーバーを自動選択

### 実行パターン
1. **理解** → コマンドの意図を解析
2. **計画** → 実行戦略を立案（並列化分析含む）
3. **実行** → 適切なツールとエージェントで実行
4. **検証** → 結果の品質チェック

## 📌 SuperClaude フラグシステム

### フラグの概要
SuperClaudeのフラグシステムは、コマンドの動作を細かく制御し、最適な結果を得るための強力なツールです。ほとんどのフラグは、キーワードやコンテキストに基づいて**自動的に発動**しますが、明示的に指定することも可能です。

### 🎯 分析深度フラグ

#### `--think` (標準分析)
- **トークン使用量**: 約4,000トークン
- **適用場面**: 中程度の複雑さの分析
- **自動発動**: 複数コンポーネントの分析が必要な場合
- **使用例**: `/sc:analyze src/ --think`

#### `--think-hard` (深度分析)
- **トークン使用量**: 約10,000トークン
- **適用場面**: アーキテクチャ分析、システム全体の依存関係
- **自動発動**: 大規模な設計判断が必要な場合
- **使用例**: `/sc:analyze architecture/ --think-hard`

#### `--ultrathink` (最大深度分析)
- **トークン使用量**: 約32,000トークン
- **適用場面**: 重要システム再設計、レガシーシステム現代化
- **自動発動**: 最高レベルの複雑さの問題
- **使用例**: `/sc:analyze legacy-system/ --ultrathink`

### 🔧 MCPサーバー制御フラグ

#### `--c7 / --context7`
- **機能**: 公式ライブラリドキュメントと パターン取得
- **自動発動**: ライブラリのimport、フレームワーク質問
- **使用例**: `/sc:implement "React認証" --c7`

#### `--seq / --sequential`
- **機能**: 複数ステップの構造化推論
- **自動発動**: 複雑なデバッグ、システム設計
- **使用例**: `/sc:troubleshoot "メモリリーク" --seq`

#### `--magic`
- **機能**: モダンUIコンポーネント生成
- **自動発動**: UIコンポーネントリクエスト
- **使用例**: `/sc:ui "ダッシュボード" --magic`

#### `--play / --playwright`
- **機能**: ブラウザテスト・E2E検証
- **自動発動**: ブラウザテスト、視覚的検証
- **使用例**: `/sc:test --type e2e --play`

#### `--morph / --morphllm`
- **機能**: 一括コード変換とパターン適用
- **自動発動**: 大規模なコード変換
- **使用例**: `/sc:improve codebase/ --morph`

#### `--serena`
- **機能**: セマンティックコード理解とセッション永続化
- **自動発動**: シンボル操作、プロジェクトメモリ
- **使用例**: `/sc:analyze --serena`

### 🎨 動作モードフラグ

#### `--brainstorm / --bs`
- **機能**: 協働的ディスカバリーマインドセット
- **自動発動**: 曖昧なプロジェクトリクエスト
- **使用例**: `/sc:brainstorm --strategy creative`

#### `--introspect`
- **機能**: メタ認知分析と推論プロセスの透明化
- **自動発動**: 自己分析リクエスト、エラー回復
- **使用例**: `/sc:analyze decision-process/ --introspect`

#### `--task-manage`
- **機能**: 複数ステップタスクの階層的組織化
- **自動発動**: 3ステップ以上の操作
- **使用例**: `/sc:implement "複雑機能" --task-manage`

#### `--orchestrate`
- **機能**: インテリジェントツール選択と並列調整
- **自動発動**: マルチツール操作、パフォーマンス制約
- **使用例**: `/sc:analyze large-project/ --orchestrate`

#### `--token-efficient / --uc`
- **機能**: 30-50%のトークン削減
- **自動発動**: コンテキスト使用量>75%
- **使用例**: `/sc:analyze --uc`

### 🛡️ 実行制御フラグ

#### `--safe-mode`
- **機能**: 最大検証、保守的実行
- **自動発動**: リソース使用量>85%、本番環境
- **効果**: 自動的に`--uc`フラグを有効化

#### `--validate`
- **機能**: 実行前リスク評価と検証ゲート
- **自動発動**: リスクスコア>0.7、重要な操作

#### `--preview`
- **機能**: 実際の実行なしでアクションをシミュレート
- **使用例**: `/sc:improve --preview`

### 🎯 焦点制御フラグ

#### `--focus [domain]`
- **オプション**: `performance|security|quality|architecture|accessibility|testing`
- **使用例**: `/sc:analyze --focus security`

#### `--scope [level]`
- **オプション**: `file|module|project|system`
- **使用例**: `/sc:analyze --scope project`

### 🔄 反復制御フラグ

#### `--loop`
- **機能**: 反復改善サイクルを有効化
- **自動発動**: 改善キーワード（polish, refine, enhance）

#### `--iterations [n]`
- **機能**: 改善サイクル数を設定（1-10の範囲）
- **使用例**: `/sc:improve --iterations 3`

### 🚀 並列処理制御フラグ

#### `--delegate [mode]`
- **オプション**: `auto|files|folders`
- **自動発動**: >7ディレクトリ または >50ファイル
- **機能**: サブエージェントの並列処理を有効化

#### `--concurrency [n]`
- **範囲**: 1-15
- **機能**: 最大同時実行操作数を制御

### ⚡ 特殊用途フラグ

#### `--all-mcp`
- **機能**: すべてのMCPサーバーを有効化
- **自動発動**: 最大複雑度シナリオ

#### `--no-mcp`
- **機能**: すべてのMCPサーバーを無効化
- **使用場面**: ネイティブツールのみの実行

#### `--verbose`
- **機能**: 詳細な意思決定ロジックを表示
- **トラブルシューティング用**

### フラグ優先順位ルール

1. **セーフティファースト**: `--safe-mode` > `--validate` > 最適化フラグ
2. **明示的上書き**: ユーザーフラグ > 自動検出
3. **深度階層**: `--ultrathink` > `--think-hard` > `--think`
4. **MCP制御**: `--no-mcp`はすべての個別MCPフラグを上書き

### 実践的フラグ組み合わせ例

#### フロントエンド開発
```bash
/sc:implement "レスポンシブダッシュボード" --magic --c7 --focus accessibility
```

#### バックエンドパフォーマンス分析
```bash
/sc:analyze api/ --focus performance --seq --think-hard
```

#### 大規模プロジェクト分析
```bash
/sc:analyze . --ultrathink --all-mcp --safe-mode --scope system
```

#### 効率的なコードレビュー
```bash
/sc:analyze pull-request/ --uc --focus quality --preview
```

## 使用上のベストプラクティス

### 効果的な使用方法
1. **明確な目的**: 具体的なタスクを指定
2. **適切なフラグ**: 必要な動作を制御するフラグを使用
3. **段階的アプローチ**: 小さなタスクから始めて段階的に拡張
4. **検証習慣**: 重要な変更前後での確認

### 避けるべきパターン
- 曖昧すぎる指示（brainstormモードを先に使用）
- フラグの過剰使用
- セッション保存なしでの長時間作業
- 品質チェックの省略

## 実践例

### Web アプリケーション開発の流れ
```bash
/sc:brainstorm "タスク管理アプリ"
/sc:workflow "フロントエンドとバックエンドの実装"
/sc:implement "認証システム" --type fullstack --focus security
/sc:test --type integration --coverage
/sc:document --type api
/sc:deploy --environment staging
```

### レガシーコードの改善
```bash
/sc:analyze legacy/
/sc:troubleshoot "パフォーマンス問題"
/sc:improve legacy/ --type performance --preview
/sc:test --type unit --fix
/sc:secure --scan vulnerabilities
```

このコマンドシステムにより、Claude Codeは単純なチャットボットから、構造化された開発プラットフォームに変換されます。