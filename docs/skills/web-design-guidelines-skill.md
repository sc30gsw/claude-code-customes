---
name: web-design-guidelines
description: UIコードがWeb Interface Guidelinesに準拠しているかをレビューするスキル。アクセシビリティ、フォーカス状態、フォーム、アニメーション、タイポグラフィ、コンテンツ処理、画像、パフォーマンスをチェック。「UIをレビュー」「アクセシビリティをチェック」「デザイン監査」「UXをレビュー」「ベストプラクティスに対してサイトをチェック」時に使用。
---

# Web Design Guidelines

UIコードが Vercel の Web Interface Guidelines に準拠しているかを自動レビューするスキル。デザイン品質とベストプラクティスの監査を効率化します。

## クイックスタート

### 主要機能

このスキルは以下のリクエストで自動的に活性化:

- 「UIをレビューしてください」
- 「アクセシビリティをチェック」
- 「デザイン監査」
- 「UXをレビュー」
- 「ベストプラクティスに対してサイトをチェック」

### 処理フロー

1. ユーザーが指定したファイル/パターンを入力
2. GitHub から最新のガイドラインを自動取得
3. ファイルを読み取り、全ガイドラインルールに対してチェック
4. 検出された問題を構造化形式で出力

## コア機能

### 1. アクセシビリティ

**チェック項目:**
- ARIA ラベルの適切な使用
- セマンティック HTML の採用
- キーボード操作対応
- ライブリージョンアナウンス
- スクリーンリーダー互換性

**良い例:**
```tsx
<button aria-label="メニューを閉じる" onClick={onClose}>
  <CloseIcon aria-hidden="true" />
</button>
```

### 2. フォーカス状態

**チェック項目:**
- `:focus-visible` の使用
- 視覚的フォーカスインジケータ
- フォーカス順序の論理性
- フォーカストラップの適切な実装

**良い例:**
```css
button:focus-visible {
  outline: 2px solid var(--focus-color);
  outline-offset: 2px;
}
```

### 3. フォーム

**チェック項目:**
- 適切な入力タイプ（`email`, `tel`, `url` 等）
- `autocomplete` 属性の設定
- クリック可能なラベル
- インラインエラーハンドリング
- フォームバリデーションメッセージ

**良い例:**
```tsx
<label htmlFor="email">メールアドレス</label>
<input
  id="email"
  type="email"
  autoComplete="email"
  aria-describedby="email-error"
/>
```

### 4. アニメーション

**チェック項目:**
- `prefers-reduced-motion` の尊重
- Compositor フレンドリーな変換（`transform`, `opacity`）
- 割り込み可能なアニメーション
- アニメーション時間の適切さ

**良い例:**
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 5. タイポグラフィ

**チェック項目:**
- 正しい句読点（"…" vs "..."）
- 適切な引用符（" " vs " "）
- ノーブレークスペースの使用
- 行間と文字間隔

### 6. コンテンツ処理

**チェック項目:**
- 長いテキストの処理（`text-overflow: ellipsis`）
- 空状態のデザイン
- 可変入力長への対応
- ローディング状態

### 7. 画像とメディア

**チェック項目:**
- 明示的な寸法指定（CLS 防止）
- 遅延読み込み（`loading="lazy"`）
- 代替テキスト
- レスポンシブ画像

**良い例:**
```tsx
<Image
  src="/hero.jpg"
  alt="製品の説明"
  width={1200}
  height={600}
  priority
/>
```

### 8. パフォーマンス

**チェック項目:**
- 大規模リストの仮想化
- DOM 読み書きバッチング
- リソース事前読み込み
- 不要な再レンダリング防止

## 出力形式

問題は簡潔な `file:line` 形式で報告:

```
src/components/Button.tsx:15 - フォーカス状態が定義されていません
src/components/Form.tsx:42 - input に autocomplete 属性がありません
src/pages/index.tsx:28 - 画像に明示的な寸法がありません
```

## 使用タイミング

| シナリオ | スキル適用 |
|---------|----------|
| UI コンポーネント作成後 | 推奨 |
| アクセシビリティ監査 | 必須 |
| デザインシステム検証 | 必須 |
| リリース前レビュー | 推奨 |
| WCAG 準拠確認 | 必須 |

## ベストプラクティス概要

### アクセシビリティ優先

- セマンティック HTML を常に優先
- ARIA は最後の手段として使用
- キーボードナビゲーションを確保
- コントラスト比 WCAG AA 以上を維持

### パフォーマンス意識

- Core Web Vitals を意識
- CLS（レイアウトシフト）を防止
- 必要な時のみアニメーション使用

### ユーザー設定の尊重

- `prefers-reduced-motion` を尊重
- `prefers-color-scheme` に対応
- フォントサイズの拡大に対応

## リソース

- Web Interface Guidelines: https://rauno.me/interfaces
- WCAG 2.1 ガイドライン: https://www.w3.org/WAI/WCAG21/quickref/
- MDN アクセシビリティ: https://developer.mozilla.org/ja/docs/Web/Accessibility
- スキル詳細: `.claude/skills/web-design-guidelines/SKILL.md`
