# sdd-tasks

**Slash command**: `/sdd-tasks <slug>`
**Purpose**: Generate `tasks.md` (TASK-001..N) and `progress.md` from `requirements.md` and `design.md`.

---

## Prerequisites

- `.claude/specs/<slug>/requirements.md` must exist
- `.claude/specs/<slug>/design.md` must exist (run `/sdd-design` first)

---

## Steps

### 1. Read spec inputs

```
.claude/specs/<slug>/requirements.md
.claude/specs/<slug>/design.md
```

Extract:

- Every REQ-XXX ID with its acceptance criteria
- Every design section (§X.X) with its title
- File structure plan (§3) for deriving "Files to modify"
- Component responsibilities (§6.1) for scoping tasks

### 2. Decompose requirements into tasks

Rules for decomposition:

- Each TASK must implement one or more REQ-XXX entries
- Each TASK maps to one or more design sections via `Design ref`
- One TASK per logical unit of work (one file, one hook, one component, or one test suite)
- If a task feels L complexity, split it
- Ordering: schemas → API mutations → SWR hooks → nuqs query state → containers → presentation components → MSW handlers → tests → integration/E2E

Complexity guidelines:

| Size | Meaning                                    |
| ---- | ------------------------------------------ |
| S    | ~30 min — single file, clear scope         |
| M    | ~2 h — multiple related files, clear scope |
| L    | ~4+ h — warn user; recommend splitting     |

### 3. Write `tasks.md`

Use the format below for every task. Copy the template from `.claude/skills/sdd-tasks/templates/tasks.md` and fill it in.

```markdown
### TASK-001 — <title>

Implements: REQ-001, REQ-002
Design ref: §3.2 Component hierarchy
Type: feat | test | refactor | docs | chore
Estimated complexity: S | M | L
Files to modify:

- src/features/<feature>/schemas/<feature>-schema.ts (create)
- src/features/<feature>/hooks/use-<feature>.ts (create)
  Acceptance: matches REQ-001 acceptance criteria
```

Field rules:

- `Implements`: comma-separated REQ-XXX IDs; every REQ must appear in at least one task
- `Design ref`: `§X.X <section title>` format; every design section must appear in at least one task
- `Type`: one of `feat`, `test`, `refactor`, `docs`, `chore`
- `Files to modify`: list with `(create)` or `(modify)` suffix
- `Acceptance`: copy or paraphrase directly from the REQ acceptance criteria

### 4. Write `progress.md`

Copy the template from `.claude/skills/sdd-tasks/templates/progress.md` and fill in:

- `slug`: the spec slug
- `mode`: read from requirements.md front-matter or default to `standard`
- `started`: today's date in YYYY-MM-DD format
- Task state table: one row per TASK, all set to `pending`

### 5. Mode-specific behaviour

**`--mode standard`**: Present the task breakdown to the user. Discuss granularity and ordering. Allow the user to add, remove, or reorder tasks before writing the files.

**`--mode auto`**: Decompose autonomously. If any task has L complexity, add a warning comment directly in `tasks.md` above that task:

```markdown
<!-- ⚠️ L-complexity task — consider splitting before implementation -->
```

---

## Output

```
.claude/specs/<slug>/tasks.md
.claude/specs/<slug>/progress.md
```

---

## Validation before writing

Before writing the files, verify:

1. Every REQ-XXX from requirements.md appears in at least one `Implements:` field
2. Every design section §X.X from design.md appears in at least one `Design ref:` field
3. No duplicate TASK-XXX IDs
4. No TASK is missing an `Implements:` field

If any check fails, report the gap and ask the user whether to auto-fill or stop.

---

## Phase Gate

```
== PHASE COMPLETE: sdd-tasks ==
Artifact: .claude/specs/<slug>/tasks.md
Artifact: .claude/specs/<slug>/progress.md
Summary:
- TASK-001 through TASK-NNN generated covering all REQ-XXX entries
- All design sections §X.X covered by at least one Design ref
- Complexity estimates provided; L tasks flagged for splitting
- progress.md initialised with all tasks in pending state
- Mode recorded as standard|auto in progress.md header

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-review-plan` to proceed, or describe changes needed.
```
