# Intelligent Git Commit Command

Automatically analyze changes and create commits with appropriate granularity, generating meaningful commit messages following Conventional Commits specification.

## Usage

```bash
/commit [options]
```

## Description

Analyzes changed files to group related changes with appropriate granularity and automatically generates commit messages. Supports both task-based and file-based workflows.

## Options Chart

| Option | Short | Description | Use Case | Example |
|--------|-------|-------------|----------|---------|
| `--auto-granularity` | `-a` | Automatically detect optimal commit granularity | **Recommended default** - Let AI decide best split | `/commit -a` |
| `--smart-split` | `-s` | Split commits by logical file relationships | Multiple features changed simultaneously | `/commit -s` |
| `--by-feature` | `-f` | Group by detected feature/module | Clear feature-based development | `/commit -f` |
| `--by-type` | `-t` | Group by file type (frontend, backend, etc.) | Type-focused development workflow | `/commit -t` |
| `--single` | | Force all changes into single commit | Quick commits, hotfixes | `/commit --single` |
| `--validate` | `-v` | Run pre-commit validation checks | Ensure quality before commit | `/commit -v` |
| `--dry-run` | `-n` | Show what would be committed without committing | Preview commit plan | `/commit -a -n` |
| `--interactive` | `-i` | Interactive mode to review/edit commits | Manual control over automatic suggestions | `/commit -a -i` |
| `--scope` | | Override automatic scope detection | Custom scope specification | `/commit --scope="api"` |
| `--message` | `-m` | Custom commit message (overrides auto-generation) | Specific commit message needed | `/commit -m "custom message"` |
| `--amend` | | Amend the last commit | Fix previous commit | `/commit --amend` |
| `--no-verify` | | Skip pre-commit hooks | Emergency commits | `/commit --no-verify` |

## Basic Commands

### Auto-Granularity Commit (Recommended)
```bash
/commit --auto-granularity
# or shorter:
/commit -a
```
Analyzes changed files and creates multiple commits with appropriate granularity.

### Single Commit (All Changes)
```bash
/commit
```
Commits all staged changes as a single commit.

### Smart Split Commit
```bash
/commit --smart-split
```
Analyzes changes and splits commits logically by related files.

### Interactive Preview
```bash
/commit --auto-granularity --dry-run --interactive
```
See proposed commits and modify before executing.

## Automatic Granularity Detection

### Change Analysis Patterns

**1. File Type Classification**
- Frontend: `*.tsx, *.jsx, *.vue` → `feat(ui)`
- Backend API: `*api*, *controller*` → `feat(api)`
- Database: `*model*, *schema*, *migration*` → `feat(db)`
- Tests: `*.test.*, *.spec.*` → `test`
- Documentation: `*.md, *.txt, docs/` → `docs`
- Configuration: `*.json, *.yaml, *.env` → `chore`

**2. Feature-based Grouping**
```bash
Authentication-related files:
├── src/auth/login.ts
├── src/auth/middleware.ts
└── tests/auth.test.ts
→ Single commit: feat(auth): implement authentication system
```

**3. Dependency Analysis**
- Auto-detect multiple files belonging to same feature
- Analyze import/export relationships
- Group related files into single commits

**4. Change Size Optimization**
- Split large changes into logical chunks
- Combine small related changes
- Ensure each commit represents atomic change

## Workflow Integration

### Auto-commit on Status Change
```
/orchestration/move TASK-003 qa --auto-commit
```
Automatically commits when moving to QA status.

### Pre-commit Validation
```
/orchestration/commit --validate
```
Checks:
- All tests pass
- No linting errors
- Task requirements met
- Files match task scope

## Options

### Custom Message
```
/orchestration/commit TASK-003 --message "Custom commit message"
```
Override automatic message generation.

### Scope Detection
```
/orchestration/commit --detect-scope
```
Automatically detects scope from changed files:
- `auth` for auth-related files
- `api` for API changes
- `ui` for frontend changes

### Breaking Changes
```
/orchestration/commit --breaking
```
Adds breaking change indicator:
```
feat(api)!: restructure authentication endpoints

BREAKING CHANGE: Auth endpoints moved from /auth to /api/v2/auth
```

## Batch Operations

### Commit by Feature
```
/orchestration/commit --feature authentication
```
Groups all completed auth tasks into one commit.

### Commit by Status
```
/orchestration/commit --status qa
```
Commits all tasks currently in QA.

### Smart Grouping
```
/orchestration/commit --smart-group
```
Intelligently groups related tasks:
```
Feature Group: Authentication (3 tasks)
- TASK-001: Database schema
- TASK-003: JWT implementation  
- TASK-005: Login endpoint

Suggested commit: feat(auth): implement complete authentication system
```

## Worktree Support

### Worktree-Aware Commits
```
/orchestration/commit --worktree
```
Detects current worktree and commits only relevant tasks.

### Cross-Worktree Status
```
/orchestration/commit --all-worktrees
```
Shows commit status across all worktrees:
```
Worktree Status:
- feature/auth: 2 tasks ready to commit
- feature/payments: 1 task ready to commit
- feature/ui: No uncommitted changes
```

## Validation Features

### Pre-commit Checks
```
## Pre-commit Validation
✓ All tests passing
✓ No linting errors
✓ Task requirements met
✗ Uncommitted files outside task scope: src/unrelated.js

Proceed with commit? [y/n]
```

### Task Alignment
```
## Task Alignment Check
Changed files:
- src/auth/jwt.ts ✓ (matches TASK-003)
- src/auth/validate.ts ✓ (matches TASK-003)
- src/payments/stripe.ts ✗ (not in TASK-003 scope)

Warning: Changes outside task scope detected
```

## Integration Features

### Link to Task
```
/orchestration/commit --link-task
```
Adds task URL/reference to commit:
```
feat(auth): implement JWT validation

Task: TASK-003
Link: http://orchestration/03_15_2024/auth_system/tasks/TASK-003
```

### Update Status Tracker
```
/orchestration/commit --update-tracker
```
Updates TASK-STATUS-TRACKER.yaml with commit info:
```yaml
git_tracking:
  TASK-003:
    commits: ["abc123def"]
    commit_message: "feat(auth): implement JWT validation"
    committed_at: "2024-03-15T14:30:00Z"
```

## Examples

### Example 1: Simple Task Commit
```
/orchestration/commit TASK-003

Generated commit:
feat(auth): implement JWT token validation

- Add verification middleware
- Handle token expiration
- Implement refresh logic

Task: TASK-003 (4.5 hours)
```

### Example 2: Batch Feature Commit
```
/orchestration/commit --feature authentication --batch

Grouping 3 related tasks:
feat(auth): complete authentication system implementation

- Set up database schema (TASK-001)
- Implement JWT validation (TASK-003)
- Create login endpoints (TASK-005)

Tasks: TASK-001, TASK-003, TASK-005 (12 hours total)
```

### Example 3: Fix with Test
```
/orchestration/commit TASK-007

Generated commit:
fix(auth): resolve token expiration race condition

- Fix async validation timing issue
- Add comprehensive test coverage
- Prevent edge case in refresh flow

Fixes: #123
Task: TASK-007 (2 hours)
```

## Commit Templates

### Feature Template
```
feat(<scope>): <task-title>

- <implementation-detail-1>
- <implementation-detail-2>
- <implementation-detail-3>

Task: <task-id> (<duration>)
Status: <status-transition>
```

### Fix Template
```
fix(<scope>): <issue-description>

- <root-cause>
- <solution>
- <test-coverage>

Fixes: #<issue-number>
Task: <task-id>
```

## Best Practices

1. **Commit at Natural Breakpoints**: When moving tasks to QA
2. **Keep Commits Atomic**: One logical change per commit
3. **Use Batch Wisely**: Only group truly related tasks
4. **Validate First**: Always run validation before committing
5. **Update Status**: Ensure task status is current

## Configuration

### Auto-commit Rules
Set in orchestration config:
```yaml
auto_commit:
  on_qa: true
  on_complete: false
  require_tests: true
  require_validation: true
```

## Notes

- Integrates with task-commit-manager agent for complex scenarios
- Respects .gitignore and excluded files
- Supports conventional commits specification
- Maintains traceable history between tasks and commits