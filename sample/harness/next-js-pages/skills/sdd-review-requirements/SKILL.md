# Skill: sdd-review-requirements

## Invocation

```
/sdd-review-requirements <slug>
```

**Arguments:**

- `<slug>` — kebab-case feature identifier matching an existing `.claude/specs/<slug>/` directory

---

## Purpose

Review `requirements.md` for completeness, clarity, EARS compliance, ambiguity, and missing edge cases. Appends a structured "Requirements Review" section to `.claude/specs/<slug>/review.md`. The mode is read from `progress.md` and determines which agents are invoked and which checks are run.

---

## Execution Steps

### Step 1: Read mode and validate prerequisites

Read `.claude/specs/<slug>/progress.md`:

- Extract `**Mode**:` value (`standard` or `auto`).
- Check that `sdd-requirements` phase is marked `✅ complete`. If not, abort and instruct the user to run `/sdd-requirements <slug>` first.
- If `progress.md` does not exist, abort and instruct the user to run `/sdd-init <slug>` first.

### Step 2: Load requirements.md

Read `.claude/specs/<slug>/requirements.md` in full.

- If the file contains only the placeholder comment (`<!-- Artifact not yet generated... -->`), abort and instruct the user to run `/sdd-requirements <slug>` first.
- Count the number of REQ blocks for the review summary.

### Step 3: Mode-specific review execution

#### Standard Mode

Invoke the following in sequence:

1. **`requirements-analyst` agent** (primary)
   - Focus: EARS compliance, acceptance criteria quality, stakeholder roles, ambiguity detection.
   - Prompt: "Review the following requirements.md for EARS format compliance, ambiguous terms, missing acceptance criteria, and untestable criteria. Return a structured list of findings with REQ ID, issue description, severity, and suggested correction."

2. **`Plan` agent** (secondary)
   - Focus: Scope boundaries, dependency risks, missing scenarios, implementation sequencing concerns.
   - Prompt: "Review the following requirements for missing edge cases, scope gaps, inter-requirement conflicts, and sequencing risks. Return findings with REQ ID and impact."

3. **Project `spec-tech-research` skill** (technical feasibility)
   - Focus: Validate that each REQ is feasible given the project stack (Next.js, TypeScript, Mantine, SWR, Jotai, MSW, Vitest, aspida, Valibot).
   - Flag any REQ whose acceptance criteria would require capabilities not supported by the stack, or would require significant architectural changes.

Merge all findings into a unified table.

#### Auto Mode

Invoke only:

1. **`requirements-analyst` agent**
   - Focus: Business clarity, acceptance criteria completeness, stakeholder roles, ambiguity, risks.
   - Do NOT run `planner` or `spec-tech-research`.
   - Prioritize findings that a non-engineer product owner can act on directly.

---

## Checks Performed

Run all checks below regardless of mode. Flag each finding with the REQ ID and severity.

### Check 1: EARS Format Compliance

- Each REQ block must contain: a User Story, a `When ... the system shall ...` clause, and at least 2 Acceptance Criteria.
- Missing any element → **HIGH**
- Using EARS keywords incorrectly (e.g. "Where" used instead of "When" for event-driven behavior) → **MEDIUM**

### Check 2: Ambiguous Terms

Scan all requirement text for vague qualifiers. Flag occurrences as **MEDIUM**:

- Adjectives: "fast", "slow", "easy", "simple", "appropriate", "reasonable", "sufficient"
- Quantities: "some", "many", "few", "several", "various", "etc.", "and so on"
- Time: "soon", "quickly", "immediately" (unless a specific duration is given)
- Replace suggestion: "Replace with a measurable criterion (e.g. 'within 2 seconds', 'up to 100 items')."

### Check 3: Missing Elements

- Missing actor (role) in User Story → **HIGH**
- Missing triggering event (When clause) → **HIGH**
- Missing system response (shall clause) → **HIGH**
- Requirement describes implementation, not behavior (e.g. "the database will store...") → **MEDIUM**

### Check 4: Testability

- Each Acceptance Criterion must be binary (pass/fail) and observable without access to internals.
- Subjective criteria ("looks good", "feels intuitive") → **HIGH**
- Criteria requiring knowledge of internal state not exposed to users → **MEDIUM**

### Check 5: Completeness

- No obvious error paths covered (e.g. what happens when an API call fails) → **MEDIUM**
- No empty state handling (e.g. what the user sees when the list is empty) → **MEDIUM**
- No permission / role boundary specified when the feature involves restricted access → **HIGH**
- No pagination or data limit stated for list-type features → **LOW**

### Check 6: REQ ID Numbering

- IDs must be sequential with no gaps → **LOW**
- Duplicate IDs → **HIGH**

### Check 7: Technical Feasibility (Standard mode only)

- REQ requiring a non-existent API endpoint → **HIGH**
- REQ assuming real-time behavior (WebSocket/SSE) not currently in the stack → **MEDIUM**
- REQ whose acceptance criteria would require bypassing Valibot schema validation → **MEDIUM**

---

## Output Format

Append the following section to `.claude/specs/<slug>/review.md` under a dated heading.

If `review.md` does not yet exist, create it with this content only.

```markdown
## Requirements Review (<YYYY-MM-DD>)

**Reviewer**: sdd-review-requirements skill
**Mode**: <standard|auto>
**Requirements reviewed**: <N> REQs (REQ-001 through REQ-NNN)

### Overall Assessment

<!-- 2-4 sentences: Is this requirements doc ready to proceed? What is the most critical concern? -->

### Findings

| REQ     | Issue               | Severity | Suggestion          |
| ------- | ------------------- | -------- | ------------------- |
| REQ-001 | <issue description> | HIGH     | <corrective action> |
| REQ-002 | <issue description> | MEDIUM   | <corrective action> |
| REQ-003 | <issue description> | LOW      | <corrective action> |

_Severity: HIGH = blocks implementation, MEDIUM = should fix before design, LOW = consider before PR_

### Recommended Actions Before Proceeding

- [ ] **HIGH**: <action 1>
- [ ] **HIGH**: <action 2>
- [ ] **MEDIUM**: <action 3>

### Sign-off Condition

All HIGH severity findings must be resolved before running `/sdd-design <slug>`.
```

---

## progress.md Updates

After writing the review:

- Change `sdd-review-requirements` status from `⬜ not started` to `✅ complete`.
- Add a row to the Change Log: `| <YYYY-MM-DD> | review-requirements | N findings (X HIGH, Y MEDIUM, Z LOW) |`

---

## Notes

- Do not modify `requirements.md`. This skill is read-only with respect to requirements. The user must update requirements separately and rerun this skill if needed.
- If all checks pass with zero HIGH severity findings, state this clearly in the Overall Assessment section. The user may still choose to proceed immediately.
- In `--mode auto`, present findings in plain language without jargon. Label each finding with its business impact rather than technical category (e.g. "Users won't know what to do if the upload fails" instead of "Missing error path for REQ-003").
- If `review.md` already has a Requirements Review section, append the new dated section below the existing one. Do not overwrite prior reviews.

---

== PHASE COMPLETE: sdd-review-requirements ==
Artifact: .claude/specs/<slug>/review.md
Summary:

- Mode read from progress.md
- requirements.md loaded and analyzed (N REQs)
- Checks run: EARS compliance, ambiguity, missing elements, testability, completeness, numbering, technical feasibility (standard only)
- Agents invoked: requirements-analyst (both modes), planner + spec-tech-research (standard only)
- Findings written to review.md under dated heading
- progress.md updated: sdd-review-requirements → complete

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-design` to proceed. Or describe changes needed.
