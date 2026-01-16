---
allowed-tools: Read, Write, Glob, TodoWrite, Grep, WebSearch, mcp__sequential-thinking__sequentialthinking, mcp__serena__write_memory, mcp__serena__read_memory, mcp__serena__list_memories
description: Create quarterly OKRs based on team goals and role. Generates 3 Objectives with 3 Key Results each (9 total), with 70%/100% achievement criteria.
argument-hint: --role <role> <team-goals> [options]
---

# /okr - Advanced OKR Creation Support Command

## Overview
An advanced interactive command that helps create individual quarterly OKRs based on team-level goals. Supports file references, interactive mode, and session persistence.

## Usage
```bash
/okr --role <role> "<team-goals>" [options]
```

## Arguments

### Required Arguments
| Argument | Description |
|----------|-------------|
| `--role <role>` | Role (engineer, pm, designer, qa, data-analyst, etc.) |
| `<team-goals>` | Team-level goals (natural language text) |

### File/Directory Input Options
| Option | Description | Example |
|--------|-------------|---------|
| `--sample <path>` | Reference OKR sample file | `--sample ./okrs/samples/engineer.md` |
| `--team-okr <path>` | Reference team OKR file | `--team-okr ./okrs/team/2025-Q1.md` |
| `--context <path>` | Additional context file | `--context ./strategy.md` |
| `--previous <path>` | Reference previous quarter OKR | `--previous ./okrs/personal/2024-Q4.md` |
| `--mission <path>` | Company/team mission file | `--mission ./company/mission.md` |
| `--values <path>` | Company/team values file | `--values ./company/values.md` |

### Output Options
| Option | Description | Default |
|--------|-------------|---------|
| `--output <path>` | Output file path | Console |
| `--format <type>` | Output format: markdown/json/yaml | markdown |

### Interactive Features
| Option | Description |
|--------|-------------|
| `--interactive` | Interactive OKR creation mode |
| `--refine` | Refine vague goals through questions |

### Helper Options
| Option | Description |
|--------|-------------|
| `--quarter <Q1-Q4>` | Target quarter |
| `--year <YYYY>` | Target year |
| `--strengths <desc>` | Personal strengths to leverage |
| `--growth <desc>` | Growth areas to focus on |

### Advanced Options
| Option | Description |
|--------|-------------|
| `--benchmark` | Reference industry benchmarks |
| `--persist` | Save session to Serena memory |
| `--resume` | Resume from previous session |

## Examples

### Basic Usage
```bash
/okr --role engineer "20% revenue increase, NPS +10, 2 new product launches"
```

### With Sample Reference
```bash
/okr --role engineer "売上20%増加" --sample ./okrs/samples/engineer.md
```

### With Team OKR and Mission Alignment
```bash
/okr --role pm "チーム成長" --team-okr ./okrs/team/2025-Q1.md --mission ./company/mission.md
```

### Interactive Mode with Persistence
```bash
/okr --role engineer --interactive --persist
```

### JSON Output to File
```bash
/okr --role designer "UX improvement" --format json --output ./okrs/personal/2025-Q1.json
```

### Resume from Previous Quarter
```bash
/okr --role engineer "継続改善" --previous ./okrs/personal/2024-Q4.md --refine
```

---

## Processing Workflow

### Phase 1: Argument Parsing & Context Loading

1. **Parse Arguments**: Extract all options and flags
2. **Load Reference Files**: Read any specified files (sample, team-okr, context, etc.)
3. **Check Session**: If `--resume`, load from Serena memory
4. **Validate Inputs**: Ensure required arguments are present

**Implementation**:
```
IF $ARGUMENTS contains "--sample":
  Read sample file using Read tool
  Extract OKR patterns and examples

IF $ARGUMENTS contains "--team-okr":
  Read team OKR file
  Extract team objectives for alignment check

IF $ARGUMENTS contains "--previous":
  Read previous quarter OKR
  Identify completed, continued, and new goals

IF $ARGUMENTS contains "--resume":
  Call mcp__serena__list_memories()
  Call mcp__serena__read_memory("okr_session") if exists
  Load previous session context
```

### Phase 2: Team Goal Analysis

1. **Priority Extraction**: Identify multiple priorities from team goals
2. **Role Alignment**: Analyze how the specified role can contribute
3. **Context Integration**: Incorporate mission/values if provided

**Using Sequential Thinking**:
- Analyze team goal structure
- Identify hidden priorities and dependencies
- Determine role-appropriate focus areas
- Cross-reference with team OKR if provided

### Phase 3: Interactive Refinement (if --interactive or --refine)

If `--interactive` or `--refine` is specified, engage in dialogue:

**Questions to Ask**:
1. "What are your current challenges in achieving these goals?"
2. "Are there specific skills you want to develop this quarter?"
3. "What dependencies or blockers might affect your objectives?"
4. "How will you measure success beyond the obvious metrics?"
5. "What resources or support do you need?"

**Process**:
- Ask 2-3 clarifying questions per objective area
- Refine goals based on responses
- Validate understanding before generating OKRs

### Phase 4: Objective Design (3 Objectives)

**Characteristics of Good Objectives**:
- Qualitative and inspirational
- Clear alignment with team goals
- Achievable yet challenging
- Fits within role's responsibilities

**Design Process**:
1. Generate 3 Objective candidates corresponding to team goal priorities
2. Adjust each Objective to cover different aspects
3. Optimize expressions for the specific role
4. If sample provided, follow sample patterns

### Phase 5: Key Result Design (3 per Objective, 9 Total)

**Characteristics of Good Key Results (SMART)**:
- **S**pecific
- **M**easurable
- **A**chievable
- **R**elevant
- **T**ime-bound (quarterly)

**70%/100% Achievement Criteria Guidelines**:

| Achievement | Meaning | Setting Criteria |
|-------------|---------|------------------|
| 70% | Standard target | Highly achievable with effort |
| 100% | Stretch target | Achievable when everything goes perfectly |

**Design Process**:
1. Generate 3 measurable KRs for each Objective
2. Set dual targets: 70% (standard) and 100% (stretch) for each KR
3. Validate numerical targets for reasonableness
4. If benchmark requested, research industry standards

### Phase 6: Output Generation

**Format Handling**:

```
IF --format == "json":
  Generate JSON structure with OKR data

IF --format == "yaml":
  Generate YAML structure with OKR data

ELSE (markdown):
  Generate formatted markdown
```

**Output Handling**:

```
IF --output specified:
  Write to file using Write tool

ELSE:
  Output to console
```

### Phase 7: Session Persistence (if --persist)

```
IF --persist:
  Call mcp__serena__write_memory("okr_session", session_data)
  Include: role, goals, generated OKRs, timestamp
```

---

## Output Format

### Markdown Format (Default)

```markdown
# Quarterly OKR (FY20XX Q○)

## Your Role
[Specified role]

## Alignment with Team Goals
[Summary of input team goals]

### Reference Context
[If sample/team-okr/mission provided, note alignment]

### Extracted Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

---

## Objective 1: [Objective Name]
> [Inspirational description]

### Key Result 1.1: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 1.2: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 1.3: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

---

## Objective 2: [Objective Name]
> [Inspirational description]

[Key Results 2.1-2.3...]

---

## Objective 3: [Objective Name]
> [Inspirational description]

[Key Results 3.1-3.3...]

---

## Summary

| Objective | Key Results | Team Goal Alignment |
|-----------|-------------|---------------------|
| O1: [Name] | 3 | [Related priority] |
| O2: [Name] | 3 | [Related priority] |
| O3: [Name] | 3 | [Related priority] |
```

### JSON Format

```json
{
  "quarter": "Q1",
  "year": 2025,
  "role": "engineer",
  "teamGoals": "...",
  "objectives": [
    {
      "id": 1,
      "name": "...",
      "description": "...",
      "keyResults": [
        {
          "id": "1.1",
          "name": "...",
          "target70": "...",
          "target100": "..."
        }
      ]
    }
  ]
}
```

### YAML Format

```yaml
quarter: Q1
year: 2025
role: engineer
teamGoals: "..."
objectives:
  - id: 1
    name: "..."
    description: "..."
    keyResults:
      - id: "1.1"
        name: "..."
        target70: "..."
        target100: "..."
```

---

## Role-Specific Considerations

### Engineer
- Technical deliverables (code quality, performance improvements)
- Development efficiency improvements
- Technical debt reduction
- Learning and skill development

### PM (Product Manager)
- Product metrics (DAU, retention, etc.)
- Feature releases
- User feedback response
- Stakeholder coordination

### Designer
- UX/UI improvement metrics
- Design system creation
- Usability test results
- Brand consistency

### QA
- Quality metrics (bug detection rate, coverage)
- Test automation
- Release quality gates
- Quality process improvements

### Data Analyst
- Data quality metrics
- Analytics reports and dashboards
- Data-driven decision support
- Data pipeline improvements

---

## OKR Best Practices

### About Objectives
- **DO**: Use ambitious and inspiring language
- **DO**: Show clear connection to team goals
- **DON'T**: Include numbers (that's for KRs)
- **DON'T**: Use vague expressions

### About Key Results
- **DO**: Always set measurable numerical targets
- **DO**: Make the difference between 70% and 100% clear
- **DON'T**: Describe activities (tasks) instead of outcomes
- **DON'T**: Depend too heavily on external factors beyond your control

### Setting 70%/100% Targets
- **70%**: "Can achieve with hard work" level
- **100%**: "If everything goes perfectly" level
- 70% achievement = "Success"
- 100% achievement = "Excellence"

---

## Session Management

### Saving Sessions
```bash
/okr --role engineer "goals" --persist
```
This saves your session to Serena memory for later resumption.

### Resuming Sessions
```bash
/okr --resume
```
This loads your previous session and continues from where you left off.

### Viewing Saved Sessions
You can check existing memories using the Serena memory tools:
- List all memories: `mcp__serena__list_memories()`
- Read specific memory: `mcp__serena__read_memory("okr_session")`

---

## Notes

- Review OKRs quarterly
- Check progress weekly or bi-weekly
- Adjust flexibly based on changing circumstances
- Share and align with team members and managers
