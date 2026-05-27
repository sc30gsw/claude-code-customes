# sdd-design

**Slash command**: `/sdd-design <slug>`
**Purpose**: Create `design.md` by delegating to the `/ecc:plan` skill for architecture and step planning, then merging output into the project's design template.

---

## Prerequisites

- `.claude/specs/<slug>/requirements.md` must exist (run `/sdd-requirements` first)
- `.claude/specs/<slug>/source-notion.md` may optionally be present for additional context

---

## Steps

### 1. Read spec inputs

```
.claude/specs/<slug>/requirements.md      (required)
.claude/specs/<slug>/source-notion.md     (optional)
```

Extract:

- All REQ-XXX IDs and their acceptance criteria
- Non-functional requirements (performance, security, accessibility)
- Scope boundaries (in-scope / out-of-scope)

### 2. Invoke `/ecc:plan`

Call the `/ecc:plan` skill with the feature context derived from requirements.md.

Prompt framing for `/ecc:plan`:

```
Feature: <feature name from requirements.md>
Context: Next.js 16 / React 19 / TypeScript frontend.
  - UI: Mantine 9 + Tailwind CSS
  - Server state: SWR via useAspidaSWR
  - Client state: Jotai atoms
  - URL state: nuqs
  - API client: aspida + up-fetch wrapped in features/*/api/
  - Validation: Valibot schemas in features/*/schemas/
  - Testing: Vitest + MSW (integration-first), Playwright (E2E)
  - Linting: oxlint (no interface, no relative imports, no default export outside pages/)

Requirements summary:
<paste REQ list>

Produce: architecture decisions, file structure, component hierarchy, state management plan, API integration plan, test strategy.
```

**`--mode standard`**: Present the `/ecc:plan` output to the user. Allow the user to review, comment, and guide design interactively before proceeding. Incorporate feedback before scaffolding.

**`--mode auto`**: Run `/ecc:plan` autonomously. Produce `design.md` directly, then append a plain-language "Auto-Design Summary" section at the top of the file for non-engineer reviewers to confirm before implementation starts.

### 3. Scaffold `design.md` from template

Copy the template at `.claude/skills/sdd-design/templates/design.md` to:

```
.claude/specs/<slug>/design.md
```

### 4. Merge `/ecc:plan` output into design sections

Fill every section of the template using the `/ecc:plan` output and your own analysis:

| Template section        | Source                                                          |
| ----------------------- | --------------------------------------------------------------- |
| Overview                | requirements.md § Scope + /ecc:plan summary                         |
| Architecture diagram    | /ecc:plan architecture decisions → Mermaid                          |
| File Structure Plan     | /ecc:plan file list → mapped to features/ layout                    |
| State Management        | /ecc:plan decisions → cross-checked with state responsibility table |
| API layer               | /ecc:plan API plan → aspida endpoint patterns                       |
| Component hierarchy     | /ecc:plan component breakdown → Mermaid diagram                     |
| Error handling strategy | /ecc:plan error handling + better-result patterns                   |
| Test strategy           | /ecc:plan test plan → cross-checked with Testing Trophy targets     |

### 5. Add traceability links

Every section must end with:

```
Satisfies: REQ-XXX, REQ-YYY
```

If a section satisfies no requirements directly, write:

```
Satisfies: <!-- cross-cutting concern, no direct REQ -->
```

---

## State Management Reference

Use the following table from `.claude/rules/web/swr-jotai.md` when making state decisions:

| State type   | Tool               | Location                                |
| ------------ | ------------------ | --------------------------------------- |
| Server state | SWR (useAspidaSWR) | `features/*/hooks/use-*.ts`             |
| Client state | Jotai              | `features/*/stores/*.ts`                |
| URL state    | nuqs               | `features/*/hooks/use-*-query-state.ts` |
| Form state   | @mantine/form      | `features/*/components/*-form.tsx`      |

**Do not duplicate server state in Jotai.**

---

## API Layer Reference

Endpoint calls follow the aspida pattern from `.claude/rules/web/api-client-aspida.md`:

```typescript
// GET /api/v1/resource
apiClient.api.v1.resource.$get({ query: { page: 1 } })

// POST /api/v1/resource
apiClient.api.v1.resource.$post({ body: { resource: {...} } })

// DELETE /api/v1/resource/:id
apiClient.api.v1.resource._id(id).$delete()
```

Mutations must be wrapped in `Result.tryPromise` with `catch: toApiError` (alphabetical key order).

---

## Output

```
.claude/specs/<slug>/design.md
```

---

## Phase Gate

**Next skill after design is always `sdd-tasks`, never `sdd-review-plan`.**  
`sdd-review-plan` requires `tasks.md` and runs only after `/sdd-tasks`.

Use the same gate for the initial write and for any later revision to `design.md`.

### Initial completion

Append to `.claude/specs/<slug>/change-log.md`:

```
| <YYYY-MM-DD> | sdd-design | design.md 作成 |
```

```
== PHASE COMPLETE: sdd-design ==
Artifact: .claude/specs/<slug>/design.md
Summary:
- Architecture decisions recorded with Mermaid diagrams
- File structure mapped to features/ layout
- State management decisions documented per SWR/Jotai/nuqs table
- API layer patterns specified using aspida conventions
- All sections include Satisfies: REQ-XXX traceability links

⏸ WAITING FOR CONFIRMATION
Next: CONFIRM sdd-tasks   (run /sdd-tasks <slug> — task breakdown)
Or: describe further design changes
```

### After user-requested revisions

Append to `.claude/specs/<slug>/change-log.md`:

```
| <YYYY-MM-DD> | sdd-design | design.md 更新 (<list changed sections>) |
```

When the user asks to change sections of an existing `design.md` (do not treat this as plan review):

```
== DESIGN REVISED ==
Artifact: .claude/specs/<slug>/design.md（更新箇所: <list sections>）
Summary:
- <bullet: what changed and why>

⏸ WAITING FOR CONFIRMATION
Next (recommended): CONFIRM sdd-tasks   → /sdd-tasks <slug>
  - Required if tasks.md is still empty or predates this revision
  - Re-run tasks when file structure / API / component plan changed materially
Optional: CONFIRM sdd-review-plan   → only after tasks.md exists AND user wants plan review without regenerating tasks
Or: describe further design changes

Do NOT recommend CONFIRM sdd-review-plan as the default next step after design-only work.
```

### If `tasks.md` already exists

If design changed materially and `tasks.md` was generated from the old design:

1. Tell the user tasks may be stale.
2. Recommend `CONFIRM sdd-tasks` to regenerate (or `/sdd-tasks <slug>` after confirm).
3. Only after an up-to-date `tasks.md` exists, `CONFIRM sdd-review-plan` is valid.
