---
description: Server state via TanStack Query, client state via Jotai — boundary table, atom naming, anti-patterns
globs: ["src/features/**/hooks/*.ts", "src/features/**/stores/*.ts", "src/routes/*.tsx"]
alwaysApply: true
---

# State Management: TanStack Query + Jotai

## State-concern table

| Concern      | Tool                          | Where                              |
| ------------ | ----------------------------- | ---------------------------------- |
| Server state | TanStack Query                | `features/*/hooks/use-*.ts`        |
| Client state | Jotai                         | `features/*/stores/*.ts`           |
| URL state    | TanStack Router search params | `routes/*.tsx`                     |
| Form state   | TanStack Form                 | `features/*/components/*-form.tsx` |

**Do not duplicate server state into Jotai atoms.**

## TanStack Query: `loader` + `useSuspenseQuery`

Prefetch data in the route `loader`, then consume it in the component with `useSuspenseQuery`. The query client is provided via router context.

```typescript
// src/routes/products.tsx
export const Route = createFileRoute('/products')({
  loader: ({ context: { queryClient } }) =>
    queryClient.ensureQueryData(getProductsOptions({ query: { limit: 20 } })),
  component: ProductsPage,
})

function ProductsPage() {
  // suspense is guaranteed — loader already fetched this
  const { data } = useSuspenseQuery(getProductsOptions({ query: { limit: 20 } }))
  return <ProductList products={data.products} />
}
```

Custom query hooks live in `features/*/hooks/`:

```typescript
// features/products/hooks/use-products.ts
import { useSuspenseQuery } from "@tanstack/react-query";
import { getProductsOptions } from "~/lib/api/generated/@tanstack/react-query.gen";

export function useProducts({ limit }: { limit: number }) {
  return useSuspenseQuery(getProductsOptions({ query: { limit } }));
}
```

## Jotai: atom naming and placement

- **Naming**: suffix atom names with `Atom` (e.g., `selectedProductIdAtom`, `sidebarOpenAtom`)
- **Placement**: `features/[feature]/stores/[name].ts` for feature-scoped state; `src/stores/[name].ts` for truly global UI state (create this directory on demand)

```typescript
// features/products/stores/product-selection.ts
import { atom } from "jotai";

export const selectedProductIdAtom = atom<string | null>(null);
```

## Anti-pattern: server data in Jotai

```typescript
// WRONG: copying server state into Jotai — creates sync issues and bypasses cache
const [products, setProducts] = useAtom(productsAtom);
useEffect(() => {
  fetchProducts().then(setProducts);
}, []);

// CORRECT: let TanStack Query own the server state
const { data } = useProducts({ limit: 20 });
```

## URL state

Persist shareable UI state (filters, sort, pagination, active tab) in the URL via TanStack Router's `search` params — not in Jotai:

```typescript
export const Route = createFileRoute("/products")({
  validateSearch: (search) => v.parse(ProductSearchSchema, search),
  component: ProductsPage,
});
```
