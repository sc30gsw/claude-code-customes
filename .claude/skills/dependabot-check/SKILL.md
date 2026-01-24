---
name: dependabot-check
description: Analyze Dependabot security advisory and provide resolution strategy
---

# Dependabot Check

Analyze Dependabot security advisory and provide resolution strategy.

## Usage

```bash
/dependabot-check <dependabot_url>
```

## Workflow

### Step 1: Gather Advisory Information

Determine URL type and use appropriate command:
- If URL contains `/security/dependabot/[number]`: Use `gh api /repos/[owner]/[repo]/dependabot/alerts/[number]`
- If URL contains `/pull/`: Use `gh pr view [url] --json title,body,commits`
- If URL contains GitHub Security Advisory ID (GHSA-xxxx): Use `gh api /advisories/[GHSA-ID]`

### Step 2: Check Current Project Status

```bash
git status
pnpm list --depth=0    # Check direct dependencies
pnpm why [package]     # Check dependency tree
```

### Step 3: Dependency Analysis

1. **Check Direct vs Indirect Dependency**
   - Check if package exists in package.json
   - If yes: Direct dependency
   - If no: Indirect dependency

2. **Analyze Dependency Tree**
   - Use `pnpm why [package-name]`
   - Identify parent packages

### Step 4: Resolution Strategy

**For Direct Dependencies:**
```bash
pnpm update [package-name]
# Or modify package.json version then
pnpm install
```

**For Indirect Dependencies:**
1. Check if parent package update is minor/patch (low risk) or major (high risk)
2. For minor/patch updates: Update parent package directly
3. For major updates: Consider using pnpm overrides:

```json
{
  "pnpm": {
    "overrides": {
      "[package-name]": "^[safe-version]"
    }
  }
}
```

## Output Format

```markdown
## 🚨 Dependabot Advisory Analysis

**Reference URL**: [url]

### Vulnerable Package
- **Package Name**: [name] ([direct/indirect])
- **Current Version**: [current] → **Recommended**: [recommended]
- **Severity**: [level]

### 🔧 Resolution Strategy
- **Parent Package**: [parent] ([current] → [required])
- **Update Level**: [Major/Minor/Patch]
- **Recommended Method**: [approach]

### 📋 Checklist
- [ ] Verify lock file changes
- [ ] Identify dependency source
- [ ] Check for breaking changes
```
