# プラグイン

## 必須（全プロジェクト共通）

### 1. claude-plugins-official（既製・Anthropic公式）

- **リポジトリ**: [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

Anthropic管理の公式マーケットプレイス（284プラグイン登録）。`/plugin install {name}@claude-plugins-official` で導入。使っているのは：

#### frontend-design
「量産型AI感」を避けた独創的でプロダクション品質のUIを生成。ダッシュボード・LP等の見た目にこだわる実装で自動発動。**前後**: 没個性UI → 明確な美的方向性を持つ実装。

#### language-lsp（typescript-lsp 等）
各言語のLanguage ServerをClaude Codeに統合。型情報・定義ジャンプ・参照関係をLSPの静的解析で正確に把握させる。**前後**: コード内容からの推測 → LSP診断結果を利用した正確な編集。

#### claude-code-setup
コードベースを解析し、そのプロジェクトに合ったhooks・skills・MCP・サブエージェントを推奨。新規プロジェクトのオンボーディングに。

#### claude-md-management
`CLAUDE.md` の品質監査・セッションの学び記録・プロジェクトメモリの鮮度維持。CLAUDE.mdの肥大化・陳腐化対策。

#### hookify
複雑な `hooks.json` を手書きせず、**自然文の指示でカスタムフックを作れる**。`/hookify 危険なrm -rfコマンドを警告して` → Markdownルールが生成され再起動不要で即反映。**前後**: JSON構文を理解して手書き → 自然文で即作成。

#### security-guidance
- **ドキュメント**: [公式（日本語）](https://code.claude.com/docs/ja/security-guidance) / [ソース](https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance)

生成中のコードを脆弱性レビューし**同一セッション内で修正までさせる**3層構造：

1. **パターン警告（編集ごと）**: Edit/Write直後に約25種の危険パターン（`eval()`・`innerHTML`代入・ハードコードシークレット等）を正規表現で即検知。モデル呼び出しなし・コストゼロ
2. **ターン終了時のLLM diffレビュー**: Stopフックでそのターンの全変更をOpusがバックグラウンドレビュー。認可バイパス・IDOR・SSRF等のパターンでは拾えない問題を検出→同じ会話でClaudeに修正させる
3. **エージェント的コミットレビュー**: `git commit`/`push` 時に独立レビュアーが周辺コード・呼び出し元・サニタイザーまで追ってデータフロー全体を検証

`.claude/claude-security-guidance.md`（組織固有ルール）と `.claude/security-patterns.yaml`（独自パターン、最大50件）で拡張可能。**前後**: セキュリティレビューが人間のPRレビュー任せ → PRに到達する前にセッション内で検出・修正され、下流のレビュー負荷が下がる。

---

### 2. ECC — Everything Claude Code（既製）⭐ 特に推したい

- **リポジトリ**: [affaan-m/ECC](https://github.com/affaan-m/ECC) / [紹介ポスト](https://x.com/nobel_824/status/2044258388780228841)

#### 何を
「エージェントハーネス運用基盤」を自称する大規模プラグイン。**67エージェント・282スキル・94コマンド**に加え、rules・hooks・securityの**ガードレール設計が秀逸**。Claude Code含む7ハーネス対応。

役割分担が明確：

| 概念 | 何をするか | コンテキストでの扱い |
|---|---|---|
| Skills | TDD・セキュリティレビュー等の再利用ワークフロー | タスクに応じてロード |
| Agents | 独立コンテキスト/権限を持つ実行者 | 計画・実装・レビューを分離 |
| Rules | プロジェクト/言語の恒常的な標準 | 常時ロード（選択的インストール推奨） |
| Hooks | ハーネスイベントで発火するスクリプト | モデルコンテキスト外で実行 |
| Instincts | 実セッションから学習した確信度付きパターン | 関連時にリコール |

#### ガードレール3層（ここが本命）

**① Rules**: `rules/common/` + 言語別（typescript/python/golang等）の「常に従うべき」規約集。「TDDを守って」のような口頭指示をモデルの記憶に依存させず、恒常的制約として固定化。常時ロードなので必要なものだけ選択インストール。

**② Hooks**: イベント駆動の強制・自動化。
- **GateGuard**: 破壊的シェルコマンド（`rm`・強制`git checkout`・破壊的`find -exec`等）を**実行前にゲート**
- サプライチェーンIOC（侵害指標）スキャナーをCIで実行
- 設計思想：「Hooksはシェルを実行でき、MCPは認証情報を持ち、プロジェクト指示はコンテキストに入る — この3つは全て実行可能な設定として扱うべき」

**③ AgentShield**（[affaan-m/agentshield](https://github.com/affaan-m/agentshield)）: **エージェント設定自体を攻撃対象領域とみなす**セキュリティ監査ツール。`/security-scan` で `.claude/` ディレクトリを静的解析し、**102ルール×5カテゴリ**でA〜Fグレード採点：

1. **シークレット検出**: `sk-ant-`・AWS `AKIA`・GitHub PAT・JWT等のハードコード検知
2. **権限監査**: ワイルドカード権限・`rm -rf`/`sudo` のdeny欠如・危険なフラグ使用
3. **フック分析（34ルール）**: コマンドインジェクション・`curl POST` によるデータ持出し・リバースシェル・エラー握りつぶし
4. **MCPサーバーセキュリティ（23ルール）**: 高リスクMCP・`npx -y` タイポスクワッティング・`0.0.0.0` バインド・autoApprove
5. **エージェント設定レビュー**

`--fix` でシークレットを環境変数参照に自動置換。`--opus` でRed Team / Blue Team / Auditorの3エージェント対抗パイプラインによる敵対的深掘りも可能。GitHub Action（SARIF出力・ベースライン比較・組織ポリシー適用）としてCIゲート化できる。

#### 入れる前と後
- **前**: ガードレールは自前のhooks手書き頼み。エージェント設定自体の脆弱性は誰も見ていない
- **後**: 破壊的コマンドの事前ブロック＋設定の定期監査が仕組み化。「モデルに指示する」から「デコード可能な形で強制・監査する」へ

> ⚠️ 注意（裏取り済み）: ECCは単一メンテナ主導のプロジェクトで、Anthropic公式監査を経ていない。README記載の実績値は要注意：
> - **スター数は信頼しない**こと（実測値は異常な急増パターンを示しており、star farmingの疑いあり）
> - **Moltbook侵害は実在**（77万エージェント・150万APIトークン漏洩。原因はSupabaseのRLS未設定。一次情報: [Wiz](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)）— AgentShieldが訴える脅威の実在性の裏付けにはなる
> - README言及のCVEは **CVE-2026-25253**（CVSS 8.8）だが、対象は**OpenClaw（旧Clawdbot/Moltbot）という別製品**であり、Claude CodeやMCPサーバー全般の脆弱性ではない。露出インスタンス数も調査元により17,500〜220,000超とばらつく

---

### 3. modern-web-guidance（既製・Google Chrome + Edge チーム）

- **リポジトリ**: [googlechrome/modern-web-guidance](https://github.com/googlechrome/modern-web-guidance) / [Zenn解説（Ubie）](https://zenn.dev/ubie_dev/articles/modern-web-guidance)

#### 何を
モダンWebプラットフォームAPI・ベストプラクティス・ブラウザ互換性データ（Baseline連動）をエージェントに注入するスキル。Google I/O 2026で発表。

**解決する課題**: LLMの学習データは古いコードが多数派なので、放っておくとSubgridで済む場面で古いGridネスト、`Object.groupBy` で済む処理を `reduce` で書く。公式評価では曖昧な開発依頼75件に対し、**導入前52% → 導入後85%** がモダンな正答に。

**カバー範囲**: CSSレイアウト（コンテナクエリ・Subgrid・oklch）／View Transitions・スクロール駆動アニメーション／パフォーマンス（fetchpriority・INP・scheduler.yield）／フォーム&UI（Anchor Positioning・Popover API・dialog）／アクセシビリティ／ブラウザ内蔵AI — 計103ガイド。

**仕組み**: `search`（類似度スコア付きガイド検索）→ `retrieve`（実装手順＋コード例＋ブラウザ対応状況）。検索はオフラインのTensorFlow.jsで完結、APIキー不要。未対応環境にはフォールバックも提案。

導入: `npx modern-web-guidance@latest install`

#### 入れる前と後
- **前**: 学習データに偏った古いパターン（正答率52%）
- **後**: 最新Web標準準拠（85%）＋Baseline連動のフォールバック提案

---

### 4. codex-plugin-cc（既製・OpenAI公式）

- **リポジトリ**: [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

#### 何を
Claude Code内から**OpenAI Codexを呼び出す**公式プラグイン。ローカルのCodex CLIをラップし、認証は既存の `~/.codex/config.toml` をそのまま使う。

| コマンド | 用途 |
|---|---|
| `/codex:review` | 読み取り専用レビュー（`--base ` でブランチ比較） |
| `/codex:adversarial-review` | 設計判断・トレードオフ・隠れた前提を突く敵対的レビュー |
| `/codex:rescue` | バグ調査・修正の実タスクをCodexへ委任 |
| `/codex:transfer` | Claude CodeセッションをCodexスレッドに変換 |
| `/codex:setup` | 導入確認＋Stopフックの「レビューゲート」有効化 |

#### 入れる前と後
- **前**: 単一モデル（Claude）内で完結するレビューのみ
- **後**: **別プロバイダのGPT系モデルによる独立査読**がワークフローに入る。詰まったバグを別モデルに振れる

---

## プロジェクト別

| プラグイン | 何を | ポイント |
|---|---|---|
| [Vercel Plugin](https://vercel.com/docs/agent-resources/vercel-plugin) | Vercel公式。28スキル＋3専門エージェント（deployment-expert / performance-optimizer / ai-architect）＋5コマンド | コンテキスト自動注入はVercel/Next.jsプロジェクト検出時のみで軽量 |
| [Expo skills](https://github.com/expo/skills) | Expo公式。Router・ネイティブUI・NativeWind等の無料スキル群＋EASビルド/提出/Workflowsのサービス系スキル群 | Expo MCP同梱（docs参照・expo install・シミュレータスクショ） |
| [Convex Agent Plugins](https://github.com/get-convex/convex-agent-plugins) | Convex公式。18常時ルール＋6スキル（schema-builder / auth-setup / migration-helper等）＋2エージェント | pre-commitブロッキングチェック＋ターン終了時検証ループ |
| [Resend Plugin](https://resend.com/changelog/resend-claude-code-plugin) | Resend公式。MCP＋全スキル（resend / react-email / email-best-practices / resend-cli等）を単一インストールに統合 | `RESEND_API_KEY` 設定だけで文脈に応じて自動有効化 |

その他、使う技術スタックの公式プラグインがあればそれを優先して入れる。
