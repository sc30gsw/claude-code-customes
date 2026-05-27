---
description: Code quality principles — KISS, DRY, YAGNI, AHA, async patterns, and code smell detection
globs: ['**/*.{ts,tsx}']
alwaysApply: true
---

# Coding Standards & Best Practices

> **Note**: For naming conventions, component structure, and project structure, see `CODING_GUIDELINES.md`. This document provides complementary best practices.

## Code Quality Principles

### 1. Readability First

- Code is read more than written
- Clear variable and function names
- Self-documenting code preferred over comments
- Consistent formatting

### 2. KISS (Keep It Simple, Stupid)

- Simplest solution that works
- Avoid over-engineering
- No premature optimization
- Easy to understand > clever code

### 3. DRY (Don't Repeat Yourself)

- Extract common logic into functions
- Create reusable components
- Share utilities across modules
- Avoid copy-paste programming

### 4. YAGNI (You Aren't Gonna Need It)

- Don't build features before they're needed
- Avoid speculative generality
- Add complexity only when required
- Start simple, refactor when needed

### 5. AHA Programming (Avoid Hasty Abstractions)

> "prefer duplication over the wrong abstraction" — Sandi Metz

詳細は `CODING_GUIDELINES.md` §AHA Programming を参照。

## Immutability (CRITICAL)

```typescript
// CORRECT
const updatedUser = { ...user, name: 'New Name' }
const updatedArray = [...items, newItem]
const filteredArray = items.filter((item) => item.active)

// WRONG: 直接変更は禁止
user.name = 'New Name'
items.push(newItem)
```

## Async/Await Best Practices

```typescript
// CORRECT: 可能な場合は並列実行
const [users, departments, roles] = await Promise.all([
  fetchUsers(),
  fetchDepartments(),
  fetchRoles(),
])

// WRONG: 不要なシーケンシャル実行
const users = await fetchUsers()
const departments = await fetchDepartments()
```

## State Updates

```typescript
// CORRECT: 前の状態に依存する場合は関数形式
setCount((prev) => prev + 1)
setItems((prev) => [...prev, newItem])

// WRONG: 非同期シナリオで古い値を参照する可能性
setCount(count + 1)
```

## Conditional Rendering

```typescript
// CORRECT: 明確な条件レンダリング
{isLoading && <Spinner />}
{error && <ErrorMessage error={error} />}
{data && <DataDisplay data={data} />}

// WRONG: ネストした三項演算子
{isLoading ? <Spinner /> : error ? <ErrorMessage error={error} /> : <DataDisplay data={data} />}
```

## Code Smell Detection

以下のアンチパターンに注意:

### Long Functions

```typescript
// WRONG: 50行超の関数
function processUserData() {
  // 100 lines
}

// CORRECT: 小さな関数に分割
function processUserData() {
  const validated = validateData()
  const transformed = transformData(validated)
  return saveData(transformed)
}
```

### Deep Nesting

```typescript
// WRONG: 5階層超のネスト
if (user) {
  if (user.isAdmin) {
    if (market?.isActive) {
      // Do something
    }
  }
}

// CORRECT: Early return でフラット化
if (!user) return
if (!user.isAdmin) return
if (!market?.isActive) return
// Do something
```

### Magic Numbers

```typescript
// WRONG: 説明のない数値
if (retryCount > 3) {
}
setTimeout(callback, 500)

// CORRECT: 名前付き定数
const MAX_RETRIES = 3
const DEBOUNCE_DELAY_MS = 500
```

## Performance Best Practices

### Lazy Loading

```typescript
import { lazy, Suspense } from 'react'

const HeavyChart = lazy(() => import('./HeavyChart'))

export function Dashboard() {
  return (
    <Suspense fallback={<Spinner />}>
      <HeavyChart />
    </Suspense>
  )
}
```

> **Note**: Manual memoization (`useMemo`/`useCallback`) は禁止。React 19 + Compiler が自動最適化するため不要。

## Comments

```typescript
// CORRECT: なぜ (WHY) を説明
// APIの仕様上、ページネーションは1始まり
const page = currentPage + 1

// WRONG: 何をしているか (WHAT) を説明するだけ
// Increment counter by 1
count++
```
