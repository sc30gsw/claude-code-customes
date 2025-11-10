---
name: doc-engineer
description: Comprehensive document creation, editing, and improvement skill for all Markdown-based documentation (technical specs, requirements, ADR, RFC, README, coding rules, articles). Handles complete end-to-end workflows from initial draft to publication-ready documents.
license: Proprietary
---

# Document Engineering Skill

A comprehensive skill for creating, editing, and improving all types of Markdown documentation with automated quality checks, improvement suggestions, and end-to-end workflows.

## Overview

This skill provides professional document engineering capabilities for:
- **Technical Specifications**: Feature specs, system design, API documentation
- **Requirements Documents**: EARS format, user stories, acceptance criteria
- **Architecture Documents**: ADRs, RFCs, design proposals
- **Project Documentation**: READMEs, coding rules, contribution guides
- **Technical Articles**: Tutorials, how-tos, technical blog posts

## Workflow Decision Tree

```
User Request → Analyze Intent:
│
├─ CREATE New Document?
│  │
│  ├─ Step 1: Identify Document Type
│  │  └─ Options: technical-spec | requirements | adr | rfc | readme | coding-rules | article
│  │
│  ├─ Step 2: Gather Context
│  │  ├─ Project name, purpose, target audience
│  │  ├─ Technology stack, frameworks, languages
│  │  └─ Specific requirements or constraints
│  │
│  ├─ Step 3: Generate from Template
│  │  ├─ Use: `python scripts/template_generator.py --type {doc_type} --context {context.json}`
│  │  └─ Output: Initial draft with project-specific metadata injected
│  │
│  ├─ Step 4: Content Development (Phase 1-5)
│  │  ├─ Phase 1: Structure validation
│  │  ├─ Phase 2: Content expansion
│  │  ├─ Phase 3: Quality check
│  │  ├─ Phase 4: Apply improvements
│  │  └─ Phase 5: Final validation
│  │
│  └─ Step 5: Deliver Complete Document
│     └─ Quality score ≥ 80, all required sections present
│
├─ EDIT Existing Document?
│  │
│  ├─ Step 1: Load and Analyze
│  │  ├─ Use: `python scripts/doc_analyzer.py --file {doc_path}`
│  │  └─ Output: Quality report with identified issues
│  │
│  ├─ Step 2: Identify Edit Scope
│  │  ├─ Structural changes (add/remove/reorder sections)
│  │  ├─ Content updates (revise existing text)
│  │  └─ Format corrections (headings, links, lists)
│  │
│  ├─ Step 3: Apply Edits
│  │  ├─ For structural: Modify section hierarchy
│  │  ├─ For content: Update specific paragraphs/sections
│  │  └─ For format: Fix markdown syntax, links, formatting
│  │
│  ├─ Step 4: Validate Changes
│  │  ├─ Use: `python scripts/doc_validator.py --file {doc_path}`
│  │  └─ Ensure: Structure integrity, link validity, consistency
│  │
│  └─ Step 5: Confirm Improvements
│     └─ Compare before/after quality scores
│
└─ IMPROVE Document Quality?
   │
   ├─ Step 1: Comprehensive Analysis
   │  ├─ Use: `python scripts/doc_analyzer.py --file {doc_path} --detailed`
   │  └─ Output: Quality dashboard with scores (0-100):
   │     ├─ Structure Score: Heading hierarchy, section organization
   │     ├─ Content Score: Completeness, clarity, examples
   │     ├─ Readability Score: Sentence length, technical density
   │     └─ Overall Quality: Weighted average
   │
   ├─ Step 2: Generate Improvement Suggestions
   │  ├─ Use: `python scripts/doc_improver.py --file {doc_path} --analyze`
   │  └─ Output: Prioritized improvement list:
   │     ├─ Critical: Missing required sections, broken links
   │     ├─ High: Poor readability, inconsistent terminology
   │     └─ Medium: Missing examples, suboptimal structure
   │
   ├─ Step 3: Apply Improvements (Batch or Selective)
   │  ├─ Batch mode: `--apply-all` (applies all high-priority improvements)
   │  ├─ Selective: `--apply-ids 1,3,5` (specific improvements)
   │  └─ Interactive: Review each suggestion before applying
   │
   ├─ Step 4: Validate Improvements
   │  ├─ Re-run analyzer to confirm quality increase
   │  └─ Check: No new issues introduced, links still valid
   │
   └─ Step 5: Generate Final Report
      └─ Before/after comparison, achieved improvements
```

## Core Capabilities

### 1. Template Generation

Generate publication-ready document templates with project-specific metadata:

```bash
# Generate technical specification
python scripts/template_generator.py \
  --type technical-spec \
  --project "User Authentication System" \
  --author "Development Team" \
  --stack "Node.js, PostgreSQL, Redis"

# Generate requirements document (EARS format)
python scripts/template_generator.py \
  --type requirements \
  --project "E-commerce Platform" \
  --format ears

# Generate Architecture Decision Record
python scripts/template_generator.py \
  --type adr \
  --title "Use GraphQL for API Layer" \
  --status proposed
```

**Templates Available:**
- `technical-spec.md`: Comprehensive technical specifications
- `requirements.md`: EARS-formatted requirements with acceptance criteria
- `adr.md`: Architecture Decision Records (ADR) format
- `rfc.md`: Request for Comments (RFC) format
- `readme.md`: Project README with badges, installation, usage
- `coding-rules.md`: Coding standards and best practices
- `article.md`: Technical article/blog post structure

### 2. Quality Analysis

Comprehensive document quality assessment:

```bash
# Basic quality check
python scripts/doc_analyzer.py --file README.md

# Detailed analysis with improvement suggestions
python scripts/doc_analyzer.py --file spec.md --detailed

# Batch analysis for multiple documents
python scripts/doc_analyzer.py --directory docs/ --recursive
```

**Quality Metrics:**
- **Structure Score (0-100)**: Heading hierarchy, section completeness, TOC consistency
- **Content Score (0-100)**: Information completeness, clarity, examples, code snippets
- **Readability Score (0-100)**: Sentence complexity, paragraph length, technical term density
- **Link Health (0-100)**: Internal link validity, external URL accessibility
- **Overall Quality (0-100)**: Weighted composite score

**Analysis Output:**
```json
{
  "file": "README.md",
  "quality_score": 78,
  "metrics": {
    "structure": 85,
    "content": 72,
    "readability": 80,
    "links": 75
  },
  "issues": [
    {"type": "missing_section", "severity": "high", "section": "Installation"},
    {"type": "broken_link", "severity": "critical", "line": 45, "url": "..."},
    {"type": "readability", "severity": "medium", "line": 23, "reason": "sentence_too_long"}
  ],
  "suggestions": ["Add installation section", "Fix broken link", "Split long paragraph"]
}
```

### 3. Automated Improvements

AI-powered document enhancement:

```bash
# Analyze and suggest improvements
python scripts/doc_improver.py --file spec.md --analyze

# Apply all high-priority improvements
python scripts/doc_improver.py --file spec.md --apply-all --priority high

# Interactive improvement mode
python scripts/doc_improver.py --file spec.md --interactive

# Apply specific improvements by ID
python scripts/doc_improver.py --file spec.md --apply-ids 1,3,5,7
```

**Improvement Categories:**
- **Structure**: Reorder sections, add missing sections, improve hierarchy
- **Content**: Add examples, expand explanations, add code snippets
- **Readability**: Split long paragraphs, simplify complex sentences
- **Consistency**: Standardize terminology, unify formatting
- **Completeness**: Add missing information, expand sparse sections

**Improvement Priority Matrix:**
```
Impact │ High   │ Add missing critical sections, fix broken links
       │ Medium │ Improve readability, add examples
       │ Low    │ Minor formatting, optional enhancements
       └────────┴────────────────────────────────────────
               Low         Medium          High
                          Effort
```

### 4. Document Validation

Comprehensive validation and error checking:

```bash
# Validate structure and completeness
python scripts/doc_validator.py --file spec.md --check structure

# Check all links (internal + external)
python scripts/doc_validator.py --file README.md --check links

# Full validation (structure + links + consistency)
python scripts/doc_validator.py --file spec.md --full

# Validate against specific rules
python scripts/doc_validator.py --file adr.md --rules quality-rules/adr-rules.json
```

**Validation Checks:**
- ✅ **Structure**: Required sections present, heading hierarchy valid, TOC matches content
- ✅ **Links**: Internal links point to existing sections, external URLs accessible
- ✅ **Consistency**: Terminology used consistently, formatting uniform
- ✅ **Completeness**: All required metadata present, no placeholder text (TODO, TBD)
- ✅ **Format**: Valid Markdown syntax, proper code fence languages, valid image paths

### 5. End-to-End Workflow

Complete document creation from start to finish:

```bash
# Create complete technical specification (Phase 1-5)
python scripts/doc_workflow.py \
  --create technical-spec \
  --project "Payment Processing Service" \
  --output docs/payment-spec.md \
  --complete

# Create and improve existing document to target quality
python scripts/doc_workflow.py \
  --improve spec.md \
  --target-quality 90 \
  --output improved-spec.md

# Full workflow with custom quality rules
python scripts/doc_workflow.py \
  --create requirements \
  --project "Mobile App" \
  --rules quality-rules/custom-rules.json \
  --complete
```

**Workflow Phases:**
1. **Context Gathering**: Extract project information, technology stack, requirements
2. **Template Generation**: Create initial structure with metadata
3. **Content Development**: Expand sections, add details, include examples
4. **Quality Check**: Run validator and analyzer
5. **Improvement Application**: Apply suggested improvements automatically
6. **Final Validation**: Ensure quality target met (default: ≥80)
7. **Publication Prep**: Generate review checklist, validate all links

## Usage Examples

### Example 1: Create Technical Specification from Scratch

```python
# User request: "Create a technical specification for our authentication system"

# Step 1: Generate template
template_generator.py --type technical-spec --project "User Authentication System"

# Step 2: Claude fills in sections based on context
# - Overview and purpose
# - System architecture
# - Security considerations
# - API specifications
# - Data models

# Step 3: Quality check and improvement
doc_analyzer.py --file auth-spec.md --detailed
doc_improver.py --file auth-spec.md --apply-all --priority high

# Step 4: Final validation
doc_validator.py --file auth-spec.md --full

# Result: Complete, high-quality technical specification (quality score ≥ 80)
```

### Example 2: Improve Existing README

```python
# User request: "Improve our README.md"

# Step 1: Analyze current state
doc_analyzer.py --file README.md --detailed
# Output: Quality score 62/100
# Issues: Missing installation section, broken links, poor structure

# Step 2: Generate improvement suggestions
doc_improver.py --file README.md --analyze
# Output: 12 suggestions (3 critical, 5 high, 4 medium)

# Step 3: Apply improvements
doc_improver.py --file README.md --apply-all --priority high

# Step 4: Validate improvements
doc_analyzer.py --file README.md
# Output: Quality score 89/100

# Result: Significantly improved README with all critical issues fixed
```

### Example 3: Create ADR (Architecture Decision Record)

```python
# User request: "Document our decision to use GraphQL"

# Step 1: Generate ADR template
template_generator.py --type adr --title "Use GraphQL for API Layer" --status proposed

# Step 2: Fill in ADR sections
# - Context: API design challenges
# - Decision: Adopt GraphQL
# - Rationale: Benefits vs REST
# - Consequences: Trade-offs and implications

# Step 3: Validate ADR format
doc_validator.py --file adr-001-graphql.md --rules quality-rules/adr-rules.json

# Result: Properly formatted ADR ready for review
```

### Example 4: Batch Quality Check for Documentation Directory

```python
# User request: "Check quality of all our docs"

# Step 1: Batch analysis
doc_analyzer.py --directory docs/ --recursive --output report.json

# Step 2: Generate quality dashboard
# docs/
# ├─ README.md          (85/100) ✅
# ├─ CONTRIBUTING.md    (78/100) ⚠️
# ├─ specs/
# │  ├─ api-spec.md     (92/100) ✅
# │  └─ auth-spec.md    (65/100) ❌ Needs improvement
# └─ adrs/
#    ├─ adr-001.md      (88/100) ✅
#    └─ adr-002.md      (70/100) ⚠️

# Step 3: Auto-improve low-scoring documents
for doc in low_quality_docs:
    doc_improver.py --file {doc} --apply-all --target-quality 80

# Result: All documentation meets minimum quality threshold
```

## Quality Rules

Quality rules are defined in JSON files under `quality-rules/`:

### structure-rules.json
Defines required sections, heading hierarchy, and structural requirements for each document type.

### style-guide.json
Defines style preferences: terminology, formatting conventions, code snippet requirements.

### completeness-checklist.json
Defines completeness criteria: required metadata, minimum section count, example requirements.

## Integration with Agents

### technical-writer Agent
When the `technical-writer` agent is invoked, it automatically leverages this skill for:
- Professional document creation with proper structure
- Quality assessment and improvement suggestions
- Style and readability enhancement

### requirements-analyst Agent
When the `requirements-analyst` agent is invoked, it uses this skill for:
- EARS-formatted requirements generation
- Requirements validation against completeness criteria
- Integration with Kiro spec workflow

## Dependencies

**Python Libraries:**
```
markdown>=3.4.0      # Markdown parsing
beautifulsoup4>=4.12 # HTML/XML manipulation
requests>=2.31       # URL validation
jsonschema>=4.19     # JSON validation
```

**External Tools:**
- `pandoc` (optional): Advanced Markdown conversion
- `markdownlint` (optional): Additional linting

## File Structure Summary

```
doc-engineer/
├── SKILL.md                     # This file
├── templates/                   # Document templates (7 types)
├── scripts/                     # Python automation scripts (5 files)
├── quality-rules/               # Quality validation rules (3 files)
└── LICENSE.txt                  # License information
```

## License

Proprietary - Internal use only
