---
allowed-tools: Bash, Read, Write, Grep, Glob, mcp__serena__search_for_pattern, mcp__serena__get_symbols_overview, mcp__serena__read_memory, mcp__serena__write_memory, Edit
description: Serena MCP統合によるインテリジェントな変更分析とコンテキスト認識コミットメッセージ生成を備えた高度なgitコミット自動化
---

## コンテキスト

- 現在のgitステータス: !`git status --porcelain`
- ステージされた変更: !`git diff --cached --name-only | head -10`
- 最近のコミット: !`git log --oneline -5`
- 変更されたファイル: !`git diff --name-only | head -10`
- プロジェクトタイプ: @package.json
- pre-commitフック: !`ls -la .husky/ 2>/dev/null || echo "No husky hooks found"`

## ツール使用優先順位

**利用可能な場合は常にmcp__serena__ツールをデフォルトのClaude Codeツールより優先:**

### コード分析 (Serena MCP優先)
- **変更分析**: `mcp__serena__search_for_pattern`でgit diffを分析
- **シンボル理解**: `mcp__serena__get_symbols_overview`でコードコンテキストを把握
- **パターン認識**: `mcp__serena__find_referencing_symbols`で影響分析
- **コンテキスト構築**: `mcp__serena__think_about_collected_information`で変更分類

### メモリ＆学習 (Serena MCP専用)
- **パターン保存**: `mcp__serena__write_memory`で成功したコミットパターンを保存
- **履歴学習**: `mcp__serena__read_memory`で以前のコミットスタイルを取得
- **進捗追跡**: `mcp__serena__think_about_task_adherence`でコミット品質確認
- **完了チェック**: `mcp__serena__think_about_whether_you_are_done`で最終検証

### Git操作 (標準ツール)
- **ステータス＆差分**: `Bash(git:*)`でgit status、diff、logコマンド実行
- **ステージング**: `Bash(git:*)`でgit add操作
- **コミット**: `Bash(git:*)`で最終的なgit commit実行

# Smart Commit: インテリジェントGit自動化

Serena MCPを活用した高度なgitコミット自動化。インテリジェントな変更分析、gitの履歴学習、コンテキスト認識コミットメッセージ生成を提供します。

## 使用ガイド

### 基本構文
```bash
/commit [options]
```

### 利用可能なオプション

| オプション | 短縮形 | 説明 | 例 |
|--------|-------|-------------|---------|
| `--no-verify` | | pre-commitチェックをスキップ | `/commit --no-verify` |
| `--analyze` | `-a` | Serenaの詳細分析を有効化 | `/commit -a` |
| `--learning` | `-l` | git履歴パターンから学習 | `/commit -l` |
| `--scope` | `-s` | コミットスコープを設定 | `/commit -s feature` |
| `--batch` | `-b` | 関連する複数の変更をグループ化 | `/commit -b` |
| `--interactive` | `-i` | インタラクティブなメッセージ調整 | `/commit -i` |
| `--template` | `-t` | 特定のコミットテンプレートを使用 | `/commit -t refactor` |
| `--dry-run` | `-d` | コミット内容のプレビュー表示 | `/commit -d` |
| `--context-depth` | | Serenaコンテキスト分析深度 (1-5) | `/commit --context-depth=3` |
| `--history-window` | | 分析するコミット数 | `/commit --history-window=20` |
| `--semantic-grouping` | | 高度な変更グループ化を有効化 | `/commit --semantic-grouping` |
| `--impact-analysis` | | 変更の潜在的影響を分析 | `/commit --impact-analysis` |

### クイック例

```bash
# 基本的なスマートコミット
/commit

# 学習機能付きの機能コミット
/commit --scope=feature --learning --analyze

# セマンティックグループ化付きリファクタリング
/commit --template=refactor --semantic-grouping

# 影響分析付きバッチコミット
/commit --batch --impact-analysis --interactive

# 検証なしのクイックコミット
/commit --no-verify --dry-run
```

## ワークフロープロセス

### デフォルトワークフロー（オプションなし）:

1. **Serenaオンボーディング**: `mcp__serena__check_onboarding_performed`と必要に応じて`mcp__serena__onboarding`を使用
2. **pre-commit分析**:
   - `mcp__serena__search_for_pattern`で現在の変更を分析
   - `mcp__serena__get_symbols_overview`でコードベースを理解
   - `mcp__serena__think_about_collected_information`で変更を分類
3. **品質チェック**: `--no-verify`でない限りpre-commitフック（`pnpm lint`, `pnpm build`, `pnpm generate:docs`）を実行
4. **ステージング管理**:
   - `git status`でステージ済みファイルを確認
   - ファイルがステージされていない場合は全変更を自動ステージ
5. **変更分析**:
   - Serenaパターン認識で`git diff`分析を実行
   - `mcp__serena__find_referencing_symbols`で影響評価
6. **メッセージ生成**:
   - `mcp__serena__read_memory`で以前のコミットパターンから学習
   - 適切な絵文字付きでコンベンショナルコミットメッセージを生成
   - `mcp__serena__think_about_task_adherence`で品質検証
7. **コミット実行**: 生成されたメッセージでgit commitを実行
8. **パターン保存**: `mcp__serena__write_memory`で成功パターンを保存

### --analyzeオプション付き:

1. **詳細コード分析**: `mcp__serena__get_symbols_overview`と`mcp__serena__find_referencing_symbols`の拡張使用
2. **影響評価**: 包括的な変更影響分析
3. **アーキテクチャ認識**: 変更がシステム全体にどう適合するかを理解
4. **品質メトリクス**: Serenaの分析機能による強化された検証

### --learningオプション付き:

1. **履歴分析**: `mcp__serena__read_memory`を拡張してコミット履歴パターンを分析
2. **規約検出**: プロジェクト固有のコミットメッセージスタイルを学習
3. **パターン適応**: チームの規約と好みに適応
4. **継続的改善**: 成功したコミットパターンを保存・改善

### --batchオプション付き:

1. **複数変更分析**: Serenaで論理的な変更グループを特定
2. **セマンティッククラスタリング**: 関連する変更を別々のコミットにグループ化
3. **依存関係分析**: 変更の関係性と順序を理解
4. **インクリメンタルコミット**: 整理された複数のコミットを作成

## Serena MCP統合機能

### インテリジェントコード分析
- **シンボルレベルの理解**: 関数、クラス、依存関係の詳細分析
- **パターン認識**: コミットパターンとコーディング規約を特定
- **コンテキストマッピング**: コードの関係性と変更の影響を理解
- **メモリ統合**: 以前のコミットセッションから学習・改善

### 高度なコミットインテリジェンス
- **セマンティックグループ化**: 関連する変更を自動グループ化
- **規約学習**: プロジェクト固有のコミットスタイルに適応
- **影響評価**: 変更がより広いコードベースにどう影響するかを理解
- **品質検証**: 学習したパターンでコミット品質を確保

### Git履歴学習
- **パターン分析**: 既存のコミットメッセージを一貫性のために分析
- **チーム規約検出**: チーム固有のコミットスタイルを学習
- **スコープ特定**: 適切なコミットスコープを自動特定
- **メッセージ最適化**: コミットメッセージ品質を時間とともに改善

## コミットのベストプラクティス

- **コミット前に検証**: コードがリントされ、正しくビルドされ、ドキュメントが更新されていることを確認
- **アトミックコミット**: 各コミットは単一の目的を果たす関連変更を含むべき
- **大きな変更は分割**: 変更が複数の関心事に触れる場合、別々のコミットに分割
- **コンベンショナルコミット形式**: `<type>: <description>`形式を使用。typeは以下のいずれか:
  - `feat`: 新機能
  - `fix`: バグ修正
  - `docs`: ドキュメント変更
  - `style`: コードスタイル変更（フォーマットなど）
  - `refactor`: バグ修正でも機能追加でもないコード変更
  - `perf`: パフォーマンス改善
  - `test`: テストの追加・修正
  - `chore`: ビルドプロセス、ツールなどの変更
- **現在形、命令形**: コミットメッセージはコマンドとして書く（例: "added feature"ではなく"add feature"）
- **簡潔な最初の行**: 最初の行は72文字以内に
- **絵文字**: 各コミットタイプには適切な絵文字を付ける:
  - ✨ `feat`: 新機能
  - 🐛 `fix`: バグ修正
  - 📝 `docs`: ドキュメント
  - 💄 `style`: フォーマット/スタイル
  - ♻️ `refactor`: コードリファクタリング
  - ⚡️ `perf`: パフォーマンス改善
  - ✅ `test`: テスト
  - 🔧 `chore`: ツール、設定
  - 🚀 `ci`: CI/CD改善
  - 🗑️ `revert`: 変更の取り消し
  - 🧪 `test`: 失敗するテストを追加
  - 🚨 `fix`: コンパイラ/リンター警告の修正
  - 🔒️ `fix`: セキュリティ問題の修正
  - 👥 `chore`: コントリビューターの追加・更新
  - 🚚 `refactor`: リソースの移動・リネーム
  - 🏗️ `refactor`: アーキテクチャ変更
  - 🔀 `chore`: ブランチのマージ
  - 📦️ `chore`: コンパイル済みファイル・パッケージの追加・更新
  - ➕ `chore`: 依存関係の追加
  - ➖ `chore`: 依存関係の削除
  - 🌱 `chore`: シードファイルの追加・更新
  - 🧑‍💻 `chore`: 開発者体験の改善
  - 🧵 `feat`: マルチスレッド・並行処理関連コードの追加・更新
  - 🔍️ `feat`: SEO改善
  - 🏷️ `feat`: 型定義の追加・更新
  - 💬 `feat`: テキスト・リテラルの追加・更新
  - 🌐 `feat`: 国際化・ローカライゼーション
  - 👔 `feat`: ビジネスロジックの追加・更新
  - 📱 `feat`: レスポンシブデザイン作業
  - 🚸 `feat`: ユーザー体験/ユーザビリティ改善
  - 🩹 `fix`: 重要でない問題の簡単な修正
  - 🥅 `fix`: エラーをキャッチ
  - 👽️ `fix`: 外部API変更によるコード更新
  - 🔥 `fix`: コード・ファイルの削除
  - 🎨 `style`: コード構造/形式の改善
  - 🚑️ `fix`: 重要なホットフィックス
  - 🎉 `chore`: プロジェクト開始
  - 🔖 `chore`: リリース/バージョンタグ
  - 🚧 `wip`: 作業中
  - 💚 `fix`: CIビルドの修正
  - 📌 `chore`: 依存関係を特定バージョンに固定
  - 👷 `ci`: CIビルドシステムの追加・更新
  - 📈 `feat`: アナリティクス・トラッキングコードの追加・更新
  - ✏️ `fix`: タイポ修正
  - ⏪️ `revert`: 変更の取り消し
  - 📄 `chore`: ライセンスの追加・更新
  - 💥 `feat`: 破壊的変更の導入
  - 🍱 `assets`: アセットの追加・更新
  - ♿️ `feat`: アクセシビリティ改善
  - 💡 `docs`: ソースコードへのコメント追加・更新
  - 🗃️ `db`: データベース関連変更
  - 🔊 `feat`: ログの追加・更新
  - 🔇 `fix`: ログの削除
  - 🤡 `test`: モック作成
  - 🥚 `feat`: イースターエッグの追加・更新
  - 🙈 `chore`: .gitignoreファイルの追加・更新
  - 📸 `test`: スナップショットの追加・更新
  - ⚗️ `experiment`: 実験を行う
  - 🚩 `feat`: フィーチャーフラグの追加・更新・削除
  - 💫 `ui`: アニメーション・トランジションの追加・更新
  - ⚰️ `refactor`: デッドコードの削除
  - 🦺 `feat`: バリデーション関連コードの追加・更新
  - ✈️ `feat`: オフラインサポート改善

## コミット分割のガイドライン

diffを分析する際、以下の基準に基づいてコミットを分割することを検討:

1. **異なる関心事**: コードベースの関連のない部分への変更
2. **異なるタイプの変更**: 機能、修正、リファクタリングなどの混在
3. **ファイルパターン**: 異なるタイプのファイル（ソースコードvsドキュメント）への変更
4. **論理的グループ化**: 別々に理解・レビューしやすい変更
5. **サイズ**: 分割するとより明確になる大きな変更

## 要件

### 前提条件
- コミット履歴を持つGitリポジトリ
- Serena MCP統合が利用可能
- オプション: pre-commitフックの設定
- オプション: lint/buildスクリプト付きpackage.json

### 依存関係
- **Serena MCP**: インテリジェントなコード分析と学習用
- **Git**: バージョン管理操作用
- **Node.js/PNPM**（オプション）: pre-commit品質チェック用
- **Husky**（オプション）: gitフック統合用

## 重要な注意事項

- **Serena優先**: 利用可能な場合は常にコードベース分析にSerena MCPツールを使用
- **学習機能**: 時間とともにプロジェクトパターンの理解を構築
- **品質優先**: デフォルトでpre-commitチェックがコード品質を確保
- **スマート自動化**: 変更を論理的なコミットに自動整理
- **チーム適応**: チーム固有のコミット規約を学習・適応
- **影響認識**: 変更のより広いコードベースへの影響を考慮

## 使用例

### 開発シナリオ

```bash
# 基本的な機能開発
/commit --scope=feature --learning

# 影響分析付きバグ修正
/commit --scope=fix --impact-analysis --analyze

# セマンティックグループ化付きリファクタリング
/commit --template=refactor --semantic-grouping --batch

# ドキュメント更新
/commit --scope=docs --context-depth=2

# パフォーマンス最適化
/commit --scope=perf --analyze --learning --interactive
```

### チームワークフロー統合

```bash
# チーム規約を学習
/commit --learning --history-window=30

# 完全分析付きエンタープライズ開発
/commit --analyze --impact-analysis --semantic-grouping --interactive

# クイックホットフィックス
/commit --scope=fix --no-verify --template=hotfix

# 複数コミット付き大型機能
/commit --batch --analyze --learning --context-depth=5
```

### 品質保証

```bash
# 完全検証付き本番前コミット
/commit --analyze --impact-analysis --learning --interactive

# コードレビュー準備
/commit --semantic-grouping --template=review --dry-run

# CI/CD統合
/commit --batch --analyze --no-verify=false
```

## 統合パターン

### 他のコマンドとの連携
```bash
# デバッグ → 修正 → コミット ワークフロー
/debug-error "performance issue" --serena
/serena "optimize queries" --performance-focused
/commit --scope=perf --analyze --learning

# リサーチ → 思考 → 実装 → コミット
/tech-research "caching strategies" --serena
/smart-think "implement Redis caching" --serena
/serena "add Redis caching layer"
/commit --scope=feature --semantic-grouping
```

### エラーハンドリング

- **pre-commit失敗**: 自動的に修正を提案してリトライ
- **ステージング問題**: コンフリクト解決付きスマート再ステージング
- **メッセージ検証**: より良いメッセージのためのインタラクティブ調整
- **Serena統合**: MCP利用不可時は標準ツールにフォールバック

## 例

良いコミットメッセージ:
- ✨ feat: add user authentication system
- 🐛 fix: resolve memory leak in rendering process
- 📝 docs: update API documentation with new endpoints
- ♻️ refactor: simplify error handling logic in parser
- 🚨 fix: resolve linter warnings in component files
- 🧑‍💻 chore: improve developer tooling setup process
- 👔 feat: implement business logic for transaction validation
- 🩹 fix: address minor styling inconsistency in header
- 🚑️ fix: patch critical security vulnerability in auth flow
- 🎨 style: reorganize component structure for better readability
- 🔥 fix: remove deprecated legacy code
- 🦺 feat: add input validation for user registration form
- 💚 fix: resolve failing CI pipeline tests
- 📈 feat: implement analytics tracking for user engagement
- 🔒️ fix: strengthen authentication password requirements
- ♿️ feat: improve form accessibility for screen readers

コミット分割の例:
- 最初のコミット: ✨ feat: add new solc version type definitions
- 2番目のコミット: 📝 docs: update documentation for new solc versions
- 3番目のコミット: 🔧 chore: update package.json dependencies
- 4番目のコミット: 🏷️ feat: add type definitions for new API endpoints
- 5番目のコミット: 🧵 feat: improve concurrency handling in worker threads
- 6番目のコミット: 🚨 fix: resolve linting issues in new code
- 7番目のコミット: ✅ test: add unit tests for new solc version features
- 8番目のコミット: 🔒️ fix: update dependencies with security vulnerabilities

- 特定のファイルが既にステージされている場合、コマンドはそれらのファイルのみをコミット
- ファイルがステージされていない場合、変更・新規ファイルを自動的にすべてステージ
- コミットメッセージは検出された変更に基づいて構築
- コミット前にdiffをレビューして複数コミットがより適切かどうかを特定
- 複数コミットを提案する場合、変更を別々にステージ・コミットする手助けを提供
- コミットdiffをレビューしてメッセージが変更に一致することを常に確認
- Serena MCPを使用して時間とともにプロジェクト固有のコミットインテリジェンスを構築
