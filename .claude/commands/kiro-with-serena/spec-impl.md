---
description: Execute spec tasks using TDD methodology
allowed-tools: mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, Bash, Read, Write, Edit, MultiEdit, Grep, Glob, LS, WebFetch, WebSearch
argument-hint: <feature-name> [task-numbers]
---

# Execute Spec Tasks with TDD

Execute implementation tasks for **$1** using Kent Beck's Test-Driven Development methodology.

## Instructions

### Pre-Execution Validation
Validate required files exist for feature **$1**:
- Requirements: `.kiro/specs/$1/requirements.md`
- Design: `.kiro/specs/$1/design.md`  
- Tasks: `.kiro/specs/$1/tasks.md`
- Metadata: `.kiro/specs/$1/spec.json`

### Context Loading

**Core Steering:**
- Structure: @.kiro/steering/structure.md
- Tech Stack: @.kiro/steering/tech.md  
- Product: @.kiro/steering/product.md

**Custom Steering:**
- Additional `*.md` files in `.kiro/steering/` (excluding structure.md, tech.md, product.md)

**Spec Documents for $1:**
- Metadata: @.kiro/specs/$1/spec.json
- Requirements: @.kiro/specs/$1/requirements.md
- Design: @.kiro/specs/$1/design.md
- Tasks: @.kiro/specs/$1/tasks.md

### Task Execution
1. **Feature**: $1  
2. **Task numbers**: $2 (optional, defaults to all pending tasks)
3. **Load all context** (steering + spec documents)
4. **Execute selected tasks** using TDD methodology

### TDD Implementation
For each selected task:

1. **RED**: Write failing tests first
2. **GREEN**: Write minimal code to pass tests  
3. **REFACTOR**: Clean up and improve code structure
4. **Verify**: 
   - All tests pass
   - No regressions in existing tests
   - Code quality and test coverage maintained
5. **Mark Complete**: Update checkbox from `- [ ]` to `- [x]` in tasks.md

**Note**: Follow Kent Beck's TDD methodology strictly, implementing only the specific task requirements.

## Implementation Notes

- **Feature**: Use `$1` for feature name
- **Tasks**: Use `$2` for specific task numbers (optional)
- **Validation**: Check all required spec files exist
- **TDD Focus**: Always write tests before implementation
- **Task Tracking**: Update checkboxes in tasks.md as completed
