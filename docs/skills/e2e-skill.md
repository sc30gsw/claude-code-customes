# E2E Skill

## 概要

Playwrightを使用してエンドツーエンドテストを生成・実行するスキル。テストジャーニーの作成、テスト実行、スクリーンショット/ビデオ/トレースのキャプチャ、アーティファクトのアップロードを行います。

## アクティベーショントリガー

- クリティカルなユーザージャーニーのテスト（ログイン、決済など）
- マルチステップフローのエンドツーエンド検証
- UIインタラクションとナビゲーションのテスト
- フロントエンドとバックエンドの統合検証
- 本番デプロイ前の準備

## 使用方法

```bash
/e2e
```

## e2e-runnerエージェントの動作

1. **ユーザーフローを分析**してテストシナリオを特定
2. **Playwrightテストを生成**（Page Object Modelパターン）
3. **複数ブラウザでテストを実行**（Chrome, Firefox, Safari）
4. **失敗をキャプチャ**（スクリーンショット、ビデオ、トレース）
5. **レポートを生成**（結果とアーティファクト付き）
6. **フレーキーテストを特定**して修正を推奨

## テストアーティファクト

### すべてのテストで生成
- タイムラインと結果を含むHTMLレポート
- CI統合用JUnit XML

### 失敗時のみ生成
- 失敗状態のスクリーンショット
- テストのビデオ録画
- デバッグ用トレースファイル
- ネットワークログ
- コンソールログ

## ブラウザ設定

デフォルトで複数ブラウザでテスト実行:
- Chromium（デスクトップChrome）
- Firefox（デスクトップ）
- WebKit（デスクトップSafari）
- モバイルChrome（オプション）

## テスト構造パターン

### Page Object Model
```typescript
// pages/LoginPage.ts
export class LoginPage {
  constructor(private page: Page) {}

  async navigate() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.page.fill('[data-testid="email"]', email);
    await this.page.fill('[data-testid="password"]', password);
    await this.page.click('[data-testid="submit"]');
  }
}
```

### テストファイル
```typescript
// tests/auth.spec.ts
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('user can login successfully', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.navigate();
  await loginPage.login('user@example.com', 'password');
  await expect(page).toHaveURL('/dashboard');
});
```

## ベストプラクティス

### DO
- メンテナンス性のためにPage Object Modelを使用
- セレクタにはdata-testid属性を使用
- 任意のタイムアウトではなくAPIレスポンスを待つ
- クリティカルなユーザージャーニーをエンドツーエンドでテスト
- mainへのマージ前にテストを実行

### DON'T
- 脆いセレクタを使用しない（CSSクラスは変更される可能性がある）
- 実装詳細をテストしない
- 本番環境に対してテストを実行しない
- フレーキーテストを無視しない

## クイックコマンド

```bash
npx playwright test                    # すべてのE2Eテストを実行
npx playwright test --headed           # ヘッダーモードで実行
npx playwright test --debug            # テストをデバッグ
npx playwright show-report             # レポートを表示
```

## テストシナリオ例

### 認証フロー
- ユーザー登録
- ログイン/ログアウト
- パスワードリセット
- セッション管理

### 決済フロー
- カート追加
- チェックアウト
- 支払い処理
- 注文確認

### CRUD操作
- アイテム作成
- 一覧表示
- 詳細表示
- 編集/削除

## 成功指標

- すべてのクリティカルフローがテストされている
- テストが安定して実行される
- 失敗時にアーティファクトが保存される
- HTMLレポートが生成される
- CI/CDパイプラインに統合されている
