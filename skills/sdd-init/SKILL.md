# Skill: sdd-init

## Invocation

```
/sdd-init <slug> [notion-url] [--mode standard|auto]
```

**Arguments:**

- `<slug>` — kebab-case identifier for the feature (e.g. `user-invitation`, `supplier-csv-import`)
- `[notion-url]` — optional Notion page URL to fetch and archive as source material
- `[--mode standard|auto]` — workflow mode (default: `standard`)
  - `standard`: engineer-led — AI assists, human drives decisions
  - `auto`: AI-led — suitable for non-engineers; AI asks questions and makes decisions autonomously

---

## Purpose

Initialize a spec directory for a new feature under `.claude/specs/<slug>/`. This is always the first step in the SDD workflow. It creates the directory structure, optionally fetches a Notion page as source material, and records the chosen mode in `progress.md`.

---

## Execution Steps

### Step 1: Validate inputs

- Confirm `<slug>` is kebab-case (lowercase letters, digits, hyphens only).
- If `--mode` is not provided, default to `standard`.
- Announce to the user: "Initializing spec for `<slug>` in `--mode <mode>`."

### Step 2: Create directory structure

Create the following empty directories and files under `.claude/specs/<slug>/`:

```
.claude/specs/<slug>/
├── review-results/      ← subdirectory for review output files
├── progress.md          ← created in this step
├── change-log.md        ← created in this step
├── requirements.md      ← placeholder (created by sdd-requirements)
├── design.md            ← placeholder (created by sdd-design)
└── tasks.md             ← placeholder (created by sdd-tasks)
```

Run:

```bash
mkdir -p .claude/specs/<slug>/review-results/
```

Write placeholder files with a single comment line:

```
<!-- Artifact not yet generated. Run the corresponding sdd-* skill. -->
```

### Step 3: Fetch Notion page (if notion-url provided)

If a Notion URL is given:

1. Extract the page ID from the URL (last 32-character hex segment, with or without hyphens).
2. Call `mcp__claude_ai_Notion__notion-fetch` with the page ID.
3. Write the raw Markdown content to `.claude/specs/<slug>/source-notion.md`.
4. If the fetch fails, warn the user and continue without the source file.

If no Notion URL is given, skip this step.

### Step 4: Write progress.md and change-log.md

Write `.claude/specs/<slug>/progress.md` with the following structure:

```markdown
# Spec Progress: <slug>

**Mode**: <standard|auto>
**Initialized**: <YYYY-MM-DD>
**Notion source**: <notion-url or "none">

## Phase Status

| Phase | Skill                   | Status         |
| ----- | ----------------------- | -------------- |
| 1     | sdd-requirements        | ⬜ not started |
| 2     | sdd-review-requirements | ⬜ not started |
| 3     | sdd-design              | ⬜ not started |
| 4     | sdd-tasks               | ⬜ not started |
| 5     | sdd-review-plan         | ⬜ not started |
| 6     | sdd-impl                | ⬜ not started |
| 7     | sdd-review              | ⬜ not started |
| 8     | sdd-pr                  | ⬜ not started |

## Files

| File                                         | Description                                           |
| -------------------------------------------- | ----------------------------------------------------- |
| `requirements.md`                            | EARS-format requirements                              |
| `design.md`                                  | Architecture and design decisions                     |
| `tasks.md`                                   | Task breakdown (TASK-xxx)                             |
| `review-results/requirement-review.md`       | Requirements Review findings                          |
| `review-results/plan-review.md`              | Plan Review + Traceability findings                   |
| `review-results/code-review.md`              | Code Review + Security Review findings                |
| `change-log.md`                              | Phase completion event log                            |
```

Write `.claude/specs/<slug>/change-log.md` with the following structure:

```markdown
# Change Log: <slug>

| Date | Skill | Event |
|------|-------|-------|
| <YYYY-MM-DD> | sdd-init | スペック初期化 |
```

### Step 5: Print confirmation

Print a summary of what was created, including:

- Directory path
- Mode recorded
- Whether a Notion source was fetched
- `change-log.md` initialized with first row
- The next step to take

---

## Mode Behavior Summary

| Aspect       | `--mode standard`          | `--mode auto`              |
| ------------ | -------------------------- | -------------------------- |
| Who drives   | Engineer                   | AI                         |
| AI role      | Assist + review            | Ask + decide               |
| Notion fetch | Optional                   | Optional                   |
| Next skill   | `/sdd-requirements <slug>` | `/sdd-requirements <slug>` |

---

## Notes

- The `progress.md` file is the single source of truth for the mode. Subsequent skills MUST read mode from `progress.md` rather than accepting a `--mode` flag themselves.
- If `.claude/specs/<slug>/` already exists, warn the user and ask whether to overwrite or abort. Do NOT silently overwrite.
- The `slug` is used as-is in all file paths. Choose descriptive, stable slugs.

---

== PHASE COMPLETE: sdd-init ==
Artifact: .claude/specs/<slug>/progress.md
Summary:

- Created spec directory structure under .claude/specs/<slug>/
- Recorded mode (standard|auto) in progress.md
- Fetched Notion source (if URL provided) → source-notion.md
- All placeholder artifacts initialized

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-requirements` to proceed. Or describe changes needed.
