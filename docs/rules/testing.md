# テスト要件

テストに関するルールです。

## 最小テストカバレッジ: 80%

### テストタイプ（すべて必須）

1. **ユニットテスト** - 個々の関数、ユーティリティ、コンポーネント
2. **統合テスト** - APIエンドポイント、データベース操作
3. **E2Eテスト** - クリティカルユーザーフロー（Playwright）

## テスト駆動開発

**必須ワークフロー:**

```
1. まずテストを書く (RED)
2. テストを実行 - 失敗することを確認
3. 最小限の実装を書く (GREEN)
4. テストを実行 - 通過することを確認
5. リファクタリング (IMPROVE)
6. カバレッジ確認 (80%+)
```

## テスト失敗のトラブルシューティング

1. **tdd-guide** エージェントを使用
2. テスト分離を確認
3. モックが正しいか検証
4. 実装を修正（テストが間違っていない限り）

## エージェントサポート

| エージェント | 目的 |
|-------------|------|
| **tdd-guide** | 新機能にPROACTIVELYに使用、テストファースト強制 |
| **e2e-runner** | Playwright E2Eテスト専門家 |

## テスト構成

```
tests/
├── unit/              # ユニットテスト
│   ├── utils/
│   ├── hooks/
│   └── components/
├── integration/       # 統合テスト
│   ├── api/
│   └── db/
└── e2e/              # E2Eテスト
    ├── auth/
    ├── markets/
    └── wallet/
```

## テスト命名規則

```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', async () => {
      // test
    })

    it('should throw error when email is invalid', async () => {
      // test
    })

    it('should hash password before saving', async () => {
      // test
    })
  })
})
```

## カバレッジ要件

| コードタイプ | 最小カバレッジ |
|-------------|--------------|
| 通常のコード | 80% |
| 金融計算 | 100% |
| 認証ロジック | 100% |
| セキュリティクリティカル | 100% |
| コアビジネスロジック | 100% |

## テストすべき項目

### ハッピーパス
- 正常な入力での期待される動作
- 成功時の戻り値

### エッジケース
- null, undefined, 空の値
- 境界値（0, 負数, 最大値）
- 特殊文字、長い文字列

### エラーケース
- 無効な入力
- ネットワークエラー
- タイムアウト

### 非同期処理
- Promise解決
- Promise拒否
- 並行処理

## モッキングガイドライン

```typescript
// 外部APIをモック
jest.mock('@/lib/api', () => ({
  fetchUser: jest.fn().mockResolvedValue({ id: '1', name: 'Test' })
}))

// 時間をモック
jest.useFakeTimers()
jest.setSystemTime(new Date('2024-01-01'))

// 環境変数をモック
process.env.API_KEY = 'test-key'
```

## CI/CDでのテスト

```yaml
# .github/workflows/test.yml
- name: Run tests
  run: npm test -- --coverage

- name: Check coverage
  run: |
    COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
    if (( $(echo "$COVERAGE < 80" | bc -l) )); then
      echo "Coverage is below 80%"
      exit 1
    fi
```
