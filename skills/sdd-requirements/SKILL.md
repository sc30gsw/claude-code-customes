# Skill: sdd-requirements

## Invocation

```
/sdd-requirements <slug>
```

**Arguments:**

- `<slug>` — kebab-case feature identifier matching an existing `.claude/specs/<slug>/` directory

---

## Purpose

Create or refine `requirements.md` for the feature using the EARS (Event-Action-Response-Stimulus) format. The mode is read from `.claude/specs/<slug>/progress.md` and determines how the AI interacts with the user.

---

## Execution Steps

### Step 1: Read mode from progress.md

Read `.claude/specs/<slug>/progress.md` and extract the `**Mode**:` value.

- If `standard` → follow the Standard Mode flow below.
- If `auto` → follow the Auto Mode flow below.
- If `progress.md` does not exist, abort and instruct the user to run `/sdd-init <slug>` first.

### Step 2: Load source material (if available)

If `.claude/specs/<slug>/source-notion.md` exists, read it as background context. Do NOT output it; use it to inform questions and drafts.

### Step 3: Mode-specific execution

#### Standard Mode

Engineer-led. The AI presents a scaffold and assists completions.

1. Copy the template from `.claude/skills/sdd-requirements/templates/requirements.md` to `.claude/specs/<slug>/requirements.md` (do not overwrite if requirements.md already has real content — ask first).
2. Display the scaffold to the user.
3. Offer to help fill in individual REQ blocks:
   - "Tell me about the first user story and I'll draft the EARS format for you."
   - Suggest missing actors, triggers, or acceptance criteria.
4. After user provides input, write the refined content to `requirements.md`.
5. Validate EARS compliance and flag issues inline (see Checks section).

#### Auto Mode

AI-led. The AI asks Socratic questions, then constructs requirements autonomously.

Ask the following questions one at a time (wait for each answer before proceeding):

1. "What problem does this feature solve? Who experiences it?"
2. "Who are the main users of this feature? List their roles."
3. "What are the 3-5 most important things a user needs to be able to do?"
4. "What should the system do when each of those things happens?"
5. "What would make this feature obviously broken or incomplete?"
6. "Are there any constraints — time limits, data limits, permission rules?"
7. "What should NOT happen? Are there edge cases to guard against?"

After collecting answers:

- Synthesize them into EARS-format requirements.
- Write the full `requirements.md` without further prompting.
- State each decision made and its rationale.
- Do not ask for approval before writing — write, then present the result.

---

## EARS Format Reference

Each requirement block follows this structure:

```markdown
## REQ-001: <Short Title>

**User Story**: As a <role>, I want <goal> so that <benefit>.

**When** <triggering event or condition>, **the system shall** <observable system response>.

**Acceptance Criteria**:

- [ ] <Verifiable criterion 1>
- [ ] <Verifiable criterion 2>
- [ ] <Verifiable criterion 3>
```

**EARS keyword guide:**

- `When <event>, the system shall <response>` — event-driven behavior
- `While <condition>, the system shall <response>` — state-driven behavior
- `The system shall <response>` — unconditional behavior
- `If <condition>, then the system shall <response>` — optional/conditional feature
- `Where <feature included>, the system shall <response>` — feature-dependent behavior

---

## Validation Checks (applied after writing)

Run these checks on the completed `requirements.md` and flag issues as inline comments or a summary list:

1. **EARS compliance**: Each REQ has a When/shall clause and at least 2 acceptance criteria.
2. **Ambiguous terms**: Flag words like "fast", "easy", "some", "appropriate", "etc.", "various".
3. **Missing elements**: Each REQ must have an actor (role), trigger, and system response.
4. **Testability**: Each acceptance criterion must be binary (pass/fail), not subjective.
5. **Numbering**: REQ IDs must be sequential with no gaps (REQ-001, REQ-002, ...).

---

## Output

Write the completed requirements to `.claude/specs/<slug>/requirements.md`.

Update `.claude/specs/<slug>/progress.md`:

- Change `sdd-requirements` status from `⬜ not started` to `✅ complete`.

Append to `.claude/specs/<slug>/change-log.md`:

```
| <YYYY-MM-DD> | sdd-requirements | requirements.md 作成 (<N> REQs) |
```

---

## Notes

- Requirements must reflect user-observable behavior, not implementation details.
- Avoid implementation language ("the database will store...", "the API will call..."). Write in terms of what the system does from the user's perspective.
- In `--mode auto`, if the user's answers are ambiguous, make a stated assumption rather than looping back. Document the assumption in the REQ block as `> **Assumption**: <text>`.
- Rerunning this skill on an existing `requirements.md` opens an edit session, not a blank slate.

---

== PHASE COMPLETE: sdd-requirements ==
Artifact: .claude/specs/<slug>/requirements.md
Summary:

- Mode read from progress.md
- Source Notion content loaded as context (if available)
- Requirements elicited and written in EARS format
- EARS compliance checks run; issues flagged
- progress.md updated: sdd-requirements → complete

⏸ WAITING FOR CONFIRMATION
Type `CONFIRM sdd-review-requirements` to proceed. Or describe changes needed.
