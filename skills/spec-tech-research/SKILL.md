---
name: spec-tech-research
description: Advanced technical research command with extended thinking modes and MCP integration for comprehensive analysis
---

# Spec Tech Research

Advanced technical research with extended thinking modes and MCP integration for comprehensive analysis.

## Usage

```bash
/spec:tech-research "<topic>" [options]
```

## Thinking Modes

| Mode | Token Budget | Depth | Use Case |
|------|--------------|-------|----------|
| `think` | 10,000 | Standard | Quick research, overviews |
| `think-hard` | 20,000 | Enhanced | Detailed comparisons |
| `think-harder` | 30,000 | Structured | Complex topics, decisions |
| `ultrathink` | 50,000 | Maximum | Critical analysis, academic |

## Core Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--mode` | `-m` | Thinking mode | `-m ultrathink` |
| `--budget` | `-b` | Token budget | `-b 25000` |
| `--output` | `-o` | Output file | `-o analysis.md` |
| `--format` | `-f` | Output format | `-f json` |
| `--mcp` | | MCP tools to use | `--mcp "context7,sequential"` |

## Research Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--depth` | `-d` | Search depth (quick/standard/deep/exhaustive) | `-d deep` |
| `--template` | `-t` | Report template | `-t academic` |
| `--confidence` | `-c` | Confidence threshold (0-1) | `-c 0.9` |
| `--sources` | | Include citations | `--sources` |
| `--diagrams` | | Generate diagrams | `--diagrams` |
| `--language` | `-l` | Output language | `-l ja` |

## Tool Priorities

**ALWAYS prioritize mcp__serena__ for codebase analysis:**

### Codebase Intelligence (Serena MCP First)
- `mcp__serena__search_for_pattern` - Find implementation patterns
- `mcp__serena__find_symbol` - Understand architecture
- `mcp__serena__get_symbols_overview` - Architecture-aware recommendations
- `mcp__serena__read_memory` / `write_memory` - Research continuity

### Research Enhancement (Other MCPs)
- `mcp__context7__resolve-library-id` - Library documentation
- `mcp__sequential-thinking__sequentialthinking` - Complex analysis

## Templates

| Template | Description |
|----------|-------------|
| `overview` | Quick summary with key points |
| `comprehensive` | Full analysis with all aspects |
| `academic` | Research paper format with citations |
| `technical` | Implementation-focused with code |

## Examples

```bash
# Quick overview
/spec:tech-research "Redis vs Memcached" -d quick -t overview

# Deep framework analysis
/spec:tech-research "React architecture patterns" -m think-harder -t comprehensive --diagrams

# Security research with high confidence
/spec:tech-research "Zero-trust security model" -m ultrathink -c 0.95 --sources

# Implementation research
/spec:tech-research "Implementing OAuth 2.0 with PKCE" -t technical -m think-hard

# Codebase-aware research
/spec:tech-research "State management options" --mcp "serena,context7" --codebase-context

# Japanese technical documentation
/spec:tech-research "Docker コンテナ化" -l ja -t technical
```

## Output Structure

```markdown
# Technical Research Report: [Topic]

## Executive Summary
- Key findings and recommendations

## Table of Contents
1. Introduction
2. Core Concepts
3. Technical Analysis
4. Implementation Considerations
5. Best Practices
6. Comparisons
7. Recommendations
8. Conclusion
9. References

## Confidence Scores
- Finding 1: 95% confidence
- Finding 2: 88% confidence
```

## Integration

Research results can be used with:
- `/serena` for implementation
- `/debug-error` for context
- `/smart-think` for decisions
- `/spec:requirements` for requirements
