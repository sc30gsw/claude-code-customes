#!/usr/bin/env python3
"""
Template Generator
Generates document templates with project-specific metadata injection.
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime


class TemplateGenerator:
    """Generates documentation templates"""

    TEMPLATE_DIR = Path(__file__).parent.parent / "templates"

    TEMPLATES = {
        "technical-spec": "technical-spec.md",
        "requirements": "requirements.md",
        "adr": "adr.md",
        "rfc": "rfc.md",
        "readme": "readme.md",
        "coding-rules": "coding-rules.md",
        "article": "article.md",
    }

    def __init__(self, template_type: str, context: Dict = None):
        self.template_type = template_type
        self.context = context or {}
        self._set_default_context()

    def _set_default_context(self):
        """Set default context values"""
        defaults = {
            "project_name": "Project Name",
            "author": "Author",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "version": "1.0.0",
            "status": "Draft",
            "description": "Project description",
            "tech_stack": "Technology stack",
        }

        for key, value in defaults.items():
            if key not in self.context:
                self.context[key] = value

    def generate(self) -> str:
        """Generate template content"""
        if self.template_type not in self.TEMPLATES:
            raise ValueError(f"Unknown template type: {self.template_type}")

        template_file = self.TEMPLATE_DIR / self.TEMPLATES[self.template_type]

        if not template_file.exists():
            # Generate inline template if file doesn't exist
            return self._generate_inline_template()

        # Load and populate template
        with open(template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()

        return self._populate_template(template_content)

    def _populate_template(self, template: str) -> str:
        """Populate template with context values"""
        content = template

        # Replace placeholders
        for key, value in self.context.items():
            placeholder = "{" + key.upper() + "}"
            content = content.replace(placeholder, str(value))

        return content

    def _generate_inline_template(self) -> str:
        """Generate template inline if template file doesn't exist"""
        generators = {
            "technical-spec": self._generate_technical_spec,
            "requirements": self._generate_requirements,
            "adr": self._generate_adr,
            "rfc": self._generate_rfc,
            "readme": self._generate_readme,
            "coding-rules": self._generate_coding_rules,
            "article": self._generate_article,
        }

        if self.template_type in generators:
            return generators[self.template_type]()

        return "# Document\n\nContent here."

    def _generate_technical_spec(self) -> str:
        """Generate technical specification template"""
        return f"""---
title: {self.context['project_name']} - Technical Specification
date: {self.context['date']}
version: {self.context['version']}
author: {self.context['author']}
status: {self.context['status']}
---

# {self.context['project_name']} - Technical Specification

## Document Information

- **Version**: {self.context['version']}
- **Last Updated**: {self.context['date']}
- **Author**: {self.context['author']}
- **Status**: {self.context['status']}

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Functional Requirements](#functional-requirements)
- [Non-Functional Requirements](#non-functional-requirements)
- [API Specifications](#api-specifications)
- [Data Model](#data-model)
- [Security Considerations](#security-considerations)
- [Performance Requirements](#performance-requirements)
- [Testing Strategy](#testing-strategy)
- [Deployment Guide](#deployment-guide)

## 1. Overview

### 1.1 Purpose

{self.context.get('description', 'Describe the purpose of this system.')}

### 1.2 Scope

Define what is in scope and out of scope for this specification.

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| TBD  | To Be Defined |

## 2. System Architecture

### 2.1 High-Level Design

Describe the overall system architecture.

### 2.2 Component Diagram

```
[Insert component diagram]
```

### 2.3 Technology Stack

{self.context.get('tech_stack', 'List technologies used')}

## 3. Functional Requirements

### 3.1 User Stories

### 3.2 Features

## 4. Non-Functional Requirements

### 4.1 Performance
### 4.2 Scalability
### 4.3 Reliability
### 4.4 Maintainability

## 5. API Specifications

### 5.1 Endpoints

### 5.2 Request/Response Formats

## 6. Data Model

### 6.1 Entity Relationships

### 6.2 Schema Definitions

## 7. Security Considerations

### 7.1 Authentication
### 7.2 Authorization
### 7.3 Data Protection

## 8. Performance Requirements

### 8.1 Response Times
### 8.2 Throughput
### 8.3 Concurrent Users

## 9. Testing Strategy

### 9.1 Unit Tests
### 9.2 Integration Tests
### 9.3 End-to-End Tests

## 10. Deployment Guide

### 10.1 Prerequisites
### 10.2 Installation Steps
### 10.3 Configuration

## 11. References

- Reference 1
- Reference 2
"""

    def _generate_requirements(self) -> str:
        """Generate requirements document (EARS format)"""
        return f"""---
title: {self.context['project_name']} - Requirements Specification
date: {self.context['date']}
version: {self.context['version']}
author: {self.context['author']}
status: {self.context['status']}
format: EARS (Easy Approach to Requirements Syntax)
---

# {self.context['project_name']} - Requirements Specification

## Document Information

- **Version**: {self.context['version']}
- **Date**: {self.context['date']}
- **Author**: {self.context['author']}
- **Status**: {self.context['status']}

## 1. Introduction

### 1.1 Purpose

{self.context.get('description', 'Purpose of this requirements document')}

### 1.2 Scope

## 2. Stakeholders

| Role | Name | Responsibilities |
|------|------|-----------------|
| Product Owner | | |
| Development Team | | |
| QA Team | | |

## 3. Functional Requirements

### 3.1 Ubiquitous Requirements

> **Pattern**: The {self.context['project_name']} shall [requirement]

- REQ-F-001: The system shall...
- REQ-F-002: The system shall...

### 3.2 Event-Driven Requirements

> **Pattern**: WHEN [trigger] the system shall [requirement]

- REQ-F-010: WHEN a user logs in, the system shall authenticate credentials
- REQ-F-011: WHEN...

### 3.3 State-Driven Requirements

> **Pattern**: WHILE [in state] the system shall [requirement]

- REQ-F-020: WHILE processing payment, the system shall...
- REQ-F-021: WHILE...

### 3.4 Optional Feature Requirements

> **Pattern**: WHERE [feature enabled] the system shall [requirement]

- REQ-F-030: WHERE two-factor authentication is enabled, the system shall...
- REQ-F-031: WHERE...

### 3.5 Unwanted Behavior

> **Pattern**: IF [condition] THEN the system shall [requirement]

- REQ-F-040: IF authentication fails, the system shall log the attempt
- REQ-F-041: IF...

## 4. Non-Functional Requirements

### 4.1 Performance

- REQ-NF-001: The system shall respond to API requests within 200ms
- REQ-NF-002: The system shall...

### 4.2 Security

- REQ-NF-010: The system shall encrypt all data in transit using TLS 1.3
- REQ-NF-011: The system shall...

### 4.3 Usability

### 4.4 Reliability

### 4.5 Maintainability

## 5. Acceptance Criteria

### 5.1 Feature Acceptance

| Requirement ID | Acceptance Criteria | Priority |
|----------------|---------------------|----------|
| REQ-F-001 | AC-001: ... | High |

## 6. Constraints

### 6.1 Technical Constraints
### 6.2 Business Constraints
### 6.3 Regulatory Constraints

## 7. Assumptions and Dependencies

## 8. Glossary

| Term | Definition |
|------|------------|
|      |            |
"""

    def _generate_adr(self) -> str:
        """Generate Architecture Decision Record"""
        return f"""# ADR-XXX: {self.context.get('title', 'Decision Title')}

## Status

{self.context.get('status', 'Proposed')}

## Context

What is the issue that we're seeing that is motivating this decision or change?

## Decision

What is the change that we're proposing and/or doing?

## Rationale

Why are we making this decision? What are the benefits?

### Alternatives Considered

1. **Alternative 1**
   - Pros:
   - Cons:

2. **Alternative 2**
   - Pros:
   - Cons:

## Consequences

What becomes easier or more difficult to do because of this change?

### Positive Consequences

- Benefit 1
- Benefit 2

### Negative Consequences / Trade-offs

- Trade-off 1
- Trade-off 2

## Implementation

How will this decision be implemented?

### Migration Strategy

### Rollback Plan

## References

- Reference 1
- Reference 2

---

**Author**: {self.context['author']}
**Date**: {self.context['date']}
**Reviewers**:
**Approved by**:
"""

    def _generate_rfc(self) -> str:
        """Generate RFC (Request for Comments) template"""
        return f"""# RFC-XXX: {self.context.get('title', 'RFC Title')}

**Author**: {self.context['author']}
**Date**: {self.context['date']}
**Status**: {self.context.get('status', 'Draft')}

## Abstract

Brief summary of the proposal (2-3 sentences).

## Motivation

Why are we doing this? What problem does it solve?

## Proposal

Detailed explanation of the proposed change.

### Goals

- Goal 1
- Goal 2

### Non-Goals

- Non-goal 1
- Non-goal 2

## Design

### High-Level Design

### Detailed Design

#### Component A

#### Component B

### API Changes

```typescript
// Example API
interface Example {{
  // ...
}}
```

### Data Model Changes

## Implementation Plan

### Phase 1

### Phase 2

### Migration Strategy

## Testing Plan

### Unit Tests

### Integration Tests

### Performance Tests

## Security Considerations

## Performance Impact

## Alternatives Considered

### Alternative 1

**Pros**:
**Cons**:

### Alternative 2

**Pros**:
**Cons**:

## Open Questions

- Question 1?
- Question 2?

## References

- Reference 1
- Reference 2

## Changelog

| Date | Change | Author |
|------|--------|--------|
| {self.context['date']} | Initial draft | {self.context['author']} |
"""

    def _generate_readme(self) -> str:
        """Generate README template"""
        return f"""# {self.context['project_name']}

{self.context.get('description', 'Project description')}

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Installation commands
```

## Usage

```bash
# Usage examples
```

## Configuration

```yaml
# Configuration example
```

## Development

### Prerequisites

- Requirement 1
- Requirement 2

### Setup

```bash
# Setup commands
```

### Running Tests

```bash
# Test commands
```

## API Documentation

See [API.md](./API.md) for detailed API documentation.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

## License

{self.context.get('license', 'MIT License')}

## Authors

- {self.context['author']}

## Acknowledgments

- Credit 1
- Credit 2
"""

    def _generate_coding_rules(self) -> str:
        """Generate coding rules template"""
        return f"""# {self.context['project_name']} - Coding Standards

**Version**: {self.context['version']}
**Last Updated**: {self.context['date']}

## General Principles

1. **Code Readability**: Code should be easy to read and understand
2. **Simplicity**: Prefer simple solutions over complex ones
3. **Consistency**: Follow established patterns
4. **Testability**: Write testable code

## Naming Conventions

### Variables

- Use camelCase for variables: `userName`, `isActive`
- Use descriptive names: `user` over `u`

### Functions

- Use verb-noun pattern: `getUserData()`, `validateEmail()`
- Use camelCase: `calculateTotal()`

### Classes

- Use PascalCase: `UserService`, `PaymentProcessor`
- Use nouns: `Order`, `Customer`

### Constants

- Use UPPER_CASE: `MAX_RETRIES`, `API_KEY`

## Code Structure

### File Organization

```
src/
├── components/
├── services/
├── utils/
└── types/
```

### Module Pattern

```javascript
// Good
export class UserService {{
  // ...
}}

// Avoid
export default class {{
  // ...
}}
```

## Best Practices

### Error Handling

```javascript
// Good
try {{
  await fetchData();
}} catch (error) {{
  logger.error('Failed to fetch data:', error);
  throw new AppError('Data fetch failed');
}}

// Avoid
try {{
  await fetchData();
}} catch (e) {{
  console.log(e);
}}
```

### Comments

```javascript
// Good: Explain why, not what
// Using exponential backoff to handle rate limiting
const delay = Math.pow(2, attempt) * 1000;

// Avoid: Obvious comments
// Set delay to 1000
const delay = 1000;
```

## Testing Standards

### Test Structure

```javascript
describe('UserService', () => {{
  describe('createUser', () => {{
    it('should create user with valid data', () => {{
      // Arrange
      const userData = {{ name: 'John' }};

      // Act
      const user = service.createUser(userData);

      // Assert
      expect(user.name).toBe('John');
    }});
  }});
}});
```

### Coverage Requirements

- Unit tests: ≥ 80% coverage
- Integration tests: Critical paths
- E2E tests: Main user workflows

## Code Review Checklist

- [ ] Code follows naming conventions
- [ ] Functions are small and focused
- [ ] Error handling is appropriate
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] No console.log or debug code
- [ ] No commented-out code
- [ ] Performance considerations addressed

## Tools and Automation

### Linting

```bash
npm run lint
```

### Formatting

```bash
npm run format
```

### Type Checking

```bash
npm run type-check
```

## References

- [Style Guide Reference]()
- [Best Practices Document]()
"""

    def _generate_article(self) -> str:
        """Generate technical article template"""
        return f"""---
title: {self.context.get('title', 'Article Title')}
author: {self.context['author']}
date: {self.context['date']}
tags: []
---

# {self.context.get('title', 'Article Title')}

**Author**: {self.context['author']}
**Published**: {self.context['date']}
**Reading Time**: ~X minutes

## Introduction

Hook the reader with an interesting opening paragraph.

## Problem Statement

What problem are we solving?

## Solution Overview

Brief overview of the solution approach.

## Implementation

### Step 1: Setup

```bash
# Setup commands
```

### Step 2: Core Implementation

```python
# Code example
def example():
    pass
```

### Step 3: Testing

```python
# Test example
def test_example():
    assert True
```

## Best Practices

1. **Practice 1**: Description
2. **Practice 2**: Description
3. **Practice 3**: Description

## Common Pitfalls

### Pitfall 1

**Problem**: Description of the pitfall

**Solution**: How to avoid it

### Pitfall 2

**Problem**: Description

**Solution**: How to avoid it

## Real-World Example

Concrete example showing the solution in action.

## Performance Considerations

Discuss performance implications and optimizations.

## Conclusion

Summarize key takeaways:

- Takeaway 1
- Takeaway 2
- Takeaway 3

## Further Reading

- [Resource 1]()
- [Resource 2]()

## About the Author

{self.context['author']} - Brief bio

---

*Have questions or feedback? Leave a comment below or reach out on [platform].*
"""

    def save(self, output_path: str):
        """Generate and save template"""
        content = self.generate()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return output_path


def main():
    parser = argparse.ArgumentParser(description='Generate documentation template')
    parser.add_argument('--type', required=True,
                       choices=list(TemplateGenerator.TEMPLATES.keys()),
                       help='Template type')
    parser.add_argument('--output', required=True, help='Output file path')
    parser.add_argument('--project', help='Project name')
    parser.add_argument('--author', help='Author name')
    parser.add_argument('--title', help='Document title')
    parser.add_argument('--status', help='Document status')
    parser.add_argument('--context', help='JSON file with context data')

    args = parser.parse_args()

    # Load context
    context = {}
    if args.context:
        with open(args.context, 'r') as f:
            context = json.load(f)

    # Override with command-line arguments
    if args.project:
        context['project_name'] = args.project
    if args.author:
        context['author'] = args.author
    if args.title:
        context['title'] = args.title
    if args.status:
        context['status'] = args.status

    # Generate template
    generator = TemplateGenerator(args.type, context)
    output_file = generator.save(args.output)

    print(f"Template generated: {output_file}")


if __name__ == '__main__':
    main()
