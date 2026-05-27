---
description: Use when finishing a feature, fixing a bug, before committing React code, or when the user wants to improve code quality or clean up a codebase. Checks for score regression. Covers lint, dead code, accessibility, bundle size, architecture diagnostics.
metadata:
  github-path: skills/react-doctor
  github-ref: refs/tags/react-doctor@0.0.38
  github-repo: https://github.com/millionco/react-doctor
  github-tree-sha: 51eb45712bb6cbf45722b4a33f209ac5df13c6ff
name: react-doctor
version: 1.0.0
---

# React Doctor

Scans React codebases for security, performance, correctness, and architecture issues. Outputs a 0–100 health score.

## After making React code changes:

Run `npx -y react-doctor@latest . --verbose --diff` and check the score did not regress.

If the score dropped, fix the regressions before committing.

## For general cleanup or code improvement:

Run `npx -y react-doctor@latest . --verbose` (without `--diff`) to scan the full codebase. Fix issues by severity — errors first, then warnings.

## Command

```bash
npx -y react-doctor@latest . --verbose --diff
```

| Flag        | Purpose                                       |
| ----------- | --------------------------------------------- |
| `.`         | Scan current directory                        |
| `--verbose` | Show affected files and line numbers per rule |
| `--diff`    | Only scan changed files vs base branch        |
| `--score`   | Output only the numeric score                 |
