# コマンドディレクトリ

Claude Code カスタムコマンドのカテゴリ別一覧です。

## カテゴリ一覧

### [Kiroコマンドシステム](./kiro-system.md)
仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポート
- `/kiro:steering` - プロジェクトステアリング文書の生成・更新
- `/kiro:spec-init` - 新機能仕様の初期化
- `/kiro:spec-requirements` - EARS形式要件定義の生成
- `/kiro:spec-design` - 技術設計書の生成
- `/kiro:spec-test` - TDDテスト仕様の生成
- `/kiro:spec-tasks` - 実装タスクの生成
- `/kiro:spec-status` - 仕様進捗の表示

### [開発支援コマンド](./development-support.md)
開発プロセスを強力にサポートするコマンド群（Serena統合強化）
- `/commit` - **インテリジェントなGitコミット自動化（Serena統合）**
- `/debug-error` - **インテリジェントデバッグシステム（Serena統合）**
- `/smart-think` - **高度な多段階思考システム（Serena統合）**
- `/serena` - 高効率な構造化問題解決
- `/test` - 高度なテスト実装・実行・修正
- `/tech-research` - **コードベース認識型技術調査（Serena統合強化版）**
- `/spec:requirements` - 包括的要件定義書の生成

### [Chrome DevToolsコマンド](./chrome-devtools.md)
Chrome DevTools MCPを使用した包括的なブラウザ開発・テスト環境
- `/chrome` - **Chrome DevTools統合開発システム**
- デバッグ・エラー分析（コンソール・ネットワーク監視）
- E2Eテスト・ブラウザ自動化（ナビゲーション・入力・操作）
- パフォーマンス分析（トレース・Core Web Vitals・インサイト）
- ブラウザエミュレーション（CPU・ネットワーク・デバイス）
- マルチページ管理（タブ制御・履歴操作）

### [Git・GitHub連携コマンド](./git-github.md)
Git・GitHub連携とセキュリティ管理
- `/git:pr` - インテリジェントなプルリクエスト生成
- `/git:commit` - **高度なGitコミット自動化（Serena MCP統合）**
- `/dependabot-check` - セキュリティ脆弱性解決

### [Playwright MCPインテグレーションコマンド](./playwright-integration.md)
Playwright MCPとSerenaツールを統合したWebテストスイート
- `/e2e` - **E2Eテスト実行・動作検証**
- `/web-analyzer` - **ウェブサイト分析・仕様抽出**
- `/visual-regression` - **ビジュアルリグレッションテスト**
- `/accessibility-test` - **アクセシビリティテスト**
- `/performance-monitor` - **パフォーマンス監視**
- `/playwright-integration` - **Playwright統合診断**

### [UI/UX設計コマンド](./ui-ux.md)
UI/UXデザインとユーザビリティ向上
- `/ui-advice` - デザインパターン提案・ワイヤーフレーム

### [ファイル変換コマンド](./file-conversion.md)
様々な形式のファイルをMarkdown形式に変換し、AI分析に最適化
- `/convert-to-md` - PDF、DOCX、Excel等をMarkdownに変換（AI最適化対応）

### [ビジュアライズコマンド](./visualize.md)
ドキュメントをインフォグラフィック画像に変換し、チャットアプリでの共有を最適化
- `/visualize` - ドキュメント→インフォグラフィック変換（PNG/JPG/PDF対応）

### [開発ワークフローコマンド](./workflow-commands.md)
開発プロセス全体をサポートするワークフローコマンド
- [/plan](./plan.md) - 実装計画作成
- [/tdd](./tdd.md) - テスト駆動開発ワークフロー
- [/code-review](./code-review.md) - コードレビュー実行
- [/build-fix](./build-fix.md) - ビルドエラー修正
- [/e2e](./e2e.md) - E2Eテスト実行
- [/refactor-clean](./refactor-clean.md) - リファクタリング・クリーンアップ
- [/test-coverage](./test-coverage.md) - テストカバレッジ確認
- [/update-codemaps](./update-codemaps.md) - コードマップ更新
- [/update-docs](./update-docs.md) - ドキュメント更新

### [SuperClaude (SC) コマンド](./sc/)
SuperClaudeフレームワークのコアコマンド群
- `/sc:help` - 利用可能なSCコマンド一覧
- `/sc:pm` - プロジェクトマネージャーエージェント（常時アクティブ）
- `/sc:analyze` - コード品質・セキュリティ・パフォーマンス分析
- `/sc:implement` - 機能実装
- `/sc:design` - システム設計
- `/sc:test` - テスト実行
- `/sc:brainstorm` - 要件探索対話
- [詳細はSCコマンドディレクトリを参照](./sc/README.md)

### [Git操作コマンド](./git/)
高度なGit操作コマンド
- [/git:commit](./git/commit.md) - Serena統合スマートコミット
- [/git:pr](./git/pr.md) - PR説明生成・作成

### [Playwrightコマンド](./playwright/)
Playwright MCPを使用したテストスイート
- [/playwright:e2e](./playwright/e2e.md) - E2Eテスト
- [/playwright:accessibility-test](./playwright/accessibility-test.md) - アクセシビリティテスト
- [/playwright:performance-monitor](./playwright/performance-monitor.md) - パフォーマンス監視
- [/playwright:visual-regression](./playwright/visual-regression.md) - ビジュアルリグレッション
- [/playwright:web-analyzer](./playwright/web-analyzer.md) - Web分析

### [仕様コマンド](./spec/)
仕様・要件関連コマンド
- [/spec:requirements](./spec/requirements.md) - 要件定義書生成
- [/spec:tech-research](./spec/tech-research.md) - 技術調査

## 使用方法

各コマンドは `/コマンド名` で実行できます。詳細なオプションや使用例については、各カテゴリファイルを参照してください。

## 主要な特徴

- **Serena MCP統合強化**: コードベース認識型の高度な分析・支援
- **包括的テストスイート**: 単体テストからE2Eまでの完全カバレッジ
- **自動化重視**: 手動作業の最小化と効率的なワークフロー
- **多言語対応**: 日本語/英語での文書生成とインタラクション
- **柔軟な設定**: プロジェクトニーズに合わせたカスタマイズ対応
- **最適化されたツール設定**: 各コマンドは最大10ツールに最適化され、効率的な実行を実現