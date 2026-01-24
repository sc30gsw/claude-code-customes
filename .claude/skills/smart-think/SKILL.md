---
name: smart-think
description: Advanced multi-mode thinking system with Sequential Thinking MCP and Serena integration for complex problem solving
---

# Smart Think: Advanced Multi-Mode Problem Solving

Intelligent problem-solving with multiple thinking modes, budget control, and MCP integration for complex analysis and decision-making.

## Usage

```bash
/smart-think "<problem_description>" [options]
```

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--mode` | `-m` | Thinking mode | `think` |
| `--budget` | `-b` | Token budget | Auto |
| `--interactive` | `-i` | Interactive refinement | false |
| `--output` | `-o` | Save to file | none |
| `--serena` | `-s` | Use Serena integration | false |
| `--research` | `-r` | Include research phase | false |
| `--citations` | `-c` | Include citations | false |
| `--structured` | | Structured output | false |
| `--confidence` | | Show confidence levels | false |
| `--focus` | `-f` | Focus area | none |

## Thinking Modes

| Mode | Budget Range | Thoughts | Confidence | Best For |
|------|--------------|----------|------------|----------|
| `think` | 2,000-8,000 | 3-6 | 70-85% | Quick decisions |
| `think-hard` | 8,000-15,000 | 6-10 | 75-90% | Complex analysis |
| `think-harder` | 15,000-25,000 | 10-15 | 80-95% | Architecture decisions |
| `ultrathink` | 25,000-50,000 | 15-25 | 85-98% | Research, complex systems |

## Tool Priorities

**ALWAYS prioritize mcp__sequential-thinking__ as primary engine, with mcp__serena__ for codebase context:**

### Primary Thinking Engine (Sequential Thinking MCP)
- Use `mcp__sequential-thinking__sequentialthinking` as primary thinking tool
- Generate and test multiple solution hypotheses
- Build reasoning chains with confidence tracking

### Codebase Intelligence (Serena MCP - When --serena flag)
- Use `mcp__serena__get_symbols_overview` for technical understanding
- Use `mcp__serena__search_for_pattern` for implementation insights
- Use `mcp__serena__read_memory` / `mcp__serena__write_memory` for decision continuity

## Example Usage

```bash
# Default thinking mode
/smart-think "Should we use Redux or Zustand?"

# Deep analysis with codebase context
/smart-think "Database migration strategy" -m think-harder --serena

# Research-focused with citations
/smart-think "Technology selection" -m ultrathink --research --citations

# Quick decision with budget control
/smart-think "CSS framework choice" -b 5000 --focus=frontend
```

## Mode Selection Guidelines

1. **Think**: Quick decisions, simple problems, time constraints
2. **Think-Hard**: Important decisions, moderate complexity
3. **Think-Harder**: Critical decisions, high complexity
4. **UltraThink**: Mission-critical, research-level analysis

## Output Formats

### Default Format
- Problem Analysis
- Solution Exploration
- Recommendation
- Next Steps

### Research Format (with --research)
- Executive Summary
- Literature Review
- Technical Analysis
- Recommendations
- References

### Technical Format (with --serena)
- Technical Context
- Code Analysis
- Architecture Implications
- Implementation Strategy
