# ビジュアライズコマンド

ドキュメントをインフォグラフィック画像に変換し、チャットアプリでの共有を簡単にするコマンドです。

## `/visualize` - ドキュメント→インフォグラフィック変換コマンド

### 概要
Markdown、テキスト、PDFなどのドキュメントを視覚的に魅力的なインフォグラフィック画像（PNG/JPG/PDF）に変換します。Slack、Teams、Discordなどのチャットアプリでの共有に最適化されています。クイックサマリーから詳細なマルチセクションドキュメントまで対応。

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
| `--style` | | 出力スタイル（summary/detailed） | `summary` |
| `--audience` | `-a` | ターゲットオーディエンス（executive/team/technical） | `team` |
| `--diagram` | `-d` | Mermaidダイアグラムを含める | `false` |
| `--icons` | | キーポイントにアイコンを表示 | `true` |
| `--sections` | | セクション数（detailedスタイル用） | `auto` |

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

### 出力スタイル

| スタイル | 説明 | ユースケース |
|----------|------|-------------|
| `summary` | 単一ページ、簡潔な概要 | クイック共有、チャットプレビュー |
| `detailed` | 目次付きマルチセクションドキュメント | 詳細ドキュメント、正式レポート |

### ターゲットオーディエンス

| オーディエンス | トーン | コンテンツフォーカス |
|---------------|--------|---------------------|
| `executive` | ハイレベル、専門用語最小限 | ビジネスインパクト、KPI、ROI |
| `team` | バランス、実践的 | アクションアイテム、タイムライン、成果物 |
| `technical` | 詳細、技術的深度 | アーキテクチャ、実装、API |

### アイコンシステム

キーポイントに自動的に適切なアイコンが割り当てられます：

| カテゴリ | アイコン | 用途 |
|---------|---------|------|
| 成功/完了 | ✓ | 達成、完了項目 |
| 警告/注意 | ⚠ | リスク、懸念事項 |
| 情報 | ℹ | 一般情報 |
| 重要 | ⭐ | キーハイライト |
| 時間 | 🕐 | 期限、スケジュール |
| 人物 | 👤 | チームメンバー、ステークホルダー |
| 設定 | ⚙ | 構成、セットアップ |
| データ | 📊 | 統計、メトリクス |
| ドキュメント | 📄 | 参考資料、ドキュメント |
| コミュニケーション | 💬 | ディスカッション、フィードバック |

### Mermaidダイアグラムサポート

`--diagram`オプションを使用すると、コンテンツに基づいて適切なダイアグラムが自動選択されます：

| コンテンツパターン | ダイアグラムタイプ | 例 |
|-------------------|------------------|-----|
| プロセス/ワークフロー説明 | `flowchart` | ステップバイステップ手順 |
| 時間ベースのデータ | `gantt` | プロジェクトタイムライン |
| データ構造 | `erDiagram` | データベーススキーマ |
| システム通信 | `sequence` | API通信 |
| クラス/コンポーネント構造 | `classDiagram` | アーキテクチャ概要 |

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

#### 詳細マルチセクションインフォグラフィック
```bash
/visualize ./spec.md --style detailed --sections 4
```

#### 経営層向けエグゼクティブサマリー
```bash
/visualize ./quarterly-report.pdf --audience executive --style summary
```

#### ダイアグラム付き技術ドキュメント
```bash
/visualize ./architecture.md --audience technical --diagram --style detailed
```

#### ダイアグラム付きチーム向けドキュメント
```bash
/visualize ./process.md --diagram --theme modern --size slide
```

#### 正式レポート用PDF出力
```bash
/visualize ./project-plan.md --style detailed --format pdf --audience team
```

### 処理ワークフロー

コマンドを受け取ると、以下のステップで処理が行われます：

#### Step 1: ドキュメントの読み取りと分析
1. 入力ファイルを読み取り
2. ドキュメント構造と内容を分析
3. 主題/タイトルを特定
4. 適切なダイアグラムタイプを決定（`--diagram`が設定されている場合）

#### Step 2: オーディエンスに基づくキーポイント抽出

##### `executive`オーディエンス向け：
- **フォーカス**: ビジネスインパクト、ROI、戦略的示唆
- **メトリクス**: KPI、パーセンテージ、財務数値
- **言語**: 非技術的、意思決定重視
- **構造**: 結論先行、次に裏付け証拠

##### `team`オーディエンス向け：
- **フォーカス**: アクションアイテム、責任、タイムライン
- **メトリクス**: 進捗指標、マイルストーン
- **言語**: 技術/ビジネス用語のバランス
- **構造**: コンテキスト → 詳細 → アクションアイテム

##### `technical`オーディエンス向け：
- **フォーカス**: 実装詳細、アーキテクチャ、API
- **メトリクス**: パフォーマンス統計、技術仕様
- **言語**: 技術用語、コード参照
- **構造**: 概要 → 技術詳細 → 統合ノート

#### Step 3: Mermaidダイアグラム生成（--diagram指定時）
コンテンツを分析して適切なダイアグラムタイプを自動選択：
- フローチャート（プロセス/ワークフロー）
- ガントチャート（タイムラインデータ）
- ERダイアグラム（データ構造）
- シーケンス図（システム通信）
- クラス図（コンポーネント構造）

#### Step 4: アイコン選択（--icons指定時）
各キーポイントのカテゴリに基づいて適切なアイコンを自動選択。

#### Step 5: スタイルに基づくHTML生成

##### Summaryスタイル
単一ページレイアウト、簡潔な概要表示。

##### Detailedスタイル
マルチセクションレイアウト：
- カバーページ
- 目次
- セクションページ（各セクションにコンテンツカードとダイアグラム）
- 結論ページ（サマリーとネクストステップ）

#### Step 6: Playwrightでレンダリング
1. HTMLを一時ファイルとして保存
2. Playwright MCPでインフォグラフィックをキャプチャ
3. Mermaidレンダリングを待機（ダイアグラム含む場合）
4. スクリーンショットを取得（detailedスタイルはfullPage対応）

#### Step 7: 出力とクリーンアップ
1. 出力ファイルの作成を確認
2. 出力パスをユーザーに報告
3. 一時ファイルをクリーンアップ

### Detailedスタイル構造

```
┌─────────────────────────────────────┐
│  [Cover Page]                       │
│  Title + Subtitle                   │
│  Date + Author                      │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Table of Contents]                │
│  1. Overview                        │
│  2. Background                      │
│  3. Details                         │
│  4. Conclusion                      │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Section 1: Overview]              │
│  • Key points                       │
│  • Highlights                       │
│  📊 [Optional Diagram]              │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Section 2-N: Detail Sections]     │
│  • Topic details                    │
│  • Charts/Icons                     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Conclusion]                       │
│  • Summary                          │
│  • Next Steps                       │
└─────────────────────────────────────┘
```

### 出力形式

処理完了時の報告例：
```
Infographic generated successfully!

Output: ./docs/report-infographic.png
Size: 1200x630px
Format: png
Theme: business
Style: summary
Audience: team

Key points extracted: 5
Diagrams included: yes/no
Sections: 4 (detailed only)
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

#### Mermaidレンダリングエラー
```
Warning: Mermaid diagram failed to render.
Generating infographic without diagram.
```

### 制限事項
- **推奨最大文書サイズ**: 約10,000語（長いドキュメントは要約されます）
- **複雑なテーブルやチャート**: テキスト説明に簡略化されます
- **フォント**: システムの利用可能なフォントに依存
- **PDF解析**: すべての書式が保持されない場合があります
- **Mermaidダイアグラム**: CDN用のインターネット接続が必要
- **Detailedスタイル**: `slide`または`a4`サイズプリセットとの組み合わせが最適

### 活用シーン
- **会議サマリー**: 議事録をビジュアルサマリーに変換
- **レポート共有**: 長いレポートを一目でわかるインフォグラフィックに
- **技術仕様**: API仕様書やアーキテクチャ文書のビジュアル化
- **プレゼン資料**: ドキュメントからスライド素材を生成
- **SNS共有**: ソーシャルメディア向けビジュアルコンテンツ作成
- **経営報告**: 四半期レポートのエグゼクティブサマリー
- **プロジェクト計画**: 詳細なマルチセクションドキュメント

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
