# CLIツール

MCPを増やす代わりに、**エージェントに叩かせるCLI**で機能を足す方針（ツール定義のコンテキスト消費を避けられる＋決定論的）。**以下すべて実際に使用中**。

---

## 必須

### 0. RTK — Rust Token Killer（既製）

- **リポジトリ**: [rtk-ai/rtk](https://github.com/rtk-ai/rtk)

#### 何を
**トークン最適化CLIプロキシ**。開発系コマンドの出力をトークン効率の良い形にフィルタして返す（公称60-90%削減）。

#### どの作業のために
**Claude Codeのhookで透過的に**動かす — エージェントが `git status` を打つと自動で `rtk git status` に書き換えられる（オーバーヘッド0トークン）。エージェント側は何も意識しない。

メタコマンド：

```bash
rtk gain
```

- `rtk gain` / `rtk gain --history` — トークン節約量の分析・コマンド別履歴
- `rtk discover` — Claude Codeの履歴を解析して「rtk化できたのにしてない」機会を発見
- `rtk proxy ` — フィルタなしの生実行（デバッグ用）

#### 入れる前と後（③・実体験）
- **前**: git・テスト・ビルド等の生出力が毎回そのままコンテキストに入る
- **後**: hookが全部書き換えるので**手作業ゼロで**日常の開発コマンド出力が痩せる。`rtk gain` で節約量を定量確認できる

---

### 1. react-doctor（既製・Million製）

- **リポジトリ**: [millionco/react-doctor](https://github.com/millionco/react-doctor)

#### 何を
Reactコードベースの健全性スキャナ。キャッチコピーは「**Your agent writes bad React, this catches it**」。state & effects／パフォーマンス／アーキテクチャ／セキュリティ／アクセシビリティの5領域を**静的解析ベース（LLM非依存・決定論的）**でスキャン。Next.js・Vite・Astro・TanStack・React Native・Expo対応。

#### どの作業のために

```bash
npx react-doctor@latest
```

CI導入は1コマンド（`npx react-doctor@latest ci install`）でGitHub Actionsを追加。**差分の新規Issueのみ報告**し、既存の技術的負債はブロックしない設計。

#### 入れる前と後
- **前**: エージェントが書いたReactのレビューを人間が目視
- **後**: PRごとの自動ゲートに置き換え。※テレメトリがデフォルト有効な点は注意（`--no-telemetry`）

---

### 2. fallow（既製）

- **リポジトリ**: [fallow-rs/fallow](https://github.com/fallow-rs/fallow)

#### 何を
TS/JS向け「コードベースインテリジェンス」。未使用コード・重複・循環依存・複雑度ホットスポットを検出し、**0-100の健全性スコア＋レターグレード**を出す。アーキテクチャ境界違反（layered/hexagonal/feature-sliced等）も検証。

#### どの作業のために

```bash
npx fallow
```

- `fallow audit` — 変更ファイルのみのPRゲート（pass/warn/fail）
- `fallow dead-code --trace src/file.ts:symbol` — シンボル削除前の未使用証明
- `fallow dupes` — 重複検出（strict〜semanticモード）
- `fallow fix --dry-run` — 自動修正プレビュー

#### 入れる前と後
- **前**: 未使用コードの目視探索・重複の手動grep
- **後**: 公式ベンチではデッドコード解析がknip比で最大27倍高速（preact: 74ms vs 2.01s。ただしプロジェクトによりknipが速い場合もあると自己申告）。knipがエラーになる大規模リポジトリ（next.js等2万ファイル）でも完走

---

### 3. evlog CLI（既製）

- **リポジトリ**: [hugorcd/evlog](https://github.com/hugorcd/evlog) / [CLIドキュメント](https://www.evlog.dev/cli/overview)

#### 何を
「**Lighthouseのオブザーバビリティ版**」。ソースコードを読み、フレームワークを理解し、全エントリポイントを検出して「障害時にどんなコンテキストが残るか」をマッピングする。ランタイム依存ゼロ（静的解析のみ）。

#### どの作業のために

```bash
evlog map
```

- **`evlog map`**: 全エントリポイントのwide-eventカバレッジをスコアリング（wide-event -40 / audit -25 / structured-errors -20 等の減点方式）、**まず直すべき上位3件を提示**。何もログしないハンドラ・監査証跡のないルートを発見
- **`evlog init`**: プロジェクトを読んでから質問するガイド付きセットアップ。フレームワーク検出・エラーカタログ生成
- **`evlog doctor`**: インストール・書き込み先の検証
- **`evlog agents`**: AGENTS.md/CLAUDE.mdへevlog規約を書き込み、エージェント用スキルをインストール

全コマンドJSON出力。CIは `--min-score`（閾値ゲート）と `--baseline`（悪化時のみ失敗のラチェット方式）でゲート。

#### 入れる前と後
- **前**: 「本番障害時にログが何も残っていない」ことに障害発生後に気づく
- **後**: dark（ログ皆無）なエントリポイントが機械的に可視化され、CIで退行も防げる。※公式に「Early days」と明記の早期ツール、バグは覚悟

---

### 4. agent-browser / playwright-cli（既製）— ブラウザMCPの代替

- [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) / [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
- 使い分けの参考: [Zennベンチマーク記事（ペパボ）](https://zenn.dev/pepabo/articles/ai-browser-automation-tools-benchmark)

#### 何を
chrome-devtools MCP・playwright MCPの**代わりに使うブラウザ自動化CLI**。

- **agent-browser**（Vercel製・Rustデーモン5MB）: ref付きアクセシビリティツリー（`click @e2` 形式の決定論的操作）、React専用検査、認証Vault、`--annotate` 番号付きスクショ。エラーメッセージの親切さが売り
- **playwright-cli**（Microsoft製）: `playwright-cli install --skills` でスキルとして導入。**snapshot出力が317バイトと最小＝トークン効率最良**。認証状態の保存/復元（state-save/load・`--persistent`）が最充実

#### なぜMCPでなくCLIか
Playwright公式自身が明言：「コーディングエージェントにはCLIの方が向いている。CLI呼び出しは大きなツールスキーマや冗長なアクセシビリティツリーをコンテキストに読み込む必要がなく、トークン効率が高い」。MCPが勝るのは探索的自動化・長時間の自律ワークフローのみ。

#### Zenn実測の要点（使い分け）

| 用途 | 推奨 |
|---|---|
| 認証管理（SAML/SSO）・企業内ツール | playwright-cli |
| 自作エージェントの操作基盤 | agent-browser |
| 大量クロール | Lightpanda（メモリ16MB） |

#### 入れる前と後
- **前**: ブラウザ系MCPのツール定義＋アクセシビリティツリーでコンテキストが数十KB単位で消費
- **後**: CLI経由で必要な出力だけ。E2E検証・スクショ確認のトークンコストが激減

---

### 5. react-grab（既製）

- **サイト**: [react-grab.com](https://www.react-grab.com/)

#### 何を
**ブラウザ上でクリックしたUI要素のソースコード文脈をエージェントに渡す**ツール。`npx grab@latest init` で導入、Claude Code / Codex / Cursor対応。

#### どの作業のために
「このボタンを直して」→ クリック → 対応コンポーネントの文脈がエージェントに渡る。ファイルを手動で探す作業を省略。

#### 入れる前と後
公式ベンチマーク（331件のUI要素→定義ファイル特定タスク）：

| リゾルバ | 平均時間 | 精度 |
|---|---|---|
| **React Grab** | **20.7s** | **96%** |
| Cursor Browser | 30.7s | 95% |
| ツールなしClaude Code | 45.1s | 86% |

素のClaude Code比で**約2.2倍速・精度+10pt**。「どのファイルか説明する」手作業をやめた。

---

## Linter

### konsistent（既製・Vercel製）

- **リポジトリ**: [vercel-labs/konsistent](https://github.com/vercel-labs/konsistent) / [Changelog](https://vercel.com/changelog/enforce-consistent-code-for-agents-and-humans-with-konsistent)

#### 何を
**構造的規約**（ファイル/ディレクトリ/エクスポート構造のパターン）を強制するCLIリンター。TypeScriptやESLintがモデル化できないパターンをカバー。Vercel社内でAI SDK・Chat SDKに実運用中。

`konsistent.json` に規約を定義：
- 「パターンXに一致する全ファイルは関数Y・Zをexportしているか」
- 「ファイルXを持つ全フォルダはファイルYも持っているか」
- テンプレート変数（`${providerId.toPascalCase()}` 等）でパラメータ化可能

エージェント連携スキルも提供: `npx skills add vercel-labs/konsistent --skill konsistent-config`（設定作成）/ `--skill konsistent-fix-violations`（違反修正）。

#### 入れる前と後
- **前**: 「新規プロバイダ/パッケージが規約通りの構造か」を目視レビュー
- **後**: 機械チェック化。公式実例ではAI SDKの340ファイルを**212msでチェックし15エラー検出**。エージェントと人間の双方が同じ規約で縛られる
