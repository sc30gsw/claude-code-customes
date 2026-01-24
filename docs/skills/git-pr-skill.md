# Git PR Skill

## 概要

Serena MCP統合によるPR説明の生成とGitHubでのプルリクエスト自動作成スキル。変更を分析し、適切なPRテンプレートに従った説明を生成します。

## アクティベーショントリガー

- プルリクエストを作成する時
- 既存のPR説明を更新する時
- 変更内容を包括的にドキュメント化したい時

## 使用方法

```bash
/git:pr [options]
```

## オプション

| オプション | 説明 | 例 |
|-----------|------|-----|
| (デフォルト) | PR説明を生成してPRを作成 | `/git:pr` |
| `-p` | 現在のブランチをプッシュしてPRを作成 | `/git:pr -p` |
| `-u` | 既存のPR説明のみを更新 | `/git:pr -u` |

## ワークフロー

### デフォルト（オプションなし）
1. Serenaパターン認識で変更を分析
2. `.github/pull_request_template.md` からPRテンプレートを読み込み
3. テンプレート形式に従ってPR説明を作成
4. Context7 MCPを使用して関連ドキュメントURLを取得
5. 変更を視覚化するMermaidダイアグラムを追加
6. `gh pr create --draft` を実行

### -pオプション付き
1. 現在のブランチをプッシュ: `git push -u origin <current-branch>`
2. デフォルトワークフローを続行

### -uオプション付き
1. 変更を分析
2. Serenaメモリから以前のPRパターンを読み込み
3. 既存のPRを更新: `gh pr edit --body <description>`

## 要件

1. テンプレート構造に正確に従う
2. 全てのコンテンツを日本語で記述
3. 具体的な実装詳細を含める
4. 具体的なテスト手順をリストアップ
5. Context7 MCPでドキュメントURLを取得
6. 必ずMermaidダイアグラムを含める

## Mermaidダイアグラムガイドライン

- 適切なダイアグラムタイプを使用（flowchart, sequence, class）
- 該当する場合はビフォー・アフター状態を表示
- 新規または変更されたコンポーネントをハイライト
- 一貫したスタイリングとカラーを使用

## Context7統合

参照セクションのため、Context7 MCPで以下をクエリ：
- Next.js、React、TanStack Query ドキュメント
- Tailwind CSS、UIライブラリ ドキュメント
- 変更に基づくその他の関連技術

## ツール優先順位

### ファイル操作（Serena MCP優先）
- **ファイル読み込み**: `mcp__serena__find_file` → `Bash(git:*)` (フォールバック)
- **パターン検索**: `mcp__serena__search_for_pattern`
- **シンボル検索**: `mcp__serena__find_symbol`

### コード分析（Serena MCP）
- **シンボル概要**: `mcp__serena__get_symbols_overview`
- **シンボル参照**: `mcp__serena__find_referencing_symbols`

## 出力例

```markdown
## 概要
- 変更の要約
- 主な実装内容

## 変更内容
### 追加
- 新規ファイル/機能

### 変更
- 既存ファイルの修正

## テスト計画
- [ ] ユニットテストの実行
- [ ] 手動テスト手順

## 参照
- [関連ドキュメントURL]

## 変更の視覚化
\`\`\`mermaid
flowchart LR
    A[変更前] --> B[変更後]
\`\`\`
```
