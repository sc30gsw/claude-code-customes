---
description: Execute spec tasks using TDD methodology
allowed-tools: mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, Bash, Read, Write, Edit, MultiEdit, Grep, Glob, LS, WebFetch
argument-hint: <feature-name> <task-numbers>
---

# Execute Spec Tasks with TDD

Execute implementation tasks from spec using Kent Beck's Test-Driven Development methodology.

## Arguments: $ARGUMENTS

## Current Specs
Available specs: !`ls .kiro/specs/ 2>/dev/null || echo "No specs found"`

## Instructions

### Help Mode (--help)
If arguments contain "--help", show usage:
```
/kiro:spec-impl <feature-name> <task-numbers>

Examples:
  /kiro:spec-impl auth-system 1.1            # Execute task 1.1
  /kiro:spec-impl auth-system 1,2,3          # Execute tasks 1, 2, 3
  /kiro:spec-impl auth-system --all          # Execute all pending tasks
```

### Pre-Execution Validation
Feature name: !`echo "$ARGUMENTS" | awk '{print $1}'`

Validate required files exist:
- Requirements: !`FEATURE=$(echo "$ARGUMENTS" | awk '{print $1}'); [ -n "$FEATURE" ] && [ -f ".kiro/specs/$FEATURE/requirements.md" ] && echo "Found" || echo "Missing"`
- Design: !`FEATURE=$(echo "$ARGUMENTS" | awk '{print $1}'); [ -n "$FEATURE" ] && [ -f ".kiro/specs/$FEATURE/design.md" ] && echo "Found" || echo "Missing"`
- Tasks: !`FEATURE=$(echo "$ARGUMENTS" | awk '{print $1}'); [ -n "$FEATURE" ] && [ -f ".kiro/specs/$FEATURE/tasks.md" ] && echo "Found" || echo "Missing"`
- Metadata: !`FEATURE=$(echo "$ARGUMENTS" | awk '{print $1}'); [ -n "$FEATURE" ] && [ -f ".kiro/specs/$FEATURE/spec.json" ] && echo "Found" || echo "Missing"`

### Context Loading
**Load all required content before execution:**

**Core Steering:**
- Structure: @.kiro/steering/structure.md
- Tech Stack: @.kiro/steering/tech.md  
- Product: @.kiro/steering/product.md

**Custom Steering:**
Additional files: !`find .kiro/steering -name "*.md" ! -name "structure.md" ! -name "tech.md" ! -name "product.md" 2>/dev/null || echo "None"`

**Spec Documents:**
Feature directory: !`echo "$ARGUMENTS" | awk '{print $1}'`
- Requirements: @.kiro/specs/[FEATURE]/requirements.md
- Design: @.kiro/specs/[FEATURE]/design.md
- Tasks: @.kiro/specs/[FEATURE]/tasks.md

**Note**: [FEATURE] will be replaced with actual feature name during execution

### Task Execution
1. **Parse feature name and task numbers** from arguments
2. **Load all context** (steering + spec documents)
3. **Extract checkboxes** from tasks.md: !`FEATURE=$(echo "$ARGUMENTS" | awk '{print $1}'); [ -n "$FEATURE" ] && grep -n "^- \\[ \\]\\|^- \\[x\\]" .kiro/specs/$FEATURE/tasks.md || echo "No feature specified"`
4. **Execute each checkbox** using TDD methodology directly

### For Each Task Checkbox
Execute using TDD methodology directly:

**Implementation Steps:**
1. **Load Project Context** (read these files first):
   - Structure: .kiro/steering/structure.md  
   - Tech Stack: .kiro/steering/tech.md
   - Product: .kiro/steering/product.md
   - Custom steering files: !`find .kiro/steering -name "*.md" ! -name "structure.md" ! -name "tech.md" ! -name "product.md" 2>/dev/null || echo "None"`
   - Spec Metadata: .kiro/specs/[FEATURE]/spec.json
   - Requirements: .kiro/specs/[FEATURE]/requirements.md
   - Design: .kiro/specs/[FEATURE]/design.md
   - All Tasks: .kiro/specs/[FEATURE]/tasks.md

2. **TDD Implementation** for each specific task:
   - **RED**: Write failing tests first
   - **GREEN**: Write minimal code to pass tests
   - **REFACTOR**: Clean up and improve code structure

3. **Task Completion**:
   - Verify all tests pass
   - Update checkbox from `- [ ]` to `- [x]` in .kiro/specs/[FEATURE]/tasks.md
   - Ensure no regressions in existing tests

**For each task:**
- Extract exact checkbox content from tasks.md
- Follow Kent Beck's TDD methodology strictly
- Implement only the specific task requirements
- Maintain code quality and test coverage

## Implementation Logic

1. **Parse Arguments**:
   - Feature name: First argument
   - Task numbers: Second argument (support: "1", "1,2,3", "--all")

2. **Validate**:
   - Spec directory exists
   - Required files (requirements.md, design.md, tasks.md, spec.json) exist
   - Spec is approved for implementation

3. **Execute**:
   - **Load all file contents** into memory first
   - **Build complete context** for implementation
   - **Execute each task sequentially** using TDD methodology
   - Each task implementation receives complete project knowledge

## Error Handling

- Spec not found: Run /kiro:spec-init first
- Not approved: Complete spec workflow first
- Task failure: Keep checkbox unchecked, show error

## Success Metrics

- All selected checkboxes marked [x] in tasks.md
- Tests pass
- No regressions