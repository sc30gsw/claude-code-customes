# コーディングスタイル

コードの書き方に関するルールです。

## イミュータビリティ (CRITICAL)

**常に新しいオブジェクトを作成し、絶対にミューテーションしない:**

```javascript
// WRONG: ミューテーション
function updateUser(user, name) {
  user.name = name  // ミューテーション！
  return user
}

// CORRECT: イミュータビリティ
function updateUser(user, name) {
  return {
    ...user,
    name
  }
}
```

## ファイル構成

**多数の小さなファイル > 少数の大きなファイル:**

- 高凝集度、低結合度
- 通常200-400行、最大800行
- 大きなコンポーネントからユーティリティを抽出
- タイプではなく、機能/ドメインで整理

## エラーハンドリング

**常に包括的にエラーを処理:**

```typescript
try {
  const result = await riskyOperation()
  return result
} catch (error) {
  console.error('Operation failed:', error)
  throw new Error('Detailed user-friendly message')
}
```

## 入力検証

**常にユーザー入力を検証:**

```typescript
import { z } from 'zod'

const schema = z.object({
  email: z.string().email(),
  age: z.number().int().min(0).max(150)
})

const validated = schema.parse(input)
```

## コード品質チェックリスト

作業完了前に確認:

- [ ] コードは読みやすく適切に命名されている
- [ ] 関数は小さい（<50行）
- [ ] ファイルは集中している（<800行）
- [ ] 深いネストがない（>4レベル）
- [ ] 適切なエラーハンドリング
- [ ] console.log文がない
- [ ] ハードコードされた値がない
- [ ] ミューテーションがない（イミュータブルパターンを使用）

## 命名規則

| 種類 | 規則 | 例 |
|-----|------|-----|
| 変数 | camelCase | `userName`, `isActive` |
| 関数 | camelCase | `getUserData`, `calculateTotal` |
| クラス | PascalCase | `UserService`, `MarketController` |
| 定数 | UPPER_SNAKE | `MAX_RETRIES`, `API_ENDPOINT` |
| ファイル | kebab-case | `user-service.ts`, `market-utils.ts` |

## TypeScript固有

```typescript
// 明示的な型注釈を使用
function add(x: number, y: number): number {
  return x + y
}

// anyを避ける - unknownまたは具体的な型を使用
function process(data: unknown): void {
  if (typeof data === 'string') {
    // 型ガード後に安全に使用
  }
}

// オプショナルチェーンを活用
const name = user?.profile?.name ?? 'Anonymous'
```
