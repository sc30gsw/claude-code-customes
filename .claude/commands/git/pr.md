---
allowed-tools: mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__list_dir, Bash(gh:*), Bash(git:*), mcp__context7__resolve-library-id, mcp__context7__get-library-docs
description: Generate PR description and automatically create pull request on GitHub
---

## Context

- Current git status: !`git status`
- Changes in this PR: !`git diff develop...HEAD 2>/dev/null || git diff main...HEAD 2>/dev/null || git diff master...HEAD 2>/dev/null || git diff HEAD~1...HEAD`
- Commits in this PR: !`git log --oneline develop..HEAD 2>/dev/null || git log --oneline main..HEAD 2>/dev/null || git log --oneline master..HEAD 2>/dev/null || git log --oneline HEAD~1..HEAD`
- PR template: @.github/pull_request_template.md

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools when available:**

### File Operations (Use Serena MCP First)
- **Reading files**: Use `mcp__serena__find_file` → `Bash(git:*)` (fallback)
- **Searching patterns**: Use `mcp__serena__search_for_pattern` → `Bash(git:*)` (fallback)
- **Directory listing**: Use `mcp__serena__list_dir` → `Bash(git:*)` (fallback)
- **Finding symbols**: Use `mcp__serena__find_symbol` → `Bash(git:*)` (fallback)

### Code Analysis (Serena MCP Exclusive)
- **Symbol overview**: Use `mcp__serena__get_symbols_overview`
- **Symbol references**: Use `mcp__serena__find_referencing_symbols`
- **Code replacement**: Use `mcp__serena__replace_symbol_body` → fallbacks
- **Pattern replacement**: Use `mcp__serena__replace_regex` → fallbacks

## Your task

Based on the provided option, perform one of the following actions:

### Options:

- **No option or default**: Generate PR description and create pull request
- **-p**: Push current branch and create pull request
- **-u**: Update existing pull request description only

### Default behavior (no option):

1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. **Analyze Changes**: Use `mcp__serena__search_for_pattern` to analyze git diff and `mcp__serena__get_symbols_overview` for code understanding
3. **Read PR Template**: Use `mcp__serena__find_file` to read PR template → fallback to direct file reading
4. Create a PR description following the **exact format** of the PR template in Japanese
5. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
6. **Add a Mermaid diagram** that visualizes the changes made in this PR
7. **Progress Check**: Use `mcp__serena__think_about_task_adherence` to verify completeness
8. Execute `gh pr create --draft` with the generated title and description
9. **Store Pattern**: Use `mcp__serena__write_memory` to store successful PR patterns

### With -p option:

1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. Push current branch to remote repository using `git push -u origin <current-branch>`
3. **Analyze Changes**: Use `mcp__serena__search_for_pattern` to analyze git diff and `mcp__serena__get_symbols_overview` for code understanding
4. **Read PR Template**: Use `mcp__serena__find_file` to read PR template → fallback to direct file reading
5. Create a PR description following the **exact format** of the PR template in Japanese
6. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
7. **Add a Mermaid diagram** that visualizes the changes made in this PR
8. **Progress Check**: Use `mcp__serena__think_about_task_adherence` to verify completeness
9. Execute `gh pr create --draft` with the generated title and description
10. **Store Pattern**: Use `mcp__serena__write_memory` to store successful PR patterns

### With -u option:

1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. **Analyze Changes**: Use `mcp__serena__search_for_pattern` to analyze git diff and `mcp__serena__get_symbols_overview` for code understanding
3. **Read PR Template**: Use `mcp__serena__find_file` to read PR template → fallback to direct file reading
4. **Check Previous Patterns**: Use `mcp__serena__read_memory` to retrieve previous PR patterns
5. Create a PR description following the **exact format** of the PR template in Japanese
6. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
7. **Add a Mermaid diagram** that visualizes the changes made in this PR
8. **Progress Check**: Use `mcp__serena__think_about_task_adherence` to verify completeness
9. Update existing pull request description using `gh pr edit --body <description>`
10. **Completion Check**: Use `mcp__serena__think_about_whether_you_are_done` to confirm success

### Requirements:

1. Follow the template structure exactly
2. Use Japanese for all content
3. Include specific implementation details
4. List concrete testing steps
5. Use Context7 MCP to fetch official documentation URLs for libraries/frameworks used in the changes:
   - **Analyze dependencies**: Use `mcp__serena__find_referencing_symbols` to identify used libraries
   - **Think about information**: Use `mcp__serena__think_about_collected_information` to categorize findings
   - Query Context7 MCP for documentation of relevant technologies
   - Include official documentation links in the Reference section
   - Focus on libraries like Next.js, React, TanStack Query, Tailwind CSS, etc. based on the actual changes
6. Always include a Mermaid diagram that shows:
   - Architecture changes (if any)
   - Data flow modifications
   - Component relationships
   - Process flows affected by the changes
7. Be comprehensive but concise

### Mermaid Diagram Guidelines:

- Use appropriate diagram types (flowchart, sequence, class, etc.)
- Show before/after states if applicable
- Highlight new or modified components
- Use consistent styling and colors
- Add the diagram in a dedicated section of the PR description

**Generate the PR description and create the pull request automatically.**