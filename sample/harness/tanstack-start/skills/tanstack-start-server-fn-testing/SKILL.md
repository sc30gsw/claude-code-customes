---
name: tanstack-start-server-fn-testing
description: "Unit-test TanStack Start createServerFn handlers via a global vi.mock that combines two patterns from Discussion #2701"
user-invocable: true
origin: auto-extracted
---

# TanStack Start Server Function Unit Testing

**Updated:** 2026-05-12
**Context:** Testing internal logic of `createServerFn`-defined server functions with Vitest, without spinning up the full TanStack Start server runtime.

## Problem

`createServerFn` is a server-only API. Importing it normally in tests fails because:

1. The `'use server'` pragma check throws `Invariant failed: createServerFn must be called with a function that is marked with the 'use server' pragma` at runtime.
2. The `tanstackStart()` Vite plugin rewrites the `handler(fn)` argument into a client RPC stub at build time, so even mocking `createServerFn` can't reach the original handler logic.

## Solution: combine two patterns from Discussion #2701

This project's solution lives in `src/test/server-fn-mock.ts` and is built from **two posts in [TanStack Router Discussion #2701](https://github.com/TanStack/router/discussions/2701)** combined into one approach.

### Source 1 — overall direction (the opening post)

- URL: <https://github.com/TanStack/router/discussions/2701#discussion-7425606>
- Author: `cameronb23` (Nov 2024)
- Take: "the best that I have come up with is mocking the call globally."
- Code snippet (old `createServerFn(method, fn)` signature):
  ```ts
  vi.mock(import("@tanstack/start"), async (importOriginal) => {
    const original = await importOriginal();
    return {
      ...original,
      createServerFn: (_ignoredMethod, fn) => fn,
    };
  });
  ```
- We adopt the **global-mock direction** from this post. We do **not** adopt the literal code because it targets a legacy `createServerFn` signature; the current API is a builder.

### Source 2 — builder-aware mock (Enhanced)

- URL: <https://github.com/TanStack/router/discussions/2701#discussioncomment-15184454>
- Take: hoist a builder object that satisfies the full `.middleware().inputValidator().handler()` chain.
- Code snippet:
  ```ts
  const mockServerFunctionBuider = vi.hoisted(() => ({
    middleware: vi.fn(() => mockServerFunctionBuider),
    inputValidator: vi.fn(() => mockServerFunctionBuider),
    handler: vi.fn((func) => func),
  }));
  vi.mock("@tanstack/react-start", async (importOriginal) => ({
    ...(await importOriginal()),
    createServerFn: vi.fn(() => mockServerFunctionBuider),
  }));
  ```
- We adopt the **builder structure** from this comment, because our server fns use `.inputValidator(...).handler(...)`.

### Our project-specific divergence

The Source 2 snippet makes `inputValidator: () => builder`, which **skips the validator entirely**. We instead **run the validator** so that existing tests for `v.ValiError` (invalid input cases) continue to work end-to-end.

Concretely:

```ts
inputValidator(validate) {
  return {
    handler(fn) {
      return (opts) => fn({ data: validate(opts.data) })
    },
  }
}
```

## Required setup

Three pieces work together:

### 1. `src/test/server-fn-mock.ts`

Holds the `vi.mock("@tanstack/react-start", ...)` factory described above. The file's top-level comment cites both Discussion #2701 URLs.

### 2. `src/test/setup.ts`

Imports the mock as a side effect so it applies to every test:

```ts
import "~/test/server-fn-mock";
```

### 3. `vite.config.ts` — disable `tanstackStart()` plugin during Vitest

```ts
const isVitest = process.env.VITEST === "true";

export default defineConfig({
  plugins: [
    tailwindcss(),
    ...(isVitest ? [] : [tanstackStart()]),
    react(),
    babel({ presets: [reactCompilerPreset()] }),
  ],
});
```

Without this, the plugin replaces `handler(fn)` at build time with a client RPC stub, and the mock can never reach the original `fn`.

## Writing tests

After the setup above, server fn tests are plain imports + calls — no `import?raw`, no `new Function`, no regex source rewriting.

### GET (no input validation)

```ts
import { describe, expect, it } from "vite-plus/test";
import { fetchUsersServer } from "~/features/users/api/users-server";

describe("fetchUsersServer", () => {
  it("returns all users", async () => {
    const result = await fetchUsersServer();
    expect(result).toHaveLength(N);
  });
});
```

### POST with `inputValidator` — happy path + validation error

```ts
import * as v from "valibot";
import { describe, expect, it } from "vite-plus/test";
import { createUserServer } from "~/features/users/api/create-user-server";

describe("createUserServer", () => {
  it("creates a user", async () => {
    await expect(
      createUserServer({ data: { email: "a@b.c", name: "Alice", role: "admin" } }),
    ).resolves.toMatchObject({ email: "a@b.c" });
  });

  it("throws ValiError on invalid input", async () => {
    await expect(
      createUserServer({ data: { email: "", name: "", role: "admin" } }),
    ).rejects.toBeInstanceOf(v.ValiError);
  });
});
```

## What this approach does NOT cover

- Global / route middleware execution (Discussion #2701 also proposes an "integration harness" using `requestHandler` + `runWithStartContext` + the `#tanstack-start-server-fn-resolver` virtual module — see the opening post). We don't use it because this project has no global middleware and the integration harness is ~80 lines of glue tied to internal APIs.
- Response / Headers / Status assertions: the mock returns the handler's raw value, not a `Response`. Test the handler payload directly.
- Nested server-fn calls (one server fn calling another): not supported by either approach in Discussion #2701.

If middleware behavior or `Response` shape ever needs to be tested, revisit the integration harness option from the opening post.

## Examples in this project

All 17 server fns under `src/features/**/api/*-server.ts` (plus `src/features/auth/server/auth-server.ts`) have matching `*.test.ts` files using this pattern. Reference implementations:

- GET: `src/features/users/api/users-server.test.ts`
- POST + inputValidator: `src/features/users/api/create-user-server.test.ts`

## References

- Discussion thread: <https://github.com/TanStack/router/discussions/2701>
- Pattern 1 (global mock direction): <https://github.com/TanStack/router/discussions/2701#discussion-7425606>
- Pattern 2 (builder structure): <https://github.com/TanStack/router/discussions/2701#discussioncomment-15184454>
