# sdd-review — Post-Implementation Code Review

## Slash Command

```
/sdd-review <slug>
```

## Purpose

Run code review and security review on all changes introduced by the feature branch. Append structured findings to `review.md`. Does NOT auto-apply fixes — only proposes them.

---

## Prerequisites

- `sdd-impl` has completed: all tasks in `progress.md` are `done` (or at least one is `done`; partial reviews are allowed).
- The feature branch must have at least one commit ahead of `main`.

---

## Input Files

| File                                   | Purpose                                               |
| -------------------------------------- | ----------------------------------------------------- |
| `.claude/specs/<slug>/requirements.md` | Acceptance criteria to compare against implementation |
| `.claude/specs/<slug>/tasks.md`        | Task scope (which files were changed)                 |
| `.claude/specs/<slug>/progress.md`     | Task completion status and mode setting               |
| `.claude/specs/<slug>/review.md`       | Append-only — existing content is preserved           |

---

## Mode Behavior

Both `standard` and `auto` modes run the same two reviews. The mode difference is in how findings are presented:

| Aspect                   | `standard` (engineer-led)                      | `auto` (AI-led)                                    |
| ------------------------ | ---------------------------------------------- | -------------------------------------------------- |
| CRITICAL / HIGH findings | Listed in `review.md`, engineer decides action | Auto-fix proposals generated inline in `review.md` |
| MEDIUM / LOW findings    | Listed, engineer decides                       | Listed, no auto-proposals                          |
| Fix application          | Never auto-applied                             | Never auto-applied                                 |

---

## Steps

### 1. Get the Feature Diff

```bash
git diff main...HEAD
git log main...HEAD --oneline
```

If the project uses a different base branch (e.g., `develop`), use that. The base branch defaults to `main` unless `progress.md` specifies otherwise.

Both the diff and the log serve as input for both review steps.

### 2. Code Review (Step 1)

Invoke Claude Code's native `code-review` skill with `--effort high`.

Focus areas for this project:

| Area           | What to check                                                                   |
| -------------- | ------------------------------------------------------------------------------- |
| Correctness    | Logic matches acceptance criteria in `requirements.md`                          |
| Type safety    | No `any`, Utility Types used correctly (`Pick`, `Omit`, `Record`)               |
| Error handling | `better-result` used; `.match({err, ok})` with `err` before `ok` (alphabetical) |
| API layer      | `Result.tryPromise` with `catch` before `try` (alphabetical)                    |
| Import paths   | `~/` alias everywhere — no relative imports                                     |
| Exports        | No `export default` outside `src/pages/` and `*.config.*`                       |
| Test coverage  | Tests co-located with source; `getByRole` used; no `getByTestId`                |
| Immutability   | No direct object mutation                                                       |
| Comments       | Non-obvious logic has Japanese comments explaining WHY, not WHAT                |
| File size      | Source files under 800 lines; ideally 200–400 lines                             |
| Console logs   | No `console.log` present                                                        |
| Memoization    | No `useMemo` / `useCallback` added unnecessarily                                |
| Mantine usage  | Mantine props used before Tailwind; `cn()` only for layout wrappers             |

### 3. Security Review (Step 2)

Invoke the `/ecc:security-review` skill.

Focus areas:

| Area                  | What to check                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Secrets               | No hardcoded API keys, tokens, or passwords                                              |
| Input validation      | User input validated with Valibot at system boundaries                                   |
| Authentication        | Auth headers handled only in `src/lib/api-client.ts`                                     |
| XSS                   | No `dangerouslySetInnerHTML` without sanitization                                        |
| Sensitive data        | No PII/credentials in error messages, URLs, or logs                                      |
| Environment variables | Sensitive values use `import.meta.env.VITE_*` or `process.env.*`; fail fast if undefined |

### 4. Append to `review.md`

Append two new sections to `.claude/specs/<slug>/review.md`. Preserve all existing content above.

```markdown
## Code Review (YYYY-MM-DD)

> Scope: git diff main...HEAD — N files changed

### CRITICAL

- [ ] [FILE:LINE] Description of critical issue

### HIGH

- [ ] [FILE:LINE] Description of high-priority issue

### MEDIUM

- [ ] [FILE:LINE] Description of medium-priority issue

### LOW

- [ ] [FILE:LINE] Description of low-priority issue

### Passed Checks

- Type safety: all props use Utility Types correctly
- Import paths: ~/ alias used throughout
- (other passing items)

---

## Security Review (YYYY-MM-DD)

> Scope: git diff main...HEAD

### CRITICAL

(none)

### HIGH

- [ ] [FILE:LINE] Description of security issue

### MEDIUM

- [ ] [FILE:LINE] Description of security issue

### LOW

(none)

### Passed Checks

- No hardcoded secrets found
- Input validation present at API boundaries
- (other passing items)
```

Use `YYYY-MM-DD` format for the date (e.g., `2026-05-26`).

### 5. Auto-Fix Proposals (`auto` mode only)

For each CRITICAL or HIGH finding, append a proposal block immediately after the finding item:

````markdown
- [ ] [src/features/foo/api/mutations.ts:42] Using try/catch instead of better-result

  **Proposed fix:**

  ```typescript
  // Before
  try {
    const res = await apiClient.api.v1.foos.$post({ body: params })
    return res
  } catch (err) {
    throw err
  }

  // After
  return Result.tryPromise({
    catch: toApiError,
    try: async () => {
      return await apiClient.api.v1.foos.$post({ body: params })
    },
  })
  ```
````

```

Do NOT apply the fix. The engineer applies it manually or addresses it before running `sdd-pr`.

---

## Output Files Modified

| File | Change |
|---|---|
| `.claude/specs/<slug>/review.md` | Two sections appended: `## Code Review` + `## Security Review` |

No source files are modified by this skill.

---

## Approval Gate

```

== PHASE COMPLETE: sdd-review ==
Artifact: .claude/specs/<slug>/review.md
Summary:

- Code review complete: 0 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW
- Security review complete: 0 CRITICAL, 1 HIGH, 0 MEDIUM
- Total open issues requiring action: 3 HIGH
- Auto-fix proposals generated for all HIGH findings (auto mode only)
- No source files were modified

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-pr` to proceed to PR creation, or describe changes needed.

```

> **Warning**: If any CRITICAL findings remain unresolved, the gate message will prominently flag this. Proceeding to `sdd-pr` with open CRITICAL issues is strongly discouraged — resolve them first and re-run `/sdd-review <slug>`.
```
