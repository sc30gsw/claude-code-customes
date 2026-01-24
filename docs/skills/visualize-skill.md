# Visualize Skill

## 概要

ドキュメントをビジュアルなインフォグラフィック画像（PNG/JPG/PDF）に変換するスキル。Slack、Teams、Discordなどのチャットアプリで簡単に共有できる形式で出力します。

## アクティベーショントリガー

- ドキュメントを画像で共有したい時
- プレゼンテーション用の要約が必要な時
- 複雑な情報を視覚化したい時
- レポートのインフォグラフィックを作成したい時

## 使用方法

```bash
/visualize <input-file> [options]
```

## 引数
- `input-file`: ドキュメントへのパス（必須）
- サポート形式: `.md`, `.txt`, `.pdf`

## オプション

| オプション | 短縮 | 説明 | デフォルト |
|-----------|------|------|----------|
| `--output` | `-o` | 出力ファイルパス | `{input}-infographic.png` |
| `--format` | `-f` | 出力形式（png/jpg/pdf） | `png` |
| `--theme` | `-t` | ビジュアルテーマ | `business` |
| `--size` | `-s` | 画像サイズプリセット | `chat` |
| `--max-points` | `-m` | 最大キーポイント数 | `6` |
| `--lang` | `-l` | 出力言語（ja/en） | `ja` |
| `--style` | | 出力スタイル | `summary` |
| `--audience` | `-a` | ターゲットオーディエンス | `team` |
| `--diagram` | `-d` | Mermaidダイアグラム含む | `false` |
| `--visual-type` | `-vt` | ビジュアル形式 | `auto` |
| `--panels` | `-p` | コミック用パネル数（2-6） | `3` |

## テーマ

| テーマ | 説明 | 最適な用途 |
|-------|------|----------|
| `business` | プロフェッショナルなブルートーン | 業務プレゼンテーション |
| `modern` | 鮮やかなグラデーション | マーケティング資料 |
| `tech` | ダークアクセント、モノスペース | 技術ドキュメント |
| `minimal` | ホワイトスペース、シンプル | クリーンな要約 |
| `dark` | ダーク背景 | 画面表示向け |

## サイズプリセット

| プリセット | サイズ | 最適な用途 |
|-----------|--------|----------|
| `chat` | 1200x630px | Slack, Teams, Discord |
| `slide` | 1920x1080px | プレゼンテーション |
| `a4` | 2480x3508px | 印刷（A4縦） |
| `square` | 1080x1080px | ソーシャルメディア |

## 出力スタイル

| スタイル | 説明 | 理解レベル |
|---------|------|----------|
| `summary` | 1ページ、簡潔 | 表面（何があるか） |
| `visual` | ダイアグラム + コンテキスト | **深い（なぜ＆どのように）** |
| `detailed` | TOC付きマルチセクション | 包括的 |

## ビジュアルタイプ（visualスタイルのみ）

| タイプ | 最適な用途 |
|-------|----------|
| `diagram` | フロー、プロセス、API、データ構造 |
| `cards` | 機能リスト、比較 |
| `comic` | ユーザージャーニー、チュートリアル |
| `auto` | コンテンツに基づき自動選択 |

## 使用例

```bash
# 基本使用
/visualize ./docs/report.pdf

# テーマとサイズ指定
/visualize ./notes.md --theme modern --size slide

# ダイアグラム付きビジュアルスタイル
/visualize ./architecture.md --style visual --visual-type diagram

# コミック形式（4パネル）
/visualize ./tutorial.md --style visual --visual-type comic --panels 4

# エグゼクティブサマリー
/visualize ./quarterly-report.pdf --audience executive --style summary
```

## 処理ワークフロー

1. **読み取りと分析**: ドキュメント構造を解析
2. **キーポイント抽出**: ターゲットオーディエンスに基づく
3. **ダイアグラム生成**: `--diagram`有効時（Mermaid）
4. **アイコン選択**: カテゴリ用Lucide SVGアイコン
5. **HTML生成**: スタイルテンプレートに基づく
6. **Playwrightでレンダリング**: 画像としてキャプチャ
7. **出力とレポート**: ファイル保存と結果レポート

## 成功指標

- 画像が正常に生成される
- テーマが正しく適用される
- キーポイントが適切に抽出される
- ファイルサイズが適切
