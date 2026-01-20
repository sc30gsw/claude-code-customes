# Smart Think Command

## 概要

Sequential Thinking MCPとSerenaを統合した高度なマルチモード思考システム。複雑な問題解決のために段階的な推論を提供します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/smart-think` |
| 引数 | `<problem_description>` |
| 用途 | 複雑な問題分析、設計検討 |
| 許可ツール | すべてのツール |

## 思考モード

### 1. think（標準）
- 基本的な段階的推論
- 3-5ステップの分析
- 一般的な問題解決に適用

### 2. think-hard
- より深い分析
- 5-8ステップの推論
- 中程度の複雑さの問題向け

### 3. think-harder
- 徹底的な調査
- 8-12ステップの分析
- 複雑なアーキテクチャ問題向け

### 4. ultrathink
- 最大限の深い思考
- 12-20ステップの推論
- 非常に複雑な問題向け

## 使用例

```bash
# 標準的な思考
/smart-think "how to optimize this database query"

# 深い分析
/smart-think --think-hard "design authentication system"

# 徹底的な調査
/smart-think --ultrathink "analyze microservices architecture"
```

## 思考プロセス

1. **問題の分解** - 複雑な問題を小さな部分に分割
2. **仮説の生成** - 可能な解決策を列挙
3. **証拠の収集** - コードベースとドキュメントを調査
4. **仮説の検証** - 各アプローチを評価
5. **結論の導出** - 最適な解決策を提示

## Sequential Thinking MCP統合

```typescript
// 思考ステップの構造
{
  thought: "現在の分析内容",
  thoughtNumber: 1,
  totalThoughts: 5,
  nextThoughtNeeded: true,
  isRevision: false  // 以前の思考を修正する場合はtrue
}
```

## Serena統合

- **コードコンテキスト** - シンボル検索で関連コードを取得
- **メモリ活用** - 以前の分析結果を参照
- **パターン認識** - 類似問題の解決策を適用

## ベストプラクティス

1. **適切なモードを選択** - 問題の複雑さに応じて
2. **コンテキストを提供** - 関連ファイルや要件を明示
3. **段階的に進める** - 必要に応じてモードを上げる
4. **結論を検証** - 提案された解決策を確認
