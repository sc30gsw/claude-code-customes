# CLAUDE.md更新コマンド

プロジェクト固有のCLAUDE.mdを自動生成・更新するインテリジェントコマンド。README.md、COMMANDS.md、SUB-AGENTS.md等のプロジェクト文書を読み込み、SuperClaude Frameworkコンポーネントと統合した包括的なCLAUDE.mdを生成します。

## 基本的な使用方法

```bash
/update-claude-md                    # 自動検出で基本更新
/update-claude-md --auto --backup    # 自動検出 + バックアップ
/update-claude-md --files README.md COMMANDS.md  # 特定ファイル指定
/update-claude-md --preview          # プレビューのみ
/update-claude-md --template kiro    # Kiroテンプレート使用
```

## 主要機能

### 🔍 自動ファイル検出
- **プロジェクト構造分析**: Serena MCPによる自動プロジェクト構造分析
- **関連ファイル発見**: README.md、COMMANDS.md、SUB-AGENTS.md等の自動検出
- **パターン認識**: プロジェクトタイプ（Kiro、標準、ミニマル）の自動識別

### 🧠 インテリジェント統合
- **Strategic Thinking**: Sequential Thinking MCPによる統合戦略の策定
- **Content Merging**: 複数ソースからの情報を矛盾なく統合
- **Template Selection**: プロジェクトに最適なテンプレートの自動選択

### 📝 包括的CLAUDE.md生成
- **SuperClaude Framework統合**: 必須フレームワークコンポーネントの自動組み込み
- **プロジェクト固有情報**: 分析結果に基づくカスタマイズされたコンテキスト
- **品質保証**: 生成後の自動検証とフォーマットチェック

## コマンドオプション

### 基本オプション

| オプション | 短縮形 | 説明 | デフォルト | 例 |
|-----------|--------|------|-----------|-----|
| `--files` | `-f` | 特定ファイル指定 | 自動検出 | `-f README.md COMMANDS.md` |
| `--auto` | `-a` | MDファイル自動検出 | true | `-a` |
| `--backup` | `-b` | 既存CLAUDE.mdバックアップ | false | `-b` |
| `--preview` | `-p` | 更新前プレビュー表示 | false | `-p` |
| `--include-docs` | `-d` | docsディレクトリ含める | false | `-d` |
| `--structure` | `-s` | プロジェクト構造分析 | false | `-s` |
| `--template` | `-t` | テンプレート指定 | auto | `-t kiro` |
| `--merge` | `-m` | 既存内容とマージ | false | `-m` |
| `--output` | `-o` | 出力ファイル名 | CLAUDE.md | `-o CLAUDE_NEW.md` |

### 高度なオプション

| オプション | 説明 | 使用例 | 用途 |
|-----------|------|--------|------|
| `--exclude` | 除外パターン指定 | `--exclude "test/*,*.tmp"` | テストファイル除外 |
| `--sections` | 含めるセクション指定 | `--sections "context,workflow"` | 特定セクションのみ |
| `--framework` | SuperClaude要素制御 | `--framework minimal` | 最小限のFramework |
| `--language` | 出力言語 | `--language en` | 英語出力 |
| `--format` | 出力フォーマット | `--format structured` | 構造化フォーマット |
| `--validate` | 生成後検証 | `--validate strict` | 厳密検証 |
| `--memory-key` | Serena記憶キー | `--memory-key claude_md_config` | 設定記憶 |

## 使用例

### 標準的な使用例

#### 初回セットアップ
```bash
# プロジェクト初回分析と包括的CLAUDE.md生成
/update-claude-md --auto --include-docs --structure --backup
```

#### 定期更新
```bash
# バックアップ付きの安全な定期更新
/update-claude-md --backup --preview
```

#### 特定ファイルのみを使用した更新
```bash
# 重要なドキュメントのみを使用
/update-claude-md --files README.md COMMANDS.md SUB-AGENTS.md
```

### プロジェクトタイプ別使用例

#### Kiroスペック駆動開発プロジェクト
```bash
# Kiro専用テンプレートで包括的更新
/update-claude-md --template kiro --include-docs --structure --validate strict

# Steering文書連携更新
/kiro:steering --update-context
/update-claude-md --template kiro --include-steering
```

#### 標準的な開発プロジェクト
```bash
# 自動テンプレート選択による標準更新
/update-claude-md --auto --backup --structure

# マージモードで既存内容保持
/update-claude-md --merge --exclude "*.tmp,test/*"
```

#### ミニマルプロジェクト
```bash
# 軽量設定での最小限更新
/update-claude-md --template minimal --files README.md --framework minimal
```

## テンプレートシステム

### 利用可能なテンプレート

#### Kiroテンプレート (`--template kiro`)
**Kiroスペック駆動開発プロジェクト専用**
- Steering vs Specification の詳細説明
- フェーズベースワークフロー (Requirements → Design → Tasks → Implementation)
- Kiroコマンド統合 (`/kiro:steering`, `/kiro:spec-*`)
- `.kiro/steering/` および `.kiro/specs/` ディレクトリ管理

**生成例:**
```markdown
# Claude Code Spec-Driven Development
Kiro-style Spec Driven Development implementation using claude code slash commands

## Project Context
### Paths
- Steering: `.kiro/steering/`
- Specs: `.kiro/specs/`
- Commands: `.claude/commands/`

### Workflow
Phase 0: Steering (Optional) → Phase 1: Specification Creation → Phase 2: Progress Tracking
```

#### 標準テンプレート (`--template standard`)
**一般的な開発プロジェクト用**
- プロジェクト概要とコンテキスト
- 開発ガイドラインとワークフロー
- 利用可能なコマンドとエージェント
- ファイル構成とパターン

**生成例:**
```markdown
# Project Context
## Available Commands
[COMMANDS.mdから自動統合]

## Sub-agents
[SUB-AGENTS.mdから自動統合]

## Development Guidelines
[プロジェクト分析から自動生成]
```

#### ミニマルテンプレート (`--template minimal`)
**軽量設定用**
- 基本的なプロジェクト情報のみ
- 必要最小限のSuperClaude Framework参照
- シンプルなワークフロー

### テンプレートカスタマイズ

#### カスタムセクション指定
```bash
# 特定セクションのみを含める
/update-claude-md --template standard --sections "context,commands,workflow"

# 既存テンプレートにセクション追加
/update-claude-md --template kiro --sections "+testing,+deployment"
```

#### フレームワーク統合レベル制御
```bash
# フルフレームワーク統合
/update-claude-md --framework full

# ミニマル統合
/update-claude-md --framework minimal

# カスタム統合
/update-claude-md --framework "flags,principles,serena"
```

## 技術的特徴

### MCP統合

#### Serena MCP統合
- **プロジェクト構造分析**: `mcp__serena__list_dir` による自動レイアウト理解
- **ファイル発見**: `mcp__serena__find_file` による関連ドキュメント検出
- **パターン分析**: `mcp__serena__search_for_pattern` による特定コンテンツ抽出
- **記憶統合**: `mcp__serena__write_memory` / `mcp__serena__read_memory` による学習機能

#### Sequential Thinking MCP統合
- **戦略的計画**: `mcp__sequential-thinking__sequentialthinking` による構造化思考
- **統合戦略**: 複数ソース統合のための論理的推論
- **品質評価**: エビデンスベースの検証計画策定

### 品質保証機能

#### 自動検証
- **構文チェック**: 生成されたMarkdownの構文検証
- **構造検証**: 必須セクションの存在確認
- **内容整合性**: 情報の矛盾検出と警告
- **フレームワーク準拠**: SuperClaude Framework要件の遵守確認

#### エラーハンドリング
- **ファイル不在**: 見つからないファイルを自動スキップ
- **パース エラー**: エラーファイルをログ出力し継続実行
- **テンプレート問題**: デフォルトテンプレートへの自動フォールバック
- **記憶競合**: 最新情報を優先した自動解決

## 他コマンドとの連携

### エコシステム統合

| コマンド | 連携機能 | 目的 |
|---------|---------|------|
| `/kiro:steering` | Steering文書分析 | Kiroプロジェクト完全統合 |
| `/serena` | プロジェクト記憶活用 | コンテキスト継続性とパターン学習 |
| `/smart-think` | 構造化思考適用 | 統合戦略と品質向上の策定 |
| `/commit` | 変更分析 | プロジェクト最新状態の反映 |

### ワークフロー統合例

#### プロジェクト初期セットアップワークフロー
```bash
# 1. プロジェクト分析と戦略策定
/smart-think "CLAUDE.md configuration strategy" --serena --project-context

# 2. 包括的初期CLAUDE.md生成
/update-claude-md --auto --include-docs --structure --backup --memory-key initial_setup

# 3. 生成結果の記憶と設定保存
/serena "記憶: プロジェクト設定完了" --store-config
```

#### 継続的更新ワークフロー
```bash
# 1. プロジェクト変更の検出と分析
/commit --analyze --detect-changes

# 2. 変更を反映したCLAUDE.md更新
/update-claude-md --use-memory project_config --merge --validate

# 3. 更新記録の保存
/serena "記憶: CLAUDE.md更新 - $(date)" --update-config
```

#### Kiroプロジェクト専用ワークフロー
```bash
# 1. Steering文書の生成・更新
/kiro:steering --update-context

# 2. CLAUDE.mdにSteering情報を統合
/update-claude-md --template kiro --include-steering --validate strict

# 3. 仕様進捗の反映
/kiro:spec-status --update-claude-md
```

## 記憶と学習機能

### プロジェクト記憶
Serena MCPの記憶機能を活用し、プロジェクト固有の設定や学習内容を蓄積・活用します。

#### 記憶される情報
- **プロジェクト設定**: テンプレート選択、オプション設定
- **ファイル構造パターン**: 過去の分析結果と最適化情報
- **統合戦略**: 成功した統合パターンと回避すべき問題
- **品質基準**: プロジェクト固有の品質要件と検証基準

#### 学習機能
```bash
# 設定の記憶
/update-claude-md --memory-key project_config --auto --include-docs

# 記憶された設定の再利用
/update-claude-md --use-memory project_config --validate

# 学習内容の確認
/serena "記憶: プロジェクト設定の確認" --read-memory project_config
```

## トラブルシューティング

### よくある問題と解決方法

#### ファイルが見つからない
```bash
# 問題: 指定されたファイルが存在しない
# 解決: 自動検出モードまたはファイル確認
/update-claude-md --auto  # 自動検出で継続
ls *.md  # 利用可能なファイル確認
```

#### テンプレートエラー
```bash
# 問題: 指定されたテンプレートが適用できない
# 解決: デフォルトテンプレートまたは標準テンプレート使用
/update-claude-md --template standard  # 標準テンプレートで実行
```

#### 統合エラー
```bash
# 問題: 複数ファイルの統合時に矛盾が発生
# 解決: プレビューモードで事前確認、段階的統合
/update-claude-md --preview  # プレビューで確認
/update-claude-md --files README.md  # 段階的統合
```

#### 記憶競合
```bash
# 問題: 記憶された設定が現在のプロジェクトに不適合
# 解決: 記憶の削除または新しいキーでの記憶
/serena "記憶削除: 古い設定" --delete-memory old_config
/update-claude-md --memory-key new_config  # 新しいキーで保存
```

## ベストプラクティス

### 効果的な使用法

#### 1. 定期的な更新
```bash
# 週1回の定期更新（推奨）
/update-claude-md --backup --validate
```

#### 2. 段階的な統合
```bash
# 大規模変更時は段階的に
/update-claude-md --files README.md --preview  # 段階1: 基本情報
/update-claude-md --include-docs --merge       # 段階2: 詳細統合
```

#### 3. プロジェクトタイプ特化
```bash
# プロジェクトタイプに応じた最適化
/update-claude-md --template kiro      # Kiroプロジェクト
/update-claude-md --template standard  # 一般プロジェクト
/update-claude-md --template minimal   # 軽量プロジェクト
```

#### 4. 記憶活用による効率化
```bash
# 初回設定
/update-claude-md --auto --memory-key my_project

# 以降の更新
/update-claude-md --use-memory my_project
```

### 品質向上のポイント

1. **バックアップの習慣**: `--backup` オプションの定期使用
2. **プレビュー確認**: 大きな変更前の `--preview` による事前確認
3. **検証の実行**: `--validate` による生成後品質チェック
4. **記憶の整理**: 定期的な記憶内容の見直しと整理

## まとめ

`/update-claude-md` コマンドは、プロジェクト固有のCLAUDE.mdを自動生成・更新する強力なツールです。Serena MCPとSequential Thinking MCPの統合により、インテリジェントな分析と戦略的な統合を実現し、常に最新で高品質なCLAUDE.mdを維持できます。

記憶機能による学習と他コマンドとの連携により、プロジェクトの成長と共に進化する動的なドキュメント管理を提供します。