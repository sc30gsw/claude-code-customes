---
name: vercel-react-best-practices
description: Vercel Engineeringによる React と Next.js のパフォーマンス最適化ガイドライン。React/Next.js コードの作成、レビュー、リファクタリング時に最適なパフォーマンスパターンを確保。Reactコンポーネント、Next.jsページ、データフェッチング、バンドル最適化、パフォーマンス改善に関するタスクで使用。
---

# Vercel React ベストプラクティス

Vercel Engineering 公式の React と Next.js パフォーマンス最適化ガイドライン。40以上のルールを8カテゴリで整理し、優先度付きで提供します。

## クイックスタート

### 主要機能

このスキルは以下の場面で自動的に活性化:

- React コンポーネントや Next.js ページの新規作成
- データフェッチング（クライアント/サーバー）の実装
- パフォーマンス問題のコードレビュー
- React/Next.js コードのリファクタリング
- バンドルサイズや読み込み時間の最適化

## コア機能（8カテゴリ）

### 1. Eliminating Waterfalls（ウォーターフォール排除）

**優先度:** CRITICAL

ネットワークリクエストの連鎖を排除し、並列化を促進。

**主要ルール:**
- `async-defer-await`: 実際に使用される場所でのみ await を実行
- `async-parallel`: 独立した操作に `Promise.all()` を使用
- `async-suspense-boundaries`: Suspense を使用してコンテンツをストリーミング

**良い例:**
```typescript
// 並列フェッチング
const [users, posts] = await Promise.all([
  fetchUsers(),
  fetchPosts()
]);
```

### 2. Bundle Size Optimization（バンドルサイズ最適化）

**優先度:** CRITICAL

バンドルサイズを削減し、Time to Interactive と LCP を改善。

**主要ルール:**
- `bundle-barrel-imports`: バレルファイルを避け、直接インポート
- `bundle-dynamic-imports`: 重いコンポーネントに `next/dynamic` を使用
- `bundle-defer-third-party`: サードパーティスクリプトを遅延読み込み

**良い例:**
```typescript
// 直接インポート（バレル回避）
import { Button } from '@/components/ui/Button';

// 動的インポート
const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <Skeleton />
});
```

### 3. Server-Side Performance（サーバー側パフォーマンス）

**優先度:** HIGH

サーバーサイドの効率とキャッシング戦略を最適化。

**主要ルール:**
- `server-cache-react`: リクエスト単位のキャッシングに `React.cache()` を使用
- `server-cache-lru`: クロスリクエストのキャッシングに LRU キャッシュを使用
- `server-serialization`: クライアントコンポーネントに渡すデータを最小化
- `server-after-nonblocking`: 非ブロッキング操作に `after()` を使用

### 4. Client-Side Data Fetching（クライアント側データフェッチング）

**優先度:** MEDIUM-HIGH

クライアント側のデータ取得パターンを最適化。

**主要ルール:**
- `client-swr-dedup`: SWR による自動リクエストの重複排除
- `client-event-listeners`: グローバルイベントリスナーの重複排除

### 5. Re-render Optimization（再レンダリング最適化）

**優先度:** MEDIUM

不要な再レンダリングを防止し、React のパフォーマンスを向上。

**主要ルール:**
- `rerender-memo`: 高コストな処理をメモ化コンポーネントに抽出
- `rerender-dependencies`: エフェクトの依存関係を絞り込む
- `rerender-derived-state`: 派生ブール値を購読、生の値は不要
- `rerender-functional-setstate`: 安定なコールバック用に関数型の setState
- `rerender-transitions`: 非緊急の更新に `startTransition` を使用

### 6. Rendering Performance（レンダリングパフォーマンス）

**優先度:** MEDIUM

DOM 操作とレンダリング効率を最適化。

**主要ルール:**
- `rendering-content-visibility`: 長いリストに `content-visibility` を使用
- `rendering-hoist-jsx`: 静的 JSX をコンポーネント外に抽出
- `rendering-hydration-no-flicker`: インラインスクリプトでクライアント専用データを処理
- `rendering-conditional-render`: 条件付きレンダリングに三項演算子を使用

### 7. JavaScript Performance（JavaScript パフォーマンス）

**優先度:** LOW-MEDIUM

JavaScript の実行効率を最適化。

**主要ルール:**
- `js-batch-dom-css`: CSS 変更をグループ化
- `js-index-maps`: 繰り返しルックアップ用にマップを構築
- `js-combine-iterations`: 複数の filter/map を 1 ループに統合
- `js-early-exit`: 関数から早期に返す
- `js-set-map-lookups`: O(1) ルックアップに Set/Map を使用

### 8. Advanced Patterns（高度なパターン）

**優先度:** LOW

上級者向けの最適化パターン。

**主要ルール:**
- `advanced-event-handler-refs`: イベントハンドラーを refs に保存
- `advanced-use-latest`: 安定なコールバック参照に useLatest を使用

## 使用タイミング

| シナリオ | スキル適用 |
|---------|----------|
| React コンポーネント作成 | 必須 |
| Next.js ページ実装 | 必須 |
| データフェッチング実装 | 必須 |
| パフォーマンスレビュー | 必須 |
| コードリファクタリング | 推奨 |
| バンドル最適化 | 必須 |

## ベストプラクティス概要

### パフォーマンス優先度

1. **CRITICAL**: ウォーターフォール排除、バンドルサイズ最適化から開始
2. **HIGH**: サーバー側パフォーマンスを次に対応
3. **MEDIUM**: 再レンダリングとレンダリング最適化
4. **LOW**: JavaScript パフォーマンスと高度なパターン

### コード品質

- 各ルールの「悪い例」→「良い例」を参照
- 既存コードへの適用は段階的に実施
- パフォーマンス測定後に最適化を決定

## リソース

- React 公式ドキュメント: https://react.dev
- Next.js 公式ドキュメント: https://nextjs.org
- SWR ドキュメント: https://swr.vercel.app
- better-all ライブラリ: https://github.com/shuding/better-all
- LRU Cache: https://github.com/isaacs/node-lru-cache
- スキルルール詳細: `.claude/skills/vercel-react-best-practices/rules/`
