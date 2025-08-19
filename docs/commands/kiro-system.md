# Kiroコマンドシステム

Kiroは、仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポートするコマンドシステムです。

## 基本ワークフロー

### 1. `/kiro:steering` - プロジェクトステアリング
プロジェクトのステアリングドキュメントを生成/更新。プロジェクト概要、技術スタック、構造を文書化。

### 2. `/kiro:spec-init [詳細な機能説明]` - 仕様初期化
機能の詳細説明から仕様ディレクトリを作成。

### 3. `/kiro:spec-requirements [機能名]` - 要件定義
EARS形式で要件とユーザーストーリーを作成。

### 4. `/kiro:spec-design [機能名]` - 技術設計
アーキテクチャ、データモデル、APIを設計。

### 5. `/kiro:spec-test [機能名] [オプション]` - テスト仕様（新機能）
TDD用のテスト仕様を自動生成。単体テスト、コンポーネントテスト、フックテスト、APIテスト、E2Eテストをサポート。

**オプション**:
- `--test-lib=[jest|vitest|mocha]` - 単体テストフレームワーク（デフォルト: vitest）
- `--ui-lib=[testing-library|enzyme]` - UIテストライブラリ（デフォルト: testing-library）
- `--e2e-lib=[playwright|cypress|puppeteer]` - E2Eテストフレームワーク（デフォルト: playwright）
- `--api-lib=[supertest|axios-mock]` - APIテストライブラリ（デフォルト: supertest）
- `--coverage=[数値]` - カバレッジ目標パーセンテージ（デフォルト: 80）
- `--mock-strategy=[manual|auto]` - モック生成戦略（デフォルト: auto）

**生成される内容**:
- テスト仕様書 - 包括的なテスト戦略ドキュメント
- 単体テスト仕様 - ビジネスロジックとユーティリティのテスト
- コンポーネントテスト仕様 - Reactコンポーネントのテスト
- フックテスト仕様 - カスタムフックのテスト
- APIテスト仕様 - エンドポイントのテスト
- E2Eテスト仕様 - ユーザーワークフローのテスト
- モック仕様 - テストデータとサービスモック
- CI/CD設定 - GitHub Actionsワークフロー

### 6. `/kiro:spec-tasks [機能名]` - 実装タスク
詳細な実装ステップを作成。

### 7. `/kiro:spec-status [機能名]` - 進捗状況
各フェーズの完了状況を確認。

### 8. `/kiro:spec-impl [機能名] [タスク番号]` - 実装実行
TDD手法を使用して仕様からタスクを実装。

**引数**:
- `機能名` - 実装する機能名
- `タスク番号` - 実行するタスク（例: `1.1`, `1,2,3`, `--all`）

**例**:
```bash
/kiro:spec-impl auth-system 1.1            # タスク1.1を実行
/kiro:spec-impl auth-system 1,2,3          # タスク1, 2, 3を実行
/kiro:spec-impl auth-system --all          # 全ての未完了タスクを実行
```

## TDDワークフロー

1. **Red Phase** - 失敗するテストを先に書く
2. **Green Phase** - テストを通す最小限のコードを実装
3. **Refactor Phase** - テストを維持しながらコードを改善

## ディレクトリ構造

```
.kiro/
├── steering/              # プロジェクト全体の方針
│   ├── product.md        # 製品概要
│   ├── tech.md          # 技術スタック
│   └── structure.md     # プロジェクト構造
└── specs/               # 機能仕様
    └── [feature-name]/
        ├── requirements.md    # 要件定義
        ├── design.md         # 技術設計
        ├── tasks.md          # 実装タスク
        ├── tests/            # テスト仕様
        │   ├── test-spec.md  # テスト仕様書
        │   ├── unit/         # 単体テスト
        │   ├── component/    # コンポーネントテスト
        │   ├── hook/         # フックテスト
        │   ├── api/          # APIテスト
        │   └── e2e/          # E2Eテスト
        └── spec.json         # メタデータと承認状態
```

## 推奨ワークフロー

```bash
# 1. プロジェクト初期化
/kiro:steering

# 2. 新機能の仕様作成
/kiro:spec-init "ユーザー認証機能を実装したい。メールアドレスとパスワードでログインできるようにする"

# 3. 要件定義
/kiro:spec-requirements user-authentication

# 4. 技術設計
/kiro:spec-design user-authentication

# 5. テスト仕様生成（TDD）
/kiro:spec-test user-authentication --test-lib=vitest --e2e-lib=playwright

# 6. 実装タスク生成
/kiro:spec-tasks user-authentication

# 7. 実装実行（TDD）
/kiro:spec-impl user-authentication --all

# 8. 進捗確認
/kiro:spec-status user-authentication
```

## 特徴

- **仕様駆動開発**: 要件から実装まで体系的に管理
- **TDD対応**: テストファーストアプローチをサポート
- **自動承認**: インタラクティブな承認プロセス
- **多言語対応**: 日本語/英語での仕様生成
- **柔軟な設定**: プロジェクトに合わせてカスタマイズ可能