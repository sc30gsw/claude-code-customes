# Team Templates

Predefined team compositions for common development scenarios. Each template defines members, task dependencies, and recommended skills.

---

## 1. feature-dev

Full-cycle feature development from planning through testing.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| planner | planner | opus | Requirements analysis and implementation planning |
| architect | system-architect | opus | System design and architectural decisions |
| tester | testing-specialist | sonnet | Test strategy and implementation |

### Recommended Skills
`/plan`, `/tdd-workflow`, `/code-reviewer`

### Task Flow
```
[planner] Requirements Analysis
    ↓ blockedBy
[architect] System Design & Implementation
    ↓ blockedBy
[tester] Test Implementation & Verification
    ↓ blockedBy
[planner] Final Review & Integration
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /plan: Create implementation plans before coding
- /tdd-workflow: Test-driven development with 80%+ coverage
- /code-reviewer: Code quality review

## On Completion
1. Mark your task completed via TaskUpdate
2. Send a summary to team-lead via SendMessage
```

---

## 2. investigation

Bug investigation and root cause analysis.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| analyst | root-cause-analyst | opus | Systematic problem investigation |
| tester | testing-specialist | sonnet | Reproduce and verify fixes |
| researcher | search-specialist | sonnet | Gather context and related issues |

### Recommended Skills
`/debug-error`, `/test-coverage`

### Task Flow
```
[analyst] Define Problem Scope
    ↓ blockedBy
[researcher] Gather Context  ∥  [tester] Reproduce Issue
    ↓ blockedBy (both)
[analyst] Root Cause Analysis & Hypothesis
    ↓ blockedBy
[tester] Verify Fix
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /debug-error: Systematic debugging with Serena MCP integration
- /test-coverage: Generate tests to verify fixes

## On Completion
1. Mark your task completed via TaskUpdate
2. Send findings summary to team-lead via SendMessage
```

---

## 3. refactor

Code quality improvement and technical debt reduction.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| refactorer | refactoring-expert | opus | Identify and execute refactoring |
| reviewer | quality-engineer | sonnet | Quality verification |
| tester | testing-specialist | sonnet | Regression testing |

### Recommended Skills
`/refactor-clean`, `/code-reviewer`, `/test-coverage`

### Task Flow
```
[refactorer] Audit & Plan Refactoring
    ↓ blockedBy
[tester] Baseline Test Coverage
    ↓ blockedBy
[refactorer] Execute Refactoring
    ↓ blockedBy
[reviewer] Quality Review  ∥  [tester] Regression Verification
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /refactor-clean: Safe dead code removal with detection tools
- /code-reviewer: Comprehensive code quality review
- /test-coverage: Ensure 80%+ test coverage

## On Completion
1. Mark your task completed via TaskUpdate
2. Send a summary to team-lead via SendMessage
```

---

## 4. security-audit

Security vulnerability assessment and remediation.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| security | security-reviewer | opus | Vulnerability detection and remediation |
| reviewer | quality-engineer | sonnet | Code quality and compliance review |
| tester | testing-specialist | sonnet | Security test implementation |

### Recommended Skills
`/security-review`, `/code-reviewer`

### Task Flow
```
[security] Vulnerability Scan & Analysis
    ↓ blockedBy
[security] Remediation Plan
    ↓ blockedBy
[reviewer] Fix Review  ∥  [tester] Security Test Implementation
    ↓ blockedBy (both)
[security] Final Security Verification
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /security-review: Comprehensive security checklist (OWASP Top 10)
- /code-reviewer: Code quality and security review

## On Completion
1. Mark your task completed via TaskUpdate
2. Send security findings to team-lead via SendMessage
```

---

## 5. frontend

Frontend feature development with accessibility focus.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| designer | frontend-architect | opus | UI design and implementation |
| reviewer | quality-engineer | sonnet | Quality and accessibility review |
| e2e | e2e-runner | sonnet | End-to-end testing |

### Recommended Skills
`/senior-frontend`, `/ui-advice`, `/e2e`

### Task Flow
```
[designer] Component Design & Implementation
    ↓ blockedBy
[reviewer] Accessibility & Quality Review
    ↓ blockedBy
[e2e] E2E Test Implementation
    ↓ blockedBy
[designer] Final Polish
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /senior-frontend: React/Next.js/TypeScript/Tailwind best practices
- /ui-advice: UI/UX design pattern advice
- /e2e: Playwright E2E test generation and execution

## On Completion
1. Mark your task completed via TaskUpdate
2. Send a summary to team-lead via SendMessage
```

---

## 6. full-stack

End-to-end feature development across the entire stack.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| backend | system-architect | opus | Backend architecture and implementation |
| frontend | frontend-architect | sonnet | Frontend implementation |
| tester | testing-specialist | sonnet | Cross-stack testing |
| security | security-reviewer | sonnet | Security review |

### Recommended Skills
`/senior-backend`, `/senior-frontend`, `/tdd-workflow`, `/security-review`

### Task Flow
```
[backend] API Design & Implementation
    ↓ blockedBy
[frontend] Frontend Implementation  ∥  [tester] API Test Suite
    ↓ blockedBy (both)
[tester] Integration Testing
    ↓ blockedBy
[security] Security Audit
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /senior-backend: Scalable backend systems (Node.js, Express, Go, Python)
- /senior-frontend: Modern web applications (React, Next.js, TypeScript)
- /tdd-workflow: Test-driven development with 80%+ coverage
- /security-review: Comprehensive security checklist

## On Completion
1. Mark your task completed via TaskUpdate
2. Send a summary to team-lead via SendMessage
```

---

## 7. documentation

Documentation creation and improvement.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| writer | technical-writer | opus | Document creation and writing |
| analyst | requirements-analyst | sonnet | Requirements analysis and structure |

### Recommended Skills
`/doc-engineer`, `/update-docs`, `/spec-requirements`

### Task Flow
```
[analyst] Analyze Existing Documentation & Requirements
    ↓ blockedBy
[writer] Draft Documentation
    ↓ blockedBy
[analyst] Review & Feedback
    ↓ blockedBy
[writer] Finalize & Polish
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /doc-engineer: Comprehensive document engineering
- /update-docs: Sync documentation from source-of-truth files
- /spec-requirements: Generate requirements definitions

## On Completion
1. Mark your task completed via TaskUpdate
2. Send a summary to team-lead via SendMessage
```

---

## 8. exploration

Multi-perspective analysis for exploratory research and design.

### Members

| Name | agentType | Model | Role |
|------|-----------|-------|------|
| ux-analyst | general-purpose | opus | User experience and workflow analysis |
| tech-architect | system-architect | opus | Technical feasibility and architecture |
| devils-advocate | general-purpose | opus | Critical analysis and risk identification |

### Recommended Skills
`/plan`, `/smart-think`

### Task Flow
```
[ux-analyst] UX Analysis  ∥  [tech-architect] Technical Design  ∥  [devils-advocate] Critical Analysis
    ↓ blockedBy (all three)
[lead] Synthesis & Decision (team lead performs this)
```

### Spawn Prompt Template
```
You are the {role-name} on team "{team-name}".

## Your Task
{task-description}

## Available Skills
- /plan: Create structured implementation plans
- /smart-think: Multi-mode thinking with Sequential Thinking MCP

## Important
Provide your unique perspective. Do NOT try to be comprehensive across all domains.
Focus on YOUR specialized viewpoint. Disagreement with other perspectives is encouraged.

## On Completion
1. Mark your task completed via TaskUpdate
2. Send your analysis to team-lead via SendMessage
```
