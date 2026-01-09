---
name: explain
description: "教育的明確さを備えたコード、コンセプト、システム動作の明確な説明提供"
category: workflow
complexity: standard
mcp-servers: [sequential, context7]
personas: [educator, architect, security]
---

# /sc:explain - コードとコンセプトの説明

## トリガー
- 複雑な機能のコード理解とドキュメントリクエスト
- アーキテクチャコンポーネントのシステム動作説明ニーズ
- 知識移転のための教育コンテンツ生成
- フレームワーク固有のコンセプト明確化要件

## 使用方法
```
/sc:explain [対象] [--level basic|intermediate|advanced] [--format text|examples|interactive] [--context domain]
```

## 動作フロー
1. **分析**: 包括的な理解のために対象コード、コンセプト、システムを調査
2. **評価**: オーディエンスレベルと適切な説明の深さとフォーマットの決定
3. **構造化**: プログレッシブな複雑さと論理的フローで説明シーケンスを計画
4. **生成**: 例、図、インタラクティブ要素を含む明確な説明の作成
5. **検証**: 説明の正確性と教育効果の確認

主要な動作:
- ドメイン専門知識のためのマルチペルソナ連携（educator、architect、security）
- Context7統合によるフレームワーク固有の説明
- 複雑なコンセプト分解のためのSequential MCPによる体系的分析
- オーディエンスと複雑さに基づく適応的な説明深度

## MCP統合
- **Sequential MCP**: 複雑なマルチコンポーネント分析と構造化推論の自動有効化
- **Context7 MCP**: フレームワークドキュメントと公式パターン説明
- **ペルソナ連携**: Educator（学習）、Architect（システム）、Security（プラクティス）

## ツール連携
- **Read/Grep/Glob**: 説明コンテンツのためのコード分析とパターン特定
- **TodoWrite**: 複雑なマルチパート説明の進捗追跡
- **Task**: 体系的な分解を必要とする包括的な説明ワークフローの委任

## 主要パターン
- **プログレッシブ学習**: 基本コンセプト → 中級詳細 → 高度な実装
- **フレームワーク統合**: Context7ドキュメント → 正確な公式パターンとプラクティス
- **マルチドメイン分析**: 技術的正確性 + 教育的明確さ + セキュリティ認識
- **インタラクティブ説明**: 静的コンテンツ → 例 → インタラクティブ探索

## 使用例

### 基本コード説明
```
/sc:explain authentication.js --level basic
# 初心者向けの実践的な例を含む明確な説明
# Educatorペルソナが学習最適化された構造を提供
```

### フレームワークコンセプト説明
```
/sc:explain react-hooks --level intermediate --context react
# 公式Reactドキュメントパターンのためのcontext7統合
# プログレッシブな複雑さを持つ構造化された説明
```

### システムアーキテクチャ説明
```
/sc:explain microservices-system --level advanced --format interactive
# Architectペルソナがシステム設計とパターンを説明
# Sequential分析分解によるインタラクティブ探索
```

### セキュリティコンセプト説明
```
/sc:explain jwt-authentication --context security --level basic
# Securityペルソナが認証コンセプトとベストプラクティスを説明
# 実践的な例を含むフレームワーク非依存のセキュリティ原則
```

## 境界

**対応範囲:**
- 教育的明確さを備えた明確で包括的な説明の提供
- ドメイン専門知識と正確な分析のための関連ペルソナの自動有効化
- 公式ドキュメント統合によるフレームワーク固有の説明の生成

**対応外:**
- 徹底的な分析と正確性検証なしの説明生成
- プロジェクト固有のドキュメント標準の上書きや機密詳細の公開
- 確立された説明検証や教育品質要件のバイパス
