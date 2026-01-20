# /code-review - コードレビューコマンド

---
description: コミットされていない変更に対する包括的なセキュリティと品質レビュー
---

## 概要

`/code-review` コマンドは変更されたファイルに対して包括的なセキュリティと品質レビューを実行します。

## 機能

1. 変更ファイルの取得: `git diff --name-only HEAD`
2. 各変更ファイルに対してセキュリティと品質のチェック
3. 重大度別のレポート生成
4. CRITICALまたはHIGH問題がある場合はコミットをブロック

## チェック項目

### セキュリティ問題 (CRITICAL)

- ハードコードされた認証情報、APIキー、トークン
- SQLインジェクション脆弱性
- XSS脆弱性
- 入力検証の欠如
- 安全でない依存関係
- パストラバーサルリスク

### コード品質 (HIGH)

- 50行を超える関数
- 800行を超えるファイル
- 4レベルを超えるネスト深度
- エラーハンドリングの欠如
- console.log文
- TODO/FIXMEコメント
- 公開APIのJSDoc欠如

### ベストプラクティス (MEDIUM)

- ミューテーションパターン（不変パターンを使用）
- コード/コメント内の絵文字使用
- 新規コードのテスト欠如
- アクセシビリティ問題 (a11y)

## レポートフォーマット

```markdown
# コードレビューレポート

## サマリー
- CRITICAL: X件
- HIGH: Y件
- MEDIUM: Z件
- LOW: W件

## CRITICAL Issues

### 1. ハードコードされたAPIキー
**ファイル:** src/api/client.ts:45
**問題:** APIキーが直接コードに書かれている
**修正案:** 環境変数を使用
```typescript
// ❌ 現在
const apiKey = "sk-proj-xxxxx"

// ✅ 修正後
const apiKey = process.env.API_KEY
```

## HIGH Issues
...

## MEDIUM Issues
...
```

## 重要な注意事項

**セキュリティ脆弱性のあるコードは絶対に承認しない！**

CRITICALまたはHIGH問題が見つかった場合:
1. コミットをブロック
2. 問題を修正
3. 再度レビューを実行
4. 問題がなくなってからコミット

## 他のコマンドとの連携

- `/plan` でセキュリティ考慮を含む計画
- `/tdd` でテストを含む実装
- `/code-review` で変更をレビュー
- `/build-fix` でビルドエラー修正

## 関連エージェント

このコマンドは以下のエージェントを参照:
- `~/.claude/agents/code-reviewer.md`
- `~/.claude/agents/security-reviewer.md`
