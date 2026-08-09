# mattpocock-skills — Grill駆動の開発フロー

> 開発タスクの軸。TypeScript解説で著名なMatt Pocock氏（[@mattpocockuk](https://x.com/mattpocockuk)）製の既製スキル集。
> - 公式: [aihero.dev/skills](https://www.aihero.dev/skills)
> - リポジトリ: [mattpocock/skills](https://github.com/mattpocock/skills)

---

## なぜ使うか：思想（SDDではなく"GDD"）

Matt本人の言葉（[X投稿](https://x.com/mattpocockuk/status/2083563195671667176)）:

> みんな私のスキルをspec-driven-developmentと混同する。本当に苛立つ。私のスキルが作るspecは**即座に削除されることを意図している** — 保管したりソースコードとして扱うものではない。Birgitta Boeckelerはこれを「spec-first」開発と呼ぶが、それでもSDDの傘下に分類している。私は同意しない。独自の用語が必要だと思う。specはそれほど重要じゃない。**グリル（尋問）中に下された意思決定の投影にすぎない**。GDD？ Grill-driven-development。IDK

リポジトリREADMEのスタンスも同様:

> GSD・BMAD・Spec-Kitのようなアプローチはプロセスを「所有」することで助けようとするが、その過程でコントロールを奪い、プロセスのバグを解決困難にする。これらのスキルは小さく、適応しやすく、組み合わせ可能に設計されている。

要点：
- **意思決定の場は常にグリル（会話）**。specは決定の記録であって、決定の場ではない
- `/to-spec` は「インタビューしない。決定は済んでいる前提で統合するだけ」
- 決定の成果物は3層に振り分け：用語→`CONTEXT.md`、後戻り困難な決定→ADR、**それ以外→会話の中にのみ存在しどこにも残らない**
- チケットは使い捨ての実行単位。「ピボットしたら未完チケットは削除してspecだけ残せ」

Boeckeler氏の分類（Spec-first / Spec-anchored / Spec-as-source）で言えば、Mattのアプローチは最軽量の「specは会話の副産物」側。Kiro/spec-kit系（spec-as-source）とは対極。

> 出典整理（裏取り済み）: Mattのポストは実在・原文一致（2026年8月1日投稿）。参照先はBirgitta Böckeler「[Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)」（martinfowler.com）。なお「specは即削除」はMatt自身の主張であり、Böckelerの記事は削除を明言していない — 帰属に注意。

---

## メインフロー（GDDフロー）

```
grill-with-docs → to-spec → to-tickets → implement（+TDD） → code-review
```

| スキル | 何をするか |
|---|---|
| **grill-with-docs** | リポジトリ内で計画をグリル（質問攻め）しながら `CONTEXT.md` とADRをその場で更新。1問1答ではなく「ラウンド＝フロンティア全体」で尋問。単一セッション規模の変更の入口 |
| **to-spec** | 直前の会話をspecに統合してissue化。**インタビューしない**純粋な統合。決定済みの会話が前提 |
| **to-tickets** | specを依存関係付きの「トレーサーバレット（垂直スライス）」チケットに分割。水平スライス（層ごと）を禁止 — 26チケットを層で切って手戻り75%を出した失敗事例が設計の教訓 |
| **implement** | チケット単位（1チケット=1セッション、間でコンテキストクリア）でテストファースト実装。**tddスキルと統合**。`disable-model-invocation: true` で人間の明示起動のみ |
| **code-review** | Standards軸（リポジトリ規約準拠）とSpec軸（元issueへの忠実性）の2軸を並列サブエージェントでレビュー。※私はここだけClaude Code標準の `/code-review` を使うことが多い |

---

## 最推しスキル：wayfinder 🗺️

> 出典: [aihero.dev/skills-wayfinder](https://www.aihero.dev/skills-wayfinder) / [SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md)

### 何を
**1セッションに収まらない大規模タスクを「意思決定の地図」に変える**プランニングスキル。Matt本人いわく「より整理された、間違えようのないgrill-me」。

### 核心原則：Plan, don't do（計画せよ、実行するな）
従来のAIエージェントは大きなタスクを渡すと即実装を始めて途中で迷走する。wayfinderはコードを書く前に、曖昧なプロジェクト全体を**チケット形式の意思決定マップ**に落とし込むことだけに専念する。

### 使い分け基準
プロジェクト規模ではなく**セッション数**。1セッションで収まるなら `grill-with-docs` の方が安くて適切。複数セッションに跨る時だけwayfinder。

### マップの構造
`wayfinder:map` ラベル付きの単一issueで、チケットは子issue。マップは**インデックスであってストアではない**（決定はチケット1箇所にのみ存在、マップは要約とリンクだけ）。

- **Destination（目的地）**: マップの終着点。最初に命名され、全チケットのスコープ判定基準になる
- **Decisions so far**: クローズ済みチケット1件につき1行＋リンク
- **Not yet specified（霧・fog of war）**: 来るのは分かるがまだ鋭く言語化できない決定。判定基準は「今その問いを**正確に述べられる**か」（答えられるかではない）。チケット解決→霧が晴れて新チケットに昇格
- **Out of scope**: 目的地の外とルールした作業。霧に昇格することはない

### 4つの意思決定チケットタイプ

| タイプ | モード | 使う場面 |
|---|---|---|
| **Grilling** | HITL（デフォルト） | 会話で解決できる問い。grilling + domain-modelingスキルで対話確定 |
| **Prototype** | HITL | 「どう見えるべき/振る舞うべきか」など会話だけでは決着しない問い。使い捨てコードを作って反応を見る |
| **Research** | AFK | 外部API仕様・ドメイン知識など作業ディレクトリ外の調査。**バックグラウンドのサブエージェントが並列で解決**、`research/` ブランチに成果を残す |
| **Task** | HITL/AFK | 決めることはないが決定をブロックする手作業（サービス登録・アクセス提供・データ移動） |

HITL＝human in the loop。HITLチケットは人間との生きたやり取りでのみ解決し、**エージェントの自問自答は「壊れている」と見なされる**。

### フロンティアとクレーム
- **フロンティア** = 開いていて・ブロックされておらず・未着手のチケット群（既知の端）
- セッションは着手前にチケットを自分にアサインして「claim」→ 並行セッションがスキップできる
- ブロッキングはトラッカーのネイティブ依存関係を使い、**トラッカーUI上でフロンティアが視覚化される**

### ワークフロー
1. `/wayfinder` にざっくりしたアイデアを渡す
2. グリルで**目的地を確定**（specの定義）
3. 疑問点・ルートをチケット化してトラッカーに配置、researchサブエージェントを並列発火
4. 以降のセッションで1チケットずつ解決（1セッション1チケット厳守）
5. 全チケットがクローズ＝霧が晴れたら `/to-spec #` でマップ全体を1つのspecに畳み込み → `to-tickets` → `implement` へハンドオフ

### 入れる前と後（③・実体験）
- **前**: コンテキストウィンドウがプランの唯一の置き場。**コンテキストが手元にしか残らず、トレーサビリティが完全に破綻。「なぜそうなったのか」を後から振り返っても分からない**
- **後**: 意思決定がトラッカーに永続化され、**任意の将来セッションが引き継げる**。やめた手作業＝セッション跨ぎの引き継ぎ説明・逐一ドキュメントを残す手間・「なぜそうなったか」の調査。AIも人間も進捗と意思決定で迷わなくなるため、loop engineering / graph engineeringがスムーズに回る。実務者評（[nathanfennel.com](https://nathanfennel.com/blog/matt-pocock-skills-three-months-later)）:「文脈ファイルはセッションに知識を持ち込む。決定チケットはセッションから決定を持ち出す」

### 実例ケーススタディ（自分のリポジトリ [sc30gsw/life-pulse](https://github.com/sc30gsw/life-pulse/issues?q=is%3Aissue%20state%3Aclosed)）

完走したwayfinderマップ2枚：

**① [Convexを知らないエンジニア向け90分技術プレゼンを設計する（#9）](https://github.com/sc30gsw/life-pulse/issues/9)**
- 8チケット（grilling×4・research×1・prototype×1・task×1）を**約1.5時間で完走**
- 成果: 35枚スライド・102件の一次資料URL・90分の時間配分まで確定したMarkdown計画書
- マップの最終状態:「Not yet specified: なし。目的地までの判断を完了した」— 霧が完全に晴れた状態

**② [全チャートをTanStack Chartsへ移行して分析体験を再設計する（#17）](https://github.com/sc30gsw/life-pulse/issues/17)**
- 13チケット（grilling×2・research×2・prototype×1・task×7）
- **Notesでplanning-only既定を上書きし、実装・検証・旧依存撤去までマップ内で運んだ**応用例
- pre-alphaライブラリ（TanStack Charts 0.7.2）の移行可否をresearchチケットで確定し、prototypeチケットの成果を `prototype/tanstack-chart-ux` ブランチに保存

**体験から言えること**：
- HITLのグリルは時間がかかるし調査も必要で正直苦痛。**だが後が断然楽** — ガードレールと同じで、ここで詰めることで圧倒的に手戻りが減り、**ほぼ放置で良くなる**
- 使い分けはタスクの大きさ。**1機能・軽めの修正なら通常フロー（grill-with-docs→to-spec→to-tickets→implement）の方が良い**。複数セッションに跨る規模でwayfinder
- specはMattの思想どおり**捨てている**。specはグリルで下した意思決定の投影にすぎず、決定そのものはチケット（トラッカー）に永続化されているから

### なぜ「意思決定の永続化」が今アツいか（業界文脈）

Gitのコミット中心モデルは、変更内容（diff）は記録できても**それを生んだAIとの対話・検討過程・却下した代替案までは残せない**（いわゆる "Decision Shadow" 問題）。GitHubも2026年3月にCopilotエージェントのコミットへセッションログの永続リンク（`Agent-Logs-Url`）を付ける部分対応を始めたが、後付けに留まる。[Cursor Origin](https://cursor.com/origin)（エージェント大量並列コミット向けGitホスティング、2026年6月発表・秋リリース予定）やZedの[DeltaDB](https://zed.dev/blog/introducing-deltadb)（操作単位で会話履歴そのものを記録する新VCS）のように、前提を土台から作り直す動きが2026年に相次いでいる。

**wayfinderの「意思決定をissueトラッカーに永続化する」は、この業界課題への今日から使える運用解。**

参考: [Matt PocockのYouTube解説](https://www.youtube.com/watch?v=F3lL98Pj90o) / [v1.1チェンジログ](https://www.aihero.dev/skills/skills-changelog-v1-1-wayfinder-to-spec-to-tickets-grilling-improvements)

---

## その他よく使うスキル

### セットアップ
- **setup-matt-pocock-skills**: リポジトリごとに1回実行。issueトラッカー設定・triageラベル・`docs/agents/` 配下のドメインドキュメント配置・`CLAUDE.md`への `## Agent skills` ブロック追加。これでトラッカー非依存（GitHub/Linear/ローカルmarkdown何でも）になる

### Shaping系
- **grill-me**: 作業ディレクトリ不要のステートレス尋問ループ。漠然としたアイデアを固める。ファイルは書かない
- **prototype**: 使い捨てコードで設計判断に答える。テスト・エラーハンドリング・抽象化なし。現在は `prototype/` ブランチに残して次セッションの一次情報源にする方式
- **research**: バックグラウンドエージェントが一次情報源を調査してMarkdown 1本に集約。wayfinderのresearchチケットのバックエンドでもある

### 保守系
- **diagnosing-bugs**: 6段階の規律あるバグ診断ループ（再現→最小化→仮説→計測→修正→リグレッションテスト）。「この不具合でREDになるコマンド」がない限り先に進ませない
- **improve-codebase-architecture**: シャロー（浅い）モジュールを探して視覚的HTMLレポート（Strong / Worth exploring / Speculative）を提示、選んだ候補をグリル
- **triage**: 外部由来のissue（バグ報告・機能要望・無断PR）をステートマシンで仕分け。自分で作ったチケットには使わない
- **resolving-merge-conflicts**: merge/rebase競合を両側の一次情報に立ち返って意図ベースで解決。`--abort` せず完遂

### 生産性系
- **handoff**: 別セッション/エージェントへの引き継ぎ用「携行可能ファイル」を書き出す。`/compact`（圧縮継続）とも `/clear`（破棄）とも違う「移動」特化
- **wait-what**: たった3行のスキル。直前の発言を `CONTEXT.md` の語彙で平易に説明し直させる。冗長な出力が理解できなかった時に

### 参照系（他スキルから呼ばれる）
- **domain-modeling**: ユビキタス言語の構築。用語の衝突を指摘し、決着した瞬間に `CONTEXT.md` へ書き込む
- **codebase-design**: 「深いモジュール」設計の共有語彙（Module/Interface/Depth/Seam/Adapter/Leverage/Locality）。tddスキルもこれを参照

---

## 発表用まとめ

| ①何を | ②どの作業で | ③前後の変化 |
|---|---|---|
| mattpocock-skills（既製） | 開発タスク全般（計画→spec→チケット→実装→レビュー） | 「いきなり実装して迷走」が消えた。意思決定が会話（グリル）で固まってから手が動く。wayfinderで大規模タスクの意思決定がトラッカーに永続化され、セッションを跨げるようになった |
