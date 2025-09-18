# Claude Commands カスタムコマンド集

このリポジトリには、Claude Codeで使用できるカスタムコマンドが含まれています。

## カテゴリ別コマンド一覧

詳細なコマンド情報については、以下のカテゴリ別ファイルを参照してください：

### [Kiroコマンドシステム](./commands/kiro-system.md)
仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポート
- `/kiro:steering` - プロジェクトステアリング文書の生成・更新
- `/kiro:spec-init` - 新機能仕様の初期化
- `/kiro:spec-requirements` - EARS形式要件定義の生成
- `/kiro:spec-design` - 技術設計書の生成
- `/kiro:spec-test` - TDDテスト仕様の生成
- `/kiro:spec-tasks` - 実装タスクの生成
- `/kiro:spec-status` - 仕様進捗の表示

### [開発支援コマンド](./commands/development-support.md)
開発プロセスを強力にサポートするコマンド群（Serena統合強化）
- `/debug-error` - **インテリジェントデバッグシステム（Serena統合）**
- `/smart-think` - **高度な多段階思考システム（Serena統合）**
- `/serena` - 高効率な構造化問題解決
- `/test` - 高度なテスト実装・実行・修正
- `/spec:tech-research` - **コードベース認識型技術調査（Serena統合強化版）**
- `/spec:requirements` - 包括的要件定義書の生成
- `/update-claude-md` - **プロジェクト固有CLAUDE.md自動生成・更新（Serena統合）**

### [Git・GitHub連携コマンド](./commands/git-github.md)
Git・GitHub連携とセキュリティ管理
- `/git:pr` - インテリジェントなプルリクエスト生成
- `/git:commit` - **高度なGitコミット自動化（Serena MCP統合）**
- `/dependabot-check` - セキュリティ脆弱性解決

### [Playwright MCPインテグレーションコマンド](./commands/playwright-integration.md)
Playwright MCPとSerenaツールを統合したWebテストスイート
- `/e2e` - **E2Eテスト実行・動作検証**
- `/web-analyzer` - **ウェブサイト分析・仕様抽出**
- `/visual-regression` - **ビジュアルリグレッションテスト**
- `/accessibility-test` - **アクセシビリティテスト**
- `/performance-monitor` - **パフォーマンス監視**
- `/playwright-integration` - **Playwright統合診断**

### [UI/UX設計コマンド](./commands/ui-ux.md)
UI/UXデザインとユーザビリティ向上
- `/ui-advice` - デザインパターン提案・ワイヤーフレーム

---

## 全コマンド一覧

| コマンド | カテゴリ | 説明 |
|---------|---------|------|
| `/kiro:steering` | Kiro基本 | プロジェクトステアリング文書の生成・更新 |
| `/kiro:spec-init` | Kiro基本 | 新機能仕様の初期化 |
| `/kiro:spec-requirements` | Kiro基本 | EARS形式要件定義の生成 |
| `/kiro:spec-design` | Kiro基本 | 技術設計書の生成 |
| `/kiro:spec-test` | Kiro基本 | TDDテスト仕様の生成 |
| `/kiro:spec-tasks` | Kiro基本 | 実装タスクの生成 |
| `/kiro:spec-status` | Kiro基本 | 仕様進捗の表示 |
| `/commit` | **開発支援（Serena統合）** | **インテリジェントなGitコミット自動化** |
| `/debug-error` | **開発支援（Serena統合）** | **インテリジェントデバッグシステム** |
| `/smart-think` | **開発支援（Serena統合）** | **高度な多段階思考システム** |
| `/serena` | 開発支援 | 構造化問題解決・デバッグ・設計 |
| `/test` | 開発支援 | 高度なテスト実装・実行・修正 |
| `/tech-research` | **開発支援（Serena統合強化）** | **コードベース認識型技術調査** |
| `/spec:requirements` | 開発支援 | 包括的要件定義書の生成 |
| `/update-claude-md` | **開発支援（Serena統合）** | **プロジェクト固有CLAUDE.md自動生成・更新** |
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

---

## 主要な特徴

- **Serena MCP統合強化**: コードベース認識型の高度な分析・支援
- **包括的テストスイート**: 単体テストからE2Eまでの完全カバレッジ
- **自動化重視**: 手動作業の最小化と効率的なワークフロー
- **多言語対応**: 日本語/英語での文書生成とインタラクション
- **柔軟な設定**: プロジェクトニーズに合わせたカスタマイズ対応