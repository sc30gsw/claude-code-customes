## Destination

`docs/ai-share-session/` の全ドキュメントが (1) **Notionに即貼りできる最終版**（内容確定・未検証情報の解消・③欄が本人の実体験）かつ (2) **発表台本つき**（wayfinderを目玉に、当日話す流れ・時間配分を含む）になった状態。

## Notes

- 発表フォーマット: ①何を（名前・自作/既製）②どの作業のために ③入れる前後の変化（時間・回数・やめた手作業）
- 目玉アイテムは **wayfinder** — 04のドキュメントと台本の厚みを最優先
- ③欄はベンダー公称値ではなく**ユーザー本人の体験**が正。公称値は補足に格下げ
- グリルには grilling スキル相当の姿勢で臨む（HITLチケットの自問自答は禁止）
- Notionへの実アップロードは本マップの外（ユーザーが手動で行う）

## Decisions so far

- チャーティング時のグリル（2026-08-10） — 目的地=Notion最終版+台本 / ③=実体験に差替え / 食い違い6点=research裏取り / 目玉=wayfinder
- [R1: Mintlifyベンチ数値の裏取り](https://github.com/sc30gsw/claude-code-customes/issues/2) — Xとブログは同一実験の別表現（64.0s vs 121.6s ≒ 48%短縮）。ブログ数値を主、X生タイムを併記
- [R2: ENABLE_TOOL_SEARCH v2.1.221注記の裏取り](https://github.com/sc30gsw/claude-code-customes/issues/3) — 正確。英語版docに逐語的に存在（日本語版は未反映）。v2.1.119無効化→v2.1.221で4.5世代以降のみ再有効化
- [R3: ECC実績値の一次ソース追跡](https://github.com/sc30gsw/claude-code-customes/issues/4) — スター数は信頼性なし（削除）。Moltbook侵害はWiz一次情報で検証済み。CVE-2026-25253はOpenClaw固有（Claude Code/MCP全般ではない）と限定必須
- [R4: pstack日次自動化の一次確認](https://github.com/sc30gsw/claude-code-customes/issues/5) — poteto氏ポスト実在・Cursor Automations機能も公式doc実在。現状表記「作者推奨Tips」は正確
- [R5: GDD命名ポストの確認](https://github.com/sc30gsw/claude-code-customes/issues/6) — ポスト実在・引用原文一致。Boeckeler参照元はmartinfowler.comのSDD 3分類記事。「即削除」はPocockの主張として帰属明確化
- [R6: AIトレーサビリティとGitHub代替の裏取り](https://github.com/sc30gsw/claude-code-customes/issues/7) — Cursor Origin実在（2026年6月発表・秋リリース予定）だが主目的はエージェント並列コミットのスケール。トレーサビリティ本命はZedのDeltaDB。GitHubも2026年3月に部分対応済み
- [G1: 体験談グリル — wayfinder（目玉）](https://github.com/sc30gsw/claude-code-customes/issues/8) — 実例=life-pulseマップ2枚（#9: 8チケット約1.5h完走 / #17: planning-only上書きで実装まで）。導入前はトレーサビリティ破綻・「なぜ」が消失。グリルは苦痛だが手戻り激減でほぼ放置可。使い分け=タスク規模。specは思想どおり即削除
- [G2: 体験談グリル — 本体設定](https://github.com/sc30gsw/claude-code-customes/issues/9) — ENABLE_TOOL_SEARCH=true実設定。Switch models flaggedは**true**（当初メモから訂正）。最大ワークフロー実例=本資料作成セッション（12サブエージェント）
- [G3: 体験談グリル — MCP/プラグイン/CLI](https://github.com/sc30gsw/claude-code-customes/issues/10) — Mintlify=Context7から乗り換え。CLIツール5種すべて使用中
- [G4: 発表台本のグリル](https://github.com/sc30gsw/claude-code-customes/issues/11) — 20分・wayfinderライブデモ・新アイテムRTK追加・聴衆=この環境に馴染みのないエンジニア
- [T1: 食い違い6点の本文修正](https://github.com/sc30gsw/claude-code-customes/issues/12) — R1〜R6の結果を01/02/04/05/06/09に反映
- [T2: ③欄を実体験に差替え](https://github.com/sc30gsw/claude-code-customes/issues/13) — G1〜G3の実体験を反映、公称値は参考ラベル化
- [T3: wayfinder目玉化](https://github.com/sc30gsw/claude-code-customes/issues/14) — 04にlife-pulseケーススタディ＋業界文脈を追加
- [T4: 発表台本作成](https://github.com/sc30gsw/claude-code-customes/issues/15) — 10-presentation-script.md 作成
- [T5: Notion最終磨き](https://github.com/sc30gsw/claude-code-customes/issues/16) — 00更新・全体整合

## Not yet specified

（なし — 目的地までの判断を完了した）

## Out of scope

- Notionへの実際のアップロード作業（ユーザーが手動で実施すると明言）
- Notion移行後のページ構造の設計（フラット vs DB化）
- wayfinderライブデモ用プロジェクトの用意（ユーザーが自分で作ると明言）
- 共有会当日の他メンバー向け資料・議事録
- 新規スキル/プラグインの作成や導入検証

---

🏁 **Status: Destination reached（2026-08-10）** — 全16チケットクローズ。ドキュメント11ファイルが最終版（[docs/ai-share-session/](https://github.com/sc30gsw/claude-code-customes/tree/main/docs/ai-share-session)）。ローカル版マップ: [wayfinder/MAP.md](https://github.com/sc30gsw/claude-code-customes/blob/main/docs/ai-share-session/wayfinder/MAP.md)
