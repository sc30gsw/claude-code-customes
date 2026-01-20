# /build-fix - ビルドエラー修正コマンド

---
description: TypeScriptとビルドエラーを段階的に修正
---

## 概要

`/build-fix` コマンドは **build-error-resolver** エージェントを呼び出し、TypeScriptとビルドエラーを段階的に修正します。

## 機能

1. ビルド実行: `npm run build` または `pnpm build`
2. エラー出力の解析
3. エラーごとの修正と検証
4. サマリー表示

## 動作フロー

### 1. ビルド実行とエラー解析

```bash
npm run build
```

エラー出力を解析:
- ファイルごとにグループ化
- 重大度順にソート

### 2. 各エラーに対して

```
1. エラーコンテキストを表示（前後5行）
2. 問題を説明
3. 修正を提案
4. 修正を適用
5. ビルドを再実行
6. エラーが解決したことを確認
```

### 3. 停止条件

以下の場合は停止:
- 修正が新しいエラーを導入した場合
- 同じエラーが3回試行後も持続する場合
- ユーザーが一時停止を要求した場合

### 4. サマリー表示

```
修正されたエラー: 5
残りのエラー: 2
新規導入エラー: 0
```

## 共通エラーパターン

### パターン1: 型推論失敗

```typescript
// ❌ ERROR: Parameter 'x' implicitly has an 'any' type
function add(x, y) { return x + y }

// ✅ FIX: 型注釈を追加
function add(x: number, y: number): number { return x + y }
```

### パターン2: Null/Undefinedエラー

```typescript
// ❌ ERROR: Object is possibly 'undefined'
const name = user.name.toUpperCase()

// ✅ FIX: オプショナルチェーン
const name = user?.name?.toUpperCase()
```

### パターン3: プロパティ欠如

```typescript
// ❌ ERROR: Property 'age' does not exist on type 'User'
interface User { name: string }
const user: User = { name: 'John', age: 30 }

// ✅ FIX: インターフェースにプロパティ追加
interface User { name: string; age?: number }
```

### パターン4: インポートエラー

```typescript
// ❌ ERROR: Cannot find module '@/lib/utils'

// ✅ FIX 1: tsconfigパスが正しいか確認
// ✅ FIX 2: 相対インポートを使用
import { formatDate } from '../lib/utils'
```

## 重要な原則

**安全のため1つずつエラーを修正！**

### DO:
- ✅ 欠けている型注釈を追加
- ✅ 必要なnullチェックを追加
- ✅ インポート/エクスポートを修正
- ✅ 欠けている依存関係を追加
- ✅ 型定義を更新
- ✅ 設定ファイルを修正

### DON'T:
- ❌ 無関係なコードをリファクタリング
- ❌ アーキテクチャを変更
- ❌ 変数/関数の名前変更（エラーの原因でない限り）
- ❌ 新機能を追加
- ❌ ロジックフローを変更（エラー修正でない限り）

## 他のコマンドとの連携

- `/plan` でアーキテクチャ変更が必要な場合
- `/tdd` でテスト失敗の場合
- `/code-review` で変更をレビュー

## 関連エージェント

このコマンドは以下のエージェントを呼び出します:
`~/.claude/agents/build-error-resolver.md`
