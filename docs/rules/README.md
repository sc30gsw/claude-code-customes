# Rules - コーディングルール

Claude Codeの動作を制御するルールファイルのドキュメントです。

## ルール一覧

### 開発プロセス

| ルール | 説明 | ファイル |
|-------|------|---------|
| [agents](./agents.md) | エージェント連携ルール | `.claude/rules/agents.md` |
| [git-workflow](./git-workflow.md) | Gitワークフロー | `.claude/rules/git-workflow.md` |
| [testing](./testing.md) | テスト要件 | `.claude/rules/testing.md` |

### コード品質

| ルール | 説明 | ファイル |
|-------|------|---------|
| [coding-style](./coding-style.md) | コーディングスタイル | `.claude/rules/coding-style.md` |
| [patterns](./patterns.md) | 共通パターン | `.claude/rules/patterns.md` |
| [security](./security.md) | セキュリティガイドライン | `.claude/rules/security.md` |

### システム設定

| ルール | 説明 | ファイル |
|-------|------|---------|
| [hooks](./hooks.md) | フックシステム | `.claude/rules/hooks.md` |
| [performance](./performance.md) | パフォーマンス最適化 | `.claude/rules/performance.md` |

## ルールの適用

ルールは `.claude/rules/` ディレクトリに配置され、Claude Codeセッション中に自動的に参照されます。

### ルールの優先度

1. **CRITICAL** - 必ず従う（セキュリティ、データ整合性）
2. **HIGH** - 強く推奨（コード品質、テスト）
3. **MEDIUM** - 推奨（スタイル、パターン）
4. **LOW** - 任意（最適化、便利機能）

## 関連リソース

- [エージェント](../sub-agents/README.md) - 専門エージェント一覧
- [コマンド](../commands/README.md) - 利用可能なコマンド
