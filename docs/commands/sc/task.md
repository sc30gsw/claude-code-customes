---
name: task
description: "インテリジェントなワークフロー管理と委任による複雑なタスクの実行"
category: special
complexity: advanced
mcp-servers: [sequential, context7, magic, playwright, morphllm, serena]
personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
---

# /sc:task - 高度タスク管理

## トリガー
- マルチエージェント連携と委任を必要とする複雑なタスク
- 構造化されたワークフロー管理とクロスセッション永続化を必要とするプロジェクト
- インテリジェントなMCPサーバールーティングとドメイン専門知識を必要とする操作
- 体系的な実行とプログレッシブな強化から恩恵を受けるタスク

## 使用方法
```
/sc:task [アクション] [ターゲット] [--strategy systematic|agile|enterprise] [--parallel] [--delegate]
```

## 動作フロー
1. **分析**: タスク要件を解析し最適な実行戦略を決定
2. **委任**: 適切なMCPサーバーにルーティングし関連ペルソナを有効化
3. **連携**: インテリジェントなワークフロー管理と並列処理でタスクを実行
4. **検証**: 品質ゲートと包括的なタスク完了検証を適用
5. **最適化**: パフォーマンスを分析し強化推奨事項を提供

主要な動作:
- architect、frontend、backend、security、devopsドメイン全体でのマルチペルソナ連携
- インテリジェントなMCPサーバールーティング（Sequential、Context7、Magic、Playwright、Morphllm、Serena）
- プログレッシブなタスク強化とクロスセッション永続化による体系的実行
- 階層的分解と依存関係管理による高度なタスク委任

## MCP統合
- **Sequential MCP**: 複雑なマルチステップタスク分析と体系的な実行計画
- **Context7 MCP**: フレームワーク固有のパターンと実装ベストプラクティス
- **Magic MCP**: UI/UXタスク連携とデザインシステム統合
- **Playwright MCP**: テストワークフロー統合と検証自動化
- **Morphllm MCP**: 大規模タスク変換とパターンベースの最適化
- **Serena MCP**: クロスセッションタスク永続化とプロジェクトメモリ管理

## ツール連携
- **TodoWrite**: Epic → Story → Taskレベル全体での階層的タスク分解と進捗追跡
- **Task**: 複雑なマルチエージェント連携とサブタスク管理のための高度な委任
- **Read/Write/Edit**: タスクドキュメントと実装連携
- **sequentialthinking**: 複雑なタスク依存関係分析のための構造化された推論

## 主要パターン
- **タスク階層**: Epicレベル目標 → Story連携 → Task実行 → Subtask粒度
- **戦略選択**: Systematic（包括的） → Agile（反復的） → Enterprise（ガバナンス）
- **マルチエージェント連携**: ペルソナ有効化 → MCPルーティング → 並列実行 → 結果統合
- **クロスセッション管理**: タスク永続化 → コンテキスト継続性 → プログレッシブ強化

## 使用例

### 複雑な機能開発
```
/sc:task create "エンタープライズ認証システム" --strategy systematic --parallel
# マルチドメイン連携による包括的なタスク分解
# architect、security、backend、frontendペルソナを有効化
```

### アジャイルスプリント連携
```
/sc:task execute "機能バックログ" --strategy agile --delegate
# インテリジェントな委任による反復的タスク実行
# スプリント継続性のためのクロスセッション永続化
```

### マルチドメイン統合
```
/sc:task execute "マイクロサービスプラットフォーム" --strategy enterprise --parallel
# コンプライアンス検証付きのエンタープライズ規模連携
# 複数の技術ドメイン間での並列実行
```

## 境界

**対応範囲:**
- マルチエージェント連携とインテリジェントな委任による複雑なタスクの実行
- クロスセッション永続化を備えた階層的タスク分解の提供
- 最適なタスク結果のための複数MCPサーバーとペルソナの連携

**対応外:**
- 高度なオーケストレーションを必要としない単純タスクの実行
- 速度や利便性のための品質標準の妥協
- 適切な検証と品質ゲートなしでの操作
