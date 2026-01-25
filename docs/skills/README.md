# スキルディレクトリ

Claude Code スキルシステムの一覧です。スキルは特定のタスクに特化した機能セットを提供します。

## 利用可能なスキル

### From [SKILLS.sh](https://skills.sh/)
- [agent-browser](https://skills.sh/vercel-labs/agent-browser/agent-browser)
- [email-best-practice]https://skills.sh/resend/email-best-practices/email-best-practices
- [context7](https://skills.sh/intellectronica/agent-skills/context7)

### ドキュメント・計画
- [doc-engineer-skill](./doc-engineer-skill.md) - ドキュメント作成・編集・改善
- [writing-plans-skill](./writing-plans-skill.md) - 計画書作成
- [plan-skill](./plan-skill.md) - 実装計画作成（ユーザー確認待ち）
- [okr-skill](./okr-skill.md) - 四半期OKR作成

### 開発スキル
- [senior-frontend-skill](./senior-frontend-skill.md) - シニアフロントエンド開発
- [senior-backend-skill](./senior-backend-skill.md) - シニアバックエンド開発
- [frontend-design-skill](./frontend-design-skill.md) - フロントエンドデザイン
- [vercel-react-best-practices-skill](./vercel-react-best-practices-skill.md) - React/Next.js パフォーマンス最適化
- [serena-skill](./serena-skill.md) - Serena MCPによる構造化開発
- [smart-think-skill](./smart-think-skill.md) - マルチモード思考システム

### 開発・ビルド
- [build-fix-skill](./build-fix-skill.md) - ビルド/TypeScriptエラー修正
- [chrome-skill](./chrome-skill.md) - Chrome DevTools統合
- [debug-error-skill](./debug-error-skill.md) - デバッグシステム（Serena統合）
- [refactor-clean-skill](./refactor-clean-skill.md) - デッドコード削除

### 品質・セキュリティスキル
- [code-reviewer-skill](./code-reviewer-skill.md) - コードレビュー専門
- [security-review-skill](./security-review-skill.md) - セキュリティレビュー
- [tdd-workflow-skill](./tdd-workflow-skill.md) - テスト駆動開発ワークフロー

### テスト・品質
- [test-skill](./test-skill.md) - 包括的テスト実装
- [test-coverage-skill](./test-coverage-skill.md) - カバレッジ分析・改善
- [e2e-skill](./e2e-skill.md) - E2Eテスト（Playwright）

### ドキュメント・変換
- [convert-to-md-skill](./convert-to-md-skill.md) - ファイル→Markdown変換
- [update-docs-skill](./update-docs-skill.md) - ドキュメント自動同期
- [update-claude-md-skill](./update-claude-md-skill.md) - CLAUDE.md自動更新
- [update-codemaps-skill](./update-codemaps-skill.md) - コードマップ更新
- [visualize-skill](./visualize-skill.md) - ドキュメント→画像変換

### Git・バージョン管理
- [git-commit-skill](./git-commit-skill.md) - Git自動コミット（Serena統合）
- [git-pr-skill](./git-pr-skill.md) - PR自動作成
- [dependabot-check-skill](./dependabot-check-skill.md) - Dependabot分析

### UI・デザイン
- [ui-advice-skill](./ui-advice-skill.md) - UI/UXアドバイス・ワイヤーフレーム

### 仕様・要件
- [spec-requirements-skill](./spec-requirements-skill.md) - 要件定義書生成
- [spec-tech-research-skill](./spec-tech-research-skill.md) - 技術調査

### AI・プロンプトスキル
- [senior-prompt-engineer-skill](./senior-prompt-engineer-skill.md) - プロンプトエンジニアリング

### メタスキル
- [skill-creator-skill](./skill-creator-skill.md) - スキル作成ガイド

## 使用方法

各スキルは自動的に適切なコンテキストで有効化されます。詳細な機能や使用例については、各スキルファイルを参照してください。

スキルは `/skill-name` の形式でコマンドとして呼び出すこともできます:

```bash
# 例
/build-fix          # ビルドエラーを修正
/test LoginForm     # テストを実装
/git:commit         # コミットを作成
/plan               # 実装計画を作成
/e2e                # E2Eテストを実行
```

## カテゴリ別スキル数

| カテゴリ | スキル数 |
|----------|---------|
| ドキュメント・計画 | 4 |
| 開発スキル | 6 |
| 開発・ビルド | 4 |
| 品質・セキュリティ | 3 |
| テスト・品質 | 3 |
| ドキュメント・変換 | 5 |
| Git・バージョン管理 | 3 |
| UI・デザイン | 1 |
| 仕様・要件 | 2 |
| AI・プロンプト | 1 |
| メタスキル | 1 |
| **合計** | **33** |

## 公式Skills

- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [Expo Skills](https://github.com/expo/skills)
- [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)
