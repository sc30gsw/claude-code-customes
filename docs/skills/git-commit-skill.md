# Git Commit Skill

## 概要

Serena MCPを統合した高度なGitコミット自動化スキル。インテリジェントな変更分析、Git履歴学習、コンテキスト認識型コミットメッセージ生成を提供します。

## アクティベーショントリガー

- 変更をコミットしたい時
- 適切なコミットメッセージを生成したい時
- 変更の影響分析が必要な時
- Gitワークフローを効率化したい時

## 使用方法

```bash
/git:commit [options]
```

## オプション

| オプション | 短縮形 | 説明 | 例 |
|------------|--------|------|-----|
| `--no-verify` | | pre-commitチェックをスキップ | `/git:commit --no-verify` |
| `--analyze` | `-a` | Serena深層分析を有効化 | `/git:commit -a` |
| `--learning` | `-l` | Git履歴パターンから学習 | `/git:commit -l` |
| `--scope` | `-s` | コミットスコープを設定 | `/git:commit -s feature` |
| `--batch` | `-b` | 関連する複数の変更をグループ化 | `/git:commit -b` |
| `--interactive` | `-i` | インタラクティブなメッセージ修正 | `/git:commit -i` |
| `--template` | `-t` | 特定のコミットテンプレートを使用 | `/git:commit -t refactor` |
| `--dry-run` | `-d` | コミット内容をプレビュー | `/git:commit -d` |
| `--impact-analysis` | | 変更の影響分析 | `/git:commit --impact-analysis` |

## Serena MCP ツール優先

### コード分析
- `mcp__serena__search_for_pattern` - git diffを分析
- `mcp__serena__get_symbols_overview` - コードコンテキスト理解
- `mcp__serena__find_referencing_symbols` - 影響範囲分析

### メモリ＆学習
- `mcp__serena__write_memory` - コミットパターンを保存
- `mcp__serena__read_memory` - 過去のコミットスタイルを参照

## ワークフロー

1. **Pre-commit分析**: Serenaパターン認識で変更を分析
2. **品質チェック**: pre-commitフック実行（lint, build）`--no-verify`でスキップ可能
3. **ステージング管理**: ステージされていない場合は全変更を自動ステージ
4. **変更分析**: git diff分析を実行
5. **メッセージ生成**: 絵文字付きconventional commitを生成
6. **コミット実行**: git commitを実行

## Conventional Commitフォーマット

```
<type>: <description>

<optional body>
```

### タイプと絵文字

| タイプ | 絵文字 | 説明 |
|--------|--------|------|
| `feat` | ✨ | 新機能 |
| `fix` | 🐛 | バグ修正 |
| `docs` | 📝 | ドキュメント |
| `style` | 💄 | フォーマット/スタイル |
| `refactor` | ♻️ | コードリファクタリング |
| `perf` | ⚡️ | パフォーマンス |
| `test` | ✅ | テスト |
| `chore` | 🔧 | ツール、設定 |
| `ci` | 🚀 | CI/CD |
| `revert` | 🗑️ | 変更の取り消し |

## 使用例

```bash
# 基本的な機能開発
/git:commit --scope=feature --learning

# 影響分析付きバグ修正
/git:commit --scope=fix --impact-analysis --analyze

# バッチコミット付きリファクタリング
/git:commit --template=refactor --batch

# クイックホットフィックス
/git:commit --scope=fix --no-verify
```

## コミット分割ガイドライン

以下の場合はコミットを分割:

1. **異なる関心事**: 無関係な部分への変更
2. **異なるタイプ**: 機能、修正、リファクタリングの混在
3. **ファイルパターン**: 異なるタイプのファイル
4. **論理的グループ**: 別々の方が理解しやすい
5. **サイズ**: 非常に大きな変更

## コミットメッセージ例

```
✨ feat: ユーザー認証機能を追加

- JWTベースの認証を実装
- ログイン/ログアウトエンドポイントを追加
- セッション管理を改善
```

```
🐛 fix: ログインフォームのバリデーションエラーを修正

空のメールアドレスで送信時にクラッシュする問題を修正
```

```
♻️ refactor: ユーザーサービスを分割

大きなUserServiceを以下に分割:
- AuthService
- ProfileService
- NotificationService
```

## ベストプラクティス

1. **説明的なメッセージ** - 何をしたかではなく、なぜしたか
2. **適切な粒度** - 1つのコミットで1つの論理的変更
3. **テスト確認** - コミット前にテストが通ることを確認
4. **レビュー準備** - コミットがレビューしやすいか確認
5. **影響分析** - 大きな変更は影響を確認

## 成功指標

- Conventional Commit形式に準拠
- 適切な絵文字が付与される
- 変更内容が正確に反映される
- コミット履歴が読みやすい
- 影響分析が正確
