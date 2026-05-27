---
description: Secret handling, input validation via Valibot, XSS safety
globs: ["**/*.{ts,tsx}"]
alwaysApply: true
---

# Security

## Secrets

NEVER hardcode secrets, tokens, or credentials in source files.

```typescript
// CORRECT: read from environment at startup
const apiKey = import.meta.env.VITE_API_KEY;
if (!apiKey) throw new Error("VITE_API_KEY is required");

// WRONG: hardcoded secret
const apiKey = "sk-abc123...";
```

### dotenvx environment management

- **Commit `.env`, `.env.development`, `.env.production`, and `.env.local` while they remain encrypted** (`encrypted:...` format; safe even if an AI reads them).
- **Never commit `.env.keys` or share it in plain text** (it is gitignored).
- When adding a new variable, use `vp run env:set NEW_VAR "value" -f .env.development` (do not hand-write `encrypted:` values).
- `import.meta.env.VITE_*` is decrypted and inlined at build time by dotenvx, so **plain values end up in the client bundle**—follow the `VITE_` prefix convention.
- **Server-only values** (e.g. `SESSION_SECRET`) have **no** `VITE_` prefix. Read them with `process.env.SESSION_SECRET` and **do not** expose them via `import.meta.env`.
- **Fail fast:** if a required env var is `undefined`, **throw at startup** with `throw new Error(...)` (keep the same pattern as existing code).

## Input validation

ALWAYS validate user input and external API data at system boundaries using Valibot. See [typescript/valibot-validation.md](../typescript/valibot-validation.md) for schema patterns.

```typescript
// CORRECT: validate before use
const result = v.safeParse(ProductSchema, rawInput);
if (!result.success) throw new ValidationError(result.issues);

// WRONG: trusting unvalidated external data
const product = rawApiResponse.data as Product;
```

## XSS

Avoid `dangerouslySetInnerHTML`. If HTML rendering is unavoidable, sanitize the input first with a trusted library.
