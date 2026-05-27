# sdd-review-plan

**Slash command**: `/sdd-review-plan <slug>`
**Purpose**: Comprehensive pre-implementation review of requirements, design, and tasks. Appends "Traceability Coherence" and "Plan Review" sections to `review.md`.

---

## Prerequisites

- `.claude/specs/<slug>/requirements.md` must exist
- `.claude/specs/<slug>/design.md` must exist
- `.claude/specs/<slug>/tasks.md` must exist
- `.claude/specs/<slug>/progress.md` must exist (used to read `mode`)

---

## Steps

### 1. Read all spec inputs

```
.claude/specs/<slug>/requirements.md
.claude/specs/<slug>/design.md
.claude/specs/<slug>/tasks.md
.claude/specs/<slug>/progress.md    (read mode: standard | auto)
```

Build three indexes in memory:

- **REQ index**: all `REQ-XXX` IDs found in requirements.md
- **Design section index**: all `§X.X <title>` headings found in design.md
- **TASK index**: all `TASK-XXX` IDs found in tasks.md

### 2. Run traceability coherence check (BOTH modes)

Run all six checks below. For each check, record either ✅ (pass) or ❌ (fail) with specific IDs.

#### Check A — REQ → Design coverage

Every REQ-XXX in the REQ index appears in at least one `Satisfies:` line in design.md.

Failure example:

```
❌ REQ-004 has no Satisfies: line in design.md
   Fix: add "Satisfies: REQ-004" to the relevant design section
```

#### Check B — REQ → Task coverage

Every REQ-XXX in the REQ index appears in at least one `Implements:` line in tasks.md.

Failure example:

```
❌ REQ-006 has no Implements: entry in tasks.md
   Fix: add REQ-006 to an existing task's Implements field, or create TASK-NNN
```

#### Check C — Design → Task coverage

Every design section §X.X in the design section index appears in at least one `Design ref:` line in tasks.md.

Failure example:

```
❌ §7 Error Handling Strategy has no Design ref: entry in tasks.md
   Fix: add "Design ref: §7 Error Handling Strategy" to the relevant task
```

#### Check D — Task → REQ completeness

Every TASK-XXX in tasks.md has at least one `Implements:` entry (not empty).

Failure example:

```
❌ TASK-005 has no Implements: field
   Fix: add "Implements: REQ-XXX" to TASK-005
```

#### Check E — Dangling references

All REQ-XXX IDs referenced in `Satisfies:` or `Implements:` fields actually exist in the REQ index.
All §X.X references in `Design ref:` fields actually exist in the design section index.

Failure example:

```
❌ tasks.md TASK-003 references "Design ref: §9 Deployment" but §9 does not exist in design.md
   Fix: correct the section reference or add §9 to design.md
```

#### Check F — Duplicate IDs

No repeated REQ-XXX IDs in requirements.md.
No repeated TASK-XXX IDs in tasks.md.

Failure example:

```
❌ TASK-002 appears twice in tasks.md
   Fix: renumber the second occurrence
```

### 3. Write Traceability Coherence table to `review.md`

Append to `.claude/specs/<slug>/review.md` under the heading:

```markdown
## Traceability Coherence (YYYY-MM-DD)

| Check            | Result  | Details                               |
| ---------------- | ------- | ------------------------------------- |
| A: REQ → Design  | ✅ / ❌ | <!-- IDs or "all covered" -->         |
| B: REQ → Task    | ✅ / ❌ | <!-- IDs or "all covered" -->         |
| C: Design → Task | ✅ / ❌ | <!-- sections or "all covered" -->    |
| D: Task → REQ    | ✅ / ❌ | <!-- IDs or "all have Implements" --> |
| E: Dangling refs | ✅ / ❌ | <!-- broken refs or "none" -->        |
| F: Duplicate IDs | ✅ / ❌ | <!-- duplicates or "none" -->         |
```

### 4. CRITICAL gate — stop on any traceability failure

If ANY check is ❌, output the following and STOP. Do NOT output the PHASE COMPLETE gate.

```
⚠️ TRACEABILITY ERRORS FOUND — cannot proceed to implementation

The following issues must be fixed in the spec files before proceeding:

[list each ❌ with the specific IDs and how to fix]

Fix the issues listed above, then re-run /sdd-review-plan <slug>.
```

Only continue to Step 5 if ALL six checks are ✅.

### 5. Mode-specific plan review

**`--mode standard`**:

1. Invoke `Plan` agent with the full requirements + design + tasks context
2. Invoke `ecc:architect` agent with the same context
3. Invoke the `spec-tech-research` skill for the technology stack used in design.md
4. Collect all findings

**`--mode auto`**:

1. Invoke `ecc:architect` agent only (skip Plan agent and spec-tech-research)
2. Collect findings

### 6. Append Plan Review to `review.md`

Append under:

```markdown
## Plan Review (YYYY-MM-DD)

### Reviewer: Plan agent (standard mode only)

<!-- findings -->

### Reviewer: architect agent

<!-- findings -->

### Reviewer: spec-tech-research (standard mode only)

<!-- findings -->

### Summary

<!-- 3-5 bullet points: key risks, open questions, recommendations -->
```

---

## Output

```
.claude/specs/<slug>/review.md    (appended, not overwritten)
```

---

## Phase Gate

Only output this block when ALL six traceability checks are ✅ AND plan review is complete:

```
== PHASE COMPLETE: sdd-review-plan ==
Artifact: .claude/specs/<slug>/review.md
Summary:
- All 6 traceability coherence checks passed (A-F)
- Plan reviewed by architect agent (+ planner + spec-tech-research in standard mode)
- Key risks and open questions documented in review.md
- Spec is ready for implementation
- Run /sdd-impl <slug> TASK-001 to begin

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-impl` to proceed with implementation, or describe changes needed.
```
