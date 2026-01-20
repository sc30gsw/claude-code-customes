# /refactor-clean - リファクタリング・クリーンアップコマンド

---
description: テスト検証付きでデッドコードを安全に特定・削除
---

## 概要

`/refactor-clean` コマンドは **refactor-cleaner** エージェントを呼び出し、デッドコードの検出と安全な削除を行います。

## 機能

1. デッドコード分析ツールを実行
2. 包括的なレポート生成
3. 重大度別に分類
4. 安全な削除のみを提案
5. 各削除前後にテスト検証
6. クリーンアップサマリー表示

## 分析ツール

```bash
# knip: 未使用エクスポートとファイルを検出
npx knip

# depcheck: 未使用依存関係を検出
npx depcheck

# ts-prune: 未使用TypeScriptエクスポートを検出
npx ts-prune
```

## 動作フロー

### 1. デッドコード分析

分析ツールを実行して結果を収集。

### 2. 重大度別分類

- **SAFE**: テストファイル、未使用ユーティリティ
- **CAUTION**: APIルート、コンポーネント
- **DANGER**: 設定ファイル、メインエントリポイント

### 3. 安全な削除のみを提案

### 4. 各削除前にテスト検証

```
1. フルテストスイートを実行
2. テストが通過することを確認
3. 変更を適用
4. テストを再実行
5. テストが失敗した場合はロールバック
```

### 5. クリーンアップサマリー

```markdown
# クリーンアップサマリー

## 削除したファイル
- src/old-component.tsx - 置き換え: src/new-component.tsx
- lib/deprecated-util.ts - 機能移動先: lib/utils.ts

## 削除した依存関係
- old-package@1.0.0 - 最終使用: never

## 削除した未使用エクスポート
- src/utils/helpers.ts - 関数: foo(), bar()

## 影響
- 削除ファイル: 5
- 削除依存関係: 2
- 削除コード行: 500
- バンドルサイズ削減: ~15 KB
```

## 削除前チェックリスト

何かを削除する前に:
- [ ] 検出ツールを実行
- [ ] すべての参照をgrep
- [ ] 動的インポートを確認
- [ ] git履歴をレビュー
- [ ] 公開APIの一部か確認
- [ ] すべてのテストを実行
- [ ] バックアップブランチを作成

各削除後:
- [ ] ビルド成功
- [ ] テスト通過
- [ ] コンソールエラーなし
- [ ] 変更をコミット

## 共通の削除パターン

### 1. 未使用インポート

```typescript
// ❌ 未使用インポートを削除
import { useState, useEffect, useMemo } from 'react' // useStateのみ使用

// ✅ 使用するもののみ保持
import { useState } from 'react'
```

### 2. デッドコードブランチ

```typescript
// ❌ 到達不能コードを削除
if (false) {
  doSomething()
}

// ❌ 未使用関数を削除
export function unusedHelper() {
  // コードベース内に参照なし
}
```

### 3. 重複コンポーネント

```typescript
// ❌ 複数の類似コンポーネント
components/Button.tsx
components/PrimaryButton.tsx
components/NewButton.tsx

// ✅ 1つに統合
components/Button.tsx (variantプロップ付き)
```

## 重要な注意事項

**テストを実行せずにコードを削除しない！**

削除後に問題が発生した場合:

1. **即時ロールバック:**
   ```bash
   git revert HEAD
   npm install
   npm run build
   npm test
   ```

2. **調査:**
   - 何が失敗したか？
   - 動的インポートだったか？
   - 検出ツールが見逃した方法で使用されていたか？

3. **前方修正:**
   - 項目を「削除禁止」としてノートにマーク
   - 検出ツールが見逃した理由を文書化

## 使用しない場面

以下の場合は使用しない:
- 活発な機能開発中
- 本番デプロイ直前
- コードベースが不安定な時
- 適切なテストカバレッジがない時
- 理解していないコードに対して

## 他のコマンドとの連携

- `/test-coverage` でクリーンアップ前にカバレッジを確認
- `/code-review` で変更をレビュー

## 関連エージェント

このコマンドは以下のエージェントを呼び出します:
`~/.claude/agents/refactor-cleaner.md`
