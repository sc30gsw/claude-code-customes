# パフォーマンス最適化

パフォーマンスに関するルールです。

## モデル選択戦略

### Haiku 4.5 (Sonnetの90%能力、3倍のコスト削減)

用途:
- 頻繁に呼び出される軽量エージェント
- ペアプログラミングとコード生成
- マルチエージェントシステムのワーカーエージェント

### Sonnet 4.5 (最高のコーディングモデル)

用途:
- メイン開発作業
- マルチエージェントワークフローのオーケストレーション
- 複雑なコーディングタスク

### Opus 4.5 (最深の推論)

用途:
- 複雑なアーキテクチャ決定
- 最大限の推論が必要な場合
- リサーチと分析タスク

## コンテキストウィンドウ管理

### コンテキストの最後20%を避けるタスク

- 大規模リファクタリング
- 複数ファイルにまたがる機能実装
- 複雑なインタラクションのデバッグ

### コンテキスト感度が低いタスク

- 単一ファイル編集
- 独立したユーティリティ作成
- ドキュメント更新
- シンプルなバグ修正

## Ultrathink + Planモード

深い推論が必要な複雑なタスクに:

1. `ultrathink` で強化された思考を使用
2. **Planモード** で構造化アプローチを有効化
3. 複数の批評ラウンドで「エンジンを回す」
4. 多様な分析のために分割ロールサブエージェントを使用

## ビルドトラブルシューティング

ビルドが失敗した場合:

1. **build-error-resolver** エージェントを使用
2. エラーメッセージを分析
3. 段階的に修正
4. 各修正後に検証

## React/Next.js パフォーマンス

### レンダリング最適化

```typescript
// メモ化を使用
const MemoizedComponent = React.memo(ExpensiveComponent)

// useMemoで計算をキャッシュ
const expensiveValue = useMemo(() => computeExpensive(data), [data])

// useCallbackで関数をメモ化
const handleClick = useCallback(() => {
  doSomething(id)
}, [id])
```

### バンドル最適化

```typescript
// 動的インポート
const HeavyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <Skeleton />,
  ssr: false
})

// バレルインポートを避ける
// ❌ import { Button, Input } from '@/components'
// ✅ import { Button } from '@/components/Button'
```

### データフェッチング

```typescript
// 並列データフェッチ
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts()
])

// SWRでデータキャッシュ
const { data, error } = useSWR('/api/user', fetcher)
```

## データベースパフォーマンス

```sql
-- インデックスを適切に使用
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- N+1問題を避ける
SELECT posts.*, users.name
FROM posts
JOIN users ON posts.user_id = users.id;
```

## 監視指標

| 指標 | 目標 |
|-----|------|
| LCP | < 2.5s |
| FID | < 100ms |
| CLS | < 0.1 |
| TTI | < 3.8s |
| Bundle Size | < 200KB (gzip) |
