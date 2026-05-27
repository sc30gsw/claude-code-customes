---
description: Core coding style — naming, comments, import order, file size, immutability
globs: ['**/*.{ts,tsx,js,jsx}']
alwaysApply: true
---

# Coding Style

Full conventions are in [CODING_GUIDELINES.md](/CODING_GUIDELINES.md) §コードスタイル and §React/TypeScript規約. The rules below highlight the most critical points and those enforced by hooks.

## Immutability

ALWAYS return new values; NEVER mutate in place:

```typescript
// CORRECT: return new copy
const updated = { ...user, name: 'new name' }

// WRONG: mutates original
user.name = 'new name'
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
import { tenantsFixture } from './tenants-fixture'
import { helper } from '../utils/helper'

// CORRECT: always ~
import { tenantsFixture } from '~/features/tenants/mocks/tenants-fixture'
import { helper } from '~/features/tenants/utils/helper'
```

- **No `export default`** outside `src/pages/**` and `*.config.{ts,js,mjs,cjs}`

## TypeScript Utility Types (必須)

1〜2個のプロパティには専用型を定義せず直接 Utility Type を使用する:

```typescript
// CORRECT: 1 prop → Record
export function Container({ children }: Record<'children', ReactNode>) { ... }

// CORRECT: 既存型から派生 → Pick
export function UserName({ name }: Pick<User, 'name'>) { ... }

// WRONG: 1プロパティのために専用型を定義
type ContainerProps = { children: ReactNode }
export function Container({ children }: ContainerProps) { ... }
```

よく使う Utility Type: `Record<K, V>` / `Pick<T, K>` / `Omit<T, K>` / `Partial<T>` / `Required<T>`

## Japanese Comments

コードコメントは日本語で書く。WHAT ではなく WHY を説明する。

```typescript
// CORRECT: 理由を説明 (日本語)
// APIの仕様上、ページネーションは1始まり
const page = currentPage + 1

// WRONG: コードを繰り返すだけ / 英語コメント
// Increment page by 1
const page = currentPage + 1
```

## `as const satisfies` パターン

オブジェクト定数にはリテラル型を保持しつつ型チェックを行う:

```typescript
// CORRECT
const roleLabels = {
  admin: '管理者',
  manager: 'マネージャー',
  member: 'メンバー',
} as const satisfies Record<UserRole, string>

// WRONG: 型推論が string に広がる
const roleLabels: Record<UserRole, string> = { ... }
```

## Forbidden Patterns

以下を発見したら指摘する:

1. `console.log` の残存（デバッグ後は削除）
2. `any` 型の過剰使用（TypeScript Utility Type を活用）
3. ハードコードされたシークレット（環境変数を使用）
4. 800行超のファイル（200〜400行が理想）
5. 50行超の関数（コンポーネントを除く）
6. 4階層を超えるネスト

## Code Review Checklist

作業完了前に確認:

1. **CRITICAL**: better-result 違反、イミュータビリティ違反、シークレットのハードコード → **必ず修正**
2. **HIGH**: Utility Type 未使用、相対パス、default export、英語コメント、console.log → **強く推奨**
3. **MEDIUM**: ファイルサイズ、関数サイズ、ネスト深度、as const satisfies → **提案レベル**
