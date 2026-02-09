# Team Builder Skill

## 概要

ユーザーの要件を分析し、最適なClaude Code Agent Teamを自動構成・デプロイするスキル。プロジェクト、ユーザー、グローバル、プラグインの全5スコープから利用可能なスキルとエージェントを検出し、タスク依存関係グラフを生成して、マルチエージェントワークフローをオーケストレーションします。

## アクティベーショントリガー

- 複雑なタスクで並列作業が必要な場面
- マルチエージェントチームの作成リクエスト
- 大規模な機能開発、調査、リファクタリング
- セキュリティ監査やフルスタック開発の開始時

## 使用方法

```bash
# 自動モード: リクエスト分析からチーム構成
/team-builder "Design and implement JWT authentication system"

# テンプレートモード: 定義済みテンプレートを使用
/team-builder -t feature-dev "User management API"

# マニュアルモード: エージェントとスキルを直接指定
/team-builder -a "planner,frontend-architect,e2e-runner" -s "senior-frontend,e2e,ai-sdk"

# ドライラン: デプロイせずにプレビュー
/team-builder --dry-run "Large-scale refactoring"

# コスト最適化 + 自動デプロイ
/team-builder -m budget --auto "Documentation cleanup"

# 高リスク作業での計画承認モード
/team-builder -t full-stack -p "Payment processing system"
```

## 引数一覧

| 引数 | 短縮 | 説明 | 例 |
|------|------|------|-----|
| `--agents` | `-a` | 含めるエージェントタイプ（カンマ区切り） | `-a "planner,system-architect"` |
| `--skills` | `-s` | チームメイトに使用させるスキル（カンマ区切り） | `-s "tdd-workflow,security-review"` |
| `--template` | `-t` | 定義済みテンプレートを使用 | `-t feature-dev` |
| `--name` | `-n` | チーム名（省略時は自動生成） | `-n "auth-team"` |
| `--model` | `-m` | モデル戦略: deep/adaptive/fast/budget | `-m adaptive` |
| `--size` | | チームサイズ上限（デフォルト: auto、最大: 5） | `--size 3` |
| `--lead` | `-l` | リードエージェントタイプ | `-l planner` |
| `--dry-run` | | デプロイせずに構成をプレビュー | `--dry-run` |
| `--auto` | | 確認なしで自動デプロイ | `--auto` |
| `--delegate` | `-d` | リードがコーディネーションのみに集中 | `--delegate` |
| `--plan-approval` | `-p` | チームメイトに計画承認を要求 | `-p` |
| `--display` | | 表示モード: in-process/split | `--display split` |

## 3つのワークフローモード

### AUTOモード（デフォルト）

`--template` も `--agents` も未指定の場合:

1. **リクエスト分析** - ドメインキーワードを検出して作業種別を特定
2. **リソース検出** - `discover_resources.py` で全5スコープのリソースをカタログ化
3. **関連性スコアリング** - ドメインマッピングでエージェント/スキルをマッチング
4. **チーム提案** - タスク依存関係付きの最適構成を生成
5. **確認** - ユーザー承認を待機（`--auto` でスキップ）
6. **デプロイ** - TeamCreate → TaskCreate → Task spawn を実行

### TEMPLATEモード（`-t` 指定時）

1. 定義済みテンプレートを読み込み
2. ユーザーのリクエストでタスク説明をカスタマイズ
3. `-a`, `-s` の上書きを適用
4. デプロイ実行

### MANUALモード（`-a` のみ指定時）

1. 指定されたエージェントタイプでチームを構築
2. `-s` のスキルを適切なロールにルーティング
3. ユーザーリクエストからタスクを自動生成
4. デプロイ実行

## 利用可能なテンプレート

| テンプレート | ユースケース | メンバー |
|-------------|------------|---------|
| `feature-dev` | フルサイクル機能開発 | planner + architect + tester |
| `investigation` | バグ調査・根本原因分析 | analyst + tester + researcher |
| `refactor` | コード品質改善 | refactorer + reviewer + tester |
| `security-audit` | セキュリティ評価 | security + reviewer + tester |
| `frontend` | フロントエンド機能開発 | designer + reviewer + e2e |
| `full-stack` | エンドツーエンド開発 | backend + frontend + tester + security |
| `documentation` | ドキュメント作成 | writer + analyst |
| `exploration` | 多角的分析 | ux-analyst + tech-architect + devils-advocate |

## ドメイン自動検出

| ドメイン | キーワード | 推奨エージェント | 推奨スキル |
|---------|----------|----------------|-----------|
| 機能開発 | build, implement, create, add | planner, system-architect, testing-specialist | /plan, /tdd-workflow, /code-reviewer |
| バグ調査 | debug, fix, investigate, error | root-cause-analyst, testing-specialist | /debug-error, /test-coverage |
| リファクタリング | refactor, clean, improve | refactoring-expert, quality-engineer | /refactor-clean, /code-reviewer |
| セキュリティ | security, audit, vulnerability | security-reviewer, quality-engineer | /security-review |
| フロントエンド | UI, component, design | frontend-architect, e2e-runner | /senior-frontend, /e2e |
| バックエンド | API, endpoint, database | system-architect, testing-specialist | /senior-backend, /tdd-workflow |
| ドキュメント | document, docs, spec | technical-writer, requirements-analyst | /doc-engineer, /update-docs |
| パフォーマンス | performance, optimize, slow | performance-engineer, system-architect | /test-coverage |
| 探索 | explore, research, analyze | general-purpose (複数) | /plan, /smart-think |

## モデル選択戦略

| 戦略 (`-m`) | リード | アーキテクト/アナリスト | ワーカー |
|------------|-------|---------------------|---------|
| `deep` | opus | opus | opus |
| `adaptive`（デフォルト） | opus | opus | sonnet |
| `fast` | sonnet | sonnet | sonnet |
| `budget` | sonnet | haiku | haiku |

## スキルインジェクション

各チームメイトのスポーンプロンプトに利用可能なスキルを埋め込むことで、チームメイトが適切なスキルを活用できるようにします:

```
You are the {role-name} on team "{team-name}". Your task is: {task-description}

## Available Skills
Invoke the following skills as needed during your work:
- /tdd-workflow: Test-driven development with 80%+ coverage
- /security-review: Comprehensive security checklist
- /code-reviewer: Code quality review

## On Completion
1. Use TaskUpdate to mark your task as completed
2. Send a summary to team-lead via SendMessage
```

スキルリストは `discover_resources.py` の出力から動的に生成され、全スコープのスキルがチームメイトのロールに応じてマッチングされます。

## バンドルリソース

### scripts/
- `discover_resources.py` - 全5スコープのエージェント/スキルを自動検出。`--format json|table` と `--scope project|user|global|plugin|all` フラグ対応。

### references/
- `team-templates.md` - 8つの定義済みチームテンプレート（メンバー定義、タスクフロー、スポーンプロンプトテンプレート付き）
- `composition-guide.md` - チーム構成ベストプラクティス（サイジング、モデル選択、タスク粒度、ファイル競合回避、アンチパターン）

## 他のコマンドとの連携

チーム構成後：
- `/plan` - 個々のタスクの実装計画
- `/tdd-workflow` - テスト駆動開発
- `/code-reviewer` - コードレビュー
- `/security-review` - セキュリティレビュー

## ベストプラクティス

1. **チームサイズ** - 最大5名（それ以上はコミュニケーションオーバーヘッドが増大）
2. **ファイル所有権** - 各チームメイトが異なるファイルセットを担当
3. **タスク粒度** - 1タスク = 明確な成果物を生む自己完結型作業単位
4. **モデル戦略** - コスト/品質バランスに応じて適切な戦略を選択
5. **スキル注入** - スポーンプロンプトに必ず関連スキルを記載
6. **デリゲートモード** - リードはコーディネーションに集中し、実装はチームメイトに委任
