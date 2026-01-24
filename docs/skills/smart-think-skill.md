# Smart Think Skill

## 概要

Sequential Thinking MCPとSerena統合による高度なマルチモード思考システム。複雑な問題解決のために、複数の思考モード、バジェット制御、MCP統合を提供します。

## アクティベーショントリガー

- 複雑な技術的意思決定が必要な時
- アーキテクチャ設計の検討時
- 複数の選択肢を比較分析したい時
- 深い思考と研究が必要な問題

## 使用方法

```bash
/smart-think "<problem_description>" [options]
```

## オプション

| オプション | 短縮形 | 説明 | デフォルト |
|------------|--------|------|-----------|
| `--mode` | `-m` | 思考モード | `think` |
| `--budget` | `-b` | トークンバジェット | 自動 |
| `--interactive` | `-i` | インタラクティブな改善 | false |
| `--output` | `-o` | ファイルに保存 | なし |
| `--serena` | `-s` | Serena統合を使用 | false |
| `--research` | `-r` | リサーチフェーズを含む | false |
| `--citations` | `-c` | 引用を含む | false |
| `--structured` | | 構造化出力 | false |
| `--confidence` | | 信頼度レベルを表示 | false |
| `--focus` | `-f` | フォーカスエリア | なし |

## 思考モード

| モード | バジェット範囲 | 思考数 | 信頼度 | 最適な用途 |
|--------|---------------|--------|--------|-----------|
| `think` | 2,000-8,000 | 3-6 | 70-85% | 迅速な意思決定 |
| `think-hard` | 8,000-15,000 | 6-10 | 75-90% | 複雑な分析 |
| `think-harder` | 15,000-25,000 | 10-15 | 80-95% | アーキテクチャ決定 |
| `ultrathink` | 25,000-50,000 | 15-25 | 85-98% | 研究、複雑システム |

## MCPツール優先

### プライマリ思考エンジン (Sequential Thinking MCP)
- `mcp__sequential-thinking__sequentialthinking` - メイン思考ツール
- 複数の解決仮説を生成・テスト
- 信頼度追跡付き推論チェーンを構築

### コードベースインテリジェンス (Serena MCP - --serenaフラグ時)
- `mcp__serena__get_symbols_overview` - 技術的理解
- `mcp__serena__search_for_pattern` - 実装インサイト
- `mcp__serena__read_memory` / `write_memory` - 意思決定の継続性

## 使用例

```bash
# デフォルト思考モード
/smart-think "Should we use Redux or Zustand?"

# コードベースコンテキスト付き深層分析
/smart-think "Database migration strategy" -m think-harder --serena

# 引用付きリサーチフォーカス
/smart-think "Technology selection" -m ultrathink --research --citations

# バジェット制御付き迅速な意思決定
/smart-think "CSS framework choice" -b 5000 --focus=frontend
```

## モード選択ガイドライン

1. **Think**: 迅速な意思決定、シンプルな問題、時間制約
2. **Think-Hard**: 重要な意思決定、中程度の複雑さ
3. **Think-Harder**: 重大な意思決定、高い複雑さ
4. **UltraThink**: ミッションクリティカル、研究レベルの分析

## 出力形式

### デフォルト形式
- Problem Analysis（問題分析）
- Solution Exploration（解決策探索）
- Recommendation（推奨）
- Next Steps（次のステップ）

### リサーチ形式（--research付き）
- Executive Summary（エグゼクティブサマリー）
- Literature Review（文献レビュー）
- Technical Analysis（技術分析）
- Recommendations（推奨事項）
- References（参考文献）

### テクニカル形式（--serena付き）
- Technical Context（技術コンテキスト）
- Code Analysis（コード分析）
- Architecture Implications（アーキテクチャへの影響）
- Implementation Strategy（実装戦略）

## 出力例

```markdown
# Analysis: Redux vs Zustand

## Problem Analysis
State management library selection for React application

## Confidence: 85%

## Options Explored

### Option 1: Redux
- **Pros**: Mature ecosystem, DevTools, Middleware
- **Cons**: Boilerplate, Learning curve
- **Fit Score**: 7/10

### Option 2: Zustand
- **Pros**: Simple API, TypeScript, Minimal boilerplate
- **Cons**: Smaller ecosystem
- **Fit Score**: 8/10

## Recommendation
Zustand for medium-sized applications with TypeScript

## Next Steps
1. Prototype with Zustand
2. Evaluate performance
3. Document patterns
```

## ベストプラクティス

1. **問題を明確に** - 具体的な問題記述
2. **適切なモード選択** - 複雑さに応じたモード
3. **コンテキスト提供** - --serenaでコードベース理解
4. **フォーカス設定** - 関連領域を指定
5. **出力を保存** - 重要な分析は--outputで保存

## 成功指標

- 問題が明確に分析される
- 複数の選択肢が比較される
- 信頼度が適切に評価される
- 推奨事項が具体的
- 次のステップが明確
