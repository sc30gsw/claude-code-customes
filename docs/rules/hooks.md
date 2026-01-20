# フックシステム

Claude Codeのフックシステムに関するルールです。

## フックタイプ

| タイプ | 説明 | タイミング |
|-------|------|----------|
| PreToolUse | ツール実行前 | 検証、パラメータ変更 |
| PostToolUse | ツール実行後 | 自動フォーマット、チェック |
| Stop | セッション終了時 | 最終検証 |

## 現在のフック (`~/.claude/settings.json`)

### PreToolUse

| フック | 説明 |
|-------|------|
| tmux reminder | 長時間実行コマンド（npm, pnpm, yarn, cargo等）にtmuxを提案 |
| git push review | プッシュ前にZedでレビューを開く |
| doc blocker | 不要な.md/.txtファイルの作成をブロック |

### PostToolUse

| フック | 説明 |
|-------|------|
| PR creation | PR URLとGitHub Actionsステータスをログ |
| Prettier | 編集後にJS/TSファイルを自動フォーマット |
| TypeScript check | .ts/.tsx編集後にtscを実行 |
| console.log warning | 編集ファイル内のconsole.logを警告 |

### Stop

| フック | 説明 |
|-------|------|
| console.log audit | セッション終了前に全変更ファイルのconsole.logをチェック |

## 自動承認パーミッション

注意して使用:

- ✅ 信頼できる、明確に定義された計画に対して有効化
- ❌ 探索的作業では無効化
- ❌ `dangerously-skip-permissions` フラグは使用しない
- 代わりに `~/.claude.json` で `allowedTools` を設定

## TodoWrite ベストプラクティス

TodoWriteツールを使用して:

- マルチステップタスクの進捗を追跡
- 指示の理解を確認
- リアルタイムステアリングを有効化
- 詳細な実装ステップを表示

Todoリストで明らかになること:

- 順序が間違っているステップ
- 欠落している項目
- 不要な追加項目
- 間違った粒度
- 誤解された要件

## フック設定例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "check-long-running-command.sh"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit",
        "command": "prettier --write $FILE"
      }
    ],
    "Stop": [
      {
        "command": "audit-console-logs.sh"
      }
    ]
  }
}
```

## カスタムフックの作成

1. シェルスクリプトを作成
2. settings.jsonに登録
3. 適切なmatcherを設定
4. テスト実行

### 例: TypeScriptチェックフック

```bash
#!/bin/bash
# post-edit-ts-check.sh
if [[ "$FILE" == *.ts ]] || [[ "$FILE" == *.tsx ]]; then
  npx tsc --noEmit "$FILE"
fi
```
