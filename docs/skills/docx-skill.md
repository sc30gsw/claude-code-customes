# 📄 DOCXスキル - Word文書の作成・編集・分析

Claude Codeで Microsoft Word 文書（.docx）を完全に操作できるプロフェッショナルスキルです。

## 🎯 概要

DOCXスキルは、Word文書に関する以下の操作を提供します：

| 操作タイプ | 機能 | 使用ツール |
|-----------|------|-----------|
| 📝 **作成** | 新規文書の生成 | docx.js (JavaScript/TypeScript) |
| ✏️ **編集** | 既存文書の変更・変更履歴追加 | Document library (Python) |
| 🔍 **分析** | テキスト抽出・コメント読み取り | pandoc / XML直接アクセス |

### 主な特徴

- ✅ **プロフェッショナルな変更履歴**: 法務・学術レベルのレッドライニング対応
- ✅ **完全なOOXMLサポート**: ISO標準準拠のXML操作
- ✅ **自動検証**: スキーマ検証とレッドライニング検証の2層保護
- ✅ **柔軟な変換**: DOCX ⇄ PDF ⇄ 画像の相互変換

## 🚀 クイックスタート

### 新規文書を作成する

```javascript
const docx = require("docx");
const { Document, Paragraph, TextRun } = docx;

// 最小限の文書作成
const doc = new Document({
    sections: [{
        properties: {},
        children: [
            new Paragraph({
                children: [
                    new TextRun("こんにちは、DOCXスキル！")
                ],
            }),
        ],
    }],
});
```

### 既存文書からテキストを抽出する

```bash
# Markdownに変換（変更履歴を保持）
pandoc --track-changes=all document.docx -o output.md

# 変更履歴を受け入れて変換
pandoc --track-changes=accept document.docx -o output.md
```

## 📖 ワークフロー解説

### 📋 ワークフロー決定木

```
何をしたい？
├─ 新規文書を作成 → docx.jsライブラリ（ワークフロー1）
├─ 既存文書を編集
│  ├─ 自分の文書 → Document library（ワークフロー2A）
│  └─ 他者の文書（変更履歴必須） → Redliningワークフロー（ワークフロー2B）
└─ 文書を読み取り・分析
   ├─ テキストのみ → pandoc変換（ワークフロー3A）
   └─ コメント/書式/メディア → XML直接アクセス（ワークフロー3B）
```

---

## 🆕 ワークフロー1: 新規文書作成（docx.js）

### 基本構造

```javascript
const { Document, Paragraph, TextRun, AlignmentType } = require("docx");

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            // タイトル
            new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [
                    new TextRun({
                        text: "提案書",
                        bold: true,
                        size: 32, // 16pt（半ポイント単位）
                    })
                ],
            }),

            // 本文
            new Paragraph({
                children: [
                    new TextRun("本文はここに記述します。")
                ],
            }),
        ],
    }],
});
```

### 重要な制約

| 制約 | 正しい方法 | 間違った方法 |
|------|-----------|-------------|
| 改行 | 別の`Paragraph`を作成 | `\n`を使用 ❌ |
| リスト | `LevelFormat.BULLET`定数使用 | Unicode記号 ❌ |
| 画像 | `type`パラメータ必須 | typeなしで`ImageRun` ❌ |
| テーブルシェーディング | `ShadingType.CLEAR` | 他の値 ❌ |
| ページ区切り | `Paragraph`内に配置 | 単体で配置 ❌ |

### 推奨フォント

- **Arial**: 最も普遍的、デフォルト推奨
- **Times New Roman + Arial**: クラシック組み合わせ
- **Georgia + Verdana**: モダンな組み合わせ

### 実用例：ビジネスレポート

```javascript
const { Document, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, WidthType, BorderStyle } = require("docx");

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            // ヘッダー
            new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [
                    new TextRun({
                        text: "月次レポート",
                        bold: true,
                        size: 32,
                        font: "Arial"
                    })
                ],
            }),

            new Paragraph({ text: "" }), // 空行

            // テーブル
            new Table({
                width: {
                    size: 100,
                    type: WidthType.PERCENTAGE,
                },
                rows: [
                    new TableRow({
                        children: [
                            new TableCell({
                                children: [new Paragraph("項目")],
                            }),
                            new TableCell({
                                children: [new Paragraph("数値")],
                            }),
                        ],
                    }),
                    new TableRow({
                        children: [
                            new TableCell({
                                children: [new Paragraph("売上")],
                            }),
                            new TableCell({
                                children: [new Paragraph("¥1,000,000")],
                            }),
                        ],
                    }),
                ],
            }),
        ],
    }],
});
```

---

## ✏️ ワークフロー2A: 既存文書の基本編集

### Documentライブラリの基本

```python
from scripts.document import Document

# 文書を開く（自動的に作業コピーを作成）
doc = Document("original.docx", "author_name")

# ノードを検索
node = doc.get_node("w:t", contains="古いテキスト")

# テキストを置換
new_xml = '<w:t xml:space="preserve">新しいテキスト</w:t>'
doc.replace_node(node, new_xml)

# 保存（デフォルトで検証）
doc.save()
```

### 主要メソッド一覧

| メソッド | 用途 | 例 |
|---------|------|-----|
| `get_node()` | ノード検索 | `get_node("w:p", line_number=10)` |
| `replace_node()` | ノード置換 | `replace_node(old, new_xml)` |
| `insert_after()` | 後に挿入 | `insert_after(node, xml)` |
| `append_to()` | 子要素として追加 | `append_to(parent, xml)` |
| `save()` | 保存と検証 | `save(validate=True)` |

### 自動処理される機能

Documentライブラリは以下を自動的に処理します：

- ✅ 一時作業コピーの作成
- ✅ `people.xml`の自動生成
- ✅ RSIDの自動生成と注入
- ✅ `settings.xml`への`trackRevisions`設定
- ✅ コメントファイル（`comments*.xml`）の自動生成
- ✅ リレーションシップ・コンテンツタイプの管理

---

## 🔄 ワークフロー2B: レッドライニング（変更履歴付き編集）

### いつ使う？

- ✅ 他者が作成した文書を編集する場合
- ✅ 法務・学術・ビジネス・政府文書
- ✅ 変更の透明性が重要な場合
- ✅ レビュープロセスが必要な場合

### 推奨ワークフロー（7ステップ）

```bash
# 1. Markdown変換で現状を把握
pandoc --track-changes=all original.docx -o current.md

# 2. 変更内容を特定してバッチ化（3-10個の関連変更ずつ）

# 3. OOXML技術リファレンスを読み込み
# .claude/skills/docx/ooxml.md（600行）を完全に読む

# 4. 文書をUnpack
python .claude/skills/docx/ooxml/scripts/unpack.py original.docx unpacked/

# 5. Pythonスクリプトでバッチ実装
python batch1_contract_terms.py

# 6. Pack
python .claude/skills/docx/ooxml/scripts/pack.py unpacked/ reviewed.docx

# 7. 最終検証
pandoc --track-changes=all reviewed.docx -o final.md
grep -E "deleted|inserted" final.md
```

### レッドライニングの重要原則

#### ❌ 悪い例：文全体を置換

```xml
<w:del><w:r><w:delText>The term is 30 days.</w:delText></w:r></w:del>
<w:ins><w:r><w:t>The term is 60 days.</w:t></w:r></w:ins>
```

#### ✅ 良い例：変更箇所のみマーク

```xml
<w:r w:rsidR="00AB12CD"><w:t>The term is </w:t></w:r>
<w:del><w:r><w:delText>30</w:delText></w:r></w:del>
<w:ins><w:r><w:t>60</w:t></w:r></w:ins>
<w:r w:rsidR="00AB12CD"><w:t> days.</w:t></w:r>
```

### Documentライブラリでの変更履歴操作

```python
from scripts.document import Document

doc = Document("contract.docx", "Legal Team")

# 削除提案
node = doc.get_node("w:t", contains="古い条項")
doc.suggest_deletion(node)

# 挿入の却下
insertion = doc.get_node("w:ins", line_number=45)
doc.revert_insertion(insertion)

# 削除の復元
deletion = doc.get_node("w:del", line_number=60)
doc.revert_deletion(deletion)

doc.save()
```

---

## 🔍 ワークフロー3A: テキスト分析（pandoc）

### 基本的な変換

```bash
# シンプルなMarkdown変換
pandoc document.docx -o output.md

# 変更履歴を保持
pandoc --track-changes=all document.docx -o output.md

# 変更履歴を受け入れ
pandoc --track-changes=accept document.docx -o output.md

# 変更履歴を却下
pandoc --track-changes=reject document.docx -o output.md
```

### フォーマット付き変換

```bash
# HTML変換（スタイル保持）
pandoc document.docx -o output.html

# プレーンテキスト
pandoc document.docx -t plain -o output.txt
```

---

## 🔍 ワークフロー3B: RAW XML アクセス

### Unpack/Pack の使い方

```bash
# Unpack: .docx → ディレクトリ展開
python .claude/skills/docx/ooxml/scripts/unpack.py document.docx unpacked/

# ディレクトリ構造
unpacked/
├── word/
│   ├── document.xml      # 本文
│   ├── comments.xml      # コメント
│   ├── styles.xml        # スタイル
│   └── media/            # 画像・メディア
├── _rels/                # リレーションシップ
└── [Content_Types].xml   # コンテンツタイプ

# Pack: ディレクトリ → .docx
python .claude/skills/docx/ooxml/scripts/pack.py unpacked/ new.docx
```

### XMLファイルの直接編集

```python
import xml.etree.ElementTree as ET

# XMLを読み込み
tree = ET.parse('unpacked/word/document.xml')
root = tree.getroot()

# 名前空間の定義
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# テキストノードを検索
for t in root.findall('.//w:t', ns):
    if t.text == "検索文字":
        t.text = "置換文字"

# 保存
tree.write('unpacked/word/document.xml', encoding='utf-8', xml_declaration=True)
```

---

## 💼 実用例

### 例1: ビジネス提案書の生成

```javascript
const { Document, Paragraph, TextRun, HeadingLevel,
        AlignmentType, TableOfContents } = require("docx");

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            // 表紙
            new Paragraph({
                text: "システム導入提案書",
                heading: HeadingLevel.TITLE,
                alignment: AlignmentType.CENTER,
            }),

            new Paragraph({
                text: "株式会社〇〇 御中",
                alignment: AlignmentType.RIGHT,
            }),

            // 目次
            new TableOfContents("目次", {
                hyperlink: true,
                headingStyleRange: "1-3",
            }),

            // セクション
            new Paragraph({
                text: "1. 提案概要",
                heading: HeadingLevel.HEADING_1,
            }),

            new Paragraph({
                text: "本提案では、貴社の業務効率化を実現するシステムを提案いたします。",
            }),
        ],
    }],
});
```

### 例2: 契約書のレビュー（変更履歴付き）

```python
from scripts.document import Document

# 契約書を開く
doc = Document("contract_v1.docx", "Legal Review Team")

# 期間の変更
term_node = doc.get_node("w:t", contains="30 days")
doc.suggest_deletion(term_node)
new_term = '<w:t xml:space="preserve">60 days</w:t>'
doc.insert_after(term_node.getparent(), f'<w:ins>{new_term}</w:ins>')

# 条項にコメント追加
clause = doc.get_node("w:p", line_number=25)
doc.add_comment(
    clause.find('.//w:r', doc.ns)[0],  # 開始位置
    clause.find('.//w:r', doc.ns)[-1], # 終了位置
    "この条項は法務部の確認が必要です。"
)

# 保存
doc.save("contract_v2.docx")
```

### 例3: 技術ドキュメントの自動生成

```javascript
const { Document, Paragraph, TextRun, Table, TableRow, TableCell,
        ExternalHyperlink, ImageRun } = require("docx");
const fs = require("fs");

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            new Paragraph({
                text: "API仕様書",
                heading: HeadingLevel.HEADING_1,
            }),

            // コードブロック風の表現
            new Paragraph({
                children: [
                    new TextRun({
                        text: "GET /api/users/{id}",
                        font: "Courier New",
                        color: "2E3440",
                    })
                ],
            }),

            // パラメータテーブル
            new Table({
                rows: [
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph("パラメータ")] }),
                            new TableCell({ children: [new Paragraph("型")] }),
                            new TableCell({ children: [new Paragraph("説明")] }),
                        ],
                    }),
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph("id")] }),
                            new TableCell({ children: [new Paragraph("integer")] }),
                            new TableCell({ children: [new Paragraph("ユーザーID")] }),
                        ],
                    }),
                ],
            }),

            // 外部リンク
            new Paragraph({
                children: [
                    new ExternalHyperlink({
                        children: [
                            new TextRun({
                                text: "詳細なドキュメントはこちら",
                                style: "Hyperlink",
                            }),
                        ],
                        link: "https://example.com/docs",
                    }),
                ],
            }),
        ],
    }],
});
```

### 例4: データからのレポート自動生成

```javascript
const { Document, Paragraph, Table, TableRow, TableCell } = require("docx");

// データソース
const salesData = [
    { month: "1月", sales: 1000000, target: 950000 },
    { month: "2月", sales: 1200000, target: 1100000 },
    { month: "3月", sales: 980000, target: 1050000 },
];

// テーブル行を動的生成
const tableRows = [
    // ヘッダー行
    new TableRow({
        children: [
            new TableCell({ children: [new Paragraph("月")] }),
            new TableCell({ children: [new Paragraph("売上")] }),
            new TableCell({ children: [new Paragraph("目標")] }),
            new TableCell({ children: [new Paragraph("達成率")] }),
        ],
    }),
    // データ行
    ...salesData.map(data => {
        const rate = ((data.sales / data.target) * 100).toFixed(1);
        return new TableRow({
            children: [
                new TableCell({ children: [new Paragraph(data.month)] }),
                new TableCell({ children: [new Paragraph(`¥${data.sales.toLocaleString()}`)] }),
                new TableCell({ children: [new Paragraph(`¥${data.target.toLocaleString()}`)] }),
                new TableCell({ children: [new Paragraph(`${rate}%`)] }),
            ],
        });
    }),
];

const doc = new Document({
    sections: [{
        properties: {},
        children: [
            new Paragraph({ text: "売上レポート", heading: HeadingLevel.HEADING_1 }),
            new Table({ rows: tableRows }),
        ],
    }],
});
```

---

## 🔧 高度な機能

### コメントと変更履歴

#### コメント追加

```python
from scripts.document import Document

doc = Document("report.docx", "Reviewer")

# 段落の最初と最後のrunを取得
para = doc.get_node("w:p", line_number=15)
runs = para.findall('.//w:r', doc.ns)

# コメント追加
doc.add_comment(runs[0], runs[-1], "この段落は要確認です。")

# コメントに返信
doc.reply_to_comment(parent_id=1, text="確認しました。修正します。")

doc.save()
```

#### 変更履歴の種類

| メソッド | 機能 | 結果 |
|---------|------|------|
| `suggest_deletion()` | 削除を提案 | 取り消し線表示 |
| `suggest_insertion()` | 挿入を提案 | 下線表示 |
| `revert_insertion()` | 挿入を却下 | 削除 |
| `revert_deletion()` | 削除を復元 | 復活 |

### スタイルとフォーマット

```javascript
const { Document, Paragraph, TextRun, AlignmentType,
        UnderlineType, TabStopType, TabStopPosition } = require("docx");

new Paragraph({
    // 配置
    alignment: AlignmentType.JUSTIFIED,

    // インデント（Twips単位: 1/20 pt）
    indent: {
        left: 720,   // 0.5インチ
        right: 720,
        firstLine: 360, // 0.25インチ
    },

    // 行間
    spacing: {
        before: 200,
        after: 200,
        line: 276,  // 1.15倍行間
    },

    // タブストップ
    tabStops: [
        {
            type: TabStopType.LEFT,
            position: TabStopPosition.MAX,
        },
    ],

    children: [
        new TextRun({
            text: "スタイル付きテキスト",
            bold: true,
            italics: true,
            underline: {
                type: UnderlineType.DOUBLE,
                color: "FF0000",
            },
            color: "2E3440",
            size: 24, // 12pt（半ポイント単位）
            font: {
                name: "Arial",
                hint: "default",
            },
        }),
    ],
})
```

### 画像とメディア

```javascript
const { Document, Paragraph, ImageRun, Media } = require("docx");
const fs = require("fs");

// 画像ファイルを読み込み
const image = Media.addImage(doc, fs.readFileSync("logo.png"), 200, 100);

new Paragraph({
    children: [
        new ImageRun({
            data: fs.readFileSync("logo.png"),
            transformation: {
                width: 200,
                height: 100,
            },
            type: "png", // 必須！
        }),
    ],
})
```

### 文書変換

#### DOCX → PDF → 画像

```bash
# 1. DOCX → PDF
soffice --headless --convert-to pdf document.docx

# 2. PDF → JPEG画像（各ページ）
pdftoppm -jpeg -r 150 document.pdf page
# 出力: page-1.jpg, page-2.jpg, ...

# オプション
pdftoppm -jpeg -r 300 document.pdf page  # 高解像度（300 DPI）
pdftoppm -png -r 150 document.pdf page   # PNG形式
pdftoppm -jpeg -f 1 -l 3 document.pdf page  # ページ1-3のみ
```

---

## ⚠️ トラブルシューティング

### よくある問題

#### 問題1: 依存関係エラー

```bash
# エラー: pandoc not found
brew install pandoc  # macOS
apt-get install pandoc  # Ubuntu

# エラー: soffice not found
brew install libreoffice  # macOS
apt-get install libreoffice  # Ubuntu

# エラー: pdftoppm not found
brew install poppler  # macOS
apt-get install poppler-utils  # Ubuntu
```

#### 問題2: XMLパースエラー

```python
# エラー: XML parsing failed

# 解決策1: 検証を実行
from ooxml.scripts.validate import validate_docx
validate_docx("document.docx")

# 解決策2: unpackして内容確認
python .claude/skills/docx/ooxml/scripts/unpack.py document.docx temp/
# XMLを手動で確認・修正
```

#### 問題3: フォーマット破損

```bash
# 症状: Wordで開くとエラー

# デバッグ手順:
# 1. Unpack
python .claude/skills/docx/ooxml/scripts/unpack.py broken.docx unpacked/

# 2. 検証
python .claude/skills/docx/ooxml/scripts/validate.py unpacked/

# 3. エラー箇所を特定
grep -r "w:rsidR" unpacked/word/document.xml

# 4. XMLを修正後、Pack
python .claude/skills/docx/ooxml/scripts/pack.py unpacked/ fixed.docx
```

### デバッグのヒント

| 問題 | デバッグ方法 | ツール |
|------|------------|--------|
| テキストが正しく抽出されない | pandoc変換結果を確認 | `pandoc -t plain` |
| 変更履歴が表示されない | `trackRevisions`設定確認 | `grep trackRevisions unpacked/word/settings.xml` |
| RSIDエラー | RSID形式を確認（8桁16進数） | `grep -E 'rsidR="[^0-9A-F]' unpacked/word/document.xml` |
| コメントが表示されない | コメントファイルとリレーション確認 | `ls unpacked/word/comments*.xml` |
| 画像が表示されない | メディアファイルとリレーション確認 | `ls unpacked/word/media/` |

---

## 🛠️ 開発者向け情報

### スキルファイル構成

```
.claude/skills/docx/
├── SKILL.md              # メインワークフロー・使用方法
├── LICENSE.txt           # Anthropic独占ライセンス
├── docx-js.md           # docx.jsチュートリアル（500行）
├── ooxml.md             # OOXML技術リファレンス（600行）
├── scripts/             # Python編集ライブラリ
│   ├── document.py      # Documentクラス（50KB）
│   ├── utilities.py     # XMLEditor基底クラス
│   └── templates/       # XMLテンプレート
└── ooxml/               # OOXML操作ツール
    ├── scripts/
    │   ├── pack.py      # ディレクトリ → .docx
    │   ├── unpack.py    # .docx → ディレクトリ
    │   ├── validate.py  # スキーマ検証
    │   └── validation/  # 検証モジュール
    └── schemas/         # 39個のXSDスキーマ
```

### 依存関係

#### 必須ツール

```bash
# テキスト抽出
brew install pandoc

# 新規文書作成
npm install docx

# PDF変換
brew install libreoffice

# PDF→画像変換
brew install poppler

# Python XML処理
pip install defusedxml
```

#### Pythonライブラリ

```python
# document.py の依存関係
from defusedxml import ElementTree as ET
import zipfile
import shutil
import os
from datetime import datetime
```

### OOXMLスキーマソース

| スキーマセット | ファイル数 | 用途 |
|--------------|-----------|------|
| ISO-IEC29500-4_2016 | 29 | DrawingML, WordprocessingML, SpreadsheetML等 |
| ECMA 第4版 | 4 | OPC（Open Packaging Conventions） |
| Microsoft拡張 | 5 | 2010-2020年の拡張機能 |
| MCE | 1 | マークアップ互換性 |

### カスタマイズと拡張

#### カスタムテンプレートの作成

```python
from scripts.document import Document

class CustomDocument(Document):
    def __init__(self, path, author):
        super().__init__(path, author)
        # カスタム初期化
        self.custom_styles = []

    def add_custom_header(self, text):
        """カスタムヘッダー追加"""
        header_xml = f'''
        <w:p>
            <w:pPr>
                <w:jc w:val="center"/>
            </w:pPr>
            <w:r>
                <w:t>{text}</w:t>
            </w:r>
        </w:p>
        '''
        # ヘッダーに追加
        header = self.get_header()
        self.append_to(header, header_xml)
```

#### バッチ処理スクリプト

```python
import glob
from scripts.document import Document

def batch_review(pattern, reviewer):
    """複数ファイルの一括レビュー"""
    for filepath in glob.glob(pattern):
        doc = Document(filepath, reviewer)

        # 共通の変更を適用
        nodes = doc.tree.findall('.//w:t', doc.ns)
        for node in nodes:
            if "古い会社名" in (node.text or ""):
                node.text = node.text.replace("古い会社名", "新しい会社名")

        # 保存
        output = filepath.replace(".docx", "_reviewed.docx")
        doc.save(output)

# 使用例
batch_review("contracts/*.docx", "Legal Team")
```

### OOXML重要ルール

| ルール | 詳細 | 例 |
|-------|------|-----|
| 要素順序 | `<w:pPr>`内は順序厳守 | `pStyle` → `numPr` → `spacing` → `ind` → `jc` |
| 空白保持 | 空白含む`<w:t>`には属性必須 | `<w:t xml:space="preserve"> text </w:t>` |
| RSID形式 | 8桁16進数のみ | `w:rsidR="00AB1234"` |
| trackRevisions配置 | `<w:proofState>`の後 | `settings.xml`内の順序 |

---

## 📚 参考資料

### スキル関連ドキュメント

- **SKILL.md**: ワークフロー概要と使用ガイド
- **docx-js.md**: 新規文書作成の完全チュートリアル（500行）
- **ooxml.md**: 既存文書編集の技術リファレンス（600行）

### 外部リソース

- [docx.js 公式ドキュメント](https://docx.js.org/)
- [Office Open XML 仕様](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)
- [Pandoc ユーザーガイド](https://pandoc.org/MANUAL.html)

### ライセンス

**Anthropic独占ライセンス** - Anthropicサービス内での使用に限定

---

## 🎓 まとめ

DOCXスキルは、Claude CodeでWord文書を完全に制御できる強力なツールです。

### 使い分けのポイント

| シナリオ | 推奨アプローチ |
|---------|-------------|
| 📝 新規ビジネス文書作成 | docx.js |
| ✏️ 自分の文書を編集 | Document library（基本編集） |
| 🔄 法務・学術文書のレビュー | Redliningワークフロー |
| 🔍 テキスト抽出・分析 | pandoc変換 |
| 🛠️ 高度なXML操作 | unpack + 直接編集 |

### 次のステップ

1. **学習**: `docx-js.md`と`ooxml.md`を読む
2. **実践**: 簡単な文書作成から始める
3. **応用**: レッドライニングワークフローに挑戦
4. **最適化**: バッチ処理スクリプトを作成

DOCXスキルを使って、プロフェッショナルな文書操作を実現しましょう！
