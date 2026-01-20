# /tdd - テスト駆動開発コマンド

---
description: テスト駆動開発ワークフローを強制。インターフェースをスキャフォールドし、テストを先に生成、最小限のコードを実装。80%+カバレッジを確保。
---

## 概要

`/tdd` コマンドは **tdd-guide** エージェントを呼び出し、テスト駆動開発の方法論を強制します。

## 機能

1. **インターフェーススキャフォールド** - まず型/インターフェースを定義
2. **テストを先に生成** - 失敗するテストを書く (RED)
3. **最小限のコード実装** - テストを通過するだけのコードを書く (GREEN)
4. **リファクタリング** - テストをグリーンに保ちながらコードを改善 (REFACTOR)
5. **カバレッジ確認** - 80%+のテストカバレッジを確保

## 使用タイミング

以下の場合に `/tdd` を使用:
- 新機能の実装
- 新しい関数/コンポーネントの追加
- バグ修正（まずバグを再現するテストを書く）
- 既存コードのリファクタリング
- クリティカルなビジネスロジックの構築

## TDDサイクル

```
RED → GREEN → REFACTOR → REPEAT

RED:      失敗するテストを書く
GREEN:    テストを通過する最小限のコードを書く
REFACTOR: テストを通過させながらコードを改善
REPEAT:   次の機能/シナリオへ
```

## 使用例

```
User: /tdd マーケット流動性スコアを計算する関数が必要

Agent (tdd-guide):
# TDDセッション: マーケット流動性スコア計算機

## Step 1: インターフェース定義 (SCAFFOLD)

```typescript
// lib/liquidity.ts
export interface MarketData {
  totalVolume: number
  bidAskSpread: number
  activeTraders: number
  lastTradeTime: Date
}

export function calculateLiquidityScore(market: MarketData): number {
  // TODO: 実装
  throw new Error('Not implemented')
}
```

## Step 2: 失敗するテストを書く (RED)

```typescript
// lib/liquidity.test.ts
describe('calculateLiquidityScore', () => {
  it('should return high score for liquid market', () => {
    const market = {
      totalVolume: 100000,
      bidAskSpread: 0.01,
      activeTraders: 500,
      lastTradeTime: new Date()
    }

    const score = calculateLiquidityScore(market)

    expect(score).toBeGreaterThan(80)
    expect(score).toBeLessThanOrEqual(100)
  })

  it('should handle edge case: zero volume', () => {
    const market = {
      totalVolume: 0,
      bidAskSpread: 0,
      activeTraders: 0,
      lastTradeTime: new Date()
    }

    const score = calculateLiquidityScore(market)

    expect(score).toBe(0)
  })
})
```

## Step 3: テスト実行 - 失敗を確認

```bash
npm test lib/liquidity.test.ts

FAIL lib/liquidity.test.ts
  ✕ should return high score for liquid market (2 ms)
    Error: Not implemented
```

✅ 期待通りテストが失敗。実装準備完了。

## Step 4: 最小限のコード実装 (GREEN)

[実装コード]

## Step 5: テスト実行 - 通過を確認

```bash
npm test lib/liquidity.test.ts

PASS lib/liquidity.test.ts
  ✓ should return high score for liquid market (3 ms)
  ✓ should handle edge case: zero volume (1 ms)

2 tests passed
```

✅ 全テスト通過！

## Step 6: カバレッジ確認

```bash
npm test -- --coverage lib/liquidity.test.ts

File           | % Stmts | % Branch | % Funcs | % Lines
---------------|---------|----------|---------|--------
liquidity.ts   |   100   |   100    |   100   |   100

Coverage: 100% ✅ (Target: 80%)
```
```

## TDDベストプラクティス

**DO:**
- ✅ 実装の前にテストを書く
- ✅ 実装前にテストが失敗することを確認
- ✅ テストを通過する最小限のコードを書く
- ✅ テストがグリーンになってからリファクタリング
- ✅ エッジケースとエラーシナリオを追加
- ✅ 80%+カバレッジを目指す（クリティカルコードは100%）

**DON'T:**
- ❌ テストの前に実装を書く
- ❌ 各変更後のテスト実行をスキップ
- ❌ 一度に多くのコードを書く
- ❌ 失敗するテストを無視
- ❌ 実装詳細をテスト（動作をテスト）
- ❌ すべてをモック（統合テストを優先）

## カバレッジ要件

- **80%最小** - すべてのコード
- **100%必須** - 以下に対して:
  - 金融計算
  - 認証ロジック
  - セキュリティクリティカルなコード
  - コアビジネスロジック

## 他のコマンドとの連携

- `/plan` を先に使用して何を構築するか理解
- `/tdd` でテストと共に実装
- `/build-fix` でビルドエラー発生時
- `/code-review` で実装をレビュー
- `/test-coverage` でカバレッジを確認

## 関連エージェント

このコマンドは以下のエージェントを呼び出します:
`~/.claude/agents/tdd-guide.md`

参照スキル:
`~/.claude/skills/tdd-workflow/`
