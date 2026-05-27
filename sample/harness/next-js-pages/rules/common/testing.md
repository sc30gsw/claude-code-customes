---
description: Testing strategy, Testing Trophy, TDD workflow, co-location, and query priority
globs: ['**/*.{test,spec}.{ts,tsx}', 'vitest.config.ts', 'playwright.config.ts']
alwaysApply: true
---

# Testing

Full guidance is in [CODING_GUIDELINES.md](/CODING_GUIDELINES.md) §テストを念頭に入れたコーディング.

## Testing Trophy Strategy

```
E2E (Playwright)          ▓░░░░░░░░░  10%
Integration (Vitest+MSW)  ▓▓▓▓▓▓░░░░  60%  ← sweet spot
Unit (Vitest)             ▓▓▓░░░░░░░  25%
Visual (Storybook VRT)    ▓░░░░░░░░░   5%
Static (TS + oxlint)      ----------  baseline
```

Integration tests are the primary investment. MSW handlers from `src/features/*/mocks/handlers.ts` (already maintained for Storybook) are reused directly in Vitest tests.

## Coverage Threshold: 80%

Lines / Functions / Branches / Statements すべて 80% 以上。

```bash
pnpm test:coverage
```

## Test-Driven Development

MANDATORY workflow:

1. Write test first (RED)
2. Run test — it should FAIL
3. Write minimal implementation (GREEN)
4. Run test — it should PASS
5. Refactor (IMPROVE)
6. Verify coverage (80%+)

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
const button = screen.getByRole('button', { name: '送信' })
expect(screen.getByRole('heading', { name: 'ユーザー一覧' })).toBeInTheDocument()

// WRONG: testId or DOM selectors
const button = screen.getByTestId('submit-button')
const heading = document.querySelector('.heading-text')
```

**`data-testid` is forbidden.** If an element has no accessible role or text, add an `aria-label` instead.

## Feature Layer Test Priorities

| Layer                                  | Test Type                | Priority |
| -------------------------------------- | ------------------------ | -------- |
| `schemas/`                             | Unit (valibot safeParse) | **P1**   |
| `hooks/use-*-actions` (mutation hooks) | Integration (MSW)        | **P1**   |
| `hooks/use-*` (query hooks, SWR)       | Integration (MSW)        | **P2**   |
| `utils/`                               | Unit                     | **P2**   |
| `components/*-container`               | Integration (render+MSW) | **P2**   |
| `components/*` (presentation)          | Unit (render+props)      | **P3**   |
| `stores/`                              | Unit                     | **P3**   |
| `api/mutations.ts`                     | Skip (tested via hooks)  | --       |

## File Organization: Co-located

Place test files adjacent to source files — NOT in `src/__tests__/`:

```
src/features/auth/
├── schemas/
│   ├── login-schema.ts
│   └── login-schema.test.ts      ← co-located
├── hooks/
│   ├── use-login.ts
│   └── use-login.test.ts         ← co-located
└── components/
    ├── login-form.tsx
    └── login-form.test.tsx       ← co-located
```

## Infrastructure

Key test infrastructure files:

- **`src/lib/msw/server.ts`** — MSW `setupServer()` for Node environment
- **`src/utils/render-with-test-providers.tsx`** — Mantine+SWR provider wrapper
- **`vitest.setup.ts`** — MSW server lifecycle (`beforeAll/afterEach/afterAll`)

## Vitest setup

Import test utilities from `vitest` directly:

```typescript
// CORRECT
import { describe, expect, it, vi } from 'vitest'

// WRONG: wrong package
import { expect, test } from 'vite-plus/test'
```

Run tests with `pnpm test:run` (single run) or `pnpm test` (watch mode).

## MSW Handler Mismatch Awareness

The existing Storybook auth handlers (`src/features/auth/mocks/handlers.ts`) match old Devise Token Auth paths (`*/auth/v1/users/sign_in`). Current API mutations use aspida paths (`/api/v1/auth/sign_in`). When testing mutation hooks, use `vi.mock('~/features/auth/api/mutations')` instead of relying on MSW interception.

The `*/api/v1/me` handler DOES match — use MSW directly for `useGetAuth` tests.

## Agent Support

- **tdd-guide** — Use PROACTIVELY for new features, enforces write-tests-first
- **e2e-runner** — Playwright E2E testing specialist

## Related skills

- `webapp-testing` — testing patterns and helpers for this project
