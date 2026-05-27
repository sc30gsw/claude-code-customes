---
description: Core coding style — naming, comments, import order, file size, immutability
globs: ["**/*.{ts,tsx,js,jsx}"]
alwaysApply: true
---

# Coding Style

Full conventions are in [CODING_GUIDELINES.md](/CODING_GUIDELINES.md) §コードスタイル and §React/TypeScript規約. The rules below highlight the most critical points and those enforced by hooks.

## Immutability

ALWAYS return new values; NEVER mutate in place:

```typescript
// CORRECT: return new copy
const updated = { ...user, name: "new name" };

// WRONG: mutates original
user.name = "new name";
```

## File size

- 200–400 lines typical
- 800 lines maximum — extract utilities when approaching this limit
- One primary responsibility per file

## Naming

| Target         | Convention       | Example                      |
| -------------- | ---------------- | ---------------------------- |
| Variables / fn | lowerCamelCase   | `userName`, `getProducts`    |
| Components     | UpperCamelCase   | `ProductList`, `LoginForm`   |
| Types          | UpperCamelCase   | `Product`, `CreateUserInput` |
| Constants      | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT`            |
| Files          | kebab-case       | `product-list.tsx`           |

## Hook-backed bans

The following are also caught by PostToolUse hooks in `.claude/settings.json`:

> Also enforced by PostToolUse hook in `.claude/settings.json`

- **No `console.log`** in committed code
- **No `interface`** — use `type` everywhere
- **No relative imports** — always use the `~/` alias, even for files in the same directory or adjacent directories

```typescript
// WRONG: relative paths, even when the file is right next to you
import { tenantsFixture } from "./tenants-fixture";
import { helper } from "../utils/helper";

// CORRECT: always ~
import { tenantsFixture } from "~/features/tenants/mocks/tenants-fixture";
import { helper } from "~/features/tenants/utils/helper";
```

- **No `export default`** outside `src/routes/**` and `*.config.ts`
