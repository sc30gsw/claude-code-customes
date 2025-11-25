---
allowed-tools: Read, Write, Bash, Edit, mcp__serena__search_for_pattern, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__read_memory, mcp__serena__write_memory, mcp__serena__replace_symbol_body
description: Token-efficient Serena MCP command for structured app development and problem-solving
---

## Context

- Current project: @package.json
- Project structure: !`find . -maxdepth 2 -name "package.json" -o -name "*.config.*" | head -5 2>/dev/null || echo "No config files"`
- Git status: !`git status --porcelain 2>/dev/null | head -3 || echo "Not git repo"`
- Recent activity: !`git log --oneline -3 2>/dev/null || echo "No git history"`
- Code complexity: !`find . -name "*.js" -o -name "*.ts" -o -name "*.py" | wc -l | xargs echo "Code files:"`
- Serena memory: !`ls -la .serena/ 2>/dev/null | head -3 || echo "No Serena memory"`

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools as the primary development and analysis engine:**

### Primary Development Tools (Serena MCP)
- **Project Analysis**: Use `mcp__serena__get_symbols_overview` for codebase understanding
- **Code Search**: Use `mcp__serena__search_for_pattern` for finding code patterns
- **Symbol Management**: Use `mcp__serena__find_symbol` and `mcp__serena__find_referencing_symbols`
- **Code Modification**: Use `mcp__serena__replace_symbol_body` and `mcp__serena__replace_regex`
- **Intelligent Insertion**: Use `mcp__serena__insert_before_symbol` / `mcp__serena__insert_after_symbol`

### Memory & Learning (Serena MCP Only)
- **Knowledge Storage**: Use `mcp__serena__write_memory` to store patterns and solutions
- **Experience Retrieval**: Use `mcp__serena__read_memory` to access previous work
- **Progress Tracking**: Use `mcp__serena__think_about_task_adherence` for quality control
- **Completion Assessment**: Use `mcp__serena__think_about_whether_you_are_done`

### Supporting Tools (Secondary)
- **Documentation Research**: Use `mcp__context7__resolve-library-id` and `mcp__context7__get-library-docs`
- **File Operations**: Use Read, Write, Edit when Serena tools insufficient
- **Process Management**: Use TodoWrite for complex task breakdown

### Fallback Tools (Last Resort)
- **Basic Search**: Use Grep, Glob only when Serena search unavailable
- **Simple Operations**: Use Bash for build, test, and deployment commands

# Serena: Intelligent App Development

Token-efficient Serena MCP command for structured app development and problem-solving

## Quick Reference

```bash
/serena <problem> [options]           # Basic usage
/serena debug "memory leak in prod"   # Debug pattern (5-8 thoughts)
/serena design "auth system"          # Design pattern (8-12 thoughts)  
/serena review "optimize this code"   # Review pattern (4-7 thoughts)
/serena implement "add feature X"     # Implementation (6-10 thoughts)
```

## Options

| Option | Description | Usage | Use Case |
|--------|-------------|-------|----------|
| `-q` | Quick mode (3-5 thoughts/steps) | `/serena "fix button" -q` | Simple bugs, minor features |
| `-d` | Deep mode (10-15 thoughts/steps) | `/serena "architecture design" -d` | Complex systems, major decisions |
| `-c` | Code-focused analysis | `/serena "optimize performance" -c` | Code review, refactoring |
| `-s` | Step-by-step implementation | `/serena "build dashboard" -s` | Full feature development |
| `-v` | Verbose output (show process) | `/serena "debug issue" -v` | Learning, understanding process |
| `-r` | Include research phase | `/serena "choose framework" -r` | Technology decisions |
| `-t` | Create implementation todos | `/serena "new feature" -t` | Project management |

## Usage Patterns

### Basic Usage
```bash
# Simple problem solving
/serena "fix login bug"

# Quick feature implementation  
/serena "add search filter" -q

# Code optimization
/serena "improve load time" -c
```

### Advanced Usage
```bash
# Complex system design with research
/serena "design microservices architecture" -d -r -v

# Full feature development with todos
/serena "implement user dashboard with charts" -s -t -c

# Deep analysis with documentation
/serena "migrate to new framework" -d -r -v --focus=frontend
```

## Context (Auto-gathered)
- Project files: !`find . -maxdepth 2 -name "package.json" -o -name "*.config.*" | head -5 2>/dev/null || echo "No config files"`
- Git status: !`git status --porcelain 2>/dev/null | head -3 || echo "Not git repo"`

## Core Workflow

### 1. Problem Detection & Template Selection
Automatically select thinking pattern based on keywords:
- **Debug**: error, bug, issue, broken, failing → 5-8 thoughts
- **Design**: architecture, system, structure, plan → 8-12 thoughts  
- **Implement**: build, create, add, feature → 6-10 thoughts
- **Optimize**: performance, slow, improve, refactor → 4-7 thoughts
- **Review**: analyze, check, evaluate → 4-7 thoughts

### 2. MCP Selection & Execution
```
App Development Tasks → Serena MCP
- Component implementation
- API development
- Feature building
- System architecture

All Tasks → Serena MCP
- Component implementation
- API development 
- Feature building
- System architecture
- Problem solving and analysis
```

### 3. Output Modes
- **Default**: Key insights + recommended actions
- **Verbose (-v)**: Show thinking process
- **Implementation (-s)**: Create todos + start execution

## Problem-Specific Templates

### Debug Pattern (5-8 thoughts)
1. Symptom analysis & reproduction
2. Error context & environment check  
3. Root cause hypothesis generation
4. Evidence gathering & validation
5. Solution design & risk assessment
6. Implementation plan
7. Verification strategy
8. Prevention measures

### Design Pattern (8-12 thoughts)  
1. Requirements clarification
2. Constraints & assumptions
3. Stakeholder analysis
4. Architecture options generation
5. Option evaluation (pros/cons)
6. Technology selection
7. Design decisions & tradeoffs
8. Implementation phases
9. Risk mitigation
10. Success metrics
11. Validation plan
12. Documentation needs

### Implementation Pattern (6-10 thoughts)
1. Feature specification & scope
2. Technical approach selection
3. Component/module design
4. Dependencies & integration points
5. Implementation sequence
6. Testing strategy
7. Edge case handling
8. Performance considerations
9. Error handling & recovery
10. Deployment & rollback plan

### Review/Optimize Pattern (4-7 thoughts)
1. Current state analysis
2. Bottleneck identification
3. Improvement opportunities
4. Solution options & feasibility
5. Implementation priority
6. Performance impact estimation
7. Validation & monitoring plan

## Advanced Options

**Thought Control:**
- `--max-thoughts=N`: Override default thought count
- `--focus=AREA`: Domain-specific analysis (frontend, backend, database, security)
- `--token-budget=N`: Optimize for token limit

**Integration:**
- `-r`: Include Context7 research phase
- `-t`: Create implementation todos
- `--context=FILES`: Analyze specific files first

**Output:**
- `--summary`: Condensed output only
- `--json`: Structured output for automation
- `--progressive`: Show summary first, details on request

## Task Execution

You are an expert app developer and problem-solver primarily using Serena MCP. For each request:

1. **Auto-detect problem type** and select appropriate approach
2. **Use Serena MCP**:
   - **All development tasks**: Use Serena MCP tools (https://github.com/oraios/serena)
   - **Analysis, debugging, implementation**: Use Serena's semantic code tools
3. **Execute structured approach** with chosen MCP
4. **Research relevant docs** with Context7 MCP if needed
5. **Synthesize actionable solution** with specific next steps
6. **Create implementation todos** if `-s` flag used

**Key Guidelines:**
- **Primary**: Use Serena MCP tools for all tasks (components, APIs, features, analysis)
- **Leverage**: Serena's semantic code retrieval and editing capabilities
- **Cross-Command**: Share context and memory across all command interactions
- **Project-Aware**: Automatically adapt to project structure and patterns
- Start with problem analysis, end with concrete actions
- Balance depth with token efficiency
- Always provide specific, actionable recommendations
- Consider security, performance, and maintainability
- **Memory Integration**: Build and maintain project knowledge over time

**Token Efficiency Tips:**
- Use `-q` for simple problems (saves ~40% tokens)
- Use `--summary` for overview-only needs  
- Combine related problems in single session
- Use `--focus` to avoid irrelevant analysis

## Integration with Other Commands

### Command Ecosystem Integration

Serena MCP is the **primary codebase analysis engine** for all Claude Code commands when in project directories. Other commands automatically leverage Serena's capabilities:

| Command | Serena Integration | Purpose |
|---------|-------------------|----------|
| `/commit` | Git history + change analysis | Intelligent commit messages |
| `/debug-error` | Symbol tracking + pattern search | Smart debugging |
| `/smart-think` | Codebase context + memory | Architecture-aware thinking |
| `/tech-research` | Implementation context + patterns | Codebase-aware research |

### Cross-Command Workflows

#### Development Workflow
```bash
# 1. Research with codebase awareness
/tech-research "authentication methods" --mcp "serena,context7" --current-patterns

# 2. Implement based on research
/serena "implement JWT auth with refresh tokens" -s -t --use-research-context

# 3. Debug any issues
/debug-error "auth token validation failing" --serena --pattern-search

# 4. Think through optimization
/smart-think "optimize auth performance" -m think-hard --serena --current-metrics

# 5. Commit with intelligent analysis
/commit --analyze --serena-context --learning
```

#### Architecture Planning Workflow
```bash
# 1. Deep architectural thinking
/smart-think "design microservices architecture" -m ultrathink --serena --implementation-ready

# 2. Research specific technologies
/tech-research "service mesh options" --mcp "serena,context7" --architecture-context

# 3. Implement architecture components
/serena "create service discovery component" -s -c --architecture-aware

# 4. Commit architectural changes
/commit --scope="architecture" --serena-deep --document-decisions
```

#### Debugging and Optimization Workflow
```bash
# 1. Systematic debugging with Serena
/debug-error "performance bottleneck in API" --serena-deep --trace --memory

# 2. Research optimization strategies
/tech-research "API performance optimization" --mcp "serena" --current-bottlenecks

# 3. Think through implementation approach
/smart-think "optimize database queries" -m think-hard --serena --impact-analysis

# 4. Implement optimizations
/serena "optimize user queries with caching" -c --performance-focused

# 5. Commit performance improvements
/commit --scope="performance" --analyze --before-after-metrics
```

### Project Directory Auto-Detection

When commands are run in project directories, Serena integration is **automatically enabled**:

#### Auto-Detection Criteria
- Presence of `package.json`, `pyproject.toml`, `Cargo.toml`, etc.
- Git repository with commit history
- Existing code structure and patterns
- Previous Serena memory for the project

#### Automatic Features
```bash
# In project directory - Serena automatically enabled
/commit                    # → Uses Serena for change analysis
/debug-error "bug"         # → Uses Serena for symbol tracking
/smart-think "decision"    # → Uses Serena for context
/tech-research "topic"     # → Uses Serena for implementation context
```

### Memory Continuity Across Commands

#### Shared Context
- **Research Findings**: `/tech-research` findings available to `/serena`
- **Debugging Insights**: `/debug-error` patterns inform `/smart-think`
- **Architecture Decisions**: `/smart-think` decisions guide `/commit` messages
- **Implementation Patterns**: `/serena` patterns enhance `/debug-error`

#### Memory Keys
```bash
# Store research context for later use
/tech-research "framework selection" --store-context=framework_research

# Use research context in implementation
/serena "implement chosen framework" --use-context=framework_research

# Reference previous debugging session
/debug-error "similar issue" --use-memory=previous_auth_bug

# Build on architectural thinking
/smart-think "extend architecture" --continue-from=microservices_design
```

### Command Chaining and Dependencies

#### Sequential Execution
```bash
# Research → Think → Implement → Commit pipeline
/tech-research "state management" --save-findings && \
/smart-think "choose state solution" --use-research && \
/serena "implement chosen solution" --use-decisions && \
/commit --intelligent --context-aware
```

#### Conditional Workflows
```bash
# Debug first, then optimize based on findings
/debug-error "slow queries" --analyze --store-findings
# If critical performance issue found:
/smart-think "query optimization strategy" --use-debug-findings
/serena "implement query optimizations" --performance-critical
```

### Best Practices for Multi-Command Workflows

#### 1. Start with Analysis
```bash
# Always understand before implementing
/tech-research "requirements" --codebase-context
/smart-think "approach" --use-research --serena
/serena "implement" --use-decisions
```

#### 2. Use Context Continuity
```bash
# Pass context between commands
/debug-error "issue" --store-context=bug_analysis
/smart-think "solution" --use-context=bug_analysis
/serena "fix" --use-solution --validate
```

#### 3. Document Decisions
```bash
# Create decision trail
/smart-think "architecture choice" --document-rationale
/tech-research "validate choice" --reference-decision
/commit "implement architecture" --include-rationale
```

#### 4. Leverage Learning
```bash
# Build on previous work
/serena "new feature" --similar-to=previous_feature
/debug-error "issue" --pattern-match=similar_bugs
/smart-think "improvement" --learn-from=past_decisions
```

### Error Handling and Recovery

#### Command Failure Recovery
```bash
# If implementation fails
/serena "implement feature" || /debug-error "implementation failure" --auto-context

# If research is insufficient
/tech-research "topic" --insufficient-info && /smart-think "approach with unknowns"

# If commit analysis fails
/commit --analyze || /commit --manual-message --context-aware
```

#### Context Preservation
- **Automatic Backup**: Serena automatically backs up context between commands
- **Recovery Mode**: Commands can recover context from previous sessions
- **Error Context**: Failed operations provide context for debugging commands

### Integration Configuration

#### Per-Project Settings
```bash
# Configure project-specific Serena behavior
# In .claude/serena-config.json:
{
  "auto_enable": true,
  "memory_retention": "30_days",
  "context_sharing": {
    "commit": true,
    "debug": true,
    "research": true,
    "thinking": true
  },
  "integration_level": "deep"
}
```

#### Command Aliases with Serena
```bash
# Smart aliases that always use Serena
alias scommit="/commit --serena-deep --learning"
alias sdebug="/debug-error --serena --pattern-search --memory"
alias sthink="/smart-think --serena --context-aware"
alias sresearch="/tech-research --mcp serena,context7 --implementation-ready"
```