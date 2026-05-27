---
description: Named exports, function declarations, Utility-type props, as const satisfies, react-compiler
globs: ["src/**/*.tsx", "src/**/hooks/*.ts"]
alwaysApply: true
---

# React Conventions

> This rule extends [CODING_GUIDELINES.md](../CODING_GUIDELINES.md) §React/TypeScript規約.

## Named exports only

> Also enforced by PostToolUse hook in `.claude/settings.json`

```typescript
// CORRECT
export function ProductList({ products }: ProductListProps) { ... }

// WRONG: default export (except src/routes/ and *.config.ts)
export default function ProductList({ products }: ProductListProps) { ... }
```

## Function declarations (not arrow functions)

Components and custom hooks must use `function` declaration syntax:

```typescript
// CORRECT
export function ProductCard({ name }: Pick<Product, 'name'>) {
  return <div>{name}</div>
}

export function useProducts({ limit }: UseProductsOptions) {
  return useSuspenseQuery(getProductsOptions({ query: { limit } }))
}

// WRONG
export const ProductCard = ({ name }: Pick<Product, 'name'>) => <div>{name}</div>
```

## Utility-type props

- **1–2 props**: skip a dedicated type; use `Pick`, `Omit`, or `Record` inline
- **3+ props**: define a named `type` near the component

```typescript
// CORRECT: 1 prop → inline Record
export function Container({ children }: Record<'children', ReactNode>) {
  return <div className="container">{children}</div>
}

// CORRECT: derived from existing type
export function UserName({ name }: Pick<User, 'name'>) {
  return <span>{name}</span>
}

// CORRECT: 3+ props → named type
type ProductCardProps = {
  isLoading?: boolean
  onDelete: (id: string) => void
  product: Product
}
export function ProductCard({ product, onDelete, isLoading }: ProductCardProps) { ... }
```

## `as const satisfies` for constants

```typescript
// CORRECT: literal types preserved + type-checked
const STATUS_LABELS = {
  active: '有効',
  inactive: '無効',
  pending: '保留中',
} as const satisfies Record<UserStatus, string>

// WRONG: widened to string
const STATUS_LABELS: Record<UserStatus, string> = { ... }
```

## react-compiler

This project runs the React Compiler babel plugin. Do **not** add manual memoization without a measured reason:

```typescript
// WRONG: unnecessary — compiler handles this
const memoizedValue = useMemo(() => computeValue(a, b), [a, b]);
const stableCallback = useCallback(() => handleClick(), []);

// CORRECT: write plain code; compiler optimizes automatically
const value = computeValue(a, b);
```

Only add `useMemo` / `useCallback` when you have a profiler measurement showing a real bottleneck.

## Prefer type inference

Let TypeScript infer return types whenever possible. Only annotate when inference produces `unknown`/`any`, or at explicit public API boundaries.

```typescript
// WRONG: explicit return type when TypeScript can infer
export const fetchTenantsServer = createServerFn().handler(
  async (): Promise<Tenant[]> => [...tenantsFixture],
);

// CORRECT: let TypeScript infer
export const fetchTenantsServer = createServerFn().handler(async () => [...tenantsFixture]);
```

## Related skills

- `react-best-practices` — patterns and architecture
- `react-doctor` — React health checks (`vp run doctor`)
