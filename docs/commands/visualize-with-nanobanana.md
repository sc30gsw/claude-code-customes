# ビジュアライズコマンド（nanobanana版）

ドキュメントをインフォグラフィック画像に変換するコマンドです。nanobananaツール（generate_image、generate_diagram、generate_story）を活用します。

## `/visualize` - ドキュメント→インフォグラフィック変換コマンド

### 概要
Markdown、テキストなどのドキュメントを視覚的に魅力的なインフォグラフィックに変換します。コンテンツを分析し、最適なnanobananaツール（画像生成、ダイアグラム生成、ストーリー生成）を自動選択します。

### 基本構文
```bash
/visualize <file-path> [options]
```

### 引数
- `file-path`: 変換対象のドキュメントファイル（必須）

### 共通オプション

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--mode` | 生成モード（auto/image/diagram/story） | `auto` |
| `--lang` | 出力言語（ja/en） | `ja` |
| `--max-points` | 抽出する最大キーポイント数（1-8） | `6` |
| `--preview` | プレビューフラグ | `false` |

---

## モード別オプション

### `--mode=image`（generate_image使用）

画像ベースのインフォグラフィックを生成します。

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--count` | 生成画像数（1-8） | `1` |
| `--styles` | スタイル指定（カンマ区切り） | - |
| `--format` | 出力形式（grid/separate） | `separate` |

#### スタイル一覧

| スタイル | 説明 |
|---------|------|
| `photorealistic` | フォトリアリスティック |
| `watercolor` | 水彩画風 |
| `oil-painting` | 油絵風 |
| `sketch` | スケッチ風 |
| `pixel-art` | ピクセルアート |
| `anime` | アニメ風 |
| `vintage` | ヴィンテージ |
| `modern` | モダン |
| `abstract` | アブストラクト |
| `minimalist` | ミニマリスト |

---

### `--mode=diagram`（generate_diagram使用）

ダイアグラムベースのビジュアライゼーションを生成します。

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--type` | ダイアグラムタイプ | `flowchart` |
| `--style` | ダイアグラムスタイル | `professional` |
| `--layout` | レイアウト方向 | `hierarchical` |
| `--complexity` | 詳細度 | `detailed` |
| `--colors` | カラースキーム | `accent` |
| `--annotations` | 注釈レベル | `detailed` |

#### ダイアグラムタイプ

| タイプ | 説明 | 最適な用途 |
|--------|------|-----------|
| `flowchart` | フローチャート | プロセス、ワークフロー |
| `architecture` | アーキテクチャ図 | システム構成 |
| `network` | ネットワーク図 | 通信フロー |
| `database` | データベース図 | ER図、スキーマ |
| `wireframe` | ワイヤーフレーム | UI設計 |
| `mindmap` | マインドマップ | アイデア整理 |
| `sequence` | シーケンス図 | API通信、処理順序 |

#### ダイアグラムスタイル

| スタイル | 説明 |
|---------|------|
| `professional` | プロフェッショナル（ビジネス向け） |
| `clean` | クリーン（シンプル） |
| `hand-drawn` | 手書き風 |
| `technical` | テクニカル（技術文書向け） |

#### レイアウト

| レイアウト | 説明 |
|-----------|------|
| `horizontal` | 横方向 |
| `vertical` | 縦方向 |
| `hierarchical` | 階層構造 |
| `circular` | 円形配置 |

#### 詳細度

| 詳細度 | 説明 |
|--------|------|
| `simple` | シンプル（概要のみ） |
| `detailed` | 詳細（標準） |
| `comprehensive` | 包括的（全情報） |

#### カラースキーム

| カラー | 説明 |
|--------|------|
| `mono` | モノクロ |
| `accent` | アクセントカラー |
| `categorical` | カテゴリ別配色 |

#### 注釈レベル

| レベル | 説明 |
|--------|------|
| `minimal` | 最小限 |
| `detailed` | 詳細 |

---

### `--mode=story`（generate_story使用）

ストーリーテリング形式のビジュアルナラティブを生成します。

| オプション | 説明 | デフォルト |
|-----------|------|-----------|
| `--steps` | ステップ数（2-8） | `4` |
| `--type` | ストーリータイプ | `process` |
| `--style` | ビジュアルスタイル | `consistent` |
| `--layout` | レイアウト形式 | `comic` |
| `--transition` | トランジション効果 | `smooth` |

#### ストーリータイプ

| タイプ | 説明 | 最適な用途 |
|--------|------|-----------|
| `story` | ストーリー | ユーザージャーニー、体験談 |
| `process` | プロセス | 手順説明、ワークフロー |
| `tutorial` | チュートリアル | ハウツーガイド |
| `timeline` | タイムライン | 時系列イベント |

#### ビジュアルスタイル

| スタイル | 説明 |
|---------|------|
| `consistent` | 一貫性のあるスタイル |
| `evolving` | 進化するスタイル（段階的変化） |

#### レイアウト形式

| レイアウト | 説明 |
|-----------|------|
| `separate` | 個別画像 |
| `grid` | グリッド配置 |
| `comic` | コミック形式 |

#### トランジション効果

| 効果 | 説明 |
|------|------|
| `smooth` | スムーズ |
| `dramatic` | ドラマチック |
| `fade` | フェード |

---

## 自動モード選択ロジック（`--mode=auto`）

`auto`モードでは、ドキュメントの内容を分析して最適なモードを自動選択します。

| コンテンツパターン | 選択されるモード | キーワード/指標 |
|-------------------|-----------------|----------------|
| プロセス/ワークフロー | `diagram` (flowchart) | process, workflow, steps, flow, pipeline |
| API/通信フロー | `diagram` (sequence) | API, request, response, communication |
| アーキテクチャ/システム | `diagram` (architecture) | architecture, system, components |
| データベース構造 | `diagram` (database) | database, schema, table, entity |
| ストーリー/ジャーニー | `story` | story, journey, tutorial, before-after |
| 機能概要/比較 | `image` | features, overview, summary, comparison |
| 不明/その他 | `image` | （デフォルトフォールバック） |

---

## 処理ワークフロー

### Step 1: パースと検証
1. ファイルパスを抽出（必須）
2. すべてのオプションをデフォルト値で解析
3. 無効なオプションがあればエラーメッセージを返す

### Step 2: ドキュメント読み取り
1. ファイル内容を読み取り
2. タイトル、セクション、キー情報を抽出
3. `--max-points`で指定した数のキーポイントを特定

### Step 3: モード自動検出（`--mode=auto`の場合）
コンテンツパターンを分析し、最適なモードとタイプを決定。

### Step 4: モード別生成

#### `--mode=image`の場合
`generate_image`ツールを呼び出し：
```
プロンプト構成:
- プロフェッショナルインフォグラフィック: [タイトル]
- キーポイント:
  1. [ポイント1 + アイコン説明]
  2. [ポイント2 + アイコン説明]
  ...
- スタイル: クリーンなビジネスインフォグラフィックレイアウト
- 言語: [--lang]で指定
- ビジュアル要素: アイコン、明確な階層、プロフェッショナルデザイン
```

#### `--mode=diagram`の場合
`generate_diagram`ツールを呼び出し：
```
プロンプト構成:
- [タイトル]: [コンテンツ構造の説明]
- 要素と接続:
  [ノード1] -> [ノード2] -> [ノード3]
  ...
- 言語: [--lang]で指定
```

#### `--mode=story`の場合
`generate_story`ツールを呼び出し：
```
プロンプト構成:
- [タイトル]: ビジュアルナラティブ
- パネル1: [シーン説明]
- パネル2: [シーン説明]
  ...
- 言語: [--lang]で指定
```

---

## 使用例

### 基本的な使用（自動モード検出）
```bash
/visualize ./report.md
```

### シーケンスダイアグラム生成（包括的詳細度）
```bash
/visualize ./api-spec.md --mode=diagram --type=sequence --complexity=comprehensive
```

### モダンスタイルの日本語インフォグラフィック
```bash
/visualize ./meeting.md --mode=image --styles=modern --lang=ja
```

### 4パネルのコミック形式チュートリアル
```bash
/visualize ./tutorial.md --mode=story --steps=4 --layout=comic
```

### アーキテクチャダイアグラム（階層レイアウト）
```bash
/visualize ./system-design.md --mode=diagram --type=architecture --layout=hierarchical
```

### プロセス説明（タイムライン形式）
```bash
/visualize ./project-plan.md --mode=story --type=timeline --steps=6
```

### 複数画像生成（グリッド形式）
```bash
/visualize ./features.md --mode=image --count=4 --format=grid --styles=minimalist
```

### マインドマップ生成
```bash
/visualize ./brainstorm.md --mode=diagram --type=mindmap --style=hand-drawn
```

---

## エラーメッセージ

| エラー | 説明 |
|--------|------|
| `Error: File path required. Usage: /visualize <file-path> [options]` | ファイルパスが指定されていない |
| `Error: Invalid --mode value. Valid: auto, image, diagram, story` | 無効なモード値 |
| `Error: File not found: [path]` | ファイルが見つからない |
| `Error: [option] value invalid. Valid: [list valid values]` | オプション値が無効 |

---

## 活用シーン

### `--mode=image`（インフォグラフィック）
- 会議サマリーの視覚化
- 機能一覧のビジュアル化
- マーケティング資料の作成
- SNS共有用コンテンツ

### `--mode=diagram`（ダイアグラム）
- APIフローの可視化
- システムアーキテクチャの説明
- データベーススキーマの図示
- ワークフローの文書化

### `--mode=story`（ストーリー）
- ユーザージャーニーの説明
- チュートリアルの作成
- Before/After比較
- プロジェクトタイムラインの表示

---

## 既存のvisualizeコマンドとの違い

| 項目 | visualize（Playwright版） | visualize（nanobanana版） |
|------|--------------------------|--------------------------|
| 基盤ツール | Playwright MCP | nanobananaツール群 |
| 生成方式 | HTML→スクリーンショット | AI画像生成 |
| 出力形式 | PNG/JPG/PDF | AI生成画像 |
| モード | summary/visual/detailed | image/diagram/story |
| ダイアグラム | Mermaid.js | generate_diagram |
| ストーリー | コミックレイアウト | generate_story |
| スタイル | CSS/テーマ | AIスタイルプロンプト |

### 使い分けの指針
- **Playwright版**: 厳密なレイアウト制御、Mermaid.jsダイアグラム、HTMLベースの出力が必要な場合
- **nanobanana版**: AI生成のクリエイティブなビジュアル、多様なスタイルオプション、シンプルなワークフローが必要な場合

---

## 使用ツール

- `Read` - 入力ファイルの読み取り
- `generate_image` - インフォグラフィック画像生成
- `generate_diagram` - ダイアグラム生成
- `generate_story` - ストーリー形式ビジュアル生成
