# TDD Workflow Skill

## 概要

新機能の実装、バグ修正、コードリファクタリング時に使用するスキル。テスト駆動開発（TDD）の原則に従い、ユニット、インテグレーション、E2Eテストを含む80%以上のカバレッジを確保します。

## アクティベーショントリガー

- 新機能や機能の実装時
- バグや問題の修正時
- 既存コードのリファクタリング時
- APIエンドポイントの追加時
- 新規コンポーネントの作成時

## コア原則

### 1. テストファースト
常にテストを先に書き、その後でテストをパスするコードを実装します。

### 2. カバレッジ要件
- 最小80%カバレッジ（ユニット + インテグレーション + E2E）
- 全エッジケースをカバー
- エラーシナリオをテスト
- 境界条件を検証

### 3. テストタイプ

| タイプ | 対象 | 割合 |
|--------|------|------|
| ユニットテスト | 個別関数、ユーティリティ、コンポーネント | 60-70% |
| インテグレーションテスト | APIエンドポイント、DB操作 | 20-30% |
| E2Eテスト | クリティカルなユーザーフロー | 5-10% |

## TDDワークフローステップ

### Step 1: ユーザージャーニーの記述
```
As a [role], I want to [action], so that [benefit]
```

### Step 2: テストケースの生成
各ユーザージャーニーに対して包括的なテストケースを作成

### Step 3: テスト実行（失敗すべき）
```bash
npm test
# テストは失敗するはず - まだ実装していない
```

### Step 4: コード実装
テストをパスするための最小限のコードを記述

### Step 5: 再度テスト実行
```bash
npm test
# テストがパスするはず
```

### Step 6: リファクタリング
テストをグリーンに保ちながらコード品質を向上

### Step 7: カバレッジ検証
```bash
npm run test:coverage
# 80%以上のカバレッジを確認
```

## テストパターン

### ユニットテストパターン（Jest/Vitest）
```typescript
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from './Button'

describe('Button Component', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })
})
```

### APIインテグレーションテストパターン
```typescript
describe('GET /api/markets', () => {
  it('returns markets successfully', async () => {
    const request = new NextRequest('http://localhost/api/markets')
    const response = await GET(request)
    expect(response.status).toBe(200)
  })
})
```

### E2Eテストパターン（Playwright）
```typescript
test('user can search and filter markets', async ({ page }) => {
  await page.goto('/')
  await page.fill('input[placeholder="Search"]', 'election')
  await expect(page.locator('[data-testid="result"]')).toHaveCount(5)
})
```

## ファイル構成

```
src/
├── components/
│   └── Button/
│       ├── Button.tsx
│       └── Button.test.tsx          # ユニットテスト
├── app/api/
│   └── markets/
│       ├── route.ts
│       └── route.test.ts            # インテグレーションテスト
└── e2e/
    └── markets.spec.ts              # E2Eテスト
```

## モッキングパターン

### Supabase Mock
```typescript
jest.mock('@/lib/supabase', () => ({
  supabase: {
    from: jest.fn(() => ({
      select: jest.fn(() => Promise.resolve({ data: [], error: null }))
    }))
  }
}))
```

## 避けるべきテストの間違い

### ❌ 実装詳細のテスト
```typescript
// 内部状態をテストしない
expect(component.state.count).toBe(5)
```

### ✅ ユーザー可視の振る舞いをテスト
```typescript
expect(screen.getByText('Count: 5')).toBeInTheDocument()
```

## ベストプラクティス

1. **テストファースト** - 常にTDD
2. **1テスト1アサート** - 単一の振る舞いにフォーカス
3. **説明的なテスト名** - テスト対象を説明
4. **AAA構造** - Arrange-Act-Assert
5. **外部依存のモック** - ユニットテストを分離
6. **エッジケースのテスト** - null, undefined, empty, large
7. **エラーパスのテスト** - ハッピーパスだけでなく
8. **テストを高速に** - ユニットテストは各50ms未満
9. **テスト後のクリーンアップ** - 副作用なし
10. **カバレッジレポートのレビュー** - ギャップを特定

## 成功指標

- 80%以上のコードカバレッジ達成
- 全テストがパス（グリーン）
- スキップまたは無効化されたテストなし
- 高速なテスト実行（ユニットテストは30秒未満）
- E2Eテストがクリティカルなユーザーフローをカバー
- テストが本番前にバグをキャッチ
