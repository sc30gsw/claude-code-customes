---
name: okr
description: Create quarterly OKRs based on team goals and role. Generates 3 Objectives with 3 Key Results each (9 total), with 70%/100% achievement criteria.
---

# OKR Creation Support

Advanced interactive command that helps create individual quarterly OKRs based on team-level goals.

## Usage

```bash
/okr --role <role> "<team-goals>" [options]
```

## Required Arguments

| Argument | Description |
|----------|-------------|
| `--role <role>` | Role (engineer, pm, designer, qa, data-analyst, etc.) |
| `<team-goals>` | Team-level goals (natural language text) |

## Options

### File Input Options
| Option | Description |
|--------|-------------|
| `--sample <path>` | Reference OKR sample file |
| `--team-okr <path>` | Reference team OKR file |
| `--previous <path>` | Reference previous quarter OKR |

### Output Options
| Option | Description |
|--------|-------------|
| `--output <path>` | Output file path |
| `--format <type>` | Output format: markdown/json/yaml |

### Interactive Features
| Option | Description |
|--------|-------------|
| `--interactive` | Interactive OKR creation mode |
| `--refine` | Refine vague goals through questions |

## Examples

```bash
# Basic usage
/okr --role engineer "20% revenue increase, NPS +10, 2 new product launches"

# With sample reference
/okr --role engineer "売上20%増加" --sample ./okrs/samples/engineer.md

# Interactive mode with persistence
/okr --role engineer --interactive --persist
```

## Output Format

### Objectives (3 total)
- Qualitative and inspirational
- Clear alignment with team goals
- Achievable yet challenging

### Key Results (3 per Objective, 9 total)
Each KR includes:
- **70% target**: Standard target (achievable with effort)
- **100% target**: Stretch target (achievable when everything goes perfectly)

## Role-Specific Considerations

### Engineer
- Technical deliverables, code quality, performance
- Development efficiency, technical debt reduction
- Learning and skill development

### PM (Product Manager)
- Product metrics (DAU, retention)
- Feature releases, user feedback
- Stakeholder coordination

### Designer
- UX/UI improvement metrics
- Design system, usability tests
- Brand consistency

### QA
- Quality metrics, test automation
- Release quality gates
- Quality process improvements
