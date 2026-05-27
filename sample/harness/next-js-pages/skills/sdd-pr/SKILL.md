# sdd-pr — Create Pull Request

## Slash Command

```
/sdd-pr <slug>
```

## Purpose

Create a GitHub Pull Request enriched with SDD-specific content: a REQ → TASK → commit traceability table, review summary, and an acceptance-criteria-derived test plan checklist. Delegates the actual PR creation to the project's `git-pr` skill.

---

## Prerequisites

- `sdd-review` has been run: `review.md` must contain a `## Code Review` section.
- The feature branch must be pushed to the remote.
- No unresolved CRITICAL findings in `review.md` (see Warning below).

---

## Input Files

| File                                   | Purpose                                   |
| -------------------------------------- | ----------------------------------------- |
| `.claude/specs/<slug>/requirements.md` | REQ definitions and acceptance criteria   |
| `.claude/specs/<slug>/tasks.md`        | TASK definitions with REQ references      |
| `.claude/specs/<slug>/design.md`       | Architecture summary for PR context       |
| `.claude/specs/<slug>/progress.md`     | Task completion status and mode setting   |
| `.claude/specs/<slug>/review.md`       | Review findings to surface in the PR body |

---

## Mode Behavior

Both `standard` and `auto` modes produce the same PR content.

| Aspect                   | `standard`                             | `auto`                                |
| ------------------------ | -------------------------------------- | ------------------------------------- |
| Before creating PR       | Show draft PR body, wait for `CONFIRM` | Create PR immediately                 |
| If CRITICAL issues exist | Stop and require user decision         | Stop and require user decision (same) |

---

## Steps

### 1. Pre-flight: Check for CRITICAL Issues

Read `.claude/specs/<slug>/review.md`. Search for unchecked CRITICAL findings:

```markdown
### CRITICAL

- [ ] ... ← unchecked = still open
- [x] ... ← checked = resolved
```

If any unchecked CRITICAL findings exist under either `## Code Review` or `## Security Review`, output:

```
WARNING: Open CRITICAL issues found in review.md:
  - [src/features/foo/api/mutations.ts:42] Description of issue

Resolve all CRITICAL issues before creating the PR.
After fixing, re-run /sdd-review <slug> to update review.md.
```

Stop. Do not proceed until the user explicitly confirms they want to continue (exceptional case only, e.g., known false positive).

### 2. Build the Traceability Table

Collect commits on the feature branch that reference task IDs:

```bash
git log main...HEAD --oneline --grep="TASK-"
```

Parse each `### TASK-xxx` block in `tasks.md` for its linked REQ ID (look for `REQ-xxx` references in the task description or metadata).

Build the table:

```markdown
| REQ        | Description                         | Tasks              | Key Commits                              |
| ---------- | ----------------------------------- | ------------------ | ---------------------------------------- |
| REQ-001    | User can log in with email/password | TASK-001, TASK-002 | feat(TASK-001): Create login schema      |
| REQ-002    | Show validation errors inline       | TASK-003           | feat(TASK-003): Add inline error display |
| (Untraced) | —                                   | TASK-012           | feat(TASK-012): Fix loading state        |
```

Tasks with no REQ reference appear in an `(Untraced)` row at the bottom.

### 3. Build the Test Plan Checklist

Extract acceptance criteria from `requirements.md`. Each `### REQ-xxx` section typically contains an "Acceptance Criteria" or "AC" subsection. Convert each criterion into a checklist item:

```markdown
## Test Plan

- [ ] REQ-001: Login with valid credentials redirects to dashboard
- [ ] REQ-001: Login with wrong password shows "メールアドレスまたはパスワードが正しくありません"
- [ ] REQ-002: Empty email field shows inline validation error before submit
- [ ] REQ-002: Invalid email format triggers Valibot error message
- [ ] Regression: pnpm test:run passes (all existing tests green)
- [ ] Build: pnpm check passes (lint + format + tsc)
```

### 4. Build the PR Body Sections

**Review summary** — extract from `review.md`:

```markdown
## Review Summary

| Severity | Code Review | Security Review |
| -------- | ----------- | --------------- |
| CRITICAL | 0 open      | 0 open          |
| HIGH     | 2 open      | 1 open          |
| MEDIUM   | 3 open      | 0 open          |

> Outstanding HIGH issues (must resolve before merge):
>
> - [src/features/foo/components/foo-form.tsx:15] Using relative import path
> - [src/lib/api-client.ts:88] Missing input validation at boundary
```

Count open (unchecked `- [ ]`) vs resolved (checked `- [x]`) findings per severity.

**Spec reference** — link to all spec documents:

```markdown
## Spec Reference

| Document                | Path                                    |
| ----------------------- | --------------------------------------- |
| Source (Notion archive) | `.claude/specs/<slug>/source-notion.md` |
| Requirements            | `.claude/specs/<slug>/requirements.md`  |
| Design                  | `.claude/specs/<slug>/design.md`        |
| Tasks                   | `.claude/specs/<slug>/tasks.md`         |
| Review                  | `.claude/specs/<slug>/review.md`        |
| Progress                | `.claude/specs/<slug>/progress.md`      |
```

### 5. Invoke `git-pr` Skill

Pass the additional SDD context to the project's `git-pr` skill. The `git-pr` skill handles `git push -u origin <branch>` (if not yet pushed) and `gh pr create`.

The full PR body structure:

```markdown
## Summary

<3-5 bullet points from git-pr — what changed and why>

## Spec Reference

<built in Step 4>

## Traceability

<built in Step 2>

## Review Summary

<built in Step 4>

## Test Plan

<built in Step 3>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

If the `git-pr` skill is unavailable, fall back to running `gh pr create` directly:

```bash
gh pr create --title "<feature title>" --body "$(cat <<'EOF'
## Summary
...
EOF
)"
```

### 6. Record the PR URL

After the PR is created, append to `.claude/specs/<slug>/progress.md`:

```markdown
## PR

- URL: https://github.com/enechange/e_value_management_frontend/pull/42
- Created: 2026-05-26
- Status: open
```

Date format: `YYYY-MM-DD`. This entry allows `sdd-workflow` to detect that the PR phase is complete.

---

## Notes

- Notion status update is out of scope — update the Notion card manually after the PR is reviewed and merged.
- The PR body intentionally surfaces open HIGH issues so reviewers are aware; this does not block PR creation.
- Only CRITICAL open issues block PR creation.

---

## Output Files Modified

| File                               | Change                                          |
| ---------------------------------- | ----------------------------------------------- |
| `.claude/specs/<slug>/progress.md` | `## PR` section appended with URL, date, status |
| GitHub                             | New PR created                                  |

---

## Approval Gate

```
== PHASE COMPLETE: sdd-pr ==
Artifact: .claude/specs/<slug>/progress.md
Summary:
- PR created: https://github.com/enechange/e_value_management_frontend/pull/42
- Traceability table: 3 REQs traced across 12 TASKs and 12 commits
- Test plan: 8 checklist items derived from acceptance criteria
- Review summary: 0 CRITICAL, 3 HIGH open (surfaced in PR body for reviewers)
- PR URL recorded in progress.md

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-workflow` to view final workflow status, or describe changes needed.
```
