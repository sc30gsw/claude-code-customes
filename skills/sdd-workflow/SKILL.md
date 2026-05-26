# sdd-workflow — Workflow Status Dashboard

## Slash Command

```
/sdd-workflow [slug]
```

## Purpose

Read-only meta skill. Displays the current state of the SDD workflow — which phases are complete, which is next, and any blockers. Does NOT modify any files.

---

## This Skill is Read-Only

`sdd-workflow` never writes to or modifies any file. It only reads spec files and git history to report status. There is no approval gate for this skill.

---

## Usage: Specific Feature

```
/sdd-workflow <slug>
```

Reads `.claude/specs/<slug>/` and displays the full phase chain with status:

```
SDD Workflow: <slug>
Mode: standard | auto
Branch: feature/<slug> (12 commits ahead of main)

Phase Chain:
[✅] sdd-init              — source-notion.md archived
[✅] sdd-requirements      — requirements.md: 5 REQs defined
[✅] sdd-review-requirements — review.md: Requirements Review present
[✅] sdd-design            — design.md: 8 sections
[✅] sdd-tasks             — tasks.md: 12 TASKs defined
[✅] sdd-review-plan       — review.md: Plan Review + Traceability ✅
[🔄] sdd-impl              — progress: 3/12 done, TASK-004 in-progress
[⏳] sdd-review            — waiting for sdd-impl to complete
[⏳] sdd-pr                — waiting

Next action: /sdd-impl <slug> TASK-004   (resume in-progress task)
       or:   CONFIRM sdd-impl            (if paused at a gate)
```

Status icons:

| Icon | Meaning               |
| ---- | --------------------- |
| ✅   | Phase complete        |
| 🔄   | Phase in progress     |
| ⚠️   | Phase has a blocker   |
| ⏳   | Phase not yet started |

---

## Usage: All Features

```
/sdd-workflow
```

Lists all spec directories under `.claude/specs/` and shows each feature's current phase:

```
SDD Workflow Overview
Specs directory: .claude/specs/

slug                     | current phase  | status
-------------------------|----------------|-----------------------------------
user-authentication      | sdd-impl       | 🔄 3/8 tasks done
mail-group-bulk-delete   | sdd-pr         | ✅ PR #42 open
supplier-csv-export      | sdd-design     | ⏳ not started
```

If `.claude/specs/` is empty or does not exist:

```
No spec directories found under .claude/specs/
Run /sdd-init <slug> to start a new feature.
```

---

## Phase Detection Logic

Each phase is detected by inspecting files inside `.claude/specs/<slug>/`. Detection is sequential: if a phase's condition is not met, all subsequent phases show `⏳`.

| Phase                     | Detected When                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| `sdd-init`                | `source-notion.md` exists OR the `<slug>` directory itself exists                            |
| `sdd-requirements`        | `requirements.md` exists AND contains at least one `## REQ-` heading                         |
| `sdd-review-requirements` | `review.md` contains a `## Requirements Review` section                                      |
| `sdd-design`              | `design.md` exists (any non-empty content)                                                   |
| `sdd-tasks`               | `tasks.md` exists AND contains at least one `### TASK-` heading                              |
| `sdd-review-plan`         | `review.md` contains `## Plan Review` AND no unchecked `❌` in its Traceability subsection   |
| `sdd-impl`                | `progress.md` has at least one task marked `done`                                            |
| `sdd-review`              | `review.md` contains `## Code Review`                                                        |
| `sdd-pr`                  | `progress.md` contains a `## PR` section with a URL, OR `review.md` contains a GitHub PR URL |

---

## Progress Metrics (sdd-impl)

When `sdd-impl` is the current phase, show task completion metrics by parsing `progress.md`:

```
[🔄] sdd-impl — progress: 3/12 done (25%), 1 in-progress, 8 pending
     In-progress: TASK-004 (Create supplier CSV export hook)
     Last completed: TASK-003 (Add export button to supplier table)
```

Count tasks by status:

- `done`: lines matching `— done` or `[x]`
- `in-progress`: lines matching `— in-progress`
- `pending`: lines matching `— pending` or `[ ]`

---

## Blocker Detection

For the currently active or blocked phase, surface known blockers:

| Phase        | Blocker Condition                                            | Warning Message                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------- |
| `sdd-impl`   | `review.md` has no `## Plan Review` section                  | ⚠️ Run /sdd-review-plan \<slug\> before implementing    |
| `sdd-review` | `progress.md` has tasks still `pending`                      | ⚠️ N tasks still pending — run /sdd-impl \<slug\> first |
| `sdd-pr`     | `review.md` has unchecked `- [ ]` items under `### CRITICAL` | ⚠️ N open CRITICAL issues — resolve before creating PR  |
| `sdd-pr`     | `review.md` has no `## Code Review` section                  | ⚠️ Run /sdd-review \<slug\> before creating PR          |

Blockers appear with ⚠️ next to the phase name and a `Blocker:` line in the output.

---

## Git Branch Detection

Display the current branch and commit count:

```bash
git branch --show-current
git log main...HEAD --oneline | wc -l
```

Output:

```
Branch: feature/user-authentication (12 commits ahead of main)
```

If the current branch does not match the slug:

```
⚠️ Current branch (feature/other-thing) does not match slug (user-authentication)
   Switch to the correct branch before running implementation or review skills.
```

---

## Full Phase Chain Reference

The complete SDD skill chain in order:

```
1. sdd-init                — Archive Notion source, create spec directory
2. sdd-requirements        — Write requirements.md from source-notion.md
3. sdd-review-requirements — Review requirements, append to review.md
4. sdd-design              — Write design.md (architecture, components, API)
5. sdd-tasks               — Write tasks.md (TASK-xxx breakdown)
6. sdd-review-plan         — Review plan, verify traceability, append to review.md
7. sdd-impl                — TDD implementation, one commit per task
8. sdd-review              — Code + security review, append to review.md
9. sdd-pr                  — Create GitHub PR with traceability and test plan
```

---

## Example: Fully Complete Feature

```
SDD Workflow: user-authentication
Mode: auto
Branch: feature/user-authentication (12 commits ahead of main)

Phase Chain:
[✅] sdd-init              — source-notion.md archived
[✅] sdd-requirements      — requirements.md: 5 REQs (REQ-001 through REQ-005)
[✅] sdd-review-requirements — review.md: Requirements Review present
[✅] sdd-design            — design.md: 6 sections
[✅] sdd-tasks             — tasks.md: 12 TASKs defined
[✅] sdd-review-plan       — review.md: Plan Review, Traceability ✅
[✅] sdd-impl              — progress: 12/12 done
[✅] sdd-review            — review.md: Code Review (2026-05-26), 0 CRITICAL, 2 HIGH open
[⏳] sdd-pr                — waiting

Next action: /sdd-pr user-authentication
```
