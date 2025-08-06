---
allowed-tools: mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory, Read, Glob, Grep, Edit, MultiEdit, Write, Bash, mcp__context7__resolve-library-id, mcp__context7__get-library-docs
description: Generate comprehensive requirements definition documents with technology selection and improvement suggestions
---

## Context

- Project requirements: @package.json
- Existing documentation: !`find . -name "*.md" | head -10`
- Project structure: !`ls -la`
- Available templates: !`ls -la .claude/templates/requirements/ 2>/dev/null || echo "No templates found"`

## Usage Guide

### Basic Syntax
```bash
/requirements <system_name> [options]
```

### Available Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--app` | `-a` | Application name | `-a "Web Store"` |
| `--function` | `-f` | Function/feature name | `-f "Authentication"` |
| `--file` | | Input file with additional requirements | `--file existing-req.txt` |
| `--output` | `-o` | Output file path (default: requirements.md) | `-o specs.md` |
| `--tech` | `-t` | Technology stack | `-t "react,nodejs,postgresql"` |
| `--priority` | `-p` | Priority level (low\|medium\|high\|critical) | `-p high` |
| `--scope` | `-s` | Scope type (mvp\|full\|enterprise) | `-s mvp` |
| `--suggest` | | Include improvement suggestions | `--suggest` |
| `--examples` | | Include implementation examples | `--examples` |
| `--template` | | Template type (standard\|agile\|waterfall) | `--template agile` |
| `--help` | `-h` | Show help message | `-h` |

### Quick Examples

```bash
# Basic requirements document
/requirements "E-commerce Platform" -a "Web Store" -t "react,nodejs"

# MVP with suggestions
/requirements "Social Media App" -s mvp -p medium --suggest

# Full enterprise system with examples
/requirements "CRM System" -s enterprise -t "react,nodejs,postgresql" --examples --template agile

# Import existing requirements
/requirements "Payment API" --file legacy-specs.txt -t "nodejs,mongodb"
```

## Tool Usage Priorities

**ALWAYS prioritize mcp__serena__ tools over default Claude Code tools when available:**

### File Operations (Use Serena MCP First)
- **Reading files**: Use `mcp__serena__find_file` → `Read` (fallback)
- **Searching patterns**: Use `mcp__serena__search_for_pattern` → `Grep` (fallback)
- **Directory listing**: Use `mcp__serena__list_dir` → `LS` (fallback)
- **Finding symbols**: Use `mcp__serena__find_symbol` → `Glob` (fallback)

### Code Analysis (Serena MCP Exclusive)
- **Symbol overview**: Use `mcp__serena__get_symbols_overview`
- **Symbol references**: Use `mcp__serena__find_referencing_symbols`
- **Code replacement**: Use `mcp__serena__replace_symbol_body` → `Edit` (fallback)
- **Pattern replacement**: Use `mcp__serena__replace_regex` → `MultiEdit` (fallback)

### Memory & Context (Serena MCP Only)
- **Task tracking**: Use `mcp__serena__think_about_task_adherence`
- **Progress checking**: Use `mcp__serena__think_about_whether_you_are_done`
- **Information analysis**: Use `mcp__serena__think_about_collected_information`
- **Memory operations**: Use `mcp__serena__write_memory`, `mcp__serena__read_memory`

## Your Task

Generate comprehensive requirements definition documents based on user inputs and system analysis.

### Execution Flow

#### 1. Pre-execution Setup
1. **Serena Onboarding**: Use `mcp__serena__check_onboarding_performed` and `mcp__serena__onboarding` if needed
2. Analyze project structure using `mcp__serena__list_dir` → `LS` (fallback)
3. Read package.json to understand project context using `mcp__serena__find_file` → `Read` (fallback)
4. Check for existing requirements or documentation files
5. **Progress Tracking**: Use `mcp__serena__think_about_task_adherence` to verify setup completion

#### 2. Requirements Generation

##### Input Processing
1. **Parse Command Arguments**:
   - Extract system name and options
   - Validate priority, scope, and template values
   - Process technology stack specifications

2. **Context Gathering**:
   - Read existing requirements from `--file` if provided
   - Analyze project dependencies for technology context
   - Search for related documentation using `mcp__serena__search_for_pattern`

3. **Template Selection**:
   - **Standard**: General purpose requirements
   - **Agile**: User story format with acceptance criteria
   - **Waterfall**: Detailed specification with phases

#### 3. Content Generation

##### Document Structure Creation
1. **Header Information**:
   - Generation timestamp
   - System name and application details
   - Priority and scope specifications

2. **Main Sections** (based on template):
   - **Functional Requirements**:
     - Core features and capabilities
     - User stories or use cases
     - Acceptance criteria
   
   - **Non-Functional Requirements**:
     - Performance specifications
     - Security requirements
     - Availability and reliability
     - Scalability considerations
   
   - **Technical Specifications**:
     - Architecture overview
     - Technology stack details
     - Integration requirements
     - Data models and schemas

3. **Technology Selection** (if `-t` specified):
   - Use Context7 MCP to reference latest best practices
   - Generate selection rationale
   - Version recommendations
   - Integration considerations

4. **Additional Sections** (if enabled):
   - Implementation examples (--examples)
   - Improvement suggestions (--suggest)
   - Imported requirements (--file)

#### 4. Output Generation

##### File Writing
1. Use `mcp__serena__replace_symbol_body` or `Write` to create output file
2. Default output: `requirements.md` unless specified with `-o`
3. Format with proper Markdown structure
4. Include table of contents for navigation

##### Progress Verification
- Use `mcp__serena__think_about_whether_you_are_done` to confirm completion
- Verify all requested sections are included
- Check document formatting and structure

### Context7 MCP Integration

#### Technology Documentation Reference

Auto-detect and reference documentation for specified technologies:

##### Frontend Frameworks
- **React**: `resolve-library-id: "react"` → Component patterns, hooks, best practices
- **Vue**: `resolve-library-id: "vue"` → Composition API, reactivity, components
- **Angular**: `resolve-library-id: "@angular/core"` → Services, dependency injection, modules

##### Backend Technologies
- **Node.js**: `resolve-library-id: "nodejs"` → API patterns, middleware, performance
- **Express**: `resolve-library-id: "express"` → Routing, middleware, error handling
- **FastAPI**: `resolve-library-id: "fastapi"` → API documentation, validation, async

##### Database Systems
- **PostgreSQL**: Best practices, query optimization, indexing
- **MongoDB**: `resolve-library-id: "mongodb"` → Document design, aggregation, indexing
- **Redis**: `resolve-library-id: "redis"` → Caching strategies, data structures

##### Cloud Platforms
- **AWS**: Service selection, architecture patterns
- **Docker**: `resolve-library-id: "docker"` → Containerization best practices
- **Kubernetes**: `resolve-library-id: "kubernetes"` → Orchestration, scaling, deployment

### Practical Examples

#### 1. E-commerce Platform
```bash
/requirements "E-commerce Platform" \
  -a "Online Store" \
  -t "react,nodejs,postgresql,redis" \
  -p high \
  -s full \
  --template agile \
  --examples \
  --suggest
```

**Generated Sections**:
- User stories for shopping cart, checkout, inventory
- React component architecture examples
- Node.js API endpoint specifications
- PostgreSQL schema design
- Redis caching strategy
- Performance requirements (< 200ms response)
- Security requirements (PCI compliance)

#### 2. API Service with Legacy Integration
```bash
/requirements "Payment API" \
  -f "Transaction Processing" \
  --file legacy-specs.txt \
  -t "nodejs,mongodb" \
  --template standard
```

**Generated Sections**:
- Transaction processing flow
- Legacy system integration requirements
- MongoDB document schemas
- API versioning strategy
- Error handling specifications
- Rate limiting requirements

#### 3. MVP Mobile Application
```bash
/requirements "Social Media App" \
  -a "iOS Client" \
  -s mvp \
  -p medium \
  --template agile
```

**Generated Sections**:
- Core MVP features (post, follow, feed)
- User stories with story points
- Acceptance criteria for each feature
- Definition of Done
- Technical debt considerations
- Phase 2 feature roadmap

### Template Details

#### 1. Standard Template Structure
```markdown
# Requirements Definition: [System Name]

## 1. Overview
### 1.1 Purpose
### 1.2 Background
### 1.3 Expected Benefits

## 2. Functional Requirements
### 2.1 Core Features
### 2.2 User Scenarios
### 2.3 Business Rules

## 3. Non-Functional Requirements
### 3.1 Performance
### 3.2 Security
### 3.3 Availability
### 3.4 Scalability

## 4. Technical Specifications
### 4.1 Architecture
### 4.2 Technology Stack
### 4.3 Integration Points

## 5. Constraints and Assumptions
## 6. Success Criteria
```

#### 2. Agile Template Structure
```markdown
# Product Requirements: [System Name]

## Epic Definition
[High-level feature description]

## User Stories

### Story 1: [Feature Name]
**As a** [user type]
**I want** [goal]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Story Points:** [1-13]

## Definition of Done
- Code reviewed
- Unit tests passing
- Documentation updated
- Deployed to staging
```

#### 3. Waterfall Template Structure
```markdown
# Software Requirements Specification: [System Name]

## 1. Introduction
### 1.1 Purpose
### 1.2 Scope
### 1.3 Definitions

## 2. Overall Description
### 2.1 Product Perspective
### 2.2 Product Functions
### 2.3 User Classes

## 3. Specific Requirements
### 3.1 Functional Requirements
### 3.2 Performance Requirements
### 3.3 Design Constraints

## 4. System Design
### 4.1 Architecture Diagram
### 4.2 Database Design
### 4.3 Interface Design

## 5. Implementation Plan
### 5.1 Development Phases
### 5.2 Testing Strategy
### 5.3 Deployment Plan

## 6. Maintenance and Support
```

### Features

#### Technology Stack Support

When `-t` option is specified, the command:

1. **Technology Analysis**:
   - Parse comma-separated technology list
   - Validate technology compatibility
   - Check for common technology combinations

2. **Documentation Generation**:
   - Selection rationale for each technology
   - Version recommendations based on stability/features
   - Related libraries and frameworks
   - Integration considerations
   - Best practices and patterns

3. **Supported Technologies**:
   - **Frontend**: React, Vue, Angular, Svelte, Next.js
   - **Backend**: Node.js, Python, Java, Go, Ruby
   - **Database**: PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch
   - **Container**: Docker, Kubernetes, Docker Compose
   - **Cloud**: AWS, GCP, Azure, Vercel, Netlify

#### Implementation Examples (`--examples`)

Generate framework-specific code examples:

```typescript
// React Component Example
interface UserProfileProps {
  userId: string;
  onUpdate: (user: User) => void;
}

const UserProfile: React.FC<UserProfileProps> = ({ userId, onUpdate }) => {
  // Implementation based on requirements
};

// Express API Example
app.post('/api/users', async (req, res) => {
  try {
    const user = await createUser(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// PostgreSQL Schema Example
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Improvement Suggestions (`--suggest`)

AI-powered analysis provides:

1. **Architecture Recommendations**:
   - Microservices vs monolithic considerations
   - Caching strategy suggestions
   - Database optimization tips

2. **Security Enhancements**:
   - Authentication/authorization improvements
   - Data encryption recommendations
   - API security best practices

3. **Performance Optimizations**:
   - Query optimization suggestions
   - Caching layer recommendations
   - CDN integration options

4. **Development Process**:
   - CI/CD pipeline suggestions
   - Testing strategy recommendations
   - Monitoring and logging setup

### Output Format

The generated document includes:

1. **Header Information**
   - Generation timestamp
   - System name
   - Application name (if specified)
   - Function name (if specified)
   - Priority level
   - Scope

2. **Main Content** (based on selected template)
   - Requirements sections
   - Technical specifications
   - User stories or use cases

3. **Technology Selection** (if specified)
   - Selected technologies with rationale
   - Version recommendations
   - Integration considerations

4. **Additional Sections** (if enabled)
   - Implementation examples
   - Improvement suggestions
   - Additional requirements from file

#### Execution Completion Report

```markdown
📋 Requirements Definition Generated

📁 Output File: requirements.md
📏 Document Size: 2,456 lines
📑 Sections Created: 12

✅ Included Features:
- ✓ Functional Requirements (45 items)
- ✓ Non-Functional Requirements (18 items)
- ✓ Technology Stack Analysis
- ✓ Implementation Examples
- ✓ Improvement Suggestions

🛠️ Technology Stack:
- Frontend: React 18.2.0
- Backend: Node.js 20.x with Express 4.18
- Database: PostgreSQL 15
- Cache: Redis 7.0

📊 Metrics:
- User Stories: 23
- Total Story Points: 144
- Estimated Timeline: 3-4 sprints
```

### Error Handling & Limitations

#### Common Issues

1. **Missing System Name**:
   ```bash
   ❌ Error: System name is required
   Usage: /requirements "System Name" [options]
   ```

2. **Invalid Template Type**:
   ```bash
   ❌ Error: Invalid template 'custom'
   Valid templates: standard, agile, waterfall
   ```

3. **File Not Found**:
   ```bash
   ❌ Error: Cannot read file 'requirements.txt'
   Please verify file path and permissions
   ```

#### Limitations

- Maximum file input size: 100KB
- Technology stack limited to 10 technologies
- Output file size may be large for enterprise scope
- Examples are framework-specific and may need customization

### Best Practices

#### Writing Good Requirements

1. **Be Specific and Measurable**
   - ❌ "The system should be fast"
   - ✅ "The system should respond within 200ms for 95% of requests"

2. **Use Clear Language**
   - Avoid ambiguous terms
   - Define technical terminology
   - Use consistent vocabulary

3. **Prioritize Requirements**
   - Use MoSCoW method (Must, Should, Could, Won't)
   - Consider business value vs. effort
   - Identify dependencies

4. **Include Acceptance Criteria**
   - Define "Definition of Done"
   - Specify test scenarios
   - Include edge cases

5. **Maintain Traceability**
   - Link requirements to business objectives
   - Track changes and versions
   - Document decisions and rationale

#### Review Checklist

- [ ] All stakeholders identified
- [ ] Requirements are testable
- [ ] Non-functional requirements included
- [ ] Dependencies documented
- [ ] Risks identified and mitigated
- [ ] Compliance requirements addressed
- [ ] User experience considered
- [ ] Technical constraints defined

### Integration Workflow

1. **Requirements Generation**:
   ```bash
   /requirements "Project Name" -t "react,nodejs" --suggest
   ```

2. **Implementation Planning**:
   - Convert requirements to user stories
   - Create development tasks
   - Estimate effort and timeline

3. **Development Tracking**:
   - Use generated requirements as reference
   - Update requirements as needed
   - Track implementation progress

4. **Testing Strategy**:
   - Generate test cases from requirements
   - Ensure coverage of all requirements
   - Validate acceptance criteria

### Future Enhancements

- **Diagram Generation**: Mermaid diagrams for architecture visualization
- **Effort Estimation**: Automated story point calculation
- **Requirements Validation**: Completeness and consistency checks
- **Export Formats**: PDF, HTML, Confluence integration
- **AI Review**: Quality assessment and gap analysis
- **Collaboration**: Multi-user editing and commenting
- **Metrics**: Complexity analysis and traceability matrix