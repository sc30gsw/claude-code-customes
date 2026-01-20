# Kiro Spec Impl Command

## 概要

TDD（テスト駆動開発）方法論を使用してspecタスクを実行するコマンド。Kent Beckのテスト駆動開発に従って、テストを先に書き、実装、リファクタリングを行います。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:spec-impl` |
| 引数 | `<feature-name> [task-numbers]` |
| 用途 | TDDによるタスク実装 |
| 許可ツール | Bash, Read, Write, Edit, MultiEdit, Grep, Glob, LS, WebFetch, WebSearch |

## 前提条件の検証

以下のファイルが存在すること：
- `.kiro/specs/<feature>/requirements.md`
- `.kiro/specs/<feature>/design.md`
- `.kiro/specs/<feature>/tasks.md`
- `.kiro/specs/<feature>/spec.json`

## TDD実装フロー

各選択されたタスクに対して：

### 1. RED（失敗するテストを書く）
```typescript
describe('Feature', () => {
  it('should do something', () => {
    expect(feature.doSomething()).toBe(expected)
  })
})
```

### 2. GREEN（テストをパスする最小限のコード）
```typescript
function doSomething() {
  return expected  // テストをパスする最小限の実装
}
```

### 3. REFACTOR（コード品質の向上）
- テストをグリーンに保ちながらリファクタリング
- 重複の除去
- 可読性の向上

### 4. VERIFY（検証）
- すべてのテストがパス
- 既存テストに回帰なし
- コード品質とカバレッジを維持

### 5. MARK COMPLETE（完了マーク）
tasks.mdのチェックボックスを更新：
- `- [ ]` → `- [x]`

## 使用例

```bash
# すべての保留タスクを実行
/kiro:spec-impl user-authentication

# 特定のタスクを実行
/kiro:spec-impl user-authentication 1.1

# 複数のタスクを実行
/kiro:spec-impl user-authentication 1,2,3

# 範囲指定
/kiro:spec-impl user-authentication 1.1-1.5
```

## コンテキスト読み込み

### コアSteering
- `@.kiro/steering/structure.md`
- `@.kiro/steering/tech.md`
- `@.kiro/steering/product.md`

### カスタムSteering
- `.kiro/steering/`内の追加`.md`ファイル

### Specドキュメント
- `@.kiro/specs/<feature>/spec.json`
- `@.kiro/specs/<feature>/requirements.md`
- `@.kiro/specs/<feature>/design.md`
- `@.kiro/specs/<feature>/tasks.md`

## 実装の注意点

- Kent BeckのTDD方法論に厳密に従う
- 特定のタスク要件のみを実装
- タスク完了後にtasks.mdのチェックボックスを更新
- 各メジャータスク完了後にコミット
