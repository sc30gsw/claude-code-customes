---
description: Test user-visible behavior — role/text queries, no data-testid, Vitest via vite-plus
globs: ["**/*.{test,spec}.{ts,tsx}"]
alwaysApply: true
---

# Testing

Full guidance is in [CODING_GUIDELINES.md](../CODING_GUIDELINES.md) §テストを念頭に入れたコーディング.

## Philosophy

Write tests from the user's perspective. Assert on what the user sees and can interact with, not implementation details.

## Query priority

Prefer queries in this order:

1. **`getByRole`** — most accessible, matches semantic HTML
2. **`getByText`** — for visible text content
3. **`getByLabelText`** / **`getByPlaceholderText`** — for form fields
4. **`getByAltText`** — for images

```typescript
// CORRECT: role-based query
const button = screen.getByRole("button", { name: "送信" });
expect(screen.getByRole("heading", { name: "ユーザー一覧" })).toBeInTheDocument();

// WRONG: testId or DOM selectors
const button = screen.getByTestId("submit-button");
const heading = document.querySelector(".heading-text");
```

**`data-testid` is forbidden.** If an element has no accessible role or text, add an `aria-label` instead.

## Vitest setup

Import test utilities from `vite-plus/test`, not from `vitest` directly:

```typescript
// CORRECT
import { expect, test, vi } from "vite-plus/test";

// WRONG: direct vitest import
import { expect, test } from "vitest";
```

Run tests with `vp test`, not `vp run vitest`.

## Related skills

- `webapp-testing` — testing patterns and helpers for this project
