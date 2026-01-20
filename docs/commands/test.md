# Test Command

## 概要

ユニット/E2Eテストの高度な実装コマンド。自動実行、スマートな修正機能、カバレッジ分析を提供します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/test` |
| 引数 | `<target>` `[options]` |
| 用途 | テスト実装、実行、修正 |
| 許可ツール | すべてのツール |

## 主要機能

### 1. テスト生成
- ユニットテストの自動生成
- インテグレーションテストの作成
- E2Eテストシナリオの構築

### 2. テスト実行
- 並列テスト実行
- ウォッチモード対応
- 選択的テスト実行

### 3. スマート修正
- 失敗したテストの自動分析
- 修正提案の生成
- 回帰テストの確認

### 4. カバレッジ分析
- ライン/ブランチカバレッジ
- 未カバー領域の特定
- カバレッジ改善提案

## 使用例

```bash
# 特定ファイルのテスト生成
/test generate src/utils/validator.ts

# テスト実行
/test run --watch

# 失敗したテストの修正
/test fix

# カバレッジレポート
/test coverage --threshold 80
```

## テストタイプ

### ユニットテスト
```typescript
describe('validateEmail', () => {
  it('should return true for valid email', () => {
    expect(validateEmail('test@example.com')).toBe(true)
  })
})
```

### インテグレーションテスト
```typescript
describe('POST /api/users', () => {
  it('should create user and return 201', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com' })
    expect(response.status).toBe(201)
  })
})
```

### E2Eテスト
```typescript
test('user can login', async ({ page }) => {
  await page.goto('/login')
  await page.fill('[name="email"]', 'user@example.com')
  await page.click('button[type="submit"]')
  await expect(page).toHaveURL('/dashboard')
})
```

## オプション

| オプション | 説明 |
|------------|------|
| `--watch` | ウォッチモードで実行 |
| `--coverage` | カバレッジレポートを生成 |
| `--fix` | 失敗したテストを自動修正 |
| `--e2e` | E2Eテストのみ実行 |
| `--unit` | ユニットテストのみ実行 |

## ベストプラクティス

1. **テストファースト** - TDDワークフローに従う
2. **80%カバレッジ** - 最小カバレッジ目標を維持
3. **独立したテスト** - テスト間の依存を避ける
4. **説明的な名前** - テストの目的を明確に
