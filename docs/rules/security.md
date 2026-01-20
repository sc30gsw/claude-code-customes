# セキュリティガイドライン

セキュリティに関するルールです。

## 必須セキュリティチェック

**すべてのコミット前に確認:**

- [ ] ハードコードされたシークレットがない（APIキー、パスワード、トークン）
- [ ] すべてのユーザー入力が検証されている
- [ ] SQLインジェクション防止（パラメータ化クエリ）
- [ ] XSS防止（サニタイズされたHTML）
- [ ] CSRF保護が有効
- [ ] 認証/認可が確認済み
- [ ] すべてのエンドポイントにレート制限
- [ ] エラーメッセージが機密データを漏洩しない

## シークレット管理

```typescript
// NEVER: ハードコードされたシークレット
const apiKey = "sk-proj-xxxxx"

// ALWAYS: 環境変数
const apiKey = process.env.OPENAI_API_KEY

if (!apiKey) {
  throw new Error('OPENAI_API_KEY not configured')
}
```

## セキュリティ脆弱性パターン

### SQLインジェクション (CRITICAL)

```typescript
// ❌ CRITICAL: SQLインジェクション脆弱性
const query = `SELECT * FROM users WHERE id = ${userId}`

// ✅ CORRECT: パラメータ化クエリ
const { data } = await supabase
  .from('users')
  .select('*')
  .eq('id', userId)
```

### XSS (HIGH)

```typescript
// ❌ HIGH: XSS脆弱性
element.innerHTML = userInput

// ✅ CORRECT: textContentを使用またはサニタイズ
element.textContent = userInput
// または
import DOMPurify from 'dompurify'
element.innerHTML = DOMPurify.sanitize(userInput)
```

### SSRF (HIGH)

```typescript
// ❌ HIGH: SSRF脆弱性
const response = await fetch(userProvidedUrl)

// ✅ CORRECT: URLを検証してホワイトリスト化
const allowedDomains = ['api.example.com', 'cdn.example.com']
const url = new URL(userProvidedUrl)
if (!allowedDomains.includes(url.hostname)) {
  throw new Error('Invalid URL')
}
```

### 競合状態 (CRITICAL)

```typescript
// ❌ CRITICAL: 残高チェックでの競合状態
const balance = await getBalance(userId)
if (balance >= amount) {
  await withdraw(userId, amount)
}

// ✅ CORRECT: ロック付きアトミックトランザクション
await db.transaction(async (trx) => {
  const balance = await trx('balances')
    .where({ user_id: userId })
    .forUpdate()
    .first()

  if (balance.amount < amount) {
    throw new Error('Insufficient balance')
  }

  await trx('balances')
    .where({ user_id: userId })
    .decrement('amount', amount)
})
```

## セキュリティ対応プロトコル

セキュリティ問題が見つかった場合:

1. **即時停止**
2. **security-reviewer** エージェントを使用
3. CRITICAL問題を続行前に修正
4. 露出したシークレットをローテーション
5. コードベース全体で類似問題をレビュー

## OWASP Top 10 チェックリスト

1. **インジェクション** - パラメータ化クエリを使用
2. **認証の破綻** - 強力なパスワードハッシュ（bcrypt）
3. **機密データの露出** - HTTPS強制、暗号化
4. **XXE** - XMLパーサーを安全に設定
5. **アクセス制御の破綻** - すべてのルートで認可チェック
6. **セキュリティ設定ミス** - デフォルト認証情報を変更
7. **XSS** - 出力をエスケープ
8. **安全でないデシリアライゼーション** - 入力を検証
9. **既知の脆弱性を持つコンポーネント** - 依存関係を更新
10. **不十分なログ記録と監視** - セキュリティイベントをログ

## セキュリティヘッダー

```typescript
// Next.js next.config.js
const securityHeaders = [
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'X-XSS-Protection', value: '1; mode=block' },
  { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' },
  { key: 'Content-Security-Policy', value: "default-src 'self'" },
]
```
