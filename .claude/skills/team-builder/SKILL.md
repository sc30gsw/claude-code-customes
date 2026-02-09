---
name: team-builder
description: Intelligently compose and deploy Claude Code Agent Teams based on user requirements. Auto-selects optimal team composition from all available skills and agents (project, user, global, plugin scopes), generates task dependency graphs, and orchestrates team lifecycle. Use when creating multi-agent teams for complex tasks requiring parallel specialized work.
---

# Team Builder

Automated Agent Team composition and deployment. Analyzes user requirements to propose optimal team structure, with teammates leveraging all available skills and agents across every scope.

## Overview

This skill automates the process of creating Claude Code Agent Teams by:
- Analyzing user requirements to recommend optimal team composition
- Discovering all available skills/agents across 5 scopes (project, user, global, plugin marketplaces, plugin cache)
- Generating task dependency graphs with parallel/sequential flows
- Injecting relevant skills into teammate spawn prompts
- Supporting auto, template, and manual composition modes

## Args

| Arg | Short | Description | Example |
|-----|-------|-------------|---------|
| `--agents` | `-a` | Agent types to include (comma-separated) | `-a "planner,system-architect"` |
| `--skills` | `-s` | Skills for teammates to use (comma-separated) | `-s "tdd-workflow,security-review"` |
| `--template` | `-t` | Use predefined team template | `-t feature-dev` |
| `--name` | `-n` | Team name (auto-generated if omitted) | `-n "auth-team"` |
| `--model` | `-m` | Model strategy: deep/adaptive/fast/budget | `-m adaptive` |
| `--size` | | Team size limit (default: auto, max: 5) | `--size 3` |
| `--lead` | `-l` | Lead agent type | `-l planner` |
| `--dry-run` | | Preview composition without deploying | `--dry-run` |
| `--auto` | | Auto-deploy without confirmation | `--auto` |
| `--delegate` | `-d` | Lead focuses on coordination only | `--delegate` |
| `--plan-approval` | `-p` | Require plan approval from teammates | `-p` |
| `--display` | | Display mode: in-process or split | `--display split` |

## Workflow

### AUTO Mode (default)

When no `--template` or `--agents` specified:

1. **Analyze Request**: Detect domain keywords to identify the type of work
2. **Discover Resources**: Run `python scripts/discover_resources.py --format json` to catalog all available agents and skills across all scopes
3. **Score Relevance**: Match agents/skills to detected domain using the Domain Detection table below
4. **Propose Team**: Generate optimal team composition with task dependencies
5. **Confirm**: Present composition for user approval (skip with `--auto`)
6. **Deploy**: Execute TeamCreate -> TaskCreate (with blockedBy) -> Task spawn (with team_name) for each member

### TEMPLATE Mode (`-t` specified)

1. **Load Template**: Read matching template from `references/team-templates.md`
2. **Customize Tasks**: Inject user's request into task descriptions
3. **Override**: Apply `-a`, `-s` overrides if provided
4. **Deploy**: Execute team deployment sequence

### MANUAL Mode (`-a` only)

1. **Build Team**: Create team from specified agent types
2. **Route Skills**: Match `-s` skills to appropriate roles
3. **Generate Tasks**: Auto-create tasks from user request
4. **Deploy**: Execute team deployment sequence

## Available Templates

| Template | Use Case | Members |
|----------|----------|---------|
| `feature-dev` | Full-cycle feature development | planner + architect + tester |
| `investigation` | Bug investigation and RCA | analyst + tester + researcher |
| `refactor` | Code quality improvement | refactorer + reviewer + tester |
| `security-audit` | Security assessment | security + reviewer + tester |
| `frontend` | Frontend feature development | designer + reviewer + e2e |
| `full-stack` | End-to-end development | backend + frontend + tester + security |
| `documentation` | Documentation creation | writer + analyst |
| `exploration` | Multi-perspective analysis | ux-analyst + tech-architect + devils-advocate |

See `references/team-templates.md` for full template definitions with task flows and spawn prompts.

## Domain Detection

| Domain | Keywords | Recommended Agents | Recommended Skills |
|--------|----------|-------------------|-------------------|
| Feature Dev | build, implement, create, add, feature | planner, system-architect, testing-specialist | /plan, /tdd-workflow, /code-reviewer |
| Bug Investigation | debug, fix, investigate, error, bug | root-cause-analyst, testing-specialist | /debug-error, /test-coverage |
| Refactoring | refactor, clean, improve, optimize | refactoring-expert, quality-engineer | /refactor-clean, /code-reviewer |
| Security | security, audit, vulnerability, auth | security-reviewer, quality-engineer | /security-review |
| Frontend | UI, component, design, responsive, form | frontend-architect, e2e-runner | /senior-frontend, /e2e, /ui-advice |
| Backend | API, endpoint, database, server, service | system-architect, testing-specialist | /senior-backend, /tdd-workflow |
| Documentation | document, docs, spec, requirements, readme | technical-writer, requirements-analyst | /doc-engineer, /update-docs |
| Performance | performance, optimize, slow, benchmark, latency | performance-engineer, system-architect | /test-coverage |
| Exploration | explore, research, analyze, evaluate, compare | general-purpose (multiple) | /plan, /smart-think |

## Skill Injection

Embed in each teammate's spawn prompt to make skills discoverable:

```
You are the {role-name} on team "{team-name}". Your task is: {task-description}

## Available Skills
Invoke the following skills as needed during your work:
- /tdd-workflow: Test-driven development with 80%+ coverage
- /security-review: Comprehensive security checklist
- /code-reviewer: Code quality review
- /{plugin-skill}: {description from catalog}

## On Completion
1. Use TaskUpdate to mark your task as completed
2. Send a summary of your findings to team-lead via SendMessage
```

Skills listed are dynamically populated from `discover_resources.py` output, matching the teammate's role to relevant skills from ALL scopes.

## Model Selection Strategy

| Strategy (`-m`) | Lead | Architect/Analyst | Worker |
|-----------------|------|-------------------|--------|
| `deep` | opus | opus | opus |
| `adaptive` (default) | opus | opus | sonnet |
| `fast` | sonnet | sonnet | sonnet |
| `budget` | sonnet | haiku | haiku |

## Deployment Sequence

```
1. TeamCreate(team_name, description)
2. For each member:
   a. TaskCreate(subject, description, activeForm)
3. Set dependencies:
   a. TaskUpdate(taskId, addBlockedBy: [...])
4. For each member:
   a. Task(subagent_type, team_name, name, prompt, model, mode)
5. Assign initial tasks:
   a. TaskUpdate(taskId, owner: member-name, status: "in_progress")
```

When `--plan-approval` is set, spawn teammates with `mode: "plan"` so they submit plans for approval before implementing.

When `--delegate` is set, the lead agent focuses solely on coordination, task assignment, and synthesis.

## Usage Examples

```bash
# Auto: compose from request analysis
/team-builder "Design and implement JWT authentication system"

# Template: use predefined template
/team-builder -t feature-dev "User management API"

# Manual: specify agents and skills
/team-builder -a "planner,frontend-architect,e2e-runner" -s "senior-frontend,e2e,ai-sdk"

# Dry-run: preview composition
/team-builder --dry-run "Large-scale refactoring"

# Budget + auto: cost-optimized auto-deploy
/team-builder -m budget --auto "Documentation cleanup"

# With plan approval for high-risk work
/team-builder -t full-stack -p "Payment processing system"

# Delegate mode: lead coordinates only
/team-builder -d -t feature-dev "New notification system"

# Split display for real-time monitoring
/team-builder --display split -t exploration "Evaluate microservices migration"
```

## Resources

### scripts/
- `discover_resources.py`: Discovers all available agents and skills across all 5 scopes. Run with `--format json|table` and `--scope project|user|global|plugin|all`.

### references/
- `team-templates.md`: 8 predefined team templates with member definitions, task flows, and spawn prompt templates.
- `composition-guide.md`: Team composition best practices including sizing, model selection, task granularity, file conflict avoidance, and anti-patterns.
