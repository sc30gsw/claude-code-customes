# SDD ワークフロー — Spec-Driven Development ガイド

> **対象読者**: エンジニア・非エンジニアを問わず、AI アシスタントと協力して
> Notion のバックログチケットから Pull Request まで一気通貫で進めたい方

---

## 1. このワークフローが解決すること

### 問題定義

通常の開発では、以下のようなギャップが発生しがちです。

| 状態                            | 問題                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| Notion Backlog にチケットがある | 要件が自然言語で書かれており曖昧。実装者によって解釈が異なる |
| 実装に入った                    | 何を作ったか・なぜこう作ったかの根拠がコードに残らない       |
| レビュー・マージ後              | 要件とコードの対応関係が失われ、後から追跡できない           |

SDD ワークフローはこの問題を **9 フェーズ + 厳格な承認ゲート** で解決します。

```
Notion Backlog
    ↓ /sdd-init
source-notion.md  (Notion の内容をローカル保存)
    ↓ /sdd-requirements
requirements.md   (REQ-001..N — EARS 形式の要件定義)
    ↓ /sdd-design
design.md         (Mermaid 図 + ファイル構造)
    ↓ /sdd-tasks
tasks.md          (TASK-001..M — 実装タスク一覧)
    ↓ /sdd-impl
コード + テスト   (TASK-001 ごとにコミット)
    ↓ /sdd-pr
GitHub PR         (REQ → TASK → commit のトレーサビリティテーブル付き)
```

---

## 2. 9 フェーズの概要

| #   | フェーズ         | コマンド                                 | 主な成果物                               |
| --- | ---------------- | ---------------------------------------- | ---------------------------------------- |
| 1   | **Init**         | `/sdd-init <slug> [notion-url] [--mode]` | `source-notion.md`, `progress.md`        |
| 2   | **Requirements** | `/sdd-requirements <slug>`               | `requirements.md`                        |
| 3   | **Review Req**   | `/sdd-review-requirements <slug>`        | `review.md §Requirements Review`         |
| 4   | **Design**       | `/sdd-design <slug>`                     | `design.md`                              |
| 5   | **Tasks**        | `/sdd-tasks <slug>`                      | `tasks.md`, `progress.md` 更新           |
| 6   | **Review Plan**  | `/sdd-review-plan <slug>`                | `review.md §Plan Review + §Traceability` |
| 7   | **Implement**    | `/sdd-impl <slug> [task-id]`             | コード + テスト, `progress.md` 更新      |
| 8   | **Code Review**  | `/sdd-review <slug>`                     | `review.md §Code Review + §Security`     |
| 9   | **PR**           | `/sdd-pr <slug>`                         | GitHub PR                                |
| -   | **Meta**         | `/sdd-workflow [slug]`                   | フェーズ状態の表示（読み取り専用）       |

すべての成果物は `.claude/specs/<slug>/` 以下に保存されます。

---

## 3. 各フェーズで使うコマンドと成果物

### SDD Skill 一覧（各コマンドの役割）

SDD は `.claude/skills/sdd-*/` に定義されたスキル群です。モードは `/sdd-init` で一度だけ指定し、以降は `progress.md` を参照します。

| Skill | フェーズ | 説明 | 主な成果物 |
| ----- | -------- | ---- | ---------- |
| `/sdd-init` | 1 Init | spec ディレクトリを初期化。Notion を `source-notion.md` に保存し、mode を `progress.md` に記録 | `source-notion.md`, `progress.md` |
| `/sdd-requirements` | 2 Requirements | `source-notion.md` から EARS 形式の要件（REQ-001..N）を作成 | `requirements.md` |
| `/sdd-review-requirements` | 3 Review Req | 要件の曖昧さ・矛盾・受入基準をレビュー。ECC `requirements-analyst` を起動 | `review.md` §Requirements Review |
| `/sdd-design` | 4 Design | Mermaid 図・ファイル構造・状態管理方針を含む設計書を作成（ECC `/plan` に委譲） | `design.md` |
| `/sdd-tasks` | 5 Tasks | 設計を TDD 順の TASK-001..M に分解し、REQ・設計セクションと紐付け | `tasks.md`, `progress.md` |
| `/sdd-review-plan` | 6 Review Plan | REQ→設計→タスクのトレーサビリティ検証とプレビュー。6 項目すべて ✅ で実装可能 | `review.md` §Plan Review, §Traceability |
| `/sdd-impl` | 7 Implement | ECC `tdd-workflow` でタスクごとに TDD 実装し `feat(TASK-NNN):` でコミット | コード・テスト, `progress.md` |
| `/sdd-review` | 8 Code Review | `/code-review` と `/security-review` で差分をレビュー（自動修正なし） | `review.md` §Code Review, §Security |
| `/sdd-pr` | 9 PR | REQ→TASK→commit 表付きの GitHub PR を作成（`git-pr` に委譲） | GitHub PR |
| `/sdd-workflow` | Meta | フェーズ進捗の表示のみ（ファイルは変更しない） | — |

ビジュアル版: [SDD ワークフロー インタラクティブ図](./sdd-workflow.html)

### フェーズ 1 — Init

```bash
# Notion URL を渡す場合（推奨）
/sdd-init mail-groups-filter https://www.notion.so/enechange/xxxx

# ローカルにメモがある場合（Notion URL なし）
/sdd-init mail-groups-filter

# 自動モードで開始
/sdd-init mail-groups-filter https://... --mode auto
```

**成果物:**

```
.claude/specs/mail-groups-filter/
├── source-notion.md   # Notion の内容（または手動入力した要件メモ）
└── progress.md        # フェーズ進捗トラッカー（自動管理）
```

`source-notion.md` は Notion の内容をそのまま保存したもので、以降のフェーズで AI が参照します。

---

### フェーズ 2 — Requirements

```bash
/sdd-requirements mail-groups-filter
```

AI が `source-notion.md` を読み込み、EARS（Easy Approach to Requirements Syntax）形式で要件を構造化します。

**成果物:** `requirements.md`

```markdown
# Requirements: Mail Groups Filter

## REQ-001

**タイトル**: 名前によるフィルタリング
**EARS**: WHEN ユーザーが名前フィールドに文字を入力した場合、
システムは一致するメールグループのみを表示しなければならない
**受入基準**:

- [ ] 部分一致で検索される
- [ ] 大文字・小文字を区別しない
- [ ] 検索結果が 0 件の場合は「該当なし」と表示される

## REQ-002

...
```

**承認ゲート後**: `CONFIRM sdd-review-requirements` と入力

---

### フェーズ 3 — Review Requirements

```bash
/sdd-review-requirements mail-groups-filter
```

`requirements-analyst` エージェントが要件を検証します。

- 曖昧な表現の指摘
- 矛盾・重複の検出
- 受入基準の十分性チェック
- standard モードでは `spec-tech-research` スキルも起動し、技術的実現可能性を調査

**成果物:** `review.md` に `§Requirements Review` セクションが追加される

---

### フェーズ 4 — Design

```bash
/sdd-design mail-groups-filter
```

`architect` エージェントと `spec-tech-research` スキルが設計を作成します。

**成果物:** `design.md`

```markdown
# Design: Mail Groups Filter

## 3.1 コンポーネント図

\`\`\`mermaid
graph LR
A[MailGroupsFilterForm] --> B[useMailGroupsQueryState]
B --> C[nuqs URLパラメータ]
A --> D[useMailGroups]
D --> E[MSW / API]
\`\`\`

## 3.2 ファイル構造

\`\`\`
src/features/mail-groups/
├── components/
│ └── mail-groups-filter-form.tsx # REQ-001, REQ-002
├── hooks/
│ └── use-mail-groups-filter.ts # REQ-001
└── schemas/
└── mail-groups-filter-schema.ts # REQ-001
\`\`\`

## 3.3 データフロー

...
```

---

### フェーズ 5 — Tasks

```bash
/sdd-tasks mail-groups-filter
```

`planner` エージェントが設計をタスクに分解します。TDD（Red → Green → Refactor）順に並べられます。

**成果物:** `tasks.md`, `progress.md` 更新

```markdown
# Tasks: Mail Groups Filter

## TASK-001

**タイトル**: フィルタースキーマの作成
**対応要件**: REQ-001
**対応設計**: design.md §3.2
**種別**: Unit Test → Implementation
**ファイル**: `src/features/mail-groups/schemas/mail-groups-filter-schema.ts`

## TASK-002

**タイトル**: URL クエリ状態フックの実装
**対応要件**: REQ-001, REQ-002
**依存**: TASK-001
...
```

---

### フェーズ 6 — Review Plan

```bash
/sdd-review-plan mail-groups-filter
```

`planner` エージェントと `architect` エージェントがプランを検証します。

- タスク間の依存関係チェック
- REQ → TASK のトレーサビリティ確認
- 抜け漏れタスクの検出
- standard モードでは `spec-tech-research` スキルも実行

**成果物:** `review.md` に `§Plan Review` と `§Traceability Coherence` セクションが追加

---

### フェーズ 7 — Implement

```bash
# 全タスクを順番に実装
/sdd-impl mail-groups-filter

# 特定タスクのみ（中断後の再開）
/sdd-impl mail-groups-filter TASK-003
```

`tdd-workflow` スキルに従い、テストを先に書いてから実装します。

**各タスクのコミットメッセージ形式:**

```
feat(TASK-001): フィルタースキーマを追加

- MailGroupsFilterSchema を valibot で定義
- name, status フィールドのバリデーション追加
```

**成果物:** コード・テストファイル、`progress.md` 更新（各タスク完了時）

---

### フェーズ 8 — Code Review

```bash
/sdd-review mail-groups-filter
```

Claude Code `/code-review` スキルと ECC `/security-review` スキルが実行されます。

**成果物:** `review.md` に以下セクションが追加

- `§Code Review` — CRITICAL / HIGH / MEDIUM の指摘事項
- `§Security Review` — セキュリティ観点の指摘事項

CRITICAL 指摘がある場合は、修正してから次フェーズに進みます。

---

### フェーズ 9 — PR

```bash
/sdd-pr mail-groups-filter
```

`git-pr` スキルが GitHub PR を作成します。PR 本文には以下が含まれます。

- 実装の概要
- REQ → TASK → commit のトレーサビリティテーブル

```markdown
## Traceability

| 要件                             | タスク             | コミット         |
| -------------------------------- | ------------------ | ---------------- |
| REQ-001 名前フィルタリング       | TASK-001, TASK-002 | abc1234, def5678 |
| REQ-002 ステータスフィルタリング | TASK-003           | ghi9012          |
```

---

### Meta — Workflow 状態確認

```bash
# 現在作業中の slug の状態を確認
/sdd-workflow

# 特定 slug の状態を確認
/sdd-workflow mail-groups-filter
```

読み取り専用コマンドです。どのフェーズが完了・進行中・未着手かを表示します。

---

## 4. `--mode standard` と `--mode auto` の違い

モードは `/sdd-init <slug> [--mode standard|auto]` で指定します（省略時は `standard`）。以降のスキルは `progress.md` の Mode を読み取ります。

### モードの選び方

| モード | 向いている人 | 特徴 |
| ------ | ------------ | ---- |
| **`standard`**（デフォルト） | エンジニア | 人間が意思決定。各フェーズと TDD サイクルで確認しながら進める。技術調査スキルを併用 |
| **`auto`** | 非エンジニア / AI に任せたいエンジニア | AI が草案・実装まで進める。承認は要件レビュー・プラン・コードレビューなど重要ゲートに集中 |

### 比較表

| 観点             | `standard`（デフォルト）                           | `auto`                                 |
| ---------------- | -------------------------------------------------- | -------------------------------------- |
| **想定ユーザー** | エンジニア                                         | 非エンジニア / AI に任せたいエンジニア |
| **主導者**       | 人間が意思決定、AI がサポート                      | AI が主導、人間は承認のみ              |
| **要件定義**     | 人間が REQ を記述、AI が EARS 整形を支援           | AI が質問 → 回答から `requirements.md` を一括作成 |
| **要件レビュー** | analyst + planner + `spec-tech-research`           | analyst のみ（ビジネス観点を優先）     |
| **プラン review**| planner + architect + `spec-tech-research`       | architect のみ                         |
| **実装**         | RED / GREEN / REFACTOR ごとに停止して確認          | TDD を連続実行、タスク完了まで自動ループ |
| **コードレビュー** | 指摘一覧を提示、修正はエンジニアが判断           | CRITICAL / HIGH に修正案を併記（適用はしない） |
| **承認ゲート**   | 全フェーズで `CONFIRM` が必要                      | 重要なゲートのみ（フェーズ 3, 6, 8）   |
| **対話**         | AI に質問しながら進める                            | AI からの確認事項を最小化              |

### フェーズごとのモード差（要約）

| フェーズ | `standard` | `auto` |
| -------- | ---------- | ------ |
| 2 Requirements | テンプレートを人間が埋める | 7 問のヒアリング後、AI が一括作成 |
| 3 Review Req | 技術実現性を含む多角的レビュー | 受入基準・ビジネス観点中心。懸念を平易に説明 |
| 7 Implement | TDD 各段階で一時停止 | タスク単位で自動コミット。`pnpm check` 失敗時は最大 3 回自己修正 |
| 8 Code Review | エンジニア向けの技術指摘 | 重大な指摘に修正案を添える |

### auto モードの使い方

```bash
/sdd-init payment-refactor https://notion.so/... --mode auto
```

auto モードでは、AI は各フェーズを自動的に進め、承認ゲートに達したときだけ停止して確認を求めます。

```
AI: フェーズ 3（要件レビュー）が完了しました。
    以下の点が懸念されます：
    - REQ-003 の受入基準が具体的でない可能性があります

    続行するには CONFIRM sdd-design と入力してください。
    修正が必要な場合は、修正内容を指示してください。
```

---

## 5. トレーサビリティ規約

SDD の核心は「なぜこのコードがあるか」を追跡できるようにすることです。

### ID 書式

| 成果物   | 形式                       | 例                                          |
| -------- | -------------------------- | ------------------------------------------- |
| 要件     | `REQ-NNN`                  | `REQ-001`, `REQ-012`                        |
| タスク   | `TASK-NNN`                 | `TASK-001`, `TASK-015`                      |
| コミット | `feat/fix(TASK-NNN): 説明` | `feat(TASK-003): URLクエリ状態フックを追加` |

### トレーサビリティ連鎖

```
REQ-001（要件）
  ↓ 設計で参照
  design.md §3.2（設計）
  ↓ タスクで参照
  TASK-001（タスク）
  ↓ コミットで参照
  feat(TASK-001): フィルタースキーマを追加（コミット）
  ↓ PR で集約
  PR #123 — トレーサビリティテーブル（PR）
```

### ファイル内での参照例

`tasks.md` では必ず対応要件と設計セクションを明記します:

```markdown
## TASK-003

**対応要件**: REQ-001, REQ-002
**対応設計**: design.md §3.2
```

`review.md` では指摘事項に要件 ID を紐付けます:

```markdown
### [HIGH] REQ-001: 部分一致ロジックが大文字を考慮していない

ファイル: `src/features/mail-groups/hooks/use-mail-groups-filter.ts:45`
```

---

## 6. 承認ゲートの読み方と進め方

各フェーズの終わりに、AI は承認ゲートを提示します。

### 実際の出力例

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ フェーズ 2（Requirements）完了

成果物: .claude/specs/mail-groups-filter/requirements.md
要件数: 5 件（REQ-001 〜 REQ-005）

【確認が必要な点】
- REQ-004 の「適切なタイムアウト」は具体的な秒数を決める必要があります
- REQ-005 はスコープ外の可能性があります（チームで確認推奨）

次のフェーズ: sdd-review-requirements（要件レビュー）

👉 続行: CONFIRM sdd-review-requirements
   修正: 修正内容を日本語で指示してください
   スキップ: SKIP sdd-review-requirements（非推奨）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 操作方法

| 操作               | 入力                                           | 効果                                   |
| ------------------ | ---------------------------------------------- | -------------------------------------- |
| 次フェーズへ進む   | `CONFIRM sdd-review-requirements`              | フェーズ 3 を開始                      |
| 修正を指示         | `REQ-004 のタイムアウトは 30 秒にしてください` | 修正後に再度ゲートを表示               |
| スキップ（非推奨） | `SKIP sdd-review-requirements`                 | レビューなしで次へ（品質低下のリスク） |

---

## 7. トラブルシュート / 再開方法

### 中断した場合

セッションが中断した場合、以下の手順で再開します。

```bash
# 1. 現在の状態を確認
/sdd-workflow mail-groups-filter

# 出力例:
# フェーズ 1 Init         ✅ 完了
# フェーズ 2 Requirements ✅ 完了
# フェーズ 3 Review Req   ✅ 完了
# フェーズ 4 Design       ✅ 完了
# フェーズ 5 Tasks        ✅ 完了
# フェーズ 6 Review Plan  ✅ 完了
# フェーズ 7 Implement    🔄 進行中（TASK-003 まで完了）
# フェーズ 8 Code Review  ⬜ 未着手
# フェーズ 9 PR           ⬜ 未着手

# 2. 中断したタスクから再開
/sdd-impl mail-groups-filter TASK-004
```

### よくある問題

| 問題                         | 対処                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| 要件が大きく変わった         | `/sdd-requirements <slug>` を再実行して `requirements.md` を更新。フェーズ 3 以降をやり直す |
| タスクが多すぎる             | `/sdd-tasks <slug>` を再実行して `tasks.md` を再生成。スコープを絞るよう AI に指示          |
| コミットメッセージが規約違反 | `git commit --amend` で修正。`feat(TASK-NNN):` 形式を維持する                               |
| `progress.md` の状態がズレた | `/sdd-workflow <slug>` で確認後、AI に状態の修正を依頼                                      |
| テストが通らない             | `/sdd-impl <slug> TASK-NNN` を再実行。AI に原因の調査を依頼                                 |

### スペックファイルの場所

```
.claude/specs/
└── <slug>/
    ├── source-notion.md    # 元の Notion 内容
    ├── requirements.md     # 要件（REQ-NNN）
    ├── design.md           # 設計
    ├── tasks.md            # タスク（TASK-NNN）
    ├── review.md           # 各フェーズのレビュー結果
    └── progress.md         # フェーズ・タスク進捗
```

---

## 8. 既存 ECC / Claude Code スキルとの対応関係

SDD ワークフローは既存のスキル・エージェントを組み合わせて動作します。

| フェーズ                   | 使用されるスキル / エージェント | 役割                         |
| -------------------------- | ------------------------------- | ---------------------------- |
| 3: Review Req（standard）  | `spec-tech-research`            | 技術的実現可能性の調査       |
| 3: Review Req              | ECC `requirements-analyst`      | 要件の品質チェック           |
| 4: Design                  | ECC `planner`                   | 実装計画の作成               |
| 4: Design（standard）      | `spec-tech-research`            | ライブラリ選定・技術調査     |
| 6: Review Plan（standard） | `spec-tech-research`            | 設計の技術妥当性確認         |
| 6: Review Plan             | ECC `planner`                   | タスク分解の検証             |
| 6: Review Plan             | ECC `architect`                 | アーキテクチャ観点のレビュー |
| 7: Implement               | ECC `tdd-workflow`              | テスト駆動実装               |
| 8: Code Review             | Claude Code `/code-review`      | コード品質チェック           |
| 8: Code Review             | ECC `/security-review`          | セキュリティチェック         |
| 9: PR                      | `git-pr`                        | GitHub PR の作成             |

### プロジェクト固有スキル

このプロジェクト（`e_value_management_frontend`）では以下のスキルが `spec-tech-research` から呼び出されます:

- `mantine-form` — Mantine フォームパターンの調査
- `swr-jotai` パターン — SWR / Jotai の使い方確認
- `vitest` — テスト設計のベストプラクティス
- `msw-mocking` — MSW ハンドラの設計

---

## 参考リンク

- [SDD ワークフロー インタラクティブ図](./sdd-workflow.html) — フェーズ遷移の視覚的確認
- [CODING_GUIDELINES.md](../../../../CODING_GUIDELINES.md) — コーディング規約
- [.claude/rules/common/testing.md](../../../../.claude/rules/common/testing.md) — テスト戦略
- [ECC プラグイン活用ガイド](../ecc/ecc-index.md) — ECC スキル一覧
