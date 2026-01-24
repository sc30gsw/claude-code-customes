# Update CLAUDE.md Skill

## 概要

プロジェクト固有のCLAUDE.mdを自動生成・更新するインテリジェントなスキル。Serena MCPとSequential Thinking MCPを統合して、プロジェクトコンテキストを効果的にドキュメント化します。

## アクティベーショントリガー

- CLAUDE.mdの作成・更新が必要な時
- プロジェクト構造が変更された時
- 新しいドキュメントが追加された時
- フレームワーク設定を更新したい時

## 使用方法

```bash
/update-claude-md                    # 自動検出による基本更新
/update-claude-md --auto --backup    # 自動検出 + バックアップ
/update-claude-md --files README.md COMMANDS.md  # 特定ファイル
/update-claude-md --preview          # プレビューのみ
/update-claude-md --template kiro    # Kiroテンプレート使用
```

## オプション

| オプション | 短縮 | 説明 | デフォルト |
|-----------|------|------|----------|
| `--files` | `-f` | ファイルを指定 | 自動検出 |
| `--auto` | `-a` | MDファイルを自動検出 | true |
| `--backup` | `-b` | 既存CLAUDE.mdをバックアップ | false |
| `--preview` | `-p` | 更新前にプレビュー表示 | false |
| `--include-docs` | `-d` | docsディレクトリを含める | false |
| `--structure` | `-s` | プロジェクト構造を分析 | false |
| `--template` | `-t` | テンプレートを指定 | auto |
| `--merge` | `-m` | 既存コンテンツとマージ | false |
| `--output` | `-o` | 出力ファイル名 | CLAUDE.md |

## 利用可能なテンプレート

### Kiroテンプレート (`--template kiro`)
- Steering vs Specificationの説明
- フェーズベースのワークフロー
- Kiroコマンド統合

### Standardテンプレート (`--template standard`)
- プロジェクト概要とコンテキスト
- 開発ガイドライン
- 利用可能なコマンドとエージェント

### Minimalテンプレート (`--template minimal`)
- 基本的なプロジェクト情報のみ
- 最小限のフレームワーク参照

## ワークフロー

1. **プロジェクト分析**: Serena MCPがプロジェクト構造を分析
2. **コンテンツ統合**: Sequential Thinkingがマージ戦略を計画
3. **CLAUDE.md生成**: フレームワーク統合 + プロジェクトコンテキスト
4. **品質保証**: 生成コンテンツの検証

## 生成される構造

```markdown
# What I want you to do
[ユーザー固有の指示]

# Framework Components
@FLAGS.md
@PRINCIPLES.md
@RULES.md

# MCP Documentation
@MCP_Context7.md
@MCP_Playwright.md
@MCP_Sequential.md
@MCP_Serena.md

# [プロジェクト名]
[自動生成されたプロジェクト説明]

## Project Context
[自動検出されたセクション]

## Development Guidelines
[プロジェクト固有のガイドライン]
```

## 成功指標

- ✅ 完全なフレームワーク統合
- ✅ 正確なプロジェクト固有情報
- ✅ 既存ドキュメントからの情報統合
- ✅ 将来の更新への適応性
