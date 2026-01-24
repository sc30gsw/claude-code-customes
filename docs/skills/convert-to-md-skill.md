# Convert to Markdown Skill

## 概要

markitdown MCPを使用して様々なファイル形式をMarkdownに変換するスキル。AI可読性を最適化した出力を提供します。

## アクティベーショントリガー

- PDF、Word、Excelファイルの変換が必要な時
- ドキュメントをMarkdown形式で読みたい時
- 複数ファイルを統合したい時
- AIが読みやすい形式に変換したい時

## 使用方法

```bash
/convert-to-md <files> [options]
```

## 引数
- `files`: 変換する入力ファイルまたはディレクトリ（必須）

## オプション

| オプション | 説明 |
|-----------|------|
| `--recursive`, `-r` | サブディレクトリを再帰的に処理 |
| `--filter <types>` | ファイルタイプでフィルタ（例: pdf,docx,xlsx） |
| `--combine`, `-c` | 複数ファイルを1つのMarkdownに統合 |
| `--toc` | 目次を生成 |
| `--metadata`, `-m` | ファイルメタデータを出力に含める |
| `--ai-optimize` | AI読み取り用に出力を最適化 |
| `--output`, `-o <path>` | 出力ディレクトリまたはファイルを指定 |
| `--verbose`, `-v` | 詳細な進捗を表示 |

## 使用例

```bash
# 単一ファイルの変換
/convert-to-md document.pdf

# AI最適化付きで複数ファイルを変換
/convert-to-md --ai-optimize file1.docx file2.xlsx

# フィルタ付きでディレクトリを再帰的に変換
/convert-to-md --recursive --filter pdf,docx ./documents

# TOC付きでファイルを1つに統合
/convert-to-md --combine --toc *.pdf -o combined.md
```

## ワークフロー

1. 引数を解析し入力ファイルを検証
2. パターンとフィルタに基づいてファイルリストを取得
3. 各ファイルに対して:
   - `mcp__markitdown__convert_to_markdown`をファイルURIで呼び出し
   - AI最適化が有効な場合は適用
   - 出力場所に保存
4. `--combine`の場合、オプションのTOCで全出力をマージ
5. サマリーをレポート（成功/失敗カウント）

## AI最適化機能

`--ai-optimize`が有効な場合:
- ファイルコンテキストヘッダーを追加（ファイル名、元の形式）
- 構造ヒントを追加（ヘッダー、コードブロック、テーブル）
- 過剰な空白をクリーンアップ
- 長いドキュメント用の読み取りノートを追加

## サポートするファイル形式

| 形式 | 拡張子 |
|------|--------|
| PDF | `.pdf` |
| Microsoft Word | `.doc`, `.docx` |
| Microsoft Excel | `.xls`, `.xlsx` |
| Microsoft PowerPoint | `.ppt`, `.pptx` |
| テキストファイル | `.txt` |
| HTMLファイル | `.html`, `.htm` |

## 成功指標

- ファイルが正常に変換される
- Markdown形式が正しい
- AI最適化が適用される（有効な場合）
- 目次が正確（有効な場合）
