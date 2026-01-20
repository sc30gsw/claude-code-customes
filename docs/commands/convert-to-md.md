# Convert to Markdown Command

## 概要

markitdown MCPを使用して、様々なファイル形式をMarkdownに変換するコマンド。AI読み取りに最適化された出力を生成します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/convert-to-md` |
| 引数 | `<file_path>` |
| 用途 | ファイル形式変換、AI読み取り最適化 |
| 許可ツール | Bash, Read, Write, Edit, Glob |

## サポートファイル形式

- **ドキュメント**: PDF, DOCX, PPTX, XLSX
- **画像**: PNG, JPG（OCR対応）
- **Web**: HTML, XML
- **データ**: JSON, YAML, CSV
- **その他**: RTF, TXT

## 使用例

```bash
# PDFをMarkdownに変換
/convert-to-md document.pdf

# 画像からテキストを抽出
/convert-to-md screenshot.png

# Excelファイルを変換
/convert-to-md data.xlsx
```

## 変換プロセス

1. **ファイル形式の検出** - 拡張子とMIMEタイプを確認
2. **markitdown MCPの呼び出し** - 適切な変換パラメータで実行
3. **出力の最適化** - AI読み取り用にフォーマット調整
4. **結果の保存** - `.md`ファイルとして出力

## 出力特性

- **構造化されたMarkdown** - 見出し、リスト、テーブルを適切に使用
- **メタデータの保持** - ドキュメント情報を維持
- **画像のOCR処理** - テキストを抽出してインライン化
- **リンクの維持** - 元のリンク構造を保持

## ベストプラクティス

1. **大きなファイルは分割** - パフォーマンス向上のため
2. **OCR精度の確認** - 画像からのテキスト抽出は要確認
3. **出力のレビュー** - 変換結果の品質をチェック
4. **機密情報の注意** - 変換前にセキュリティを考慮
