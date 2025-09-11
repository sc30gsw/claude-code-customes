# Claude Commands カスタムコマンド集

このリポジトリには、Claude Codeで使用できるカスタムコマンドが含まれています。

## カテゴリ別コマンド一覧

詳細なコマンド情報については、以下のカテゴリ別ファイルを参照してください：

### [Kiroコマンドシステム](./commands/kiro-system.md)
以下からinstall
https://github.com/gotalab/cc-sdd

仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポート

#### `/kiro:steering` - プロジェクトステアリング文書の生成・更新
プロジェクトのステアリングドキュメントを生成/更新。プロジェクト概要、技術スタック、構造を文書化。
- プロダクト概要ドキュメントの生成
- 技術スタック・アーキテクチャの文書化
- プロジェクト構造の定義
- 既存プロジェクトの分析と文書化

#### `/kiro:spec-init [詳細な機能説明]` - 新機能仕様の初期化
機能の詳細説明から仕様ディレクトリを作成し、開発プロセスを開始。
- 機能説明の自動解析
- 仕様ディレクトリ構造の作成
- 初期メタデータの生成

#### `/kiro:spec-requirements [機能名]` - EARS形式要件定義の生成
EARS形式（Easy Approach to Requirements Syntax）で要件とユーザーストーリーを作成。
- EARS形式での機能要件定義
- 非機能要件の分析
- ユーザーストーリーとアクセプタンス基準の生成
- プロダクトバックログ形式での出力

#### `/kiro:spec-design [機能名]` - 技術設計書の生成
アーキテクチャ、データモデル、APIを含む包括的な技術設計を作成。
- アーキテクチャ設計
- データモデル設計
- API設計とインターフェース定義
- セキュリティとパフォーマンスの考慮
- 実装ガイドラインの作成

#### `/kiro:spec-tasks [機能名]` - 実装タスクの生成
技術設計を基に詳細な実装ステップとTDDタスクを生成。
- 設計から実装タスクへの自動変換
- TDDサイクルでの実装ステップ定義
- 依存関係の考慮した実装順序
- 各タスクの完了基準定義

#### `/kiro:spec-status [機能名]` - 仕様進捗の表示
各仕様フェーズの進捗状況を可視化し、次のステップを提示。

#### `/kiro:validate-gap [機能名]` - 実装ギャップ分析
既存コードベースと要件間のギャップを分析し、実装戦略を提案。
- 既存コードベースの分析
- 実装可能性の評価
- 複数の実装アプローチの提示
- 技術リサーチ要件の特定
- 実装複雑度の評価（S/M/L/XL）

#### `/kiro:validate-design [機能名]` - 設計品質レビュー
技術設計の品質を対話的にレビューし、GO/NO-GO判定を行う。
- 既存アーキテクチャとの整合性チェック
- 設計一貫性・標準準拠の確認
- 拡張性・保守性の評価
- 型安全性・インターフェース設計の検証
- 最大3つの重要課題に焦点を当てたレビュー

### [開発支援コマンド](./commands/development-support.md)
開発プロセスを強力にサポートするコマンド群（Serena統合強化）

#### `/debug-error "[エラー説明]" [オプション]` - **インテリジェントデバッグシステム（Serena統合）**
Serena MCPを活用した高度なデバッグシステム。パターン認識、シンボル追跡、過去の解決例学習により効率的なエラー解決を実現。
- Serena MCPによるシンボルレベルのエラー分析
- 過去のデバッグセッションからの学習とパターン適用
- コードベース全体での類似問題パターン検索
- 精密なコード修正とインパクト評価
- デバッグ専門知識の蓄積と再利用
主要オプション：`--analyze`, `--trace`, `--serena-deep`, `--pattern-search`, `--memory`, `--interactive`, `--implement`

#### `/smart-think "[問題説明]" [オプション]` - **高度な多段階思考システム（Serena統合）**
Sequential Thinking MCPとSerena MCPを統合した高度な問題解決システム。4段階の思考モード（think/think-hard/think-harder/ultrathink）で複雑な技術的意思決定をサポート。
- Sequential Thinking MCPによる構造化された仮説生成・検証
- Serena MCPによるコードベース認識型技術決定
- 証拠ベースの推論と信頼度追跡（70-98%）
- 複数視点からの包括的分析
- 実装ロードマップとリスク評価
トークン予算：2,000-50,000（モードによる）

#### `/serena [問題] [オプション]` - 高効率な構造化問題解決
トークン効率を重視した構造化された問題解決コマンド。複雑な開発問題の分析・設計・実装を段階的に行う。
- クイックモード（3-5思考）からディープモード（10-15思考）まで対応
- デバッグ、設計、レビュー、実装の各パターンに特化
- TODOリスト自動生成とステップバイステップ実装
- 高いトークン効率で最大限の問題解決能力

#### `/test` - 高度なテスト実装・実行・修正
包括的なテスト環境管理と自動テスト生成・実行・修正機能。
- 単体テストからE2Eテストまでの完全カバレッジ
- テストファーストでの実装アプローチ
- 自動テストケース生成
- テスト失敗時の自動修正提案

#### `/spec:tech-research` - **コードベース認識型技術調査（Serena統合強化版）**
Serena MCPを活用したコードベース認識型の技術調査・評価システム。
- 既存コードベースとの互換性評価
- 技術選定の根拠と実装影響分析
- ベストプラクティスとアンチパターンの識別
- 段階的移行計画の策定

#### `/spec:requirements` - 包括的要件定義書の生成
プロジェクト要件の体系的な文書化と管理。
- 機能要件と非機能要件の明確な分離
- ステークホルダー分析と優先度設定
- リスク評価と緩和策の定義
- トレーサビリティマトリックスの生成

### [Git・GitHub連携コマンド](./commands/git-github.md)
Git・GitHub連携とセキュリティ管理

#### `/git:pr [オプション]` - インテリジェントなプルリクエスト生成
変更内容を自動分析してプルリクエストの説明文を生成し、GitHub上にPRを自動作成。
- Git変更履歴の自動分析（`git diff`, `git log`, `git status`）
- コミットメッセージからの意図推定
- プルリクエストテンプレートとの連携
- Serena MCPによる高速ファイル分析・シンボル解析
- Context7連携による関連ドキュメントURL取得
- Mermaid図表による変更の可視化
- GitHub APIを使用した自動PR作成・更新
オプション：`-p`（プッシュ後PR作成）、`-u`（既存PR更新のみ）

#### `/git:commit [オプション]` - **高度なGitコミット自動化（Serena MCP統合）**
Serena MCPを活用した高度なコミット自動化システム。変更内容の意味的分析、git履歴学習、コンテキスト認識によるコミットメッセージ生成。
- Serena MCPによるコードベース理解とパターン認識
- Git履歴からのコミット規約学習と適応
- conventional commitフォーマットでの絵文字付きメッセージ自動生成
- 変更の意味的分析による適切なコミット分割提案
- チーム固有のコミットパターンへの継続的適応
主要オプション：`--no-verify`, `--analyze`, `--learning`, `--scope`, `--batch`, `--interactive`, `--semantic-grouping`, `--impact-analysis`

#### `/dependabot-check [URL]` - セキュリティ脆弱性解決
Dependabotアラートを分析し、セキュリティ脆弱性の解決戦略を提供。
- GitHub Security Advisoryの詳細分析
- CVSS スコアに基づく脆弱性リスク評価
- 影響範囲の可視化（依存関係ツリー）
- 修正優先度の自動判定
- 複数修正手法の比較提示（メジャーアップデート、パッチ適用、代替パッケージ）
- 修正後の影響評価・テスト提案
- 自動化された修正スクリプト・コマンド生成

### [Playwright MCPインテグレーションコマンド](./commands/playwright-integration.md)
Playwright MCPとSerenaツールを統合したWebテストスイート

#### `/e2e [対象] [オプション]` - **E2Eテスト実行・動作検証**
Playwright MCPとSerenaツールを統合したアプリケーション動作テストと仕様検証。
- アプリケーション動作の自動検証
- 仕様書との動作比較
- インタラクティブテスト実行
- マルチデバイス対応
- 詳細なレポート生成
主要オプション：`-s/--spec`（仕様検証）、`-r/--report`（レポート生成）、`-i/--interactive`（対話モード）、`-d/--device`（デバイス指定）

#### `/web-analyzer [URL] [オプション]` - **ウェブサイト分析・仕様抽出**
Playwright MCPとSerenaツールを使用したウェブサイト構造・UI・UXの分析と開発用参考資料の自動生成。
- HTMLページ構造解析
- デザインシステム要素抽出
- UXフローの可視化
- 技術スタック検出
- Reactコンポーネント仕様生成
- 競合比較分析
主要オプション：`-d/--deep`（深層分析）、`-u/--ui-focus`（UI重点）、`-x/--ux-flow`（UXフロー）、`-t/--tech-stack`（技術検出）、`-c/--components`（コンポーネント抽出）

#### `/visual-regression [対象] [オプション]` - **ビジュアルリグレッションテスト**
Playwright MCPとSerenaツールを統合したビジュアル変更検出と意図しない修正の防止。
- ベースライン画像管理
- 差異検出・比較
- マルチデバイス対応
- 動的コンテンツ除外
- 差異レポート生成
- CI/CD統合
主要オプション：`-b/--baseline`（ベースライン作成）、`-c/--compare`（比較実行）、`-f/--full-page`（フルページ）、`-t/--threshold`（差異閾値）

#### `/accessibility-test [対象] [オプション]` - **アクセシビリティテスト**
Playwright MCPとSerenaツールを活用したWCAG 2.1/2.2準拠のアクセシビリティ検証。
- WCAG準拠チェック（A/AA/AAA）
- キーボードナビゲーション検証
- 色・コントラスト分析
- ARIA属性検証
- スクリーンリーダーシミュレーション
- 自動修正提案
- インタラクティブ修正
主要オプション：`-l/--level`（WCAGレベル）、`-k/--keyboard`（キーボードテスト）、`-c/--color`（色テスト）、`--screen-reader`（スクリーンリーダー）、`--auto-fix`（自動修正）

#### `/performance-monitor [対象] [オプション]` - **パフォーマンス監視**
Playwright MCPとSerenaツールを統合したWebアプリケーションパフォーマンス測定と最適化提案。
- Core Web Vitals測定（LCP、FID、CLS）
- Lighthouse監査
- ネットワーク分析
- JavaScript実行分析
- メモリ使用量監視
- ベースライン比較
- パフォーマンス予算
- 最適化提案
主要オプション：`-v/--vitals`（Core Web Vitals）、`-l/--lighthouse`（Lighthouse監査）、`-n/--network`（ネットワーク分析）、`-m/--memory`（メモリ監視）

#### `/playwright-integration [オプション]` - **Playwright統合診断**
Playwright MCPインテグレーションシステムの診断・設定確認・トラブルシューティング。
- 各コマンド動作確認
- Playwright MCP接続確認
- Serenaメモリ整合性チェック
- 設定ファイル検証
- 権限・セキュリティチェック
- 自動修復機能
オプション：`--diagnose`（全般診断）、`--check-browser`（ブラウザ確認）、`--check-serena`（Serena確認）、`--repair`（自動修復）

### [UI/UX設計コマンド](./commands/ui-ux.md)
UI/UXデザインとユーザビリティ向上

#### `/ui-advice [要件]` - デザインパターン提案・ワイヤーフレーム
UI/UXの専門知識に基づき、デザインパターンの提案とテキストワイヤーフレームを生成。
- 世界的に認知されたデザインパターンライブラリに基づく提案
- 3-5種類のデザインパターン提案（Material Design、Apple HIG、独自パターン等）
- 各パターンの特徴・メリット・デメリット・実装複雑度の詳細説明
- ASCII形式のテキストワイヤーフレーム生成
- 状況に応じた最適パターンの推奨とその理由
- WCAG、モバイルファースト、ユーザビリティを考慮した設計指針

### [Dev3000統合開発支援コマンド](./commands/dev3000-integration.md)
dev3000の統合ログ機能、Playwrightのブラウザ自動化、SerenaのコードインテリジェンスとSequential Thinkingの高度な分析能力を組み合わせた完全な開発ワークフロー管理システム

#### `/dev-3000 [アクション] [対象] [オプション]` - 包括的開発支援システム
**主要機能**:
- **Dev3000統合**: 統合ログ表示、自動エラー検出、リアルタイム監視、パフォーマンス追跡
- **Playwright統合**: E2Eテスト、視覚的回帰テスト、アクセシビリティテスト、クロスブラウザテスト
- **Serena統合**: スマートコード分析、自動バグ修正、パフォーマンス推奨、テスト生成
- **Sequential Thinking統合**: 体系的デバッグ、根本原因分析、最適化戦略、証拠ベース推論

**主要アクション**:
- `logs`: ログ表示・分析（`--filter`, `--watch`, `--last`）
- `errors`: ブラウザエラー分析（`--last`, `--context`, `--analyze`）
- `monitor`: リアルタイム監視（`--watch`, `--type`, `--threshold`）
- `debug`: 特定問題のデバッグ（`--fix`, `--interactive`, `--analyze`）
- `analyze`: コード分析（`--file`, `--performance`, `--suggestions`）
- `fix`: 自動修正（`--type`, `--dry-run`, `--validate`）
- `perf`: パフォーマンス分析（`--component`, `--analyze`, `--optimize`）
- `e2e`: E2Eテスト実行（`--scenario`, `--record`, `--verify`）
- `screenshot`: スクリーンショット取得（`--selector`, `--full-page`, `--save`）
- `browse`: ブラウザ自動化（`--action`, `--target`, `--value`）

---

## 全コマンド一覧

| コマンド | カテゴリ | 説明 |
|---------|---------|------|
| `/kiro:steering` | Kiro基本 | プロジェクトステアリング文書の生成・更新 |
| `/kiro:spec-init` | Kiro基本 | 新機能仕様の初期化 |
| `/kiro:spec-requirements` | Kiro基本 | EARS形式要件定義の生成 |
| `/kiro:spec-design` | Kiro基本 | 技術設計書の生成 |
| `/kiro:spec-tasks` | Kiro基本 | 実装タスクの生成 |
| `/kiro:spec-status` | Kiro基本 | 仕様進捗の表示 |
| `/kiro:validate-gap` | Kiro基本 | 実装ギャップ分析 |
| `/kiro:validate-design` | Kiro基本 | 設計品質レビュー |
| `/commit` | **開発支援（Serena統合）** | **インテリジェントなGitコミット自動化** |
| `/debug-error` | **開発支援（Serena統合）** | **インテリジェントデバッグシステム** |
| `/smart-think` | **開発支援（Serena統合）** | **高度な多段階思考システム** |
| `/serena` | 開発支援 | 構造化問題解決・デバッグ・設計 |
| `/test` | 開発支援 | 高度なテスト実装・実行・修正 |
| `/spec:tech-research` | **開発支援（Serena統合強化）** | **コードベース認識型技術調査** |
| `/spec:requirements` | 開発支援 | 包括的要件定義書の生成 |
| `/git:pr` | Git・GitHub | インテリジェントなPR生成 |
| `/git:commit` | Git・GitHub | **高度なGitコミット自動化（Serena MCP統合）** |
| `/dependabot-check` | Git・GitHub | セキュリティ脆弱性解決 |
| `/e2e` | **Playwright MCPインテグレーション** | **E2Eテスト実行・動作検証** |
| `/web-analyzer` | **Playwright MCPインテグレーション** | **ウェブサイト分析・仕様抽出** |
| `/visual-regression` | **Playwright MCPインテグレーション** | **ビジュアルリグレッションテスト** |
| `/accessibility-test` | **Playwright MCPインテグレーション** | **アクセシビリティテスト** |
| `/performance-monitor` | **Playwright MCPインテグレーション** | **パフォーマンス監視** |
| `/playwright-integration` | **Playwright MCPインテグレーション** | **Playwright統合診断** |
| `/ui-advice` | UI/UX | デザインパターン提案・ワイヤーフレーム |
| `/dev-3000` | **Dev3000統合** | **包括的開発支援システム** |

---

## 主要な特徴

- **Serena MCP統合強化**: コードベース認識型の高度な分析・支援
- **包括的テストスイート**: 単体テストからE2Eまでの完全カバレッジ
- **自動化重視**: 手動作業の最小化と効率的なワークフロー
- **多言語対応**: 日本語/英語での文書生成とインタラクション
- **柔軟な設定**: プロジェクトニーズに合わせたカスタマイズ対応