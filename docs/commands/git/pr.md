---
allowed-tools: mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__list_dir, Bash(gh:*), Bash(git:*), mcp__context7__resolve-library-id, mcp__context7__get-library-docs
description: PR説明を生成し、GitHubでプルリクエストを自動作成
---

## コンテキスト

- 現在のgitステータス: !`git status`
- このPRの変更: !`git diff develop...HEAD 2>/dev/null || git diff main...HEAD 2>/dev/null || git diff master...HEAD 2>/dev/null || git diff HEAD~1...HEAD`
- このPRのコミット: !`git log --oneline develop..HEAD 2>/dev/null || git log --oneline main..HEAD 2>/dev/null || git log --oneline master..HEAD 2>/dev/null || git log --oneline HEAD~1..HEAD`
- PRテンプレート: @.github/pull_request_template.md

## ツール使用優先順位

**利用可能な場合は常にmcp__serena__ツールをデフォルトのClaude Codeツールより優先:**

### ファイル操作 (Serena MCP優先)
- **ファイル読み込み**: `mcp__serena__find_file` → `Bash(git:*)`（フォールバック）
- **パターン検索**: `mcp__serena__search_for_pattern` → `Bash(git:*)`（フォールバック）
- **ディレクトリ一覧**: `mcp__serena__list_dir` → `Bash(git:*)`（フォールバック）
- **シンボル検索**: `mcp__serena__find_symbol` → `Bash(git:*)`（フォールバック）

### コード分析 (Serena MCP専用)
- **シンボル概要**: `mcp__serena__get_symbols_overview`を使用
- **シンボル参照**: `mcp__serena__find_referencing_symbols`を使用
- **コード置換**: `mcp__serena__replace_symbol_body` → フォールバック
- **パターン置換**: `mcp__serena__replace_regex` → フォールバック

## タスク

提供されたオプションに基づいて、以下のいずれかのアクションを実行:

### オプション:

- **オプションなしまたはデフォルト**: PR説明を生成し、プルリクエストを作成
- **-p**: 現在のブランチをプッシュし、プルリクエストを作成
- **-u**: 既存のプルリクエスト説明のみを更新

### デフォルト動作（オプションなし）:

1. **Serenaオンボーディング**: `mcp__serena__check_onboarding_performed`と必要に応じて`mcp__serena__onboarding`を使用
2. **変更分析**: `mcp__serena__search_for_pattern`でgit diffを分析し、`mcp__serena__get_symbols_overview`でコードを理解
3. **PRテンプレート読み込み**: `mcp__serena__find_file`でPRテンプレートを読み込み → 直接ファイル読み込みにフォールバック
4. PRテンプレートの**正確なフォーマット**に従ってPR説明を日本語で作成
5. **Context7 MCP**を使用してReferenceセクション用の関連ドキュメントURLを取得
6. このPRで行われた変更を視覚化する**Mermaidダイアグラム**を追加
7. **進捗チェック**: `mcp__serena__think_about_task_adherence`で完全性を検証
8. 生成されたタイトルと説明で`gh pr create --draft`を実行
9. **パターン保存**: `mcp__serena__write_memory`で成功したPRパターンを保存

### -pオプション付き:

1. **Serenaオンボーディング**: `mcp__serena__check_onboarding_performed`と必要に応じて`mcp__serena__onboarding`を使用
2. `git push -u origin <current-branch>`で現在のブランチをリモートリポジトリにプッシュ
3. **変更分析**: `mcp__serena__search_for_pattern`でgit diffを分析し、`mcp__serena__get_symbols_overview`でコードを理解
4. **PRテンプレート読み込み**: `mcp__serena__find_file`でPRテンプレートを読み込み → 直接ファイル読み込みにフォールバック
5. PRテンプレートの**正確なフォーマット**に従ってPR説明を日本語で作成
6. **Context7 MCP**を使用してReferenceセクション用の関連ドキュメントURLを取得
7. このPRで行われた変更を視覚化する**Mermaidダイアグラム**を追加
8. **進捗チェック**: `mcp__serena__think_about_task_adherence`で完全性を検証
9. 生成されたタイトルと説明で`gh pr create --draft`を実行
10. **パターン保存**: `mcp__serena__write_memory`で成功したPRパターンを保存

### -uオプション付き:

1. **Serenaオンボーディング**: `mcp__serena__check_onboarding_performed`と必要に応じて`mcp__serena__onboarding`を使用
2. **変更分析**: `mcp__serena__search_for_pattern`でgit diffを分析し、`mcp__serena__get_symbols_overview`でコードを理解
3. **PRテンプレート読み込み**: `mcp__serena__find_file`でPRテンプレートを読み込み → 直接ファイル読み込みにフォールバック
4. **以前のパターン確認**: `mcp__serena__read_memory`で以前のPRパターンを取得
5. PRテンプレートの**正確なフォーマット**に従ってPR説明を日本語で作成
6. **Context7 MCP**を使用してReferenceセクション用の関連ドキュメントURLを取得
7. このPRで行われた変更を視覚化する**Mermaidダイアグラム**を追加
8. **進捗チェック**: `mcp__serena__think_about_task_adherence`で完全性を検証
9. `gh pr edit --body <description>`で既存のプルリクエスト説明を更新
10. **完了チェック**: `mcp__serena__think_about_whether_you_are_done`で成功を確認

### 要件:

1. テンプレート構造に正確に従う
2. すべてのコンテンツは日本語で記述
3. 具体的な実装の詳細を含める
4. 具体的なテスト手順を列挙
5. Context7 MCPを使用して、変更で使用されているライブラリ/フレームワークの公式ドキュメントURLを取得:
   - **依存関係分析**: `mcp__serena__find_referencing_symbols`で使用ライブラリを特定
   - **情報の検討**: `mcp__serena__think_about_collected_information`で発見を分類
   - 関連技術のドキュメントをContext7 MCPにクエリ
   - Referenceセクションに公式ドキュメントリンクを含める
   - 実際の変更に基づいてNext.js、React、TanStack Query、Tailwind CSSなどのライブラリに焦点を当てる
6. 常に以下を示すMermaidダイアグラムを含める:
   - アーキテクチャの変更（ある場合）
   - データフローの変更
   - コンポーネントの関係
   - 変更によって影響を受けるプロセスフロー
7. 包括的だが簡潔に

### Mermaidダイアグラムのガイドライン:

- 適切なダイアグラムタイプを使用（flowchart、sequence、classなど）
- 該当する場合、変更前/変更後の状態を表示
- 新規または変更されたコンポーネントをハイライト
- 一貫したスタイリングと色を使用
- PR説明の専用セクションにダイアグラムを追加

**PR説明を生成し、プルリクエストを自動的に作成してください。**
