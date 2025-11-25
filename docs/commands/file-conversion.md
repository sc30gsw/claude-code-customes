# ファイル変換コマンド

様々なファイル形式をMarkdown形式に変換し、AI分析に最適化するコマンドです。

## `/convert-to-md` - ファイル→Markdown変換コマンド

### 概要
PDF、DOCX、Excel等の様々なファイル形式をMarkdown形式に変換し、AIによる分析や処理に最適化します。Markitdown MCPを使用してファイルの変換を行います。

### 基本構文
```bash
/convert-to-md <files> [options]
```

### 引数
- `files`: 変換対象のファイルまたはディレクトリ（必須）

### オプション
- `--recursive`, `-r`: サブディレクトリを再帰的に処理
- `--filter <types>`: ファイル種類でフィルタリング（例：pdf,docx,xlsx）
- `--combine`, `-c`: 複数ファイルを1つのMarkdownファイルに結合
- `--toc`: 目次を生成
- `--metadata`, `-m`: ファイルメタデータを出力に含める
- `--ai-optimize`: AI読み取りに最適化した出力
- `--output`, `-o <path>`: 出力ディレクトリまたはファイルを指定
- `--verbose`, `-v`: 詳細な進行状況を表示

### 使用例

#### 単一ファイル変換
```bash
/convert-to-md document.pdf
```

#### AI最適化付き複数ファイル変換
```bash
/convert-to-md --ai-optimize file1.docx file2.xlsx
```

#### ディレクトリの再帰処理とフィルタリング
```bash
/convert-to-md --recursive --filter pdf,docx ./documents
```

#### 複数ファイルを1つに結合（目次付き）
```bash
/convert-to-md --combine --toc *.pdf -o combined.md
```

### 対応ファイル形式
- PDF（.pdf）
- Microsoft Word（.docx, .doc）
- Microsoft Excel（.xlsx, .xls）
- Microsoft PowerPoint（.pptx, .ppt）
- その他、Markitdown MCPがサポートする形式

### AI最適化機能
`--ai-optimize`オプションを使用すると、以下の最適化が適用されます：

1. **ファイル情報ヘッダー**: 元ファイル名と形式を明記
2. **構造ヒント**: 文書構造（階層、コードブロック、テーブル等）の注釈
3. **読みやすさの改善**: 過剰な改行削除、タブ→スペース変換
4. **長文書への配慮**: 語数カウントと分析のヒント

### 出力例（AI最適化有効時）
```markdown
<!-- File: document.pdf -->
<!-- Original Format: .pdf -->
<!-- Converted for AI Reading -->
<!-- Document Structure: Hierarchical with headers -->
<!-- Contains Tables -->

# 元の文書タイトル

文書の内容...

---

<!-- AI Reading Notes -->
<!-- Word Count: ~2500 words -->
<!-- Document Length: Long - Consider section-by-section analysis -->
```

### 活用シーン
- **文書分析**: PDF/DOCX文書のAI解析前準備
- **資料統合**: 複数文書を統一Markdown形式で管理
- **情報抽出**: 表やデータの構造化テキスト変換
- **アーカイブ**: レガシー文書のMarkdown化

### 注意事項
- ファイルサイズや複雑さによって処理時間が変動します
- 画像や複雑なレイアウトは完全に再現されない場合があります
- `--combine`オプション使用時は出力ファイル名を指定することを推奨します

### 使用ツール
- `Read`, `Write`, `Edit` - ファイル操作
- `Bash`, `Glob`, `Grep` - ファイル検索・処理
- `mcp__markitdown__convert_to_markdown` - 各種形式からMarkdownへの変換
- `TodoWrite` - 大量ファイル処理時の進捗管理
- `WebFetch` - リモートファイルの取得
- `mcp__serena__list_dir` - ディレクトリ構造の確認