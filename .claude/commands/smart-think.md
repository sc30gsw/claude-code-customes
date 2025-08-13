---
allowed-tools: Read, Glob, Grep, Edit, MultiEdit, Write, Bash, TodoWrite, mcp__sequential-thinking__sequentialthinking, mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory
description: Advanced multi-mode thinking system with Sequential Thinking MCP and Serena integration for complex problem solving
---

## Context

- Current problem space: @package.json
- Recent decisions: !`git log --oneline --grep="decision\|choice\|decide" -3 2>/dev/null || echo "No recent decision commits"`
- Project complexity: !`find . -name "*.js" -o -name "*.ts" -o -name "*.py" | wc -l | xargs echo "Code files:"`
- Architecture docs: !`find . -name "*architecture*" -o -name "*design*" -o -name "*spec*" | head -5`
- Previous thinking: !`ls -la .claude/memory/thinking/ 2>/dev/null | head -3 || echo "No previous thinking sessions"`
- Decision context: !`grep -r "TODO\|FIXME\|DECIDE" . --include="*.md" | head -3 2>/dev/null || echo "No pending decisions"`

## Tool Usage Priorities

**ALWAYS prioritize mcp__sequential-thinking__ as primary engine, with mcp__serena__ for codebase context:**

### Primary Thinking Engine (Sequential Thinking MCP)
- **Structured Reasoning**: Use `mcp__sequential-thinking__sequentialthinking` as primary thinking tool
- **Hypothesis Generation**: Generate and test multiple solution hypotheses
- **Evidence-Based Analysis**: Build reasoning chains with confidence tracking
- **Iterative Refinement**: Adjust thinking process based on new information

### Codebase Intelligence (Serena MCP - When --serena flag)
- **Code Context**: Use `mcp__serena__get_symbols_overview` for technical understanding
- **Pattern Analysis**: Use `mcp__serena__search_for_pattern` for implementation insights
- **Architecture Awareness**: Use `mcp__serena__find_referencing_symbols` for system understanding
- **Memory Integration**: Use `mcp__serena__read_memory` / `mcp__serena__write_memory` for decision continuity

### Supporting Tools (Standard)
- **Documentation**: Use Read, Write for creating thinking artifacts
- **Research**: Use Glob, Grep for finding relevant information
- **Process Management**: Use TodoWrite for breaking down complex thinking tasks

# Smart Think: Advanced Multi-Mode Problem Solving

Intelligent problem-solving with multiple thinking modes, budget control, and MCP integration for complex analysis and decision-making.

## Usage Guide

### Basic Syntax
```bash
/smart-think "<problem_description>" [options]
```

### Available Options

| Option | Short | Description | Default | Example |
|--------|-------|-------------|---------|---------|
| `--mode` | `-m` | Thinking mode | `think` | `-m ultrathink` |
| `--budget` | `-b` | Token budget | Auto | `-b 15000` |
| `--interactive` | `-i` | Interactive refinement | false | `-i` |
| `--output` | `-o` | Save to file | none | `-o analysis.md` |
| `--serena` | `-s` | Use Serena integration | false | `-s` |
| `--research` | `-r` | Include research phase | false | `-r` |
| `--citations` | `-c` | Include citations | false | `-c` |
| `--structured` | | Structured output | false | `--structured` |
| `--confidence` | | Show confidence levels | false | `--confidence` |
| `--min-thoughts` | | Minimum thoughts | Mode default | `--min-thoughts=5` |
| `--max-thoughts` | | Maximum thoughts | Mode default | `--max-thoughts=20` |
| `--focus` | `-f` | Focus area | none | `-f security` |
| `--perspective` | `-p` | Analysis perspective | multiple | `-p user` |

### Quick Examples

```bash
# Default thinking mode
/smart-think "Should we use Redux or Zustand?"

# Deep analysis with codebase context
/smart-think "Database migration strategy" -m think-harder --serena

# Interactive problem solving
/smart-think "API design approach" -m think-hard --interactive

# Research-focused with citations
/smart-think "Technology selection" -m ultrathink --research --citations

# Quick decision with budget control
/smart-think "CSS framework choice" -b 5000 --focus=frontend
```

## Thinking Modes

| Mode | Budget Range | Thoughts | Confidence | Best For |
|------|--------------|----------|------------|----------|
| `think` | 2,000-8,000 | 3-6 | 70-85% | Quick decisions, simple problems |
| `think-hard` | 8,000-15,000 | 6-10 | 75-90% | Complex analysis, design decisions |
| `think-harder` | 15,000-25,000 | 10-15 | 80-95% | Architecture, critical decisions |
| `ultrathink` | 25,000-50,000 | 15-25 | 85-98% | Research, complex systems |

## MCP Integration

### Sequential Thinking MCP (Primary Engine)
🧠 **Core thinking capability** for all reasoning tasks
- Structured hypothesis generation and testing
- Evidence-based reasoning with confidence tracking
- Iterative refinement and branch exploration
- Dynamic thought count adjustment

### Serena MCP Integration (When --serena flag)
🔧 **Codebase intelligence** for technical problems
- Code context analysis and pattern recognition
- Implementation feasibility assessment
- Technical debt and maintainability considerations
- Architecture-aware decision making

### Integration Modes

| Combination | Use Case | Example |
|-------------|----------|---------|
| Sequential Only | General problem solving | Business decisions, strategy |
| Sequential + Serena | Technical decisions | Architecture, code design |
| Sequential + Research | Knowledge synthesis | Technology evaluation |
| All MCPs | Complex technical research | Platform migrations |

## Workflow Process

### Default Workflow (Sequential Thinking MCP):

1. **Problem Analysis**: Use `mcp__sequential-thinking__sequentialthinking` to break down the problem
2. **Hypothesis Generation**: Generate multiple solution approaches
3. **Evidence Gathering**: Collect supporting information and constraints
4. **Iterative Reasoning**: Test and refine hypotheses through reasoning chains
5. **Confidence Assessment**: Evaluate confidence levels for each conclusion
6. **Solution Synthesis**: Combine insights into actionable recommendations

### With --serena Integration:

1. **Codebase Context**: Use `mcp__serena__get_symbols_overview` to understand technical context
2. **Pattern Analysis**: Use `mcp__serena__search_for_pattern` for implementation insights
3. **Sequential Reasoning**: Apply Sequential Thinking MCP with technical context
4. **Implementation Assessment**: Evaluate solutions against existing codebase
5. **Memory Integration**: Use `mcp__serena__write_memory` to store decisions

### With --research Flag:

1. **External Research**: Gather information from available sources
2. **Knowledge Synthesis**: Combine external and internal knowledge
3. **Enhanced Reasoning**: Apply Sequential Thinking with broader context
4. **Citation Tracking**: Maintain source attribution for recommendations

## Thinking Mode Details

### Think Mode (Quick Analysis)
**Budget: 2,000-8,000 tokens | Thoughts: 3-6 | Confidence: 70-85%**
- Fast problem assessment with basic hypothesis testing
- Solution generation with simple trade-off analysis
- Quick decision support for time-sensitive issues
- Pattern matching against known solutions

```bash
/smart-think "Button styling approach" -m think
```

### Think-Hard Mode (Enhanced Analysis)
**Budget: 8,000-15,000 tokens | Thoughts: 6-10 | Confidence: 75-90%**
- Detailed problem breakdown with multiple solution paths
- Risk assessment and mitigation strategies
- Implementation considerations and resource requirements
- Stakeholder impact analysis

```bash
/smart-think "State management strategy" -m think-hard --serena
```

### Think-Harder Mode (Deep Analysis)
**Budget: 15,000-25,000 tokens | Thoughts: 10-15 | Confidence: 80-95%**
- Comprehensive analysis with multiple perspectives
- Second-order effects and long-term implications
- Detailed trade-offs with quantitative assessment
- Implementation roadmap with milestone planning

```bash
/smart-think "System architecture redesign" -m think-harder --structured
```

### UltraThink Mode (Maximum Depth)
**Budget: 25,000-50,000 tokens | Thoughts: 15-25 | Confidence: 85-98%**
- Research-level analysis with academic rigor
- Multiple domain expertise integration
- Complex system modeling and simulation
- Comprehensive documentation and knowledge transfer

```bash
/smart-think "Platform migration strategy" -m ultrathink --research --citations
```

## Structured Output Formats

### Default Format
```
## Problem Analysis
- Core challenge identification
- Key constraints and requirements

## Solution Exploration
- Option 1: [Approach]
- Option 2: [Alternative]
- Option 3: [Innovative]

## Recommendation
- Preferred solution with rationale
- Implementation approach
- Risk mitigation

## Next Steps
- Immediate actions
- Success metrics
```

### Research Format (with --research)
```
## Executive Summary
## Literature Review
## Technical Analysis
## Comparative Analysis
## Recommendations
## Implementation Plan
## References
```

### Technical Format (with --serena)
```
## Technical Context
## Code Analysis
## Architecture Implications
## Implementation Strategy
## Testing Approach
## Deployment Considerations
```

## Requirements

### Prerequisites
- Clear problem statement or decision to be made
- Sequential Thinking MCP integration available
- Optional: Serena MCP for technical problems
- Optional: Access to relevant documentation and resources

### Dependencies
- **Sequential Thinking MCP**: Primary reasoning engine
- **Serena MCP** (optional): For codebase-aware technical decisions
- **Research Sources** (optional): For external knowledge integration
- **Documentation Tools**: For output generation and storage

## Best Practices

### Mode Selection Guidelines
1. **Think**: Quick decisions, simple problems, time constraints, familiar domains
2. **Think-Hard**: Important decisions, moderate complexity, stakeholder impact
3. **Think-Harder**: Critical decisions, high complexity, architectural changes
4. **UltraThink**: Mission-critical, research-level, maximum insight needed, new domains

### Sequential Thinking Optimization
1. **Start Simple**: Begin with lower modes and escalate if needed
2. **Clear Problem Framing**: Provide specific, well-defined problem statements
3. **Context Inclusion**: Include relevant constraints and requirements
4. **Iterative Refinement**: Use interactive mode for complex undefined problems

### Serena Integration Strategy
1. **Technical Problems**: Always use `--serena` for code-related decisions
2. **Architecture Decisions**: Combine `--serena` with higher thinking modes
3. **Implementation Planning**: Use Serena memory for continuity
4. **Pattern Recognition**: Leverage Serena for similar problem identification

### Output and Documentation
1. **Structured Output**: Use `--structured` for decision documentation
2. **Confidence Tracking**: Include `--confidence` for risk assessment
3. **Memory Storage**: Save important decisions for future reference
4. **Citation Management**: Use `--citations` for research-based decisions

## Usage Examples

### Development Scenarios

```bash
# UI/UX decisions with design focus
/smart-think "Color scheme for admin dashboard" -m think --focus=design --confidence

# Simple technical trade-offs
/smart-think "REST vs GraphQL for this API" -m think-hard --serena --focus=api

# System design with implementation planning
/smart-think "Design real-time notification system" -m think-harder --serena --structured

# Strategic architecture decisions
/smart-think "Monorepo vs multi-repo for our team" -m ultrathink --structured --confidence
```

### Research and Analysis

```bash
# Technology evaluation with evidence
/smart-think "Blockchain integration for supply chain" -m ultrathink --research --citations

# Competitive analysis with strategic thinking
/smart-think "Market positioning strategy" -m think-harder --research --structured

# Performance optimization with codebase context
/smart-think "Optimize React app rendering" -m think-hard --serena --focus=performance

# Security architecture with risk assessment
/smart-think "Zero-trust security implementation" -m think-harder --serena --focus=security --confidence
```

### Team and Process Decisions

```bash
# Development workflow optimization
/smart-think "Improve CI/CD pipeline efficiency" -m think-hard --structured --focus=devops

# Team structure and responsibilities
/smart-think "Restructure development teams for microservices" -m think-harder --interactive --structured
```

## Integration Patterns

### With Other Commands
```bash
# Research → Think → Implement workflow
/tech-research "microservices patterns" --serena
/smart-think "choose microservices architecture" -m think-harder --serena --use-research
/serena "implement service discovery" --use-decisions

# Debug → Think → Optimize workflow
/debug-error "performance bottleneck" --serena
/smart-think "optimization strategy" -m think-hard --serena --use-debug-context
/serena "implement caching layer" --performance-focused

# Think → Commit workflow
/smart-think "refactoring approach" -m think-hard --serena --structured
/commit --scope=refactor --serena-context --document-decisions
```

### Decision Documentation
```bash
# Architecture decision with full documentation
/smart-think "database selection" -m think-harder --structured --confidence --output=db-decision.md

# Team collaboration preparation
/smart-think "API design approach" -m think-hard --interactive --citations --structured

# Risk assessment for critical changes
/smart-think "production deployment strategy" -m ultrathink --serena --impact --confidence
```

## Troubleshooting

### Common Issues
| Issue | Solution | Prevention |
|-------|----------|------------|
| "Budget exceeded" | Reduce mode or increase budget | Start with appropriate mode for complexity |
| "Low confidence results" | Use higher mode or add `--research` | Include more context in problem statement |
| "Too generic" | Add `--focus` or `--serena` | Be specific about constraints and requirements |
| "No technical insights" | Add `--serena` flag | Use Serena for all code-related problems |
| "Unclear recommendations" | Use `--structured` and `--confidence` | Request specific output format |
| "Missing context" | Add relevant background information | Include stakeholder and constraint information |

### Performance Tips
1. **Match Mode to Complexity**: Start conservative, escalate as needed
2. **Use Focus Areas**: Prevent scope creep with specific focus parameters
3. **Leverage MCP Integration**: Use Serena for technical context, research for knowledge
4. **Document Decisions**: Save important analysis for reuse and reference
5. **Iterative Approach**: Use interactive mode for evolving requirements

## Error Handling

- **Budget Exceeded**: Automatic mode adjustment or budget increase suggestions
- **Low Confidence**: Recommendations for additional research or higher thinking modes
- **Missing Context**: Prompts for additional information or Serena integration
- **Complex Problems**: Automatic escalation to higher thinking modes

## Future Enhancements

Planned features:
- **Team Collaboration**: Multi-user thinking sessions with shared context
- **Template Library**: Pre-built thinking templates for common decision types
- **Learning Integration**: Improve reasoning quality based on past decision outcomes
- **External Integration**: Real-time data integration for informed decision making
- **Visualization**: Interactive thinking process diagrams and decision trees
- **Version Control**: Track thinking evolution and decision rationale over time
- **Automated Follow-up**: Scheduled reassessment of critical decisions