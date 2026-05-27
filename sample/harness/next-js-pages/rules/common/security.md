---
description: Secret handling, input validation via Valibot, XSS safety
globs: ['**/*.{ts,tsx}']
alwaysApply: true
---

# Security

## Secrets

NEVER hardcode secrets, tokens, or credentials in source files.

```typescript
// CORRECT: read from environment at startup
const apiKey = import.meta.env.VITE_API_KEY
if (!apiKey) throw new Error('VITE_API_KEY is required')

// WRONG: hardcoded secret
const apiKey = 'sk-abc123...'
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
const result = v.safeParse(ProductSchema, rawInput)
if (!result.success) throw new ValidationError(result.issues)

// WRONG: trusting unvalidated external data
const product = rawApiResponse.data as Product
```

## XSS

Avoid `dangerouslySetInnerHTML`. If HTML rendering is unavoidable, sanitize the input first with a trusted library.

## Mandatory Security Checks

コミット前に全項目を確認:

- [ ] ハードコードされたシークレットなし（APIキー、パスワード、トークン）
- [ ] ユーザー入力を全て検証済み
- [ ] SQLインジェクション対策（パラメータ化クエリ）
- [ ] XSS対策（HTMLのサニタイズ）
- [ ] CSRF保護を有効化
- [ ] 認証・認可の検証
- [ ] 全エンドポイントにレート制限
- [ ] エラーメッセージが機密情報を漏洩しない

## Security Response Protocol

セキュリティ問題を発見した場合:

1. **即座に停止する**
2. **security-reviewer** エージェントを使用する
3. CRITICAL な問題を修正してから作業を再開する
4. 漏洩したシークレットをローテートする
5. コードベース全体で類似の問題を確認する
