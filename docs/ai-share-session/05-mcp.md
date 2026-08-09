# MCP — 使うのは2つだけ

MCPはツール定義だけでコンテキストを食うので、**Mintlify Index** と **context-mode** の2つに絞っている（他のブラウザ系・docs系はCLIやスキルで代替 → [08-cli-tools.md](08-cli-tools.md)）。

---

## 1. Mintlify Index（既製）

- **発表**: [Mintlify公式ブログ（2026年8月）](https://www.mintlify.com/blog/mintlify-index) / [Xでの発表](https://x.com/mintlify/status/2085410422111494651)
- **ドキュメント**: [mintlify.com/docs](https://www.mintlify.com/docs)

### 何を
**パブリッシャー直結のドキュメント検索レイヤー**。Mintlifyがホストする5,000以上のドキュメントサイト（Anthropic・Microsoft・Notion等の高トラフィックdocsを含むエコシステム）を集約し、コーディングエージェント向けに自然言語検索を提供する。

ルーティングの仕組み：
1. クエリがMintlifyホストの製品docsに関するものか判定
2. 該当 → パブリッシャー管理の公式docsを最適化検索で返す
3. 非該当 → Web検索プロバイダにルーティング
4. 片方が失敗したらもう片方にフォールバック

### ベンチマーク（vs Context7）
50製品・150件の実装計画タスクでの公式ベンチマーク（[公式ブログ](https://www.mintlify.com/blog/mintlify-index)と[X発表スレッド](https://x.com/mintlify/status/2085410422111494651)は**同一実験の別表現**であることを裏取り済み — 生タイム64.0s vs 121.6sは (121.6−64.0)/121.6≒48%短縮と算数上一致）：

- ブラインドジャッジが**150件中96件（約2/3）でIndex側のプランを優位**と判定
- タスク完了が**48%高速**（生タイム: 64.0s vs 121.6s ≒ 2倍速）
- 事実的正確性 +10%、引用の裏付け +10%、重大エラー -17%
- ※「初期9,000ページ」「エコシステム20万org」はMintlify自己申告（X投稿のみ、独立検証なし）

### 導入方法

```bash
claude mcp add --transport http mintlify-index https://index.mintlify.com
```

または対応エージェント自動判定のワンコマンド：

```bash
npx mint index
```

**無料・認証不要**（レート制限：10req/秒、1,000req/日）。

### どの作業のために
ライブラリ・フレームワーク・SDK・API・CLIの調査全般。構文・設定・マイグレーション・セットアップの質問は必ずこれを通す（学習データが古い可能性があるため、既知のライブラリでも使う）。`context` ツールはトークン予算内（デフォルト3000）に収まるよう抜粋を組み立てて返す。

### 入れる前と後（③・実体験）
- **前**: **Context7を使っていた**が、WebFetch/WebSearch併用で複数ページを取得して目視確認。生ページ全文がコンテキストに入る
- **後**: **Context7から乗り換えた**。引用付きの要約が1コールで返り、ページ全文読み込みをやめた。全ライブラリ調査をこれ経由に統一（グローバルルールで強制）

---

## 2. context-mode（既製）

- **リポジトリ**: [mksglu/context-mode](https://github.com/mksglu/context-mode)（2.5k★、Elastic License 2.0）

### 何を
**コンテキストウィンドウ保護**のためのMCPサーバー＋フックプラグイン。核心概念は **"Think in Code"**：

> LLMは分析を「計算する」のではなく「プログラムする」べき。50ファイルを読んで関数を数えるのではなく、数えるスクリプトを書いて結果だけをconsole.log()する。

生データはサンドボックス内に留まり、**console出力（導出された答え）だけが会話に入る**。README記載の例：47ファイルを `Read()` で読むと700KB消費 → `ctx_execute()` 1回で3.6KB。

### 主要ツール

| ツール | 役割 | 削減例（README記載） |
|---|---|---|
| `ctx_batch_execute` | 複数コマンド＋検索クエリを1コールで並列実行、結果を自動インデックス（FTS5/BM25） | 986KB → 62KB |
| `ctx_execute` | 12言語対応サンドボックスでコード実行、stdoutのみ会話へ | 56KB → 299B |
| `ctx_execute_file` | ファイルをサンドボックス内で処理、生の中身は出さない | 45KB → 155B |
| `ctx_search` | インデックス済みコンテンツ＋セッション記憶を複数クエリで検索 | オンデマンド |
| `ctx_fetch_and_index` | WebFetch代替（URL取得→チャンク化→インデックス、24hキャッシュ） | 60KB → 40B |
| `ctx_stats` / `ctx_doctor` / `ctx_purge` | 統計 / 診断 / 全削除 | — |

### フック連携（ここが強い）
- **SessionStart**: ルーティング指示を注入。**コンパクション後はSession Guide（未解決タスク・決定事項・変更ファイル等15カテゴリ）を自動再構築して注入**
- **PreToolUse**: Bash/Read/WebFetch等をインターセプトしてサンドボックスへリダイレクト（Claude Codeでは自動強制）
- `ctx_search` にはProgressive Throttling（乱用すると段階的に絞られ `ctx_batch_execute` へ誘導）

### 導入方法

```bash
claude mcp add context-mode -- npx -y context-mode
```

プラグイン版（フック込み）は `/plugin marketplace add mksglu/context-mode` → `/plugin install context-mode@context-mode`。

完全ローカル動作（テレメトリなし・アカウント不要・無料）。

### どの作業のために
大量のログ・ビルド出力・API応答・ブラウザスナップショットなど「読む」より「集計・フィルタする」タスク全般。トークン管理の要。

### 入れる前と後（③・実体験）
- **前**: 生ログやページ全文をRead/WebFetchで会話に読み込み、コンテキストが数ターンで枯渇。コンパクション後に状況を再説明
- **後**: 長セッションでもコンテキストが痩せない。コンパクション後の再説明という手作業をやめた（Session Guide自動再構築）
- 参考: 公称値は**最大98%削減**（315KB→5.4KB、README記載）
