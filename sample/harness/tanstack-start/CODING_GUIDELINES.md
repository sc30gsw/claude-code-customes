# コーディング規約

このドキュメントは `e_value_management_admin` フロントエンドプロジェクトのコーディング規約を定義します。

## 目次

1. [プロジェクト構造](#プロジェクト構造)
2. [型定義規約](#型定義規約)
3. [テストを念頭に入れたコーディング](#テストを念頭に入れたコーディング)
4. [コードスタイル](#コードスタイル)
5. [React/TypeScript規約](#reacttypescript規約)
6. [追加推奨事項](#追加推奨事項)

---

## プロジェクト構造

[Bulletproof React](https://github.com/alan2207/bulletproof-react) のFeature-based構造を採用しています。

```
src/
├── features/       # 機能別モジュール（メイン）
│   └── [feature]/
│       ├── api/          # query/mutation ラッパー（生成物から派生）
│       ├── components/   # feature固有のコンポーネント
│       ├── hooks/        # feature固有のカスタムフック
│       ├── schemas/      # Valibotスキーマ（生成物の再利用も可）
│       ├── stores/       # Jotaiストア
│       ├── types/        # 型定義（生成物からの派生）
│       └── mocks/        # テスト用MSWハンドラ
├── routes/         # TanStack Router のfile-basedルート（ロジックは最小限）
├── lib/            # ライブラリ設定・初期化
│   ├── api/
│   │   ├── client.ts     # ky/hey-api クライアント設定（timeout/retry等）
│   │   └── generated/    # openapi-ts による自動生成（編集禁止）
│   ├── theme.ts          # Mantine テーマ
│   └── utils.ts          # 共通ユーティリティ（cn など）
└── styles.css
```

`src/components/`・`src/hooks/`・`src/stores/`・`src/utils/` は必要になった時点で作成します。

### ディレクトリの役割

| ディレクトリ  | 説明                                                                                               |
| ------------- | -------------------------------------------------------------------------------------------------- |
| `features/`   | ビジネスロジックの中心。機能ごとに独立したモジュールとして構成                                     |
| `components/` | Button, Modal など複数のfeatureで共有するUIコンポーネント（必要になったら作成）                    |
| `routes/`     | TanStack Router のfile-basedルート。`createFileRoute` でロジックは最小限にしてfeatureを呼び出す    |
| `lib/api/`    | `client.ts` はクライアント設定のみ。`generated/` は `vp run generate:api` の出力（手で編集しない） |
| `lib/`        | Mantine テーマ等ライブラリの設定・ラッパー                                                         |

### インポートパス（必須）

**`~` エイリアスの使用は必須です。** 相対パスでのインポートは禁止します。

```typescript
// ✅ Good: ~ エイリアスを使用
import { useUsers } from "~/features/users/hooks/use-users";
import type { User } from "~/features/users/types/user";
import { Button } from "~/components/ui/button";

// ❌ Bad: 相対パスは禁止
import { useUsers } from "../../../features/users/hooks/use-users";
import { Button } from "../../components/ui/button";
```

> **注意**: 同一ディレクトリ内のファイルでも `~` を使用してください。これにより、ファイル移動時のインポートパス修正が不要になります。

---

## 型定義規約

### const assertion + satisfies パターン

オブジェクト定数には `as const satisfies` を使用して型安全性を確保します。

```typescript
// ✅ Good: リテラル型を保持しつつ型チェックも行う
const roleLabels = {
  admin: "管理者",
  manager: "マネージャー",
  member: "メンバー",
} as const satisfies Record<UserRole, string>;

// ❌ Bad: 型推論が string になってしまう
const roleLabels: Record<UserRole, string> = {
  admin: "管理者",
  manager: "マネージャー",
  member: "メンバー",
};
```

### Single Source of Truth

型は一箇所で定義し、派生型は親の型から生成します。`src/lib/api/generated/types.gen.ts` の生成型を基底として派生させることを優先してください。

```typescript
// types/user.ts - 一箇所で定義
export type UserRole = "admin" | "manager" | "member";
export type UserStatus = "active" | "inactive" | "pending";

export type User = {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  status: UserStatus;
  createdAt: string;
  updatedAt: string;
};

// 派生型は親の型から作成
export type CreateUserInput = Pick<User, "email" | "name" | "role"> & {
  password: string;
};

export type UpdateUserInput = Pick<User, "name" | "role" | "status">;
```

### type vs interface

基本的に `type` を使用します。

```typescript
// ✅ Good
type User = {
  id: string;
  name: string;
};

type UserTableProps = {
  users: User[];
  isLoading?: boolean;
};

// ❌ Bad（このプロジェクトでは interface を避ける）
interface User {
  id: string;
  name: string;
}
```

### 型推論を優先する

**明示的な型注釈よりも型推論を優先します。** TypeScriptが正しく推論できる場合は、型を書きません。

```typescript
// ❌ Wrong: TypeScriptが推論できるのに明示的に書いている
export const fetchTenantsServer = createServerFn().handler(
  async (): Promise<Tenant[]> => [...tenantsFixture],
);

// ✅ Good: 型推論に任せる
export const fetchTenantsServer = createServerFn().handler(async () => [...tenantsFixture]);
```

型注釈を書くのは、推論結果が `unknown` や `any` になる場合、または API の境界（外部から呼び出される公開関数）で意図を明示する必要がある場合のみです。

### TypeScript Utility型の積極的活用（必須）

**Props型など型定義では、可能な限りTypeScriptのUtility型を活用します。** 特に1〜2個のプロパティしかない場合は、専用の型を定義せず、直接Utility型を使用してください。

```typescript
import type { ReactNode } from 'react'

// ✅ Good: 1つのプロパティ → 型定義せず直接Utility型を使用
export function Container({ children }: Record<'children', ReactNode>) {
  return <div className="container">{children}</div>
}

// ✅ Good: 既存の型から派生 → Pick/Omitを活用
export function UserName({ name }: Pick<User, 'name'>) {
  return <span>{name}</span>
}

// ✅ Good: 複数の既存型から合成
export function UserCard(props: Pick<User, 'name' | 'email'> & Record<'className', string>) {
  return <div className={props.className}>{props.name}</div>
}

// ❌ Bad: 1つのプロパティのために専用型を定義
type ContainerProps = {
  children: ReactNode
}

export function Container({ children }: ContainerProps) {
  return <div className="container">{children}</div>
}

// ❌ Bad: 既存の型から簡単に派生できるのに新規定義
type UserNameProps = {
  name: string
}
```

**よく使用するUtility型:**

| Utility型      | 用途                                 | 例                              |
| -------------- | ------------------------------------ | ------------------------------- |
| `Record<K, V>` | 特定のキーと値の型を持つオブジェクト | `Record<'children', ReactNode>` |
| `Pick<T, K>`   | 既存の型から特定のプロパティを抽出   | `Pick<User, 'name' \| 'email'>` |
| `Omit<T, K>`   | 既存の型から特定のプロパティを除外   | `Omit<User, 'password'>`        |
| `Partial<T>`   | すべてのプロパティをオプショナルに   | `Partial<UserFormData>`         |
| `Required<T>`  | すべてのプロパティを必須に           | `Required<Config>`              |
| `Readonly<T>`  | すべてのプロパティを読み取り専用に   | `Readonly<State>`               |

**ガイドライン:**

1. **1〜2個のプロパティ** → 専用型を定義せず直接Utility型を使用
2. **3個以上のプロパティ** → 状況に応じて専用型の定義も可
3. **既存の型から派生可能** → 必ずPick/Omitなどを使用して派生させる

---

## テストを念頭に入れたコーディング

> **現状**: テストコードは未整備です。以下はテスト整備時の方針です。`vp test`（Vitest）で実行します。

### トリガーエレメントの取得

ユーザーがアクションを起こすためのボタンやリンクは、**role** を基準に取得します。

```typescript
// ✅ Good: roleベースでの取得
const submitButton = screen.getByRole("button", { name: "送信" });
const deleteLink = screen.getByRole("link", { name: "削除する" });

// ❌ Bad: testIdやクラス名での取得
const submitButton = screen.getByTestId("submit-button");
const deleteLink = document.querySelector(".delete-link");
```

### アサーションエレメントの取得

表示結果を確認するための要素も、可能な限り **role** や **テキスト** を基準に取得します。

```typescript
// ✅ Good: ユーザーが見る内容でアサート
expect(screen.getByRole("heading", { name: "ユーザー一覧" })).toBeInTheDocument();
expect(screen.getByText("登録が完了しました")).toBeInTheDocument();
expect(screen.getByRole("alert")).toHaveTextContent("エラーが発生しました");

// ❌ Bad: 実装詳細への依存
expect(screen.getByTestId("success-message")).toBeInTheDocument();
expect(document.querySelector(".error-text")).toBeTruthy();
```

### testId は使用しない

`data-testid` は実装の詳細に依存するため、使用を避けます。テストはユーザーの視点で書きましょう。

```typescript
// ❌ testIdを使用しない
<button data-testid="submit-btn">送信</button>

// ✅ アクセシブルな名前を付ける
<button type="submit">送信</button>
<button aria-label="メニューを開く"><HiMenu /></button>
```

---

## コードスタイル

[Node Style Guide](https://github.com/felixge/node-style-guide) を基準とし、プロジェクト固有の設定に従います。実際の整形は **oxfmt**（`vp check` / `vp fix` に内蔵）が担当するため、手動で整形する必要はありません。

### 基本ルール

| ルール     | 設定                 |
| ---------- | -------------------- |
| インデント | 2スペース            |
| クォート   | シングルクォート `'` |
| セミコロン | なし                 |
| 行の最大長 | 80文字（推奨）       |
| 末尾カンマ | あり                 |

```typescript
// ✅ Good
const user = {
  email: "john@example.com",
  id: "1",
  name: "John Doe",
};
```

### 命名規則

| 対象           | 規則             | 例                                |
| -------------- | ---------------- | --------------------------------- |
| 変数・関数     | lowerCamelCase   | `userName`, `getUsers`            |
| コンポーネント | UpperCamelCase   | `UserTable`, `LoginForm`          |
| 型・interface  | UpperCamelCase   | `User`, `CreateUserInput`         |
| 定数           | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT`, `API_BASE_URL` |
| ファイル名     | kebab-case       | `use-users.ts`, `users-table.tsx` |

### オブジェクトのキー順序

アルファベット順に並べます（特定のファイルは除外）。oxfmt の `sortImports` によりインポートは自動整列されます。

```typescript
// ✅ Good
const colors = {
  admin: "red",
  manager: "blue",
  member: "gray",
};

// ❌ Bad
const colors = {
  manager: "blue",
  admin: "red",
  member: "gray",
};
```

---

## React/TypeScript規約

### Named Export を使用

default export は `src/router.tsx` と `*.config.ts`（oxlint の `no-default-export` override 対象）を除き使用しません。TanStack Router のルートファイル（`src/routes/*.tsx`）は `export const Route = createFileRoute(...)` の named export で完結するため default export は不要です。

```typescript
// ✅ Good: Named Export
export function UserTable({ users }: UserTableProps) {
  // ...
}

export type UserTableProps = {
  users: User[];
};

// ❌ Bad: Default Export（上記除外対象以外）
export default function UserTable({ users }: UserTableProps) {
  // ...
}
```

### 関数スタイル

コンポーネントとカスタムフックは **関数宣言** スタイルを使用します。

```typescript
// ✅ Good: 関数宣言
export function UserTable({ users }: UserTableProps) {
  return <Table>{/* ... */}</Table>
}

export function useUsers(options: UseUsersOptions) {
  // ...
  return { users, isLoading }
}

// ❌ Bad: アロー関数
export const UserTable = ({ users }: UserTableProps) => {
  return <Table>{/* ... */}</Table>
}
```

### Props型の定義

Props型はコンポーネントの近くで定義し、明示的に型付けします。

```typescript
// ✅ Good
type UserFormProps = {
  isLoading?: boolean;
  onCancel: () => void;
  onSubmit: (data: CreateUserInput) => void;
  user?: User;
};

export function UserForm({ user, onSubmit, onCancel, isLoading }: UserFormProps) {
  // ...
}
```

### カスタムフックのパターン

TanStack React Query と `@hey-api/openapi-ts` が生成する `*Options` / `*Mutation` を組み合わせます。

```typescript
import { useSuspenseQuery } from "@tanstack/react-query";
import { getProductsOptions } from "~/lib/api/generated/@tanstack/react-query.gen";

type UseProductsOptions = {
  limit: number;
};

export function useProducts({ limit }: UseProductsOptions) {
  return useSuspenseQuery(getProductsOptions({ query: { limit } }));
}
```

ルートレベルのプリフェッチは `loader` + `useSuspenseQuery` パターンを使用します（`src/routes/products.tsx` 参照）。

```typescript
// src/routes/products.tsx
export const Route = createFileRoute('/products')({
  loader: ({ context: { queryClient } }) =>
    queryClient.ensureQueryData(getProductsOptions({ query: { limit: 20 } })),
  component: ProductsPage,
})

function ProductsPage() {
  const { data } = useSuspenseQuery(getProductsOptions({ query: { limit: 20 } }))
  return <ProductList products={data.products} />
}
```

---

## 追加推奨事項

### エラーハンドリング（better-result）

このプロジェクトでは [better-result](https://github.com/dmmulroy/better-result) ライブラリを使用した型安全なエラーハンドリングを採用しています。

#### API層

`src/lib/api/generated/sdk.gen.ts` の生成関数をラップします。

```typescript
import { Result } from "better-result";
import { createProduct } from "~/lib/api/generated/sdk.gen";

export function createProductSafe(params: CreateProductData["body"]) {
  return Result.tryPromise({
    catch: (e) => e as Error,
    try: async () => {
      const { data } = await createProduct({ body: params });
      return data;
    },
  });
}
```

#### フック層（use-\*.ts）

```typescript
// match パターン（キー順序はアルファベット順）
const result = await createProductSafe(params);

result.match({
  err: (error) => {
    showError({ message: error.message, title: "エラー" });
  },
  ok: (data) => {
    showSuccess({ message: "登録が完了しました" });
    onSuccess(data);
  },
});
```

**注意**: `if (result.isErr())` パターンは return 忘れによるバグの原因になるため、`match` パターンを使用してください。

### AHA Programming（抽象化の原則）

[AHA Programming](https://kentcdodds.com/blog/aha-programming)（Avoid Hasty Abstractions）の原則に従います。

> "prefer duplication over the wrong abstraction"
> （間違った抽象化よりも重複を選ぶ）— Sandi Metz

```typescript
// ❌ Bad: 早すぎる抽象化
// 2回しか使われていないのに汎用化
function formatEntity(entity: User | Product, type: "user" | "product") {
  if (type === "user") {
    /* user固有の処理 */
  }
  if (type === "product") {
    /* product固有の処理 */
  }
}

// ✅ Good: パターンが明確になるまで重複を許容
function formatUser(user: User) {
  /* user固有の処理 */
}
function formatProduct(product: Product) {
  /* product固有の処理 */
}
```

**実践ガイドライン：**

1. **最初は重複を許容する** — パターンが明確になるまで待つ
2. **3回目の重複で検討する** — 2回までは重複のままでよい
3. **変化に最適化する** — 将来の要件は予測不可能
4. **間違った抽象化は重複より高コスト** — リファクタリングが困難になる

### コメント規約

- 「何をしているか」ではなく「なぜそうしているか」を書く
- 複雑なビジネスロジックには説明を追加
- TODOコメントには担当者と期限を記載

```typescript
// ✅ Good: 理由を説明
// APIの仕様上、ページネーションは1始まり
const page = currentPage + 1;

// TODO(@username 2024-12): 認証API完成後に削除
const mockToken = "dev-token";

// ❌ Bad: コードを繰り返しただけ
// ページに1を足す
const page = currentPage + 1;
```

### Import順序

oxfmt の `sortImports` により自動整列されます。手動で並べ替える必要はありません。コミット時の staged フック（`vp check --fix`）でも自動修正されます。

参考として、整列後の順序は以下のとおりです：

1. 外部ライブラリ（React、サードパーティ）
2. 内部モジュール（`~/` エイリアス）
3. 型のインポート

```typescript
import { useState } from "react";
import { Button, Table } from "@mantine/core";

import { useUsers } from "~/features/users/hooks/use-users";
import { formatDate } from "~/utils/date";

import type { User, UserRole } from "~/features/users/types/user";
```

### Feature間の依存

Feature間の直接依存は避けます。共通で必要なものは上位のディレクトリに配置します。

```typescript
// ❌ Bad: feature間の直接依存
// src/features/orders/components/order-form.tsx
import { UserSelect } from "~/features/users/components/user-select";

// ✅ Good: 共有コンポーネントとして抽出
// src/components/user-select.tsx
import { UserSelect } from "~/components/user-select";
```

---

## ツール設定

このプロジェクトでは Vite+ (`vp`) に内蔵されたツールで自動チェックを行います。

| ツール     | 用途       | 設定ファイル     |
| ---------- | ---------- | ---------------- |
| oxlint     | Linter     | `vite.config.ts` |
| oxfmt      | Formatter  | `vite.config.ts` |
| TypeScript | 型チェック | `tsconfig.json`  |

### コマンド

```bash
# すべてのチェックを実行
vp check

# 自動修正
vp fix

# 個別実行
vp lint    # oxlint
vp test    # Vitest
```

`pnpm tsc` / `npx tsc` は使用しないでください。型チェックは `vp check` の typeCheck に内包されています。

---

## 参考リンク

- [Bulletproof React](https://github.com/alan2207/bulletproof-react)
- [Node Style Guide](https://github.com/felixge/node-style-guide)
- [Testing Library - Queries](https://testing-library.com/docs/queries/about)
- [TanStack Router](https://tanstack.com/router)
- [TanStack Query](https://tanstack.com/query)
- [TanStack Start](https://tanstack.com/start)
- [@hey-api/openapi-ts](https://heyapi.dev/openapi-ts/get-started)
- [ky](https://github.com/sindresorhus/ky)
- [better-result](https://github.com/dmmulroy/better-result)
- [Mantine v9](https://mantine.dev/)
- [Valibot](https://valibot.dev/)
- [oxlint](https://oxc.rs/docs/guide/usage/linter.html)
- [AHA Programming](https://kentcdodds.com/blog/aha-programming)
