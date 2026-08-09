# Cursorプラグイン

コーディング作業ではCursorも併用。[cursor/plugins](https://github.com/cursor/plugins) に依存している。

---

## 1. pstack（既製・Cursor公式plugins）

- **リポジトリ**: [cursor/plugins — pstack](https://github.com/cursor/plugins/tree/main/pstack)
- **マーケットプレイス**: [cursor.com/marketplace/cursor/pstack](https://cursor.com/marketplace/cursor/pstack)（インストールするとスキルの自動更新が効く）

### 何を
多数のスラッシュスキルの集合プラグイン（`/poteto-mode` がデフォルトエントリポイント。`/how` `/why` `/blast-radius` `/architect` `/arena` `/swarm` `/interrogate` `/tdd` `/no-comments` など多数）。「計画系スキルは意図的に含まない」という思想。

### 特に推奨されている2スキル（作者poteto氏の[推奨ポスト](https://x.com/poteto/status/2082874054483255805)）

#### `/create-verification-skill`
- **SKILL.md**: [create-verification-skill](https://github.com/cursor/plugins/blob/main/pstack/skills/create-verification-skill/SKILL.md)

**エージェントに「自分のアプリの動かし方・操作方法・デバッグ方法」を教えるスキルを生成する**スキル。5段階：

1. リポジトリを（ユーザーではなく）インタビュー＝コードから機能を推測
2. 検証スキル自体を生成
3. **フィーチャーマップ（feature map）の種を作る** — アプリの全機能を「ユーザー視点で」記述したマップ。機能ごとに `Sub-features` / `How to get to it (user POV)` / `Driving it with ` / `Gotchas` の4見出しで、その機能への到達方法・操作方法・何が観測できれば動作証明になるかを記録
4. 生成したスキルを自分で証明・検証してから納品
5. メンテナンスループ（下記）を提案

フィーチャーマップにより、**エージェントが実ユーザーと同じようにアプリをナビゲート・操作でき、自分の作業を自分で検証する能力が大幅に上がる**。

#### `/maintain-verification-skill`
- **SKILL.md**: [maintain-verification-skill](https://github.com/cursor/plugins/blob/main/pstack/skills/maintain-verification-skill/SKILL.md)

「フィーチャーマップはアプリが変わった瞬間に腐る」前提で、既存の検証スキル＋フィーチャーマップを**監査・修正する**スキル。機能ごとの並列ソースリーダー＋全機能を駆動する1つのライブセッション＋証明済み修正のPRは最大1件、という構成。

作者の推奨運用：**Cursor cloud agentsのdaily automationとして毎日実行**し、フィーチャーマップを常に最新に保つ。「強い検証スキルはチームのクリティカルなインフラになり、生産性と品質向上の基盤になる」。

> 裏取り済み: この運用は[作者のXポスト](https://x.com/poteto/status/2082874054483255805)由来でSKILL.md本体には記載なし。ただし土台となるCursorの[Automations機能](https://cursor.com/docs/cloud-agent/automations)（スケジュールトリガー／cron式指定）は公式ドキュメントに実在し、技術的に成立する。

### 入れる前と後
- **前**: エージェントは「コードを書けるが、書いたものが動くか自分で確かめられない」。検証は人間の手動確認
- **後**: エージェントがユーザー視点でアプリを操作して自己検証。検証の起点となるフィーチャーマップは日次自動化で鮮度維持

---

## 2. thermos（既製・Cursor公式plugins）

- **リポジトリ**: [cursor/plugins — thermos](https://github.com/cursor/plugins/tree/main/thermos)

### 何を
「**thermo-nuclear branch review**」プラグイン。深い正しさ・セキュリティ監査と、厳格な保守性ルーブリックを、**並列サブエージェントのオーケストレーション**で実行する。

構成：

| スキル | 観点 |
|---|---|
| `thermo-nuclear-review` | バグ・破壊的変更・セキュリティ・devex・フィーチャーゲート漏れの深いブランチ監査 |
| `thermo-nuclear-code-quality-review` | 1000行ルール・スパゲッティ・境界違反などの厳格な保守性監査 |
| `thermos` | 上記2つのサブエージェントを並列実行し、優先度付け・重複排除して統合 |

典型フロー：`git diff main...HEAD` ＋変更ファイル全文を収集 → 両サブエージェントを同時起動 → 統合レポート。

### どの作業のために
レビュー時。特にブランチ全体の変更をマージ前に叩きたい時。

### 入れる前と後
- **前**: 人間レビュアー1人が「正しさ」と「保守性」の両観点を順番に見る（観点の抜け漏れが出る）
- **後**: 2つの専門サブエージェントが並列で観点を分担し、統合レポートで受け取れる
