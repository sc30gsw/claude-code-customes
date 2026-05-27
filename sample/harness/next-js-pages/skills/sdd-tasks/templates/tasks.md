# Tasks: <!-- Feature Name -->

> **Spec slug**: <!-- slug -->
> **Generated**: <!-- YYYY-MM-DD -->
> **Total tasks**: <!-- N -->

---

### TASK-001 — Valibot schema and derived types

Implements: REQ-001, REQ-002
Design ref: §4 State Management, §5 API Layer
Type: feat
Estimated complexity: S
Files to modify:

- src/features/<feature>/schemas/<feature>-schema.ts (create)
- src/features/<feature>/types/<feature>.ts (create)
  Acceptance: Schema rejects invalid inputs and `InferOutput` type matches API contract

---

### TASK-002 — API mutations layer

Implements: REQ-003
Design ref: §5 API Layer, §5.1 Mutation Pattern
Type: feat
Estimated complexity: S
Files to modify:

- src/features/<feature>/api/mutations.ts (create)
  Acceptance: All mutations return `Result<T, ApiError>`; keys in alphabetical order (`catch` before `try`)

---

### TASK-003 — Integration tests for mutation hook

Implements: REQ-003
Design ref: §8 Test Strategy
Type: test
Estimated complexity: M
Files to modify:

- src/features/<feature>/mocks/handlers.ts (create)
- src/features/<feature>/hooks/use-<feature>-actions.test.ts (create)
- src/lib/msw/server.ts (modify)
  Acceptance: Success path and API error path both tested; queries use `getByRole`/`getByText` only

---

_Template: `.claude/skills/sdd-tasks/templates/tasks.md`_
