# スキル（mattpocock以外）

mattpocock-skills（→ [04-mattpocock-skills.md](04-mattpocock-skills.md)）以外で使っているスキル群。

---

## 必須スキル

### 1. react-stinky（既製）

- **リポジトリ**: [saschb2b/skills — react-stinky](https://github.com/saschb2b/skills/blob/main/skills/engineering/react-stinky/SKILL.md)

#### 何を
React/TypeScriptコードの「保守性の悪臭（smell）」を検出し、コスト説明＋出典リンク＋修正案付きでレポートするレビュー用スキル。

#### どの作業のために
Reactコンポーネント/フックのレビュー・保守性監査。9つの柱で体系的にチェックする：

1. **Component APIとprops**（18サブカテゴリ — boolean乱立の代わりのunion variant、discriminated union、controlled/uncontrolled、Styles API等）
2. **Stateとデータフロー**（導出可能な値のuseState保持、props→stateコピー、prop drilling、stale closure、god context）
3. **Effectsとライフサイクル**（イベントハンドラ代替のeffect、クリーンアップ漏れのfetch/timer、依存配列の不整合）
4. **コンポーネント構造とhooks**（god component、コンポーネント内定義コンポーネント、条件付きhooks）
5. **レンダリング正確性**（index key、mutation、`&&` の "leaked 0" バグ）
6. アクセシビリティとフォーカス管理
7. 非同期ハンドラ
8. エラーバウンダリ / dangerouslySetInnerHTML / TypeScript規律
9. クロスファイル重複（フォルダ/リポジトリスコープ時）

特徴：**「Don't flag」免除ルール**を持ち誤検知を抑制（MUIの`open`/`sx`、Radixの`asChild`等の確立された規約は許容）。重大度は「Rancid / Funky」等のStink ratingで表現。メモ化・再レンダー性能は別スキルへ委譲する責務分離設計。

#### 入れる前と後
- **前**: prop設計の悪習慣やeffect誤用が目視レビューで見逃されがち。観点が属人的
- **後**: 9カテゴリの体系チェックで観点の抜け漏れが消える。`[Rancid] clickable-nonsemantic (a11y markup), line 297` のような行番号付き構造化レポートが出る

---

### 2. find-docs + context7 CLI（既製）

- **スキル**: [skills.sh — upstash/context7/find-docs](https://www.skills.sh/upstash/context7/find-docs)
- **CLI**: [context7 CLI ドキュメント](https://context7.com/docs/clients/cli)

#### 何を
任意のライブラリの**最新ドキュメント・コード例を取得する**スキル。実体はContext7の `ctx7` CLIの薄いラッパーで、MCPサーバー不要：

```bash
npx ctx7@latest library react
```

```bash
npx ctx7@latest docs /facebook/react "How to use hooks for state management"
```

`ctx7 setup` で **MCPサーバーモード**（`--mcp`）と **CLI+Skillsモード**（`--cli`）を選択可能。CLI+Skillsモードなら `~/.claude/skills` にdocsスキルがインストールされ、MCPを常設せずに済む。

#### どの作業のために
最新API仕様・バージョン移行の確認。学習データの鮮度に依存しない実装をするため。

#### 入れる前と後
- **前**: LLMの学習データ依存で、最新APIやバージョン差分の誤情報リスク
- **後**: 常に最新ドキュメントをその場で取得。**MCPサーバーを増やさずに**（=コンテキストを消費せずに）docs参照ができるのがポイント

---

### 3. human-review（既製）

- **リポジトリ**: [petergyang/human-review](https://github.com/petergyang/human-review)

#### 何を
HTML/Markdownファイル（またはlocalhostのページ）を**Googleドキュメントのように視覚的に編集・コメントし、フィードバックを一括でAIに送り返す**ビジュアルレビューツール。アカウント・クラウド・APIキー不要の完全ローカル実行。

#### どの作業のために
`/human-review <ファイルパス or localhost URL>` でブラウザにエディタが開く。テキスト編集・画像操作・ブロック並べ替え・フレーズ選択コメントができ、「Send」で全編集・コメントが一括でエージェントに送られ、エージェントがソースを更新する。AI生成のプラン・LP・ドキュメントの修正指示に使う。

#### 入れる前と後
- **前**: フィードバックをチャットで長文説明。「あの部分のあれ」の齟齬が頻発
- **後**: 対象箇所に直接コメントが紐づくので解釈ミスが激減。チャットでの位置説明という手作業をやめた

---

## プロジェクト別

### mantinedev/skills（既製・Mantine公式）

- **リポジトリ**: [mantinedev/skills](https://github.com/mantinedev/skills)

Mantine公式のスキル集。現時点で3スキル：

| スキル | 用途 |
|---|---|
| `mantine-custom-components` | `factory()` / Styles API / `createVarsResolver` を使ったMantine流カスタムコンポーネント構築 |
| `mantine-form` | `@mantine/form`（useForm・バリデーション・ネストfield・uncontrolledモード） |
| `mantine-combobox` | Comboboxプリミティブでのカスタムselect/autocomplete/multiselect構築 |

インストール: `npx skills add https://github.com/mantinedev/skills --skill `

**前後の変化**: Mantine内部APIを都度ドキュメント確認 → 公式パターンに沿った実装から逸脱しなくなる。

### autoskills（既製ツール）

- **サイト**: [autoskills.sh](https://www.autoskills.sh/)

プロジェクトの技術スタックを自動検出し、**最適なスキルを自動インストールする**CLI。`npx autoskills` 一発で:

1. `package.json` 等をスキャンしてスタック検出
2. **監査済みキュレーションレジストリ**経由でスキル選定（upstream直ではない）
3. SHA-256ハッシュ照合してからインストール（改ざん検知）

`--dry-run` で一覧確認のみも可能。TypeScript→`typescript-advanced-types`、React→`react-best-practices`、Next.js→`next-best-practices` など多数のスタックに対応。

**前後の変化**: スキルを1つずつ探して入れる手作業 → スタック検出で一括、かつsupply-chainリスクも抑制。

---

## 参考：チームナレッジ（enechange/claude-code-knowledge の evp-frontend）

> [enechange/claude-code-knowledge](https://github.com/enechange/claude-code-knowledge/tree/main/plugins/evp-frontend)（社内リポジトリ）

チームで整備しているスキル群。カテゴリ別：

**テスト・ブラウザ系**: vitest / playwright-cli / agent-browser / playwright-best-practices

**実装パターン系**: tailwind-css-patterns / typescript-advanced-types / react-grab / nodejs-best-practices / nodejs-backend-patterns / better-result-adopt / oxlint

**デザイン・UX系**: emil-design-eng / improve-animations / review-animations / make-interfaces-feel-better / fixing-accessibility / accessibility / seo / web-design-guidelines / web-perf
