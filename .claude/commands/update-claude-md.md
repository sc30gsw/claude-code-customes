---
allowed-tools: Read, Glob, Grep, Edit, MultiEdit, Write, Bash, TodoWrite, mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, mcp__sequential-thinking__sequentialthinking
description: Intelligent command for automatically generating and updating project-specific CLAUDE.md (Serena + Sequential Thinking integration)
---

## Context

- Current project: @package.json
- Existing CLAUDE.md: !`test -f CLAUDE.md && echo "Found" || echo "Not found"`
- Project docs: !`find . -maxdepth 2 -name "*.md" | grep -E "(README|COMMANDS|SUB-AGENTS)" | head -5`
- Docs directory: !`find . -name "docs" -type d | head -3`
- Project structure: !`find . -maxdepth 2 -name "package.json" -o -name "*.config.*" | head -5 2>/dev/null || echo "No config files"`
- Git context: !`git status --porcelain 2>/dev/null | head -3 || echo "Not git repo"`
- Framework files: !`find . -name "FLAGS.md" -o -name "PRINCIPLES.md" -o -name "RULES.md" | head -3`

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ for codebase analysis and mcp__sequential-thinking__ for complex reasoning:**

### Primary Analysis Engine (Serena MCP)
- **Project Structure**: Use `mcp__serena__list_dir` for understanding project layout
- **File Discovery**: Use `mcp__serena__find_file` for locating relevant documentation
- **Content Analysis**: Use `mcp__serena__search_for_pattern` for finding specific patterns
- **Memory Integration**: Use `mcp__serena__write_memory` / `mcp__serena__read_memory` for project knowledge

### Strategic Thinking Engine (Sequential Thinking MCP)
- **Content Planning**: Use `mcp__sequential-thinking__sequentialthinking` for CLAUDE.md structure planning
- **Integration Strategy**: Use structured thinking for merging multiple document sources
- **Quality Assessment**: Use reasoning for validating generated content

### Supporting Tools (Standard)
- **File Operations**: Use Read, Write, Edit for document processing
- **Search Operations**: Use Glob, Grep for fallback search when MCP unavailable
- **Process Management**: Use TodoWrite for complex task breakdown

# Update CLAUDE.md: Automatic Project-Specific CLAUDE.md Generation

Analyzes project documentation and automatically generates/updates CLAUDE.md

## Quick Reference

```bash
/update-claude-md                    # Basic update with auto-detection
/update-claude-md --auto --backup    # Auto-detection + backup
/update-claude-md --files README.md COMMANDS.md  # Specific file specification
/update-claude-md --preview          # Preview only
/update-claude-md --template kiro    # Use Kiro template
```

## Core Options

| Option | Short | Description | Default | Example |
|--------|-------|-------------|---------|---------|
| `--files` | `-f` | Specify files | Auto-detect | `-f README.md COMMANDS.md` |
| `--auto` | `-a` | Auto-detect MD files | true | `-a` |
| `--backup` | `-b` | Backup existing CLAUDE.md | false | `-b` |
| `--preview` | `-p` | Show preview before update | false | `-p` |
| `--include-docs` | `-d` | Include docs directory | false | `-d` |
| `--structure` | `-s` | Analyze project structure | false | `-s` |
| `--template` | `-t` | Specify template | auto | `-t kiro` |
| `--merge` | `-m` | Merge with existing content | false | `-m` |
| `--output` | `-o` | Output filename | CLAUDE.md | `-o CLAUDE_NEW.md` |

## Advanced Options

| Option | Description | Usage | Example |
|--------|-------------|-------|---------|
| `--exclude` | Exclude pattern specification | `--exclude "test/*,*.tmp"` | Exclude test files |
| `--sections` | Include section specification | `--sections "context,workflow"` | Specific sections only |
| `--framework` | Framework element control | `--framework minimal` | Minimal Framework |
| `--language` | Output language | `--language en` | English output |
| `--format` | Output format | `--format structured` | Structured format |
| `--validate` | Post-generation validation | `--validate strict` | Strict validation |
| `--memory-key` | Serena memory key | `--memory-key claude_md_config` | Configuration memory |

## Usage Patterns

### Basic Usage
```bash
# Standard update (auto-detection)
/update-claude-md

# Safe update with backup
/update-claude-md --backup --preview

# Use specific files only
/update-claude-md --files README.md COMMANDS.md SUB-AGENTS.md
```

### Advanced Usage
```bash
# Detailed update with comprehensive analysis
/update-claude-md --auto --include-docs --structure --backup

# Kiro project-specific template
/update-claude-md --template kiro --sections "context,workflow,kiro" --validate

# Merge mode to preserve existing content
/update-claude-md --merge --exclude "*.tmp,test/*" --memory-key project_context
```

### Template-Specific Usage
```bash
# Kiro spec-driven development project
/update-claude-md --template kiro --include-docs --structure

# Regular development project
/update-claude-md --template standard --auto --backup

# Minimal configuration
/update-claude-md --template minimal --files README.md --framework minimal
```

## Context (Auto-gathered)
- Project files: !`find . -maxdepth 2 -name "*.md" | head -5 2>/dev/null || echo "No markdown files"`
- Git status: !`git status --porcelain 2>/dev/null | head -3 || echo "Not git repo"`

## Core Workflow

### 1. Project Analysis & File Discovery
Automatic project structure analysis using Serena MCP:
- **Auto Detection**: Automatic detection of README.md, COMMANDS.md, SUB-AGENTS.md, etc.
- **Structure Analysis**: Analysis of project directory structure
- **Pattern Recognition**: Identification of project types (Kiro, Standard, Minimal)
- **Memory Integration**: Utilization of past settings and learning content

### 2. Content Integration Strategy
Integration strategy formulation using Sequential Thinking MCP:
- **Source Priority**: Determining importance of each document and merge order
- **Conflict Resolution**: Resolution strategies for conflicting information
- **Template Selection**: Selecting optimal template for the project
- **Framework Integration**: Integration methods for framework components

### 3. CLAUDE.md Generation
```
Source Analysis → Template Application → Content Generation → Validation
- README.md: Project overview and context
- COMMANDS.md: Available commands and workflow
- SUB-AGENTS.md: Agent integration information
- docs/: Detailed documentation and specifications
- Project Structure: File composition and patterns
```

### 4. Quality Assurance & Validation
- **Content Validation**: Syntax and structure check of generated CLAUDE.md
- **Framework Compliance**: Verification of framework requirements compliance
- **Project Specificity**: Verification of appropriate integration of project-specific information

## Template System

### Available Templates

#### Kiro Template (`--template kiro`)
Dedicated to Kiro spec-driven development projects:
```markdown
# Kiro Spec-Driven Development
- Steering vs Specification explanation
- Phase-based workflow (Requirements → Design → Tasks → Implementation)
- Kiro command integration (/kiro:steering, /kiro:spec-*)
- .kiro/steering/ and .kiro/specs/ management
```

#### Standard Template (`--template standard`)
General development projects:
```markdown
# Project Context
- Project overview and context
- Development guidelines and workflow
- Available commands and agents
- File structure and patterns
```

#### Minimal Template (`--template minimal`)
Lightweight configuration:
```markdown
# Project Context
- Basic project information only
- Minimal framework references
- Simple workflow
```

### Template Customization
```bash
# Custom template creation
/update-claude-md --template custom --sections "intro,context,commands,workflow" --framework full

# Existing template extension
/update-claude-md --template kiro --sections "+testing,+deployment" --validate strict
```

## Advanced Features

### Intelligent File Discovery
**Serena MCP Integration:**
- **Pattern Matching**: Automatic identification of related files within the project
- **Content Analysis**: Relevance evaluation of file contents
- **Dependency Tracking**: Analysis of inter-file dependencies

### Content Merging Strategies
**Sequential Thinking MCP Integration:**
- **Conflict Resolution**: Determining integration methods for duplicate information
- **Priority Weighting**: Prioritization based on importance of information sources
- **Context Preservation**: Maintaining important context information

### Memory-Driven Configuration
**Serena Memory System:**
```bash
# Project configuration memory
/update-claude-md --memory-key project_config --auto --include-docs

# Reuse of memorized configurations
/update-claude-md --use-memory project_config --validate
```

## Integration with Other Commands

### Command Ecosystem Integration

CLAUDE.md updates seamlessly integrate with other commands:

| Command | Integration | Purpose |
|---------|-------------|----------|
| `/kiro:steering` | Steering document analysis | Kiro project integration |
| `/serena` | Project memory utilization | Context continuity |
| `/smart-think` | Structured thinking application | Integration strategy formulation |
| `/commit` | Project change analysis | Latest state reflection |

### Workflow Integration Examples

#### Initial Project Setup
```bash
# 1. Project analysis
/smart-think "CLAUDE.md configuration strategy" --serena --project-context

# 2. Initial CLAUDE.md generation
/update-claude-md --auto --include-docs --structure --backup --memory-key initial_setup

# 3. Save to Serena project memory
/serena "Memory: Project setup completed" --store-config
```

#### Continuous Updates
```bash
# 1. Project change detection
/commit --analyze --detect-changes

# 2. CLAUDE.md update based on changes
/update-claude-md --use-memory project_config --merge --validate

# 3. Save update records
/serena "Memory: CLAUDE.md update - $(date)" --update-config
```

#### Kiro Project Workflow
```bash
# 1. Steering document generation
/kiro:steering --update-context

# 2. CLAUDE.md integrated update
/update-claude-md --template kiro --include-steering --validate strict

# 3. Specification progress reflection
/kiro:spec-status --update-claude-md
```

## Output Examples

### Generated CLAUDE.md Structure
```markdown
# What I want you to do
[User-specific instructions]

# ═══════════════════════════════════════════════════
# Framework Components
# ═══════════════════════════════════════════════════

# Core Framework
@FLAGS.md
@PRINCIPLES.md
@RULES.md

# MCP Documentation
@MCP_Context7.md
@MCP_Playwright.md
@MCP_Sequential.md
@MCP_Serena.md

# Behavioral Modes
@MODE_Brainstorming.md
@MODE_Introspection.md
@MODE_Orchestration.md
@MODE_Task_Management.md
@MODE_Token_Efficiency.md

# [Project Name] - [Project Type]

[Auto-generated project description from README.md]

## Project Context

### [Auto-detected sections]
- [Paths, URLs, Configuration from analysis]

### [Available Commands]
[Integrated from COMMANDS.md]

### [Sub-agents]
[Integrated from SUB-AGENTS.md]

## Development Guidelines
[Project-specific guidelines from docs analysis]

## Workflow
[Project-specific workflow from structure analysis]
```

## Task Execution

You are an expert CLAUDE.md generator using Serena MCP and Sequential Thinking MCP. For each request:

1. **Project Analysis** with Serena MCP:
   - **Structure Discovery**: `mcp__serena__list_dir` for project layout
   - **File Detection**: `mcp__serena__find_file` for relevant documents
   - **Pattern Search**: `mcp__serena__search_for_pattern` for specific content
   - **Memory Integration**: `mcp__serena__read_memory` for project history

2. **Strategic Planning** with Sequential Thinking MCP:
   - **Template Selection**: `mcp__sequential-thinking__sequentialthinking` for optimal template choice
   - **Integration Strategy**: Structured reasoning for content merging approach
   - **Quality Framework**: Evidence-based validation planning

3. **Content Generation**:
   - **Framework Integration**: Integration of essential components
   - **Project Context**: Integration of unique information based on analysis results
   - **Command Integration**: Command information integration from COMMANDS.md
   - **Agent Integration**: Agent information integration from SUB-AGENTS.md

4. **Validation & Optimization**:
   - **Syntax Validation**: Syntax check of generated Markdown
   - **Content Coherence**: Verification of information consistency and completeness
   - **Framework Compliance**: Framework requirements compliance verification

**Key Guidelines:**
- **Primary**: Project understanding through Serena MCP and strategic thinking through Sequential Thinking MCP
- **Memory-Driven**: Accumulation and utilization of project-specific learning and settings
- **Template-Aware**: Optimal template selection according to project type
- **Quality-First**: High-quality assurance through pre-generation planning and post-generation verification
- **Integration-Focused**: Workflow optimization through integration with other commands

**Success Metrics:**
- ✅ Complete framework integration
- ✅ Accurate reflection of project-specific information
- ✅ Information integration from existing documents
- ✅ Adaptability to future updates
- ✅ Interoperability with other commands

**Error Handling:**
- **Missing Files**: Automatically skip and continue with available files
- **Parse Errors**: Log error files and continue with other files
- **Template Issues**: Fallback to default template
- **Memory Conflicts**: Prioritize latest information and update old memories