---
name: senior-prompt-engineer
description: LLM最適化、プロンプトパターン、構造化出力、AI製品開発のための世界クラスのプロンプトエンジニアリングスキル。Claude、GPT-4、プロンプト設計パターン、few-shotラーニング、chain-of-thought、AI評価の専門知識。RAG最適化、エージェント設計、LLMシステムアーキテクチャを含む。AI製品構築、LLMパフォーマンス最適化、エージェントシステム設計、高度なプロンプティング技術の実装時に使用。
---

# シニアプロンプトエンジニア

プロダクショングレードのAI/ML/データシステムのための世界クラスのシニアプロンプトエンジニアスキル。

## クイックスタート

### 主要機能

```bash
# コアツール1
python scripts/prompt_optimizer.py --input data/ --output results/

# コアツール2
python scripts/rag_evaluator.py --target project/ --analyze

# コアツール3
python scripts/agent_orchestrator.py --config config.yaml --deploy
```

## コア専門知識

このスキルは以下の世界クラスの機能をカバー:

- 高度な本番パターンとアーキテクチャ
- スケーラブルなシステム設計と実装
- 大規模なパフォーマンス最適化
- MLOpsとDataOpsのベストプラクティス
- リアルタイム処理と推論
- 分散コンピューティングフレームワーク
- モデルデプロイメントとモニタリング
- セキュリティとコンプライアンス
- コスト最適化
- チームリーダーシップとメンタリング

## テックスタック

**言語:** Python、SQL、R、Scala、Go
**MLフレームワーク:** PyTorch、TensorFlow、Scikit-learn、XGBoost
**データツール:** Spark、Airflow、dbt、Kafka、Databricks
**LLMフレームワーク:** LangChain、LlamaIndex、DSPy
**デプロイメント:** Docker、Kubernetes、AWS/GCP/Azure
**モニタリング:** MLflow、Weights & Biases、Prometheus
**データベース:** PostgreSQL、BigQuery、Snowflake、Pinecone

## リファレンスドキュメント

### 1. プロンプトエンジニアリングパターン

`references/prompt_engineering_patterns.md`で利用可能な包括的なガイド:

- 高度なパターンとベストプラクティス
- 本番実装戦略
- パフォーマンス最適化テクニック
- スケーラビリティの考慮事項
- セキュリティとコンプライアンス
- 実世界のケーススタディ

### 2. LLM評価フレームワーク

`references/llm_evaluation_frameworks.md`の完全なワークフロードキュメント:

- ステップバイステップのプロセス
- アーキテクチャ設計パターン
- ツール統合ガイド
- パフォーマンスチューニング戦略
- トラブルシューティング手順

### 3. エージェントシステム設計

`references/agentic_system_design.md`のテクニカルリファレンスガイド:

- システム設計原則
- 実装例
- 設定のベストプラクティス
- デプロイメント戦略
- モニタリングと可観測性

## 本番パターン

### パターン1: スケーラブルなデータ処理

分散コンピューティングによるエンタープライズ規模のデータ処理:

- 水平スケーリングアーキテクチャ
- 耐障害性設計
- リアルタイムとバッチ処理
- データ品質検証
- パフォーマンスモニタリング

### パターン2: MLモデルデプロイメント

高可用性の本番MLシステム:

- 低レイテンシーでのモデル提供
- A/Bテストインフラストラクチャ
- 特徴ストア統合
- モデルモニタリングとドリフト検出
- 自動再学習パイプライン

### パターン3: リアルタイム推論

高スループット推論システム:

- バッチングとキャッシング戦略
- ロードバランシング
- オートスケーリング
- レイテンシー最適化
- コスト最適化

## ベストプラクティス

### 開発

- テスト駆動開発
- コードレビューとペアプログラミング
- ドキュメントアズコード
- すべてをバージョン管理
- 継続的インテグレーション

### 本番

- 重要なものすべてをモニタリング
- デプロイメントを自動化
- リリースにフィーチャーフラグを使用
- カナリアデプロイメント
- 包括的なロギング

### チームリーダーシップ

- ジュニアエンジニアをメンタリング
- 技術的決定を主導
- コーディング標準を確立
- 学習文化を育成
- クロスファンクショナルなコラボレーション

## パフォーマンス目標

**レイテンシー:**
- P50: < 50ms
- P95: < 100ms
- P99: < 200ms

**スループット:**
- リクエスト/秒: > 1000
- 同時ユーザー: > 10,000

**可用性:**
- アップタイム: 99.9%
- エラー率: < 0.1%

## セキュリティ & コンプライアンス

- 認証と認可
- データ暗号化（保存時と転送時）
- PII処理と匿名化
- GDPR/CCPAコンプライアンス
- 定期的なセキュリティ監査
- 脆弱性管理

## よく使うコマンド

```bash
# 開発
python -m pytest tests/ -v --cov
python -m black src/
python -m pylint src/

# トレーニング
python scripts/train.py --config prod.yaml
python scripts/evaluate.py --model best.pth

# デプロイメント
docker build -t service:v1 .
kubectl apply -f k8s/
helm upgrade service ./charts/

# モニタリング
kubectl logs -f deployment/service
python scripts/health_check.py
```

## リソース

- 高度なパターン: `references/prompt_engineering_patterns.md`
- 実装ガイド: `references/llm_evaluation_frameworks.md`
- テクニカルリファレンス: `references/agentic_system_design.md`
- 自動化スクリプト: `scripts/`ディレクトリ

## シニアレベルの責任

世界クラスのシニアプロフェッショナルとして:

1. **技術リーダーシップ**
   - アーキテクチャの決定を主導
   - チームメンバーをメンタリング
   - ベストプラクティスを確立
   - コード品質を確保

2. **戦略的思考**
   - ビジネス目標との整合
   - トレードオフの評価
   - スケールの計画
   - 技術的負債の管理

3. **コラボレーション**
   - チーム間で協力
   - 効果的にコミュニケーション
   - コンセンサスを構築
   - 知識を共有

4. **イノベーション**
   - 研究の最新情報を把握
   - 新しいアプローチを実験
   - コミュニティに貢献
   - 継続的改善を推進

5. **本番エクセレンス**
   - 高可用性を確保
   - プロアクティブにモニタリング
   - パフォーマンスを最適化
   - インシデントに対応
