---
allowed-tools: Bash(gh:*), Bash(git:*), mcp__context7__resolve-library-id, mcp__context7__get-library-docs
description: Generate PR description and automatically create pull request on GitHub
---

## Context

- Current git status: !`git status`
- Changes in this PR: !`git diff develop...HEAD 2>/dev/null || git diff main...HEAD 2>/dev/null || git diff master...HEAD 2>/dev/null || git diff HEAD~1...HEAD`
- Commits in this PR: !`git log --oneline develop..HEAD 2>/dev/null || git log --oneline main..HEAD 2>/dev/null || git log --oneline master..HEAD 2>/dev/null || git log --oneline HEAD~1..HEAD`
- PR template: @.github/pull_request_template.md

## Your task

Based on the provided option, perform one of the following actions:

### Options:

- **No option or default**: Generate PR description and create pull request
- **-p**: Push current branch and create pull request
- **-u**: Update existing pull request description only

### Default behavior (no option):

1. Create a PR description following the **exact format** of the PR template in Japanese
2. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
3. **Add a Mermaid diagram** that visualizes the changes made in this PR
4. Execute `gh pr create --draft` with the generated title and description

### With -p option:

1. Push current branch to remote repository using `git push -u origin <current-branch>`
2. Create a PR description following the **exact format** of the PR template in Japanese
3. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
4. **Add a Mermaid diagram** that visualizes the changes made in this PR
5. Execute `gh pr create --draft` with the generated title and description

### With -u option:

1. Create a PR description following the **exact format** of the PR template in Japanese
2. **Use Context7 MCP** to fetch relevant documentation URLs for the Reference section
3. **Add a Mermaid diagram** that visualizes the changes made in this PR
4. Update existing pull request description using `gh pr edit --body <description>`

### Requirements:

1. Follow the template structure exactly
2. Use Japanese for all content
3. Include specific implementation details
4. List concrete testing steps
5. Use Context7 MCP to fetch official documentation URLs for libraries/frameworks used in the changes:
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