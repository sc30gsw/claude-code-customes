# AI活用大共有会 — 発表資料 概要

> 【skills / plugin / MCP — AIをどう使っているか大共有会】向け発表ドキュメント。
> Notion移行前のMDドラフト。

## 共有会の目的

- 他の人がどんな skills / plugin / MCP を使っているかを知って、各々レベルアップ
- 業務に追われがちでなかなかできない新技術のキャッチアップを、強制的に時間を作ってガッツリやる

## 発表フォーマット（各アイテム共通）

1. **何を**（名前・自作か既製か）
2. **どの作業のために使っているか**
3. **入れる前と後で何が変わったか**（時間・回数・やめた手作業）

## 私の使い方の前提

**Claude Code本体の設定だけでかなりのことを賄う**方針（これが発表のテーゼ）。特に：

- **環境変数**（`ENABLE_TOOL_SEARCH=true` / `CLAUDE_CODE_NEW_INIT` / `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`）
- **Config**（Switch models when a message is flagged / Dynamic workflow size: unrestricted）
- **標準コマンド**（/init, /goal, /code-review, /loop, /deep-research など）

その上で、開発作業は **mattpocock-skills**（Grill-Driven Development）と **ECC** プラグインを軸に回す。
MCPは **Mintlify Index** と **context-mode** の2つだけに絞り、トークン管理は **RTK**（CLIプロキシ）とhookで機械化。

**発表の目玉は wayfinder**（→ [04](04-mattpocock-skills.md)、ライブデモ予定）。

## ドキュメント構成

| ファイル | 内容 |
|---|---|
| [01-environment-variables.md](01-environment-variables.md) | 環境変数3つ |
| [02-config.md](02-config.md) | /config 設定2つ |
| [03-commands.md](03-commands.md) | よく使う標準コマンド |
| [04-mattpocock-skills.md](04-mattpocock-skills.md) | mattpocock-skills / GDD / **wayfinder深掘り＋実例ケーススタディ（目玉）** |
| [05-mcp.md](05-mcp.md) | Mintlify Index / context-mode |
| [06-plugins.md](06-plugins.md) | 必須プラグイン + プロジェクト別プラグイン |
| [07-skills.md](07-skills.md) | mattpocock以外のスキル |
| [08-cli-tools.md](08-cli-tools.md) | CLIツール（**RTK** / react-doctor / evlog / agent-browser 等） |
| [09-cursor-plugins.md](09-cursor-plugins.md) | Cursor側（pstack / thermos） |
| [10-presentation-script.md](10-presentation-script.md) | **発表台本（20分・ライブデモ構成・想定質問）** |

> 制作メモ: 本資料はwayfinderのマップ（[wayfinder/MAP.md](wayfinder/MAP.md)）で作成。research 6本の裏取りと体験談グリルを経由しており、未検証情報には注記がある。マップ自体も「wayfinderの実物」として発表で見せられる。
