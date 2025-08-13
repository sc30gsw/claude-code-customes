---
allowed-tools: mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, Bash(git:*), Bash(npm:*), Bash(pnpm:*), Read, Write, Edit
description: Advanced git commit automation with Serena MCP integration for intelligent change analysis and context-aware commit message generation
---

## Context

- Current git status: !`git status --porcelain`
- Staged changes: !`git diff --cached --name-only | head -10`
- Recent commits: !`git log --oneline -5`
- Modified files: !`git diff --name-only | head -10`
- Project type: @package.json
- Pre-commit hooks: !`ls -la .husky/ 2>/dev/null || echo "No husky hooks found"`

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools when available:**

### Code Analysis (Serena MCP First)
- **Change Analysis**: Use `mcp__serena__search_for_pattern` to analyze git diff
- **Symbol Understanding**: Use `mcp__serena__get_symbols_overview` for code context
- **Pattern Recognition**: Use `mcp__serena__find_referencing_symbols` for impact analysis
- **Context Building**: Use `mcp__serena__think_about_collected_information` for change categorization

### Memory & Learning (Serena MCP Only)
- **Pattern Storage**: Use `mcp__serena__write_memory` to store successful commit patterns
- **History Learning**: Use `mcp__serena__read_memory` to retrieve previous commit styles
- **Progress Tracking**: Use `mcp__serena__think_about_task_adherence` for commit quality
- **Completion Check**: Use `mcp__serena__think_about_whether_you_are_done` for final validation

### Git Operations (Standard Tools)
- **Status & Diff**: Use `Bash(git:*)` for git status, diff, log commands
- **Staging**: Use `Bash(git:*)` for git add operations
- **Committing**: Use `Bash(git:*)` for final git commit execution

# Smart Commit: Intelligent Git Automation

Advanced git commit automation with Serena MCP for intelligent change analysis, git history learning, and context-aware commit message generation.

## Usage Guide

### Basic Syntax
```bash
/commit [options]
```

### Available Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--no-verify` | | Skip pre-commit checks | `/commit --no-verify` |
| `--analyze` | `-a` | Enable deep Serena analysis | `/commit -a` |
| `--learning` | `-l` | Learn from git history patterns | `/commit -l` |
| `--scope` | `-s` | Set commit scope | `/commit -s feature` |
| `--batch` | `-b` | Group multiple related changes | `/commit -b` |
| `--interactive` | `-i` | Interactive message refinement | `/commit -i` |
| `--template` | `-t` | Use specific commit template | `/commit -t refactor` |
| `--dry-run` | `-d` | Show what would be committed | `/commit -d` |
| `--context-depth` | | Serena context analysis depth (1-5) | `/commit --context-depth=3` |
| `--history-window` | | Number of commits to analyze | `/commit --history-window=20` |
| `--semantic-grouping` | | Enable advanced change grouping | `/commit --semantic-grouping` |
| `--impact-analysis` | | Analyze potential change impact | `/commit --impact-analysis` |

### Quick Examples

```bash
# Basic smart commit
/commit

# Feature commit with learning
/commit --scope=feature --learning --analyze

# Refactoring with semantic grouping
/commit --template=refactor --semantic-grouping

# Batch commit with impact analysis
/commit --batch --impact-analysis --interactive

# Quick commit without verification
/commit --no-verify --dry-run
```

## Workflow Process

### Default Workflow (no options):

1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. **Pre-commit Analysis**:
   - Use `mcp__serena__search_for_pattern` to analyze current changes
   - Use `mcp__serena__get_symbols_overview` for codebase understanding
   - Use `mcp__serena__think_about_collected_information` to categorize changes
3. **Quality Checks**: Run pre-commit hooks (`pnpm lint`, `pnpm build`, `pnpm generate:docs`) unless `--no-verify`
4. **Staging Management**:
   - Check staged files with `git status`
   - Auto-stage all changes if no files are staged
5. **Change Analysis**:
   - Perform `git diff` analysis with Serena pattern recognition
   - Use `mcp__serena__find_referencing_symbols` for impact assessment
6. **Message Generation**:
   - Use `mcp__serena__read_memory` to learn from previous commit patterns
   - Generate conventional commit message with appropriate emoji
   - Use `mcp__serena__think_about_task_adherence` for quality validation
7. **Commit Execution**: Execute git commit with generated message
8. **Pattern Storage**: Use `mcp__serena__write_memory` to store successful patterns

### With --analyze option:

1. **Deep Code Analysis**: Extended use of `mcp__serena__get_symbols_overview` and `mcp__serena__find_referencing_symbols`
2. **Impact Assessment**: Comprehensive change impact analysis
3. **Architecture Awareness**: Understanding of how changes fit into overall system
4. **Quality Metrics**: Enhanced validation using Serena's analytical capabilities

### With --learning option:

1. **History Analysis**: Extended `mcp__serena__read_memory` to analyze commit history patterns
2. **Convention Detection**: Learn project-specific commit message styles
3. **Pattern Adaptation**: Adapt to team conventions and preferences
4. **Continuous Improvement**: Store and refine successful commit patterns

### With --batch option:

1. **Multi-Change Analysis**: Use Serena to identify logical change groups
2. **Semantic Clustering**: Group related changes into separate commits
3. **Dependency Analysis**: Understand change relationships and ordering
4. **Incremental Commits**: Create multiple well-organized commits

## Serena MCP Integration Features

### Intelligent Code Analysis
- **Symbol-Level Understanding**: Deep analysis of functions, classes, and dependencies
- **Pattern Recognition**: Identifies commit patterns and coding conventions
- **Context Mapping**: Understands code relationships and change impact
- **Memory Integration**: Learns and improves from previous commit sessions

### Advanced Commit Intelligence
- **Semantic Grouping**: Automatically groups related changes
- **Convention Learning**: Adapts to project-specific commit styles
- **Impact Assessment**: Understands how changes affect the broader codebase
- **Quality Validation**: Ensures commit quality using learned patterns

### Git History Learning
- **Pattern Analysis**: Analyzes existing commit messages for consistency
- **Team Convention Detection**: Learns team-specific commit styles
- **Scope Identification**: Automatically identifies appropriate commit scopes
- **Message Optimization**: Improves commit message quality over time

## Best Practices for Commits

- **Verify before committing**: Ensure code is linted, builds correctly, and documentation is updated
- **Atomic commits**: Each commit should contain related changes that serve a single purpose
- **Split large changes**: If changes touch multiple concerns, split them into separate commits
- **Conventional commit format**: Use the format `<type>: <description>` where type is one of:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (formatting, etc)
  - `refactor`: Code changes that neither fix bugs nor add features
  - `perf`: Performance improvements
  - `test`: Adding or fixing tests
  - `chore`: Changes to the build process, tools, etc.
- **Present tense, imperative mood**: Write commit messages as commands (e.g., "add feature" not "added feature")
- **Concise first line**: Keep the first line under 72 characters
- **Emoji**: Each commit type is paired with an appropriate emoji:
  - ✨ `feat`: New feature
  - 🐛 `fix`: Bug fix
  - 📝 `docs`: Documentation
  - 💄 `style`: Formatting/style
  - ♻️ `refactor`: Code refactoring
  - ⚡️ `perf`: Performance improvements
  - ✅ `test`: Tests
  - 🔧 `chore`: Tooling, configuration
  - 🚀 `ci`: CI/CD improvements
  - 🗑️ `revert`: Reverting changes
  - 🧪 `test`: Add a failing test
  - 🚨 `fix`: Fix compiler/linter warnings
  - 🔒️ `fix`: Fix security issues
  - 👥 `chore`: Add or update contributors
  - 🚚 `refactor`: Move or rename resources
  - 🏗️ `refactor`: Make architectural changes
  - 🔀 `chore`: Merge branches
  - 📦️ `chore`: Add or update compiled files or packages
  - ➕ `chore`: Add a dependency
  - ➖ `chore`: Remove a dependency
  - 🌱 `chore`: Add or update seed files
  - 🧑‍💻 `chore`: Improve developer experience
  - 🧵 `feat`: Add or update code related to multithreading or concurrency
  - 🔍️ `feat`: Improve SEO
  - 🏷️ `feat`: Add or update types
  - 💬 `feat`: Add or update text and literals
  - 🌐 `feat`: Internationalization and localization
  - 👔 `feat`: Add or update business logic
  - 📱 `feat`: Work on responsive design
  - 🚸 `feat`: Improve user experience / usability
  - 🩹 `fix`: Simple fix for a non-critical issue
  - 🥅 `fix`: Catch errors
  - 👽️ `fix`: Update code due to external API changes
  - 🔥 `fix`: Remove code or files
  - 🎨 `style`: Improve structure/format of the code
  - 🚑️ `fix`: Critical hotfix
  - 🎉 `chore`: Begin a project
  - 🔖 `chore`: Release/Version tags
  - 🚧 `wip`: Work in progress
  - 💚 `fix`: Fix CI build
  - 📌 `chore`: Pin dependencies to specific versions
  - 👷 `ci`: Add or update CI build system
  - 📈 `feat`: Add or update analytics or tracking code
  - ✏️ `fix`: Fix typos
  - ⏪️ `revert`: Revert changes
  - 📄 `chore`: Add or update license
  - 💥 `feat`: Introduce breaking changes
  - 🍱 `assets`: Add or update assets
  - ♿️ `feat`: Improve accessibility
  - 💡 `docs`: Add or update comments in source code
  - 🗃️ `db`: Perform database related changes
  - 🔊 `feat`: Add or update logs
  - 🔇 `fix`: Remove logs
  - 🤡 `test`: Mock things
  - 🥚 `feat`: Add or update an easter egg
  - 🙈 `chore`: Add or update .gitignore file
  - 📸 `test`: Add or update snapshots
  - ⚗️ `experiment`: Perform experiments
  - 🚩 `feat`: Add, update, or remove feature flags
  - 💫 `ui`: Add or update animations and transitions
  - ⚰️ `refactor`: Remove dead code
  - 🦺 `feat`: Add or update code related to validation
  - ✈️ `feat`: Improve offline support

## Guidelines for Splitting Commits

When analyzing the diff, consider splitting commits based on these criteria:

1. **Different concerns**: Changes to unrelated parts of the codebase
2. **Different types of changes**: Mixing features, fixes, refactoring, etc.
3. **File patterns**: Changes to different types of files (e.g., source code vs documentation)
4. **Logical grouping**: Changes that would be easier to understand or review separately
5. **Size**: Very large changes that would be clearer if broken down

## Requirements

### Prerequisites
- Git repository with commit history
- Serena MCP integration available
- Optional: Pre-commit hooks configured
- Optional: Package.json with lint/build scripts

### Dependencies
- **Serena MCP**: For intelligent code analysis and learning
- **Git**: For version control operations
- **Node.js/PNPM** (optional): For pre-commit quality checks
- **Husky** (optional): For git hooks integration

## Important Notes

- **Serena Priority**: Always uses Serena MCP tools for codebase analysis when available
- **Learning Capability**: Builds understanding of your project patterns over time
- **Quality First**: Pre-commit checks ensure code quality by default
- **Smart Automation**: Automatically organizes changes into logical commits
- **Team Adaptation**: Learns and adapts to team-specific commit conventions
- **Impact Awareness**: Considers broader codebase impact of changes

## Usage Examples

### Development Scenarios

```bash
# Basic feature development
/commit --scope=feature --learning

# Bug fix with impact analysis
/commit --scope=fix --impact-analysis --analyze

# Refactoring with semantic grouping
/commit --template=refactor --semantic-grouping --batch

# Documentation update
/commit --scope=docs --context-depth=2

# Performance optimization
/commit --scope=perf --analyze --learning --interactive
```

### Team Workflow Integration

```bash
# Learn team conventions
/commit --learning --history-window=30

# Enterprise development with full analysis
/commit --analyze --impact-analysis --semantic-grouping --interactive

# Quick hotfix
/commit --scope=fix --no-verify --template=hotfix

# Large feature with multiple commits
/commit --batch --analyze --learning --context-depth=5
```

### Quality Assurance

```bash
# Pre-production commit with full validation
/commit --analyze --impact-analysis --learning --interactive

# Code review preparation
/commit --semantic-grouping --template=review --dry-run

# CI/CD integration
/commit --batch --analyze --no-verify=false
```

## Integration Patterns

### With Other Commands
```bash
# Debug → Fix → Commit workflow
/debug-error "performance issue" --serena
/serena "optimize queries" --performance-focused
/commit --scope=perf --analyze --learning

# Research → Think → Implement → Commit
/tech-research "caching strategies" --serena
/smart-think "implement Redis caching" --serena
/serena "add Redis caching layer"
/commit --scope=feature --semantic-grouping
```

### Error Handling

- **Pre-commit Failure**: Automatically suggests fixes and retry
- **Staging Issues**: Smart re-staging with conflict resolution
- **Message Validation**: Interactive refinement for better messages
- **Serena Integration**: Fallback to standard tools if MCP unavailable

## Examples

Good commit messages:
- ✨ feat: add user authentication system
- 🐛 fix: resolve memory leak in rendering process
- 📝 docs: update API documentation with new endpoints
- ♻️ refactor: simplify error handling logic in parser
- 🚨 fix: resolve linter warnings in component files
- 🧑‍💻 chore: improve developer tooling setup process
- 👔 feat: implement business logic for transaction validation
- 🩹 fix: address minor styling inconsistency in header
- 🚑️ fix: patch critical security vulnerability in auth flow
- 🎨 style: reorganize component structure for better readability
- 🔥 fix: remove deprecated legacy code
- 🦺 feat: add input validation for user registration form
- 💚 fix: resolve failing CI pipeline tests
- 📈 feat: implement analytics tracking for user engagement
- 🔒️ fix: strengthen authentication password requirements
- ♿️ feat: improve form accessibility for screen readers

Example of splitting commits:
- First commit: ✨ feat: add new solc version type definitions
- Second commit: 📝 docs: update documentation for new solc versions
- Third commit: 🔧 chore: update package.json dependencies
- Fourth commit: 🏷️ feat: add type definitions for new API endpoints
- Fifth commit: 🧵 feat: improve concurrency handling in worker threads
- Sixth commit: 🚨 fix: resolve linting issues in new code
- Seventh commit: ✅ test: add unit tests for new solc version features
- Eighth commit: 🔒️ fix: update dependencies with security vulnerabilities

- If specific files are already staged, the command will only commit those files
- If no files are staged, it will automatically stage all modified and new files
- The commit message will be constructed based on the changes detected
- Before committing, the command will review the diff to identify if multiple commits would be more appropriate
- If suggesting multiple commits, it will help you stage and commit the changes separately
- Always reviews the commit diff to ensure message matches changes
- Uses Serena MCP to build project-specific commit intelligence over time