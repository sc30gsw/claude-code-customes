---
name: implement-spec
description: Implement one or more specs while maintaining a per-spec implementation
  notes file at ./.claude/learned/<slug>.md. Use when the user asks to implement a
  spec, build a feature, or provides a spec description and wants design decisions,
  deviations, tradeoffs, and open questions captured as work proceeds.
---

# Implement Spec

Implement specs while keeping a living notes file that captures every design decision, deviation, tradeoff, and open question the moment it arises — not after the fact.

## Usage

```
/implement-spec <spec>
/implement-spec ## Multiple specs
- Spec A description
- Spec B description
```

## When to use

- User says "implement this spec", "build this feature", "do this", or provides a description and asks for implementation
- User explicitly invokes `/implement-spec`

## When NOT to use

- The work requires heavy upfront planning with user sign-off → run `/plan` first, then `/implement-spec`
- The request is a bug fix or refactor without a spec → use `/debug-error` or native implementation

## Parsing the spec argument

**Single spec**: the entire argument is one spec (free-text sentence or paragraph).

**Multiple specs**: if the argument contains a heading like `## Multiple specs` (or similar) followed by a bulleted list, treat each bullet as a separate spec. Implement them in order from top to bottom. If dependencies force a different order, record the reordering reason in the first spec's note under `## Deviations`.

## Slug derivation

Derive a kebab-case slug from the spec title or its first sentence:
- Strip punctuation, lowercase, replace spaces with hyphens
- Truncate to ~40 characters
- Examples: "Creating the UI for user page" → `user-page-ui`, "Add email notifications" → `add-email-notifications`
- On slug collision with an existing file, append `-2`, `-3`, etc.

## Note initialization (BEFORE any code change)

1. Determine the slug for each spec.
2. Check whether `./.claude/learned/` exists:
   - If `cwd` is `~/.claude` itself, use `~/.claude/learned/` (avoids nesting `~/.claude/.claude/`).
   - Otherwise create `./.claude/learned/` if it does not exist.
3. Copy `assets/notes-template.md` to `./.claude/learned/<slug>.md`.
4. Fill in the frontmatter (`spec`, `created`) and the `## Spec (verbatim)` section with the user's original spec text.
5. Write the file before touching any implementation file.

## Appending to the note during implementation

Append to the note **the moment** each event occurs — do not batch at the end:

| Event | Section to append |
|---|---|
| Spec is ambiguous and you choose an interpretation | `## Design decisions` |
| You intentionally depart from the spec | `## Deviations` |
| You consider an alternative and reject it | `## Tradeoffs` |
| Something needs user confirmation before proceeding | `## Open questions` |

Each entry should be one bullet: state the decision / deviation / tradeoff / question in one sentence, then `Why: <one-line reason>`.

Keep entries concise. Do not pad with entries that have no real decision behind them.

## Completion behavior

After all specs are implemented:

1. Report to the user:
   - List of files created or modified
   - Path(s) of the generated note(s) under `./.claude/learned/`
   - Highlight any unresolved items in `## Open questions` (checkboxes not yet ticked)

2. Propose a status update:
   - If no Open questions remain → ask "Mark this note as `done`?"
   - If Open questions remain → ask "Mark this note as `blocked` until open questions are resolved?"
   - On user approval, update `status:` in the frontmatter of each note.

## Entry format (for each section)

```markdown
- <Decision / deviation / tradeoff / question in one sentence>. Why: <reason>
```

For Open questions use a checkbox:
```markdown
- [ ] <Question>. Why it matters: <reason>
```

## Related

- `~/.claude/skills/learned/` — cross-project extracted lessons (auto-extracted, not per-spec). This skill writes to a **different** location (`./.claude/learned/`) for implementation-specific notes.
- `/plan` — heavy upfront planning with user confirmation before any code change. Use it first when the scope is large and uncertain.
