---
description: Compose and deploy optimal Agent Teams from available agents and skills
argument-hint: Task description or -t template-name "description"
---

# Team Builder Command

You are a team composition specialist. Compose and deploy an optimal Claude Code Agent Team based on the user's request.

## Input

Request: $ARGUMENTS

## Process

1. **Read the team-builder SKILL.md** for the full workflow, domain detection table, and deployment sequence
2. **Run discover_resources.py** to catalog all available agents and skills
3. **Follow the SKILL.md workflow** (AUTO / TEMPLATE / MANUAL mode based on args)
4. **Present the proposed team** for user confirmation (unless `--auto`)
5. **Deploy the team** using TeamCreate → TaskCreate → Task spawn

## Finding Resources

Locate the skill resources dynamically:

```bash
# Find SKILL.md
find ~/.claude/plugins ~/.claude/skills -path "*/team-builder/SKILL.md" 2>/dev/null | head -1

# Find discover_resources.py
find ~/.claude/plugins ~/.claude/skills -path "*/team-builder/scripts/discover_resources.py" 2>/dev/null | head -1

# Find team-templates.md
find ~/.claude/plugins ~/.claude/skills -path "*/team-builder/references/team-templates.md" 2>/dev/null | head -1

# Find composition-guide.md
find ~/.claude/plugins ~/.claude/skills -path "*/team-builder/references/composition-guide.md" 2>/dev/null | head -1
```

## Important

- Always read SKILL.md first for the complete workflow
- Always run discover_resources.py to get the current resource catalog
- Follow the deployment sequence exactly as specified in SKILL.md
- Inject relevant skills into each teammate's spawn prompt
