# team-builder plugin

Claude Code Agent Teamsの最適編成を1コマンドで自動化するプラグイン。

## Install

```bash
# このリポジトリをマーケットプレースとして追加
claude plugin marketplace add https://github.com/sc30gsw/claude-code-customes

# プラグインをインストール
claude plugin install team-builder@claude-code-customes
```

## Usage

```bash
# AUTO: リクエストからチームを自動構成
/team-builder "Design and implement JWT authentication system"

# TEMPLATE: 定義済みテンプレートを使用
/team-builder -t feature-dev "User management API"

# MANUAL: エージェントとスキルを直接指定
/team-builder -a "planner,frontend-architect,e2e-runner" -s "senior-frontend,e2e"

# DRY-RUN: デプロイせずにプレビュー
/team-builder --dry-run "Large-scale refactoring"
```

## Features

- **3 Modes**: AUTO (domain detection) / TEMPLATE (8 presets) / MANUAL (direct spec)
- **5 Scope Discovery**: project, user, global, plugin marketplaces, plugin cache
- **4 Model Strategies**: deep / adaptive / fast / budget
- **Task Dependencies**: Parallel/sequential task flow with `blockedBy`
- **Skill Injection**: Auto-inject relevant skills into each teammate's prompt

## Templates

| Template | Use Case | Members |
|----------|----------|---------|
| `feature-dev` | Full-cycle feature development | planner + architect + tester |
| `investigation` | Bug investigation and RCA | analyst + tester + researcher |
| `refactor` | Code quality improvement | refactorer + reviewer + tester |
| `security-audit` | Security assessment | security + reviewer + tester |
| `frontend` | Frontend feature development | designer + reviewer + e2e |
| `full-stack` | End-to-end development | backend + frontend + tester + security |
| `documentation` | Documentation creation | writer + analyst |
| `exploration` | Multi-perspective analysis | ux-analyst + tech-architect + devils-advocate |

## Plugin Structure

```
team-builder/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── team-builder.md
├── skills/
│   └── team-builder/
│       ├── SKILL.md
│       ├── scripts/
│       │   └── discover_resources.py
│       └── references/
│           ├── team-templates.md
│           └── composition-guide.md
├── commands/
│   └── team-builder.md
└── README.md
```

## Args

| Arg | Short | Description |
|-----|-------|-------------|
| `--agents` | `-a` | Agent types (comma-separated) |
| `--skills` | `-s` | Skills for teammates (comma-separated) |
| `--template` | `-t` | Predefined template |
| `--name` | `-n` | Team name |
| `--model` | `-m` | Model strategy: deep/adaptive/fast/budget |
| `--size` | | Team size limit (max: 5) |
| `--lead` | `-l` | Lead agent type |
| `--dry-run` | | Preview without deploying |
| `--auto` | | Auto-deploy without confirmation |
| `--delegate` | `-d` | Lead focuses on coordination only |
| `--plan-approval` | `-p` | Require plan approval from teammates |
