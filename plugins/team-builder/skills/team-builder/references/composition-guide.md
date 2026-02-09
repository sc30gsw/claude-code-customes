# Team Composition Guide

Best practices for composing effective Agent Teams.

---

## Team Sizing

| Complexity | Team Size | Rationale |
|------------|-----------|-----------|
| Simple | 2 | Single specialist + reviewer/tester |
| Moderate | 3 | Planner + implementer + tester |
| Complex | 4 | Multi-role specialists with coordination |
| Large-scale | 5 (max) | Communication overhead beyond 5 degrades performance |

**Rule of thumb**: 5-6 tasks per person. Design tasks accordingly.

---

## Model Selection Strategy

| Strategy | Lead | Architect/Analyst | Worker | Use When |
|----------|------|-------------------|--------|----------|
| `deep` | opus | opus | opus | Maximum quality, complex reasoning tasks |
| `adaptive` | opus | opus | sonnet | Default - best quality/cost balance |
| `fast` | sonnet | sonnet | sonnet | Speed-critical, well-defined tasks |
| `budget` | sonnet | haiku | haiku | Simple tasks, cost-sensitive |

### Role-to-Model Mapping

- **Lead/Coordinator**: opus (complex decision-making, synthesis)
- **Architect/Analyst**: opus (deep reasoning, system design)
- **Implementer/Worker**: sonnet (efficient coding, following specs)
- **Lightweight tasks**: haiku (simple checks, formatting, data processing)

---

## Task Granularity

A well-designed task should be:

- **Self-contained**: Produces a clear, verifiable deliverable
- **Scoped**: Completable in a single agent session
- **Independent**: Minimal file overlap with other tasks
- **Testable**: Has clear success criteria

### Bad Task Examples
- "Work on the frontend" (too vague)
- "Fix everything" (no clear deliverable)
- "Help the backend team" (no ownership)

### Good Task Examples
- "Design REST API schema for user management endpoints"
- "Implement login form component with validation and error states"
- "Write integration tests for the payment processing flow"

---

## File Conflict Avoidance

Multiple teammates editing the same files causes merge conflicts and lost work.

### Strategies
1. **File ownership**: Each teammate owns different file sets
2. **Interface contracts**: Define interfaces first, implement independently
3. **Sequential dependencies**: Use `blockedBy` when file overlap is unavoidable
4. **Layer separation**: Backend and frontend work on separate file trees

### Example
```
backend-dev: owns src/api/**, src/services/**, src/models/**
frontend-dev: owns src/components/**, src/pages/**, src/hooks/**
tester: owns tests/**, __tests__/**
```

---

## Skill Injection Method

Include skill invocation instructions directly in the teammate's spawn prompt:

```
## Available Skills
Invoke the following skills as needed during your work:
- /tdd-workflow: Test-driven development with 80%+ coverage
- /security-review: Comprehensive security checklist
- /code-reviewer: Code quality review

Use these skills by invoking them with the Skill tool when appropriate.
```

### Matching Skills to Roles

| Role | Recommended Skills |
|------|-------------------|
| Planner | /plan, /smart-think, /spec-requirements |
| Architect | /plan, /smart-think, /senior-backend |
| Frontend Dev | /senior-frontend, /ui-advice, /frontend-design |
| Backend Dev | /senior-backend, /tdd-workflow |
| Tester | /tdd-workflow, /test-coverage, /e2e |
| Security | /security-review, /code-reviewer |
| Reviewer | /code-reviewer, /refactor-clean |
| Writer | /doc-engineer, /update-docs |
| Researcher | /spec-tech-research, /smart-think |

---

## Communication Pattern

### Teammate Completion Protocol
1. Use `TaskUpdate` to mark task as `completed`
2. Use `SendMessage` to send summary to team lead
3. Team lead checks `TaskList` for next assignments

### Lead Coordination Protocol
1. Monitor teammate idle notifications (automatic)
2. Review completed work via `TaskGet`
3. Assign next tasks via `TaskUpdate` with `owner`
4. Send feedback via `SendMessage`

---

## Plan Approval

Use `mode: "plan"` for the Task tool when spawning teammates for:
- Production changes
- Database modifications
- Security-sensitive operations
- Large-scale refactoring
- Infrastructure changes

The teammate will create a plan and request approval before implementing.

---

## Delegate Mode

When using delegate mode, the lead agent focuses on:
- Coordination and task assignment
- Reviewing teammate outputs
- Synthesizing results
- Making architectural decisions

The lead does NOT implement code directly, instead delegating all implementation to teammates.

---

## Available Agent Types

These are valid `subagent_type` values for the Task tool:

| Agent Type | Purpose |
|-----------|---------|
| `general-purpose` | Versatile agent with all tools |
| `planner` | Implementation planning |
| `system-architect` | System design and architecture |
| `frontend-architect` | UI/UX and frontend development |
| `testing-specialist` | Test strategy and implementation |
| `quality-engineer` | Code quality assurance |
| `security-reviewer` | Security vulnerability detection |
| `refactoring-expert` | Code refactoring and cleanup |
| `root-cause-analyst` | Bug investigation and RCA |
| `search-specialist` | Web research and information gathering |
| `technical-writer` | Documentation creation |
| `requirements-analyst` | Requirements discovery |
| `performance-engineer` | Performance optimization |
| `python-expert` | Python-specific development |
| `e2e-runner` | Playwright E2E testing |
| `build-error-resolver` | Build/TypeScript error fixing |
| `doc-updater` | Documentation updates |
| `refactor-cleaner` | Dead code removal |
| `tdd-guide` | Test-driven development |
| `learning-guide` | Educational explanations |
| `socratic-mentor` | Socratic method teaching |
| `devops-architect` | Infrastructure and deployment |
| `terraform-specialist` | Terraform/IaC |
| `serena-skills-expert` | Serena MCP integration |

---

## Scope Priority Order

Resources are discovered in priority order (earlier scopes win on name conflicts):

1. **Project** (`{cwd}/.claude/agents/`, `{cwd}/.claude/skills/`)
2. **User** (`~/.claude/agents/`, `~/.claude/skills/`)
3. **Global** (`~/.agents/skills/`)
4. **Plugin Marketplaces** (`~/.claude/plugins/marketplaces/`)
5. **Plugin Cache** (`~/.claude/plugins/cache/`)

All skills from all scopes are available to teammates since each teammate runs as a full Claude Code session.

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Teams larger than 5 | Communication overhead | Split into sub-teams or phases |
| All-opus for budget tasks | Unnecessary cost | Use adaptive or budget model strategy |
| Multiple teammates editing same files | Merge conflicts | File ownership + blockedBy deps |
| Vague spawn prompts | Poor output quality | Include specific task, skills, and completion protocol |
| No skill injection | Missed capabilities | Always list relevant skills in spawn prompt |
| Lead implementing code | Coordination bottleneck | Use delegate mode |
| No task dependencies | Race conditions | Define blockedBy relationships |
| Monolithic tasks | Too large to complete | Break into 5-6 task units per person |
