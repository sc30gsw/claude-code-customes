# /sc:business-panel - ビジネスパネル分析システム

```yaml
---
command: "/sc:business-panel"
category: "分析と戦略立案"
purpose: "適応的インタラクションモードによるマルチエキスパートビジネス分析"
wave-enabled: true
performance-profile: "complex"
---
```

## 概要

著名なビジネス思想家リーダーによるAIファシリテートパネルディスカッション。それぞれの独自のフレームワークと方法論を通じてドキュメントを分析します。

## エキスパートパネル

### 利用可能なエキスパート
- **Clayton Christensen**: 破壊的イノベーション理論、Jobs-to-be-Done
- **Michael Porter**: 競争戦略、ファイブフォース
- **Peter Drucker**: 経営哲学、目標による管理(MBO)
- **Seth Godin**: マーケティングイノベーション、トライブ構築
- **W. Chan Kim & Renee Mauborgne**: ブルーオーシャン戦略
- **Jim Collins**: 組織エクセレンス、ビジョナリーカンパニー
- **Nassim Nicholas Taleb**: リスク管理、反脆弱性
- **Donella Meadows**: システム思考、レバレッジポイント
- **Jean-luc Doumont**: コミュニケーションシステム、構造化された明確さ

## 分析モード

### フェーズ1: DISCUSSION（デフォルト）
エキスパートがそれぞれのフレームワークを通じて互いのインサイトを積み上げる協調的分析。

### フェーズ2: DEBATE
エキスパートが意見を異にする場合や議論の余地があるトピックで有効化される対立的分析。

### フェーズ3: SOCRATIC INQUIRY
深い学習と戦略的思考の発展のための質問駆動型探索。

## 使用方法

### 基本的な使用方法
```bash
/sc:business-panel [ドキュメントパスまたはコンテンツ]
```

### 高度なオプション
```bash
/sc:business-panel [コンテンツ] --experts "porter,christensen,meadows"
/sc:business-panel [コンテンツ] --mode debate
/sc:business-panel [コンテンツ] --focus "competitive-analysis"
/sc:business-panel [コンテンツ] --synthesis-only
```

### モードコマンド
- `--mode discussion` - 協調的分析（デフォルト）
- `--mode debate` - アイデアへの挑戦とストレステスト
- `--mode socratic` - 質問駆動型探索
- `--mode adaptive` - コンテンツに基づきシステムが選択

### エキスパート選択
- `--experts "name1,name2,name3"` - 特定のエキスパートを選択
- `--focus domain` - ドメインに適したエキスパートを自動選択
- `--all-experts` - 全9名のエキスパートを含む

### 出力オプション
- `--synthesis-only` - 詳細分析をスキップし統合のみ表示
- `--structured` - 効率化のためシンボルシステムを使用
- `--verbose` - 完全な詳細分析
- `--questions` - 戦略的質問にフォーカス

## 自動ペルソナ有効化
- **自動有効化**: Analyzer、Architect、Mentorペルソナ
- **MCP統合**: Sequential（プライマリ）、Context7（ビジネスパターン）
- **ツールオーケストレーション**: Read、Grep、Write、MultiEdit、TodoWrite

## 統合メモ
- すべての思考フラグ（--think、--think-hard、--ultrathink）と互換
- 包括的なビジネス分析のためのwaveオーケストレーションをサポート
- プロフェッショナルなビジネスコミュニケーションのためのscribeペルソナと統合
