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
| `--style` | | 出力スタイル（summary/visual/detailed） | `summary` |
| `--audience` | `-a` | ターゲットオーディエンス（executive/team/technical） | `team` |
| `--diagram` | `-d` | Mermaidダイアグラムを含める（summary/detailed用） | `false` |
| `--icons` | | キーポイントにアイコンを表示 | `true` |
| `--sections` | | セクション数（detailedスタイル用） | `auto` |
| `--visual-type` | `-vt` | ビジュアルフォーマット（diagram/cards/comic/auto） | `auto` |
| `--panels` | `-p` | コミック形式のパネル数（2-6） | `3` |

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

| スタイル | 説明 | ユースケース | 理解レベル |
|----------|------|-------------|-----------|
| `summary` | 単一ページ、簡潔な概要 | クイック共有、チャットプレビュー | Surface（何があるか） |
| `visual` | ダイアグラム + コンテキスト説明 | ドキュメント理解 | **Deep（なぜ・どのように）** |
| `detailed` | 目次付きマルチセクションドキュメント | 詳細ドキュメント、正式レポート | Comprehensive（すべて） |

### Visualスタイルの特徴

`visual`スタイルは、単に「何があるか」をリストするのではなく、**「なぜ」「どのように」を理解する**ことに焦点を当てています。

#### 構成要素
1. **メインダイアグラム**: 構造、フロー、関係性を可視化
2. **コンテキスト説明**: 2-3文でダイアグラムの「なぜ」「どのように」を説明（箇条書きではなく文章）
3. **キーポイントカード**: 3-4個の補足ハイライト

#### Summaryスタイルとの違い
- **summary**: 箇条書きで「何があるか」を抽出
- **visual**: **構造/フローを特定** → **コンテキスト説明を生成**（「なぜ・どのように」）

#### 生成ロジック
1. ドキュメントから可視化可能な構造を抽出（フロー、関係性、階層）
2. 適切なMermaidダイアグラムタイプを選択
3. コンテキスト説明を生成（2-3文、箇条書きではない）
4. 3-4個のキーポイントカードを作成

### ビジュアルタイプ（`--visual-type`、visualスタイル専用）

| タイプ | 説明 | 最適な用途 |
|--------|------|-----------|
| `diagram` | Mermaidダイアグラム + コンテキスト説明 | フロー、プロセス、API、データ構造 |
| `cards` | カードベースレイアウト + 「なぜ」の説明 | 機能リスト、比較、カテゴリ |
| `comic` | パネルベースのストーリーテリングレイアウト | ユーザージャーニー、チュートリアル、Before/After |
| `auto` | コンテンツ分析に基づく自動選択 | **デフォルト** |

### パネルオプション（`--panels`、comicタイプ専用）

| パネル数 | レイアウト | 最適な用途 |
|---------|----------|-----------|
| `2` | 横並び（50%-50%） | Before/After比較 |
| `3` | 3カラム（33%-33%-33%） | 導入 → 展開 → 結論 |
| `4` | 2x2グリッド | ステップバイステップチュートリアル（起承転結） |
| `5-6` | **縦型レイアウト** | 長めの手順説明（読みやすさ重視） |

#### レイアウト自動切り替え

**5項目以上**の場合、Cards/Comic形式は自動的に**縦型レイアウト**に切り替わります：
- グリッドレイアウト（4項目以下）→ 縦型リストレイアウト（5項目以上）
- 各カード/パネルは左にイラスト、右にテキストの横並び配置
- 読みやすさとスクロール体験を最適化

### ビジュアルタイプ自動選択ロジック

`--visual-type auto`（デフォルト）の場合、ドキュメントの内容を分析して最適なフォーマットを選択します：

| コンテンツパターン | 選択されるタイプ | キーワード/指標 |
|-------------------|-----------------|----------------|
| フロー/プロセス | `diagram` | flow, process, step, API, pipeline, workflow |
| データ構造 | `diagram` | schema, model, database, relationship, architecture |
| 機能リスト | `cards` | features, benefits, advantages, capabilities, options |
| 比較 | `cards` | compare, vs, difference, pros/cons |
| ストーリー/ジャーニー | `comic` | story, journey, experience, before/after, transformation |
| チュートリアル | `comic` | tutorial, how to, guide, steps |
| 混合/不明 | `cards` | （不明な場合のフォールバック） |

### ターゲットオーディエンス

| オーディエンス | トーン | コンテンツフォーカス |
|---------------|--------|---------------------|
| `executive` | ハイレベル、専門用語最小限 | ビジネスインパクト、KPI、ROI |
| `team` | バランス、実践的 | アクションアイテム、タイムライン、成果物 |
| `technical` | 詳細、技術的深度 | アーキテクチャ、実装、API |

### アイコン＆イラストレーションシステム

プレゼンテーション品質を重視し、**SVGアイコン**と**unDrawイラストレーション**を使用しています。

#### SVGアイコン（Lucideベース）

キーポイントに自動的に適切なSVGアイコンが割り当てられます。フォールバックとして絵文字も対応：

| カテゴリ | SVGアイコン | フォールバック | 用途 |
|---------|------------|--------------|------|
| 成功/完了 | CheckCircle2 | ✓ | 達成、完了項目 |
| 警告/注意 | AlertTriangle | ⚠ | リスク、懸念事項 |
| 情報 | Info | ℹ | 一般情報 |
| 重要 | Star | ⭐ | キーハイライト |
| 時間 | Clock | 🕐 | 期限、スケジュール |
| 人物 | User | 👤 | チームメンバー、ステークホルダー |
| 設定 | Settings | ⚙ | 構成、セットアップ |
| データ | BarChart2 | 📊 | 統計、メトリクス |
| ドキュメント | FileText | 📄 | 参考資料、ドキュメント |
| コミュニケーション | MessageCircle | 💬 | ディスカッション、フィードバック |

#### イラストレーション（unDraw CDN）

各セクションやカバーページに、ドメインに応じたイラストレーションが自動選択されます：

| ドメイン | キーワード | イラストレーション |
|---------|-----------|------------------|
| Technical | api, code, architecture | programming.svg |
| Business | revenue, profit, roi | business_plan.svg |
| Security | security, auth, protect | security_on.svg |
| Analytics | data, chart, metric | data_trends.svg |
| Team | team, collaboration | team_spirit.svg |
| Success | complete, achieve | celebrating.svg |
| Process | workflow, flow, step | process.svg |

### テキストサイズ最適化

全スタイルで**プレゼンテーション向けの大きなフォントサイズ**を採用しています：

| 要素タイプ | 最小サイズ | 推奨サイズ |
|-----------|----------|----------|
| タイトル | 64px | 72px |
| サブタイトル | 36px | 42px |
| 本文/説明 | 24px | 28px |
| ラベル/フッター | 20px | 24px |

### Mermaidダイアグラムサポート

`--diagram`オプションまたは`--style visual`を使用すると、コンテンツに基づいて適切なダイアグラムが自動選択されます：

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

#### Visualスタイル - 自動フォーマット選択
```bash
/visualize ./architecture.md --style visual
```

#### Visualスタイル - 明示的にダイアグラム形式を指定
```bash
/visualize ./api-flow.md --style visual --visual-type diagram
```

#### Visualスタイル - カード形式
```bash
/visualize ./features.md --style visual --visual-type cards
```

#### Visualスタイル - コミック形式（デフォルト3パネル）
```bash
/visualize ./user-journey.md --style visual --visual-type comic
```

#### Visualスタイル - コミック形式（4パネル）
```bash
/visualize ./tutorial.md --style visual --visual-type comic --panels 4
```

#### Visualスタイル - Before/After比較（2パネル）
```bash
/visualize ./improvement.md --style visual --visual-type comic --panels 2
```

#### ダイアグラム付き技術ドキュメント（detailedスタイル）
```bash
/visualize ./api-spec.md --audience technical --diagram --style detailed
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
4. 適切なダイアグラムタイプを決定（`--diagram`または`--style visual`の場合）

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

#### Step 3: Mermaidダイアグラム生成（--diagramまたは--style visual指定時）
コンテンツを分析して適切なダイアグラムタイプを自動選択：
- フローチャート（プロセス/ワークフロー）
- ガントチャート（タイムラインデータ）
- ERダイアグラム（データ構造）
- シーケンス図（システム通信）
- クラス図（コンポーネント構造）

#### Step 4: アイコン＆イラストレーション選択
1. **SVGアイコン選択**: 各キーポイントのカテゴリに基づいてLucide SVGアイコンを自動選択
2. **イラストレーション選択**: ドキュメントのドメインに基づいてunDraw CDNからイラストレーションを選択
3. **フォールバック処理**: CDN読み込み失敗時は絵文字にフォールバック

#### Step 5: スタイルに基づくHTML生成

##### Summaryスタイル
単一ページレイアウト、簡潔な概要表示：
- タイトル（64px）、サブタイトル（36px）
- SVGアイコン付きキーポイント（タイトル28px、説明24px）
- フッター（20px）

##### Visualスタイル - Diagramフォーマット
理解重視のレイアウト：
- タイトル（64px）+ unDrawイラストレーション
- メインMermaidダイアグラム（構造/フロー/関係性を可視化）
- コンテキスト説明（24px、2-3文で「なぜ」「どのように」を説明）
- SVGアイコン付きキーポイントカード（3-4個、タイトル28px、説明24px）

##### Visualスタイル - Cardsフォーマット
カードベースのレイアウト：
- 3-6個のカードをグリッド/縦型表示（5項目以上で縦型自動切り替え）
- 各カードにSVGアイコン、タイトル、説明（全テキスト24px以上）
- unDrawイラストレーションをヘッダーに表示
- **「なぜ重要か」**の説明を追加（summaryとの違い）

##### Visualスタイル - Comicフォーマット
パネルベースのストーリーテリング：
- 2パネル: Before/After、問題/解決（横並び）
- 3パネル: 導入 → 展開 → 結論（横並び）
- 4パネル: 起 → 承 → 転 → 結（2x2グリッド）
- 5-6パネル: **縦型レイアウト**で詳細なステップバイステッププロセス
- 各パネルにunDrawイラストレーション、タイトル（28px）、説明（24px）

##### Detailedスタイル
マルチセクションレイアウト：
- **カバーページ**: unDrawイラストレーション + タイトル（72px）+ サブタイトル（36px）
- **目次**: セクションリスト（24px）
- **セクションページ**: 各セクションにイラストレーション、SVGアイコン付きカード（タイトル28px、説明24px）
- **結論ページ**: サマリーボックス（24px）とネクストステップ（24px）

#### Step 6: Playwrightでレンダリング
1. HTMLを一時ファイルとして保存
2. Playwright MCPでインフォグラフィックをキャプチャ
3. Mermaid/イラストレーションレンダリングを待機（3秒、CDN読み込み対応）
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
Style: visual
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
- **Mermaid/イラストレーション**: CDN用のインターネット接続が必要（unDraw CDN、Mermaid CDN）
- **フォールバック**: CDN読み込み失敗時は絵文字アイコンにフォールバック
- **Detailedスタイル**: `slide`または`a4`サイズプリセットとの組み合わせが最適

### 活用シーン
- **会議サマリー**: 議事録をビジュアルサマリーに変換
- **レポート共有**: 長いレポートを一目でわかるインフォグラフィックに
- **技術仕様**: API仕様書やアーキテクチャ文書のビジュアル化
- **プレゼン資料**: ドキュメントからスライド素材を生成
- **SNS共有**: ソーシャルメディア向けビジュアルコンテンツ作成
- **経営報告**: 四半期レポートのエグゼクティブサマリー
- **プロジェクト計画**: 詳細なマルチセクションドキュメント
- **プロセス理解**: ワークフローやアーキテクチャの深い理解（visualスタイル - diagram）
- **機能比較**: 製品機能や選択肢の比較（visualスタイル - cards）
- **ユーザージャーニー**: ユーザー体験のストーリー化（visualスタイル - comic）
- **チュートリアル**: ステップバイステップガイドの視覚化（visualスタイル - comic）
- **Before/After**: 改善前後の比較（visualスタイル - comic 2パネル）

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
