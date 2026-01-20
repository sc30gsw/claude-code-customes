# コマンドディレクトリ

Claude Code カスタムコマンドのカテゴリ別一覧です。

## カテゴリ一覧

### [Kiroコマンドシステム](./kiro/)
仕様駆動開発（Spec-Driven Development）とTDDをサポート
- [/kiro:spec-init](./kiro/spec-init.md) - 新機能仕様の初期化
- [/kiro:spec-requirements](./kiro/spec-requirements.md) - EARS形式要件定義の生成
- [/kiro:spec-design](./kiro/spec-design.md) - 技術設計書の生成
- [/kiro:spec-tasks](./kiro/spec-tasks.md) - 実装タスクの生成
- [/kiro:spec-impl](./kiro/spec-impl.md) - TDDによるタスク実装
- [/kiro:spec-status](./kiro/spec-status.md) - 仕様進捗の表示
- [/kiro:steering](./kiro/steering.md) - Steeringドキュメント管理
- [/kiro:steering-custom](./kiro/steering-custom.md) - カスタムSteering作成
- [/kiro:validate-design](./kiro/validate-design.md) - 設計品質レビュー
- [/kiro:validate-gap](./kiro/validate-gap.md) - 実装ギャップ分析

### 開発支援コマンド
- [/serena](./serena.md) - トークン効率の高い構造化開発
- [/debug-error](./debug-error.md) - Serena統合デバッグシステム
- [/smart-think](./smart-think.md) - マルチモード思考システム
- [/test](./test.md) - 高度なテスト実装・実行

### Chrome DevToolsコマンド
- [/chrome](./chrome.md) - Chrome DevTools統合開発システム

### Git・GitHub連携コマンド
- [/git:commit](./git/commit.md) - Serena統合スマートコミット
- [/git:pr](./git/pr.md) - PR説明生成・作成
- [/dependabot-check](./dependabot-check.md) - セキュリティ脆弱性解決

### Playwrightコマンド
- [/playwright:e2e](./playwright/e2e.md) - E2Eテスト
- [/playwright:accessibility-test](./playwright/accessibility-test.md) - アクセシビリティテスト
- [/playwright:performance-monitor](./playwright/performance-monitor.md) - パフォーマンス監視
- [/playwright:visual-regression](./playwright/visual-regression.md) - ビジュアルリグレッション
- [/playwright:web-analyzer](./playwright/web-analyzer.md) - Web分析
- [/playwright:spec-integration](./playwright/spec-integration.md) - 統合診断

### UI/UX設計コマンド
- [/ui-advice](./ui-advice.md) - デザインパターン提案・ワイヤーフレーム

### ファイル変換コマンド
- [/convert-to-md](./convert-to-md.md) - 各種形式をMarkdownに変換
- [/visualize](./visualize.md) - ドキュメントのインフォグラフィック化

### 開発ワークフローコマンド
- [/plan](./plan.md) - 実装計画作成
- [/tdd](./tdd.md) - テスト駆動開発ワークフロー
- [/code-review](./code-review.md) - コードレビュー実行
- [/build-fix](./build-fix.md) - ビルドエラー修正
- [/e2e](./e2e.md) - E2Eテスト実行
- [/refactor-clean](./refactor-clean.md) - リファクタリング・クリーンアップ
- [/test-coverage](./test-coverage.md) - テストカバレッジ確認
- [/update-codemaps](./update-codemaps.md) - コードマップ更新
- [/update-docs](./update-docs.md) - ドキュメント更新
- [/update-claude-md](./update-claude-md.md) - CLAUDE.md自動更新
- [/okr](./okr.md) - OKR設定支援

### [SuperClaude (SC) コマンド](./sc/)
SuperClaudeフレームワークのコアコマンド群
- [/sc:help](./sc/help.md) - 利用可能なSCコマンド一覧
- [/sc:pm](./sc/pm.md) - プロジェクトマネージャーエージェント
- [/sc:analyze](./sc/analyze.md) - コード品質・セキュリティ分析
- [/sc:implement](./sc/implement.md) - 機能実装
- [/sc:design](./sc/design.md) - システム設計
- [/sc:test](./sc/test.md) - テスト実行
- [/sc:brainstorm](./sc/brainstorm.md) - 要件探索対話
- [詳細はSCコマンドディレクトリを参照](./sc/README.md)

### 仕様コマンド
- [/spec:requirements](./spec/requirements.md) - 要件定義書生成
- [/spec:tech-research](./spec/tech-research.md) - 技術調査

## 使用方法

各コマンドは `/コマンド名` で実行できます。詳細なオプションや使用例については、各ファイルを参照してください。

## 主要な特徴

- **Serena MCP統合**: コードベース認識型の高度な分析・支援
- **Kiro Spec-Driven Development**: 仕様駆動の体系的な開発ワークフロー
- **包括的テストスイート**: 単体テストからE2Eまでの完全カバレッジ
- **自動化重視**: 手動作業の最小化と効率的なワークフロー
- **多言語対応**: 日本語/英語での文書生成とインタラクション
