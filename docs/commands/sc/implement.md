---
name: implement
description: "インテリジェントなペルソナ有効化とMCP統合による機能・コード実装"
category: workflow
complexity: standard
mcp-servers: [context7, sequential, magic, playwright]
personas: [architect, frontend, backend, security, qa-specialist]
---

# /sc:implement - 機能実装

> **コンテキストフレームワーク注記**: この動作指示は、Claude Codeユーザーが`/sc:implement`パターンを入力した際に有効化されます。包括的な実装のために専門ペルソナとMCPツールを連携するようClaudeをガイドします。

## トリガー
- コンポーネント、API、完全な機能の機能開発リクエスト
- フレームワーク固有の要件を持つコード実装ニーズ
- 連携された専門知識を必要とするマルチドメイン開発
- テストと検証統合を必要とする実装プロジェクト

## コンテキストトリガーパターン
```
/sc:implement [機能説明] [--type component|api|service|feature] [--framework react|vue|express] [--safe] [--with-tests]
```
**使用方法**: Claude Codeの会話でこれを入力すると、連携された専門知識と体系的な開発アプローチを備えた実装動作モードが有効になります。

## 動作フロー
1. **分析**: 実装要件の調査とテクノロジーコンテキストの検出
2. **計画**: アプローチの選択とドメイン専門知識のための関連ペルソナの有効化
3. **生成**: フレームワーク固有のベストプラクティスによる実装コードの作成
4. **検証**: 開発全体でセキュリティと品質検証の適用
5. **統合**: ドキュメントの更新とテスト推奨事項の提供

主要な動作:
- コンテキストベースのペルソナ有効化（architect、frontend、backend、security、qa）
- Context7とMagic MCP統合によるフレームワーク固有の実装
- Sequential MCPによる体系的なマルチコンポーネント連携
- Playwrightによる包括的なテスト統合と検証

## MCP統合
- **Context7 MCP**: React、Vue、Angular、Express向けのフレームワークパターンと公式ドキュメント
- **Magic MCP**: UIコンポーネント生成とデザインシステム統合の自動有効化
- **Sequential MCP**: 複雑なマルチステップ分析と実装計画
- **Playwright MCP**: テスト検証と品質保証統合

## ツール連携
- **Write/Edit/MultiEdit**: 実装のためのコード生成と修正
- **Read/Grep/Glob**: 一貫性のためのプロジェクト分析とパターン検出
- **TodoWrite**: 複雑なマルチファイル実装の進捗追跡
- **Task**: 体系的な連携を必要とする大規模機能開発の委任

## 主要パターン
- **コンテキスト検出**: フレームワーク/技術スタック → 適切なペルソナとMCP有効化
- **実装フロー**: 要件 → コード生成 → 検証 → 統合
- **マルチペルソナ連携**: Frontend + Backend + Security → 包括的なソリューション
- **品質統合**: 実装 → テスト → ドキュメント → 検証

## 使用例

### Reactコンポーネント実装
```
/sc:implement ユーザープロファイルコンポーネント --type component --framework react
# Magic MCPがデザインシステム統合によるUIコンポーネントを生成
# Frontendペルソナがベストプラクティスとアクセシビリティを確保
```

### APIサービス実装
```
/sc:implement ユーザー認証API --type api --safe --with-tests
# Backendペルソナがサーバーサイドロジックとデータ処理を担当
# Securityペルソナが認証ベストプラクティスを確保
```

### フルスタック機能
```
/sc:implement 決済処理システム --type feature --with-tests
# マルチペルソナ連携: architect、frontend、backend、security
# Sequential MCPが複雑な実装ステップを分解
```

### フレームワーク固有実装
```
/sc:implement ダッシュボードウィジェット --framework vue
# Context7 MCPがVue固有のパターンとドキュメントを提供
# 公式ベストプラクティスによるフレームワーク適切な実装
```

## 境界

**対応範囲:**
- インテリジェントなペルソナ有効化とMCP連携による機能実装
- フレームワーク固有のベストプラクティスとセキュリティ検証の適用
- テストとドキュメント統合を含む包括的な実装の提供

**対応外:**
- 適切なペルソナ相談なしのアーキテクチャ決定
- セキュリティポリシーやアーキテクチャ制約に矛盾する機能の実装
- ユーザー指定の安全制約の上書きや品質ゲートのバイパス
