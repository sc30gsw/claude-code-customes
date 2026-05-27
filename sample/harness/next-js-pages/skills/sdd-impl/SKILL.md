# sdd-impl — Implement Tasks (TDD)

## Slash Command

```
/sdd-impl <slug> [task-id]
```

## Purpose

Implement one task (or all pending tasks) for a spec using strict Test-Driven Development. Delegates test/implementation cycles to the `/ecc:tdd-workflow` skill and keeps `progress.md` up to date throughout.

---

## Prerequisites

Before running this skill, confirm:

- `sdd-review-plan` has been run: `review.md` must contain a `## Plan Review` section with no `❌` in the Traceability section.
- `tasks.md` exists and has at least one task in `pending` status.

If the plan review is missing, stop and instruct the user to run `/sdd-review-plan <slug>` first.

---

## Input Files

| File                               | Purpose                                       |
| ---------------------------------- | --------------------------------------------- |
| `.claude/specs/<slug>/tasks.md`    | Task definitions and acceptance criteria      |
| `.claude/specs/<slug>/progress.md` | Current task statuses and mode setting        |
| `.claude/specs/<slug>/design.md`   | Architecture decisions guiding implementation |
| `.claude/specs/<slug>/review.md`   | Checked for Plan Review completion            |

---

## Mode Behavior

Read `mode` from the YAML front matter of `progress.md`:

```yaml
---
mode: standard # or: auto
---
```

| Aspect                  | `standard` (engineer-led)                       | `auto` (AI-led)                                           |
| ----------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| After RED phase         | Pause — show failing test, wait for `CONFIRM`   | Proceed automatically                                     |
| After GREEN phase       | Pause — show implementation, wait for `CONFIRM` | Proceed automatically                                     |
| After REFACTOR phase    | Pause — show final state, wait for `CONFIRM`    | Post summary and proceed to next task                     |
| On `pnpm check` failure | Stop, show error, ask for guidance              | Attempt self-fix up to 3 iterations, then stop and report |

---

## Steps

### 1. Determine Which Task to Implement

```
If [task-id] is provided:
  - Locate that task in tasks.md
  - Verify its status in progress.md is "pending" (or "in-progress" if resuming)
  - Warn if the task is already "done"

Otherwise:
  - Find the first task with status "in-progress" in progress.md (resume case)
  - If none, find the first task with status "pending"
  - If all tasks are "done", report completion and skip to the gate
```

### 2. Mark Task as In-Progress

Update `progress.md`:

```markdown
<!-- Before -->

- [ ] TASK-001: Create user schema — pending

<!-- After -->

- [x] TASK-001: Create user schema — in-progress
```

### 3. TDD Cycle via `/ecc:tdd-workflow`

Invoke the `/ecc:tdd-workflow` skill for the selected task. Pass the task's acceptance criteria as the specification.

**RED phase — Write failing test:**

- Co-locate the test file with the source file (e.g., `use-login.ts` → `use-login.test.ts`)
- Target the acceptance criteria from `tasks.md` directly
- Run `pnpm test:run` — confirm the test fails for the right reason
- In `standard` mode: pause and display the failing test output

**GREEN phase — Minimal implementation:**

- Write the minimum code to make the test pass
- Apply project constraints (see below)
- Run `pnpm test:run` — confirm the test passes
- In `standard` mode: pause and display the passing test output

**REFACTOR phase — Clean up:**

- Remove duplication, improve naming, ensure Japanese comments on non-obvious logic
- Run `pnpm check` — must pass with no errors
- Run `pnpm test:run` — all tests must still pass
- In `standard` mode: pause and display the final state

### 4. Commit

After each task completes its TDD cycle:

```bash
git add <changed files>
git commit -m "feat(TASK-001): <task title from tasks.md>"
```

Use the exact task ID and title from `tasks.md`. Follow Conventional Commits format.

### 5. Update `progress.md`

```markdown
<!-- After completion -->

- [x] TASK-001: Create user schema — done
```

Append a brief note under the task if relevant (e.g., which files were created or modified).

### 6. Repeat

If no `[task-id]` was given (`auto` mode or batch run), loop back to Step 1 and pick the next `pending` task. Continue until all tasks are `done` or the user interrupts.

---

## Project Constraints (Enforced at Every Commit)

These are non-negotiable for this project:

| Constraint         | Rule                                                                       |
| ------------------ | -------------------------------------------------------------------------- |
| Validation command | `pnpm check` (runs oxlint + oxfmt + tsc together)                          |
| Test command       | `pnpm test:run`                                                            |
| Imports            | Always use `~/` alias — never relative paths                               |
| Type declarations  | `type` only — never `interface`                                            |
| Exports            | No `export default` outside `src/pages/` and `*.config.*` files            |
| Error handling     | `better-result` (`Result.tryPromise`, `.match({err, ok})`) — not try/catch |
| Logging            | No `console.log` in committed code                                         |
| Memoization        | No `useMemo` / `useCallback` — React Compiler handles this                 |
| Test file location | Co-located with source (e.g., `use-foo.ts` + `use-foo.test.ts`)            |
| Test queries       | `getByRole` > `getByText` > `getByLabelText` — never `getByTestId`         |
| Object key order   | Alphabetical in `better-result` calls: `catch → try`, `err → ok`           |

### `better-result` patterns

API layer (`mutations.ts`) — `catch` before `try`:

```typescript
export function createFoo(params: CreateFooParams) {
  return Result.tryPromise({
    catch: toApiError,
    try: async () => {
      const response = await apiClient.api.v1.foos.$post({ body: params })
      return response
    },
  })
}
```

Hook layer (`use-*.ts`) — `err` before `ok`:

```typescript
result.match({
  err: (error) => {
    showError({ message: error.message, title: 'エラー' })
  },
  ok: (data) => {
    showSuccess({ message: '作成しました' })
    onSuccess(data)
  },
})
```

### MSW mock placement

```
src/features/<feature>/mocks/handlers.ts
```

Handlers are registered in `src/lib/msw/server.ts` for Vitest tests.

---

## Session Resume

If the session was interrupted mid-task, re-run:

```
/sdd-impl <slug>
```

The skill reads `progress.md`, finds any task marked `in-progress`, and resumes from the appropriate TDD phase. If no `in-progress` task exists, it picks the next `pending` task.

---

## Output Files Modified

| File                               | Change                             |
| ---------------------------------- | ---------------------------------- |
| `.claude/specs/<slug>/progress.md` | Task statuses updated              |
| `src/features/<feature>/...`       | New/modified source and test files |
| `git history`                      | One commit per completed task      |

---

## Approval Gate

After all specified tasks complete (or a single task if `[task-id]` was given):

```
== PHASE COMPLETE: sdd-impl ==
Artifact: .claude/specs/<slug>/progress.md
Summary:
- Implemented TASK-001 through TASK-003 (3 tasks)
- All tests pass (pnpm test:run green)
- pnpm check passes (lint + format + tsc)
- Commits: feat(TASK-001), feat(TASK-002), feat(TASK-003)
- Remaining pending tasks: TASK-004 through TASK-012

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-review` to proceed to code review, or describe changes needed.
```
