# ビジュアライズコマンド

ドキュメントをインフォグラフィック画像に変換し、チャットアプリでの共有を簡単にするコマンドです。

## `/visualize` - ドキュメント→インフォグラフィック変換コマンド

### 概要
Markdown、テキスト、PDFなどのドキュメントを視覚的に魅力的なインフォグラフィック画像（PNG/JPG/PDF）に変換します。Slack、Teams、Discordなどのチャットアプリでの共有に最適化されています。

### 基本構文
```bash
/visualize <input-file> [options]
```

### 引数
- `input-file`: 変換対象のドキュメントファイル（必須）
  - 対応形式: `.md`, `.txt`, `.pdf`

### オプション

| オプション | 短縮形 | 説明 | デフォルト |
|-----------|--------|------|-----------|
| `--output` | `-o` | 出力ファイルパス | `{input}-infographic.png` |
| `--format` | `-f` | 出力形式（png/jpg/pdf） | `png` |
| `--theme` | `-t` | ビジュアルテーマ | `business` |
| `--size` | `-s` | 画像サイズプリセット | `chat` |
| `--max-points` | `-m` | 抽出する最大キーポイント数 | `6` |
| `--lang` | `-l` | 出力言語（ja/en） | `ja` |
| `--title` | | カスタムタイトル（自動抽出をオーバーライド） | 自動 |

### テーマ一覧

| テーマ | 説明 | 最適な用途 |
|--------|------|-----------|
| `business` | プロフェッショナルなブルートーン、クリーンレイアウト | ビジネスプレゼンテーション |
| `modern` | 鮮やかな色、グラデーション背景 | マーケティング資料 |
| `tech` | ダークアクセント、等幅フォント | 技術ドキュメント |
| `minimal` | ホワイトスペース、シンプルなタイポグラフィ | クリーンなサマリー |
| `dark` | ダーク背景、ハイコントラスト | 画面表示向け |

### サイズプリセット

| プリセット | サイズ | 最適な用途 |
|-----------|--------|-----------|
| `chat` | 1200x630px | Slack、Teams、Discord共有 |
| `slide` | 1920x1080px | プレゼンテーション |
| `a4` | 2480x3508px | 印刷（A4縦） |
| `square` | 1080x1080px | ソーシャルメディア |

### 使用例

#### 基本的な使用（PDFをインフォグラフィックに変換）
```bash
/visualize ./docs/report.pdf
```

#### テーマとサイズを指定
```bash
/visualize ./notes.md --theme modern --size slide
```

#### カスタムファイル名でJPEG出力
```bash
/visualize ./spec.txt -o ./output/summary.jpg -f jpg
```

#### 日本語出力とカスタムタイトル
```bash
/visualize ./meeting.md --lang ja --title "会議サマリー"
```

#### 技術ドキュメントスタイルで多めのポイント抽出
```bash
/visualize ./api-docs.md --theme tech --max-points 8
```

### 処理ワークフロー

コマンドを受け取ると、以下のステップで処理が行われます：

#### Step 1: ドキュメントの読み取りと分析
1. 入力ファイルを読み取り
2. ドキュメント構造と内容を分析
3. 主題/タイトルを特定

#### Step 2: キーポイントの抽出
以下の情報を抽出します：
- **タイトル**: メイントピックまたはドキュメントタイトル
- **サブタイトル**: 補足説明（該当する場合）
- **キーポイント**: 最大`--max-points`個の主要な要点
  - 各ポイントは短い見出し（5-10語）
  - 各ポイントは簡潔な説明（1-2文）
- **数値/指標**: 重要な統計やデータポイント
- **出典**: 元のドキュメント名

#### Step 3: HTMLインフォグラフィック生成
テーマ設定に基づいてHTMLドキュメントを作成。インラインCSSで自己完結型。

#### Step 4: Playwrightでレンダリング
1. HTMLを一時ファイルまたはdata URIとして保存
2. Playwright MCPでインフォグラフィックをキャプチャ：
   - ビューポートサイズを設定
   - レンダリングを待機
   - スクリーンショットを取得

#### Step 5: 出力とクリーンアップ
1. 出力ファイルの作成を確認
2. 出力パスをユーザーに報告
3. 一時ファイルをクリーンアップ

### テーマ設定詳細

#### business テーマ
```css
primary: #2563eb
secondary: #1e40af
background: #f8fafc
surface: #ffffff
text: #1e293b
accent: #3b82f6
font-family: 'Segoe UI', 'Hiragino Sans', sans-serif
```

#### modern テーマ
```css
primary: #8b5cf6
secondary: #7c3aed
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
surface: rgba(255,255,255,0.95)
text: #1e1b4b
accent: #a78bfa
font-family: 'Poppins', 'Hiragino Sans', sans-serif
```

#### tech テーマ
```css
primary: #10b981
secondary: #059669
background: #0f172a
surface: #1e293b
text: #f1f5f9
accent: #34d399
font-family: 'JetBrains Mono', 'Source Han Code JP', monospace
```

#### minimal テーマ
```css
primary: #374151
secondary: #1f2937
background: #ffffff
surface: #f9fafb
text: #111827
accent: #6b7280
font-family: 'Inter', 'Hiragino Sans', sans-serif
```

#### dark テーマ
```css
primary: #f59e0b
secondary: #d97706
background: #18181b
surface: #27272a
text: #fafafa
accent: #fbbf24
font-family: 'SF Pro Display', 'Hiragino Sans', sans-serif
```

### 出力形式

処理完了時の報告例：
```
Infographic generated successfully!

Output: ./docs/report-infographic.png
Size: 1200x630px
Format: png
Theme: business

Key points extracted: 5
```

### エラーハンドリング

#### サポートされていないファイル形式
```
Supported formats: .md, .txt, .pdf
Provided: {extension}
```

#### ファイルが見つからない
```
File not found: {path}
Please check the file path and try again.
```

#### Playwrightエラー
```
Failed to capture screenshot.
Ensure Playwright MCP is properly configured.
```

### 制限事項
- **推奨最大文書サイズ**: 約10,000語（長いドキュメントは要約されます）
- **複雑なテーブルやチャート**: テキスト説明に簡略化されます
- **フォント**: システムの利用可能なフォントに依存
- **PDF解析**: すべての書式が保持されない場合があります

### 活用シーン
- **会議サマリー**: 議事録をビジュアルサマリーに変換
- **レポート共有**: 長いレポートを一目でわかるインフォグラフィックに
- **技術仕様**: API仕様書やアーキテクチャ文書のビジュアル化
- **プレゼン資料**: ドキュメントからスライド素材を生成
- **SNS共有**: ソーシャルメディア向けビジュアルコンテンツ作成

### 使用ツール
- `Read` - 入力ファイルの読み取り
- `Write` - HTML一時ファイルの作成
- `Bash` - ファイル操作・クリーンアップ
- `Glob` - ファイル検索
- `TodoWrite` - 処理進捗管理
- `mcp__playwright__browser_navigate` - HTMLのレンダリング
- `mcp__playwright__browser_resize` - ビューポートサイズ設定
- `mcp__playwright__browser_wait_for` - レンダリング待機
- `mcp__playwright__browser_take_screenshot` - スクリーンショット取得
- `mcp__playwright__browser_close` - ブラウザのクローズ
