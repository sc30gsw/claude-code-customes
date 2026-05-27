---
description: MSW handler placement under features/*/mocks/, type-safe responses, test setup
globs: ['src/features/**/mocks/*.ts', '**/*.{test,spec}.{ts,tsx}']
alwaysApply: true
---

# MSW Mocking

## Placement: `features/*/mocks/`

Each feature owns its MSW handlers. Place them in `features/[feature]/mocks/handlers.ts`:

```
src/features/products/mocks/
└── handlers.ts
```

Aggregate handlers in a top-level `src/mocks/handlers.ts` when you need to compose across features:

```typescript
// src/mocks/handlers.ts
import { productHandlers } from '~/features/products/mocks/handlers'
import { userHandlers } from '~/features/users/mocks/handlers'

export const handlers = [...productHandlers, ...userHandlers]
```

## Type-safe responses

Use generated types from `types.gen.ts` to type mock responses:

```typescript
// features/products/mocks/handlers.ts
import { http, HttpResponse } from 'msw'
import type { Product } from '~/lib/api/generated/types.gen'

const mockProduct: Product = {
  createdAt: '2024-01-01T00:00:00Z',
  description: 'テスト商品',
  id: 'product-1',
  name: 'テスト商品A',
  price: 1000,
}

export const productHandlers = [
  http.get('/api/products', () => HttpResponse.json({ products: [mockProduct] })),
  http.post('/api/products', async ({ request }) => {
    const body = await request.json()
    return HttpResponse.json({ ...mockProduct, ...body }, { status: 201 })
  }),
]
```

## Test setup with `setupServer`

Initialize MSW once in a Vitest setup file:

```typescript
// src/test/setup.ts
import { setupServer } from 'msw/node'
import { handlers } from '~/mocks/handlers'

export const server = setupServer(...handlers)

beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

Override handlers per-test when needed:

```typescript
import { http, HttpResponse } from 'msw'
import { server } from '~/test/setup'

test('shows error state when API fails', async () => {
  server.use(http.get('/api/products', () => HttpResponse.error()))
  // ... render and assert
})
```

## Related rules

- [common/testing.md](../common/testing.md) — role/text query philosophy
