---
allowed-tools: Read, Write, Glob, TodoWrite, mcp__sequential-thinking__sequentialthinking
description: Create quarterly OKRs based on team goals and role. Generates 3 Objectives with 3 Key Results each (9 total), with 70%/100% achievement criteria.
argument-hint: --role <role> <team-goals>
---

# /okr - OKR Creation Support Command

## Overview
An interactive command that helps create individual quarterly OKRs based on team-level goals.

## Usage
```bash
/okr --role <role> "<team-goals>"
```

### Arguments
| Argument | Required | Description |
|----------|----------|-------------|
| `--role` | Yes | Role (engineer, pm, designer, qa, data-analyst, etc.) |
| `<team-goals>` | Yes | Team-level goals (natural language text) |

### Examples
```bash
/okr --role engineer "20% revenue increase, NPS +10 improvement, 2 new product launches"
/okr --role pm "Team productivity improvement, quality enhancement, technical debt reduction"
/okr --role designer "UX improvement, design system establishment, brand consistency"
```

## Processing Workflow

### Phase 1: Team Goal Analysis

1. **Argument Parsing**: Extract `--role` option and team goal text
2. **Priority Extraction**: Identify multiple priorities from team goals
3. **Role Alignment**: Analyze how the specified role can contribute to each priority

**Using Sequential Thinking**:
- Analyze team goal structure
- Identify hidden priorities and dependencies
- Determine role-appropriate focus areas

### Phase 2: Objective Design (3 Objectives)

**Characteristics of Good Objectives**:
- Qualitative and inspirational
- Clear alignment with team goals
- Achievable yet challenging
- Fits within role's responsibilities

**Design Process**:
1. Generate 3 Objective candidates corresponding to team goal priorities
2. Adjust each Objective to cover different aspects
3. Optimize expressions for the specific role

### Phase 3: Key Result Design (3 per Objective, 9 Total)

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

### Phase 4: Output & Review

Output completed OKRs in the following format:

```markdown
# Quarterly OKR (FY20XX Q○)

## Your Role
[Specified role]

## Alignment with Team Goals
[Summary of input team goals]

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

### Key Result 2.1: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 2.2: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 2.3: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

---

## Objective 3: [Objective Name]
> [Inspirational description]

### Key Result 3.1: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 3.2: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

### Key Result 3.3: [KR Name]
| Achievement | Target |
|-------------|--------|
| 70% | [Standard target] |
| 100% | [Stretch target] |

---

## Summary

| Objective | Key Results | Team Goal Alignment |
|-----------|-------------|---------------------|
| O1: [Name] | 3 | [Related priority] |
| O2: [Name] | 3 | [Related priority] |
| O3: [Name] | 3 | [Related priority] |
```

## Role-Specific Considerations

### Engineer
- Technical deliverables (code quality, performance improvements, etc.)
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
- Quality metrics (bug detection rate, coverage, etc.)
- Test automation
- Release quality gates
- Quality process improvements

### Data Analyst
- Data quality metrics
- Analytics reports and dashboards
- Data-driven decision support
- Data pipeline improvements

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

## Notes

- Review OKRs quarterly
- Check progress weekly or bi-weekly
- Adjust flexibly based on changing circumstances
- Share and align with team members and managers
