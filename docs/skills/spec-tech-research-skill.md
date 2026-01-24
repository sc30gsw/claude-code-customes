# Spec Tech Research Skill

## 概要

拡張思考モードとMCP統合による高度な技術調査コマンド。包括的な分析のための複数の思考深度、信頼度スコアリング、ダイアグラム生成をサポートします。

## アクティベーショントリガー

- 技術選定の調査が必要な時
- フレームワークやライブラリの比較時
- アーキテクチャパターンの調査時
- 最新技術トレンドの把握時

## 使用方法

```bash
/spec:tech-research "<topic>" [options]
```

## 思考モード

| モード | トークンバジェット | 深度 | ユースケース |
|--------|------------------|------|-------------|
| `think` | 10,000 | 標準 | クイック調査、概要 |
| `think-hard` | 20,000 | 強化 | 詳細比較 |
| `think-harder` | 30,000 | 構造化 | 複雑なトピック、意思決定 |
| `ultrathink` | 50,000 | 最大 | 重大な分析、学術的 |

## コアオプション

| オプション | 短縮形 | 説明 | 例 |
|------------|--------|------|-----|
| `--mode` | `-m` | 思考モード | `-m ultrathink` |
| `--budget` | `-b` | トークンバジェット | `-b 25000` |
| `--output` | `-o` | 出力ファイル | `-o analysis.md` |
| `--format` | `-f` | 出力形式 | `-f json` |
| `--mcp` | | 使用するMCPツール | `--mcp "context7,sequential"` |

## リサーチオプション

| オプション | 短縮形 | 説明 | 例 |
|------------|--------|------|-----|
| `--depth` | `-d` | 検索深度 | `-d deep` |
| `--template` | `-t` | レポートテンプレート | `-t academic` |
| `--confidence` | `-c` | 信頼度閾値 (0-1) | `-c 0.9` |
| `--sources` | | 引用を含む | `--sources` |
| `--diagrams` | | ダイアグラム生成 | `--diagrams` |
| `--language` | `-l` | 出力言語 | `-l ja` |

## Serena MCPツール優先

### コードベースインテリジェンス
- `mcp__serena__search_for_pattern` - 実装パターン検索
- `mcp__serena__find_symbol` - アーキテクチャ理解
- `mcp__serena__get_symbols_overview` - アーキテクチャ認識推奨
- `mcp__serena__read_memory` / `write_memory` - 調査継続性

### リサーチ強化（他MCP）
- `mcp__context7__resolve-library-id` - ライブラリドキュメント
- `mcp__sequential-thinking__sequentialthinking` - 複雑な分析

## テンプレート

| テンプレート | 説明 |
|--------------|------|
| `overview` | キーポイント付きクイックサマリー |
| `comprehensive` | 全側面のフル分析 |
| `academic` | 引用付き研究論文形式 |
| `technical` | コード付き実装フォーカス |

## 使用例

```bash
# クイック概要
/spec:tech-research "Redis vs Memcached" -d quick -t overview

# ディープフレームワーク分析
/spec:tech-research "React architecture patterns" -m think-harder -t comprehensive --diagrams

# 高信頼度セキュリティリサーチ
/spec:tech-research "Zero-trust security model" -m ultrathink -c 0.95 --sources

# 実装リサーチ
/spec:tech-research "Implementing OAuth 2.0 with PKCE" -t technical -m think-hard

# コードベース認識リサーチ
/spec:tech-research "State management options" --mcp "serena,context7" --codebase-context

# 日本語技術ドキュメント
/spec:tech-research "Docker コンテナ化" -l ja -t technical
```

## 出力構造

```markdown
# Technical Research Report: [Topic]

## Executive Summary
- キー発見と推奨

## Table of Contents
1. Introduction
2. Core Concepts
3. Technical Analysis
4. Implementation Considerations
5. Best Practices
6. Comparisons
7. Recommendations
8. Conclusion
9. References

## Confidence Scores
- Finding 1: 95% confidence
- Finding 2: 88% confidence
```

## 出力例

```markdown
# Technical Research Report: React State Management

## Executive Summary
React state management options analyzed with focus on scalability and developer experience.

## Confidence Score: 92%

## Options Analyzed

### Redux
- **Maturity**: 9/10
- **Performance**: 8/10
- **Learning Curve**: 6/10
- **TypeScript Support**: 9/10

### Zustand
- **Maturity**: 7/10
- **Performance**: 9/10
- **Learning Curve**: 9/10
- **TypeScript Support**: 10/10

### Jotai
- **Maturity**: 7/10
- **Performance**: 9/10
- **Learning Curve**: 8/10
- **TypeScript Support**: 10/10

## Recommendation
For new projects with TypeScript: **Zustand**
For large enterprise applications: **Redux Toolkit**

## References
- [Redux Documentation](https://redux.js.org/)
- [Zustand GitHub](https://github.com/pmndrs/zustand)
```

## 他コマンドとの統合

リサーチ結果は以下と使用可能:
- `/serena` - 実装用
- `/debug-error` - コンテキスト用
- `/smart-think` - 意思決定用
- `/spec:requirements` - 要件定義用

## ベストプラクティス

1. **適切なモード選択** - トピックの複雑さに応じて
2. **信頼度閾値設定** - 重要な決定には高い閾値
3. **ソース引用** - 検証可能性のため
4. **ダイアグラム活用** - 複雑な関係を可視化
5. **出力保存** - 重要な調査は保存

## 成功指標

- トピックが包括的にカバーされる
- 信頼度スコアが適切
- 比較が明確
- 推奨が具体的
- 参考資料が含まれる
