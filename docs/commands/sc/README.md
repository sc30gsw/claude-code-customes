# SuperClaude (SC) コマンドディレクトリ

SuperClaudeフレームワークのコアコマンド一覧です。

## コマンド一覧

### ヘルプ・リファレンス
| コマンド | 説明 |
|---------|------|
| [/sc:help](./help.md) | 利用可能な/scコマンドとフラグの一覧表示 |

### オーケストレーション
| コマンド | 説明 |
|---------|------|
| [/sc:pm](./pm.md) | プロジェクトマネージャーエージェント（常時アクティブ） |
| [/sc:spawn](./spawn.md) | メタシステムタスクオーケストレーション |
| [/sc:task](./task.md) | 複雑タスク実行と管理 |
| [/sc:workflow](./workflow.md) | PRDから実装ワークフロー生成 |
| [/sc:brainstorm](./brainstorm.md) | ソクラテス式対話による要件探索 |

### 分析・レビュー
| コマンド | 説明 |
|---------|------|
| [/sc:analyze](./analyze.md) | コード品質・セキュリティ・パフォーマンス分析 |
| [/sc:explain](./explain.md) | コード・コンセプトの教育的説明 |
| [/sc:reflect](./reflect.md) | タスク反省と検証 |
| [/sc:research](./research.md) | 深掘り調査 |
| [/sc:select-tool](./select-tool.md) | インテリジェントMCPツール選択 |
| [/sc:business-panel](./business-panel.md) | マルチエキスパートビジネス分析 |
| [/sc:spec-panel](./spec-panel.md) | エキスパート仕様レビューパネル |

### 開発・実装
| コマンド | 説明 |
|---------|------|
| [/sc:implement](./implement.md) | 機能実装（ペルソナ・MCP連携） |
| [/sc:design](./design.md) | システム・API・コンポーネント設計 |
| [/sc:build](./build.md) | ビルド・パッケージング |
| [/sc:test](./test.md) | テスト実行と品質保証 |
| [/sc:estimate](./estimate.md) | 開発見積もり |

### 改善・最適化
| コマンド | 説明 |
|---------|------|
| [/sc:improve](./improve.md) | コード品質・パフォーマンス・保守性向上 |
| [/sc:cleanup](./cleanup.md) | デッドコード削除・構造最適化 |
| [/sc:troubleshoot](./troubleshoot.md) | 問題診断と解決 |

### ドキュメント
| コマンド | 説明 |
|---------|------|
| [/sc:document](./document.md) | コンポーネント・API向けドキュメント生成 |
| [/sc:index](./index.md) | プロジェクト知識ベース生成 |

### セッション管理
| コマンド | 説明 |
|---------|------|
| [/sc:load](./load.md) | プロジェクトコンテキストのロード |
| [/sc:save](./save.md) | セッションコンテキストの永続化 |

### Git操作
| コマンド | 説明 |
|---------|------|
| [/sc:git](./git.md) | インテリジェントGit操作 |

## フラグ一覧

詳細なフラグ情報は [/sc:help](./help.md) を参照してください。

### 主要フラグ

| フラグ | 説明 |
|-------|------|
| `--think` | 標準分析モード（Sequential MCP有効化） |
| `--think-hard` | 深層分析モード（Sequential + Context7） |
| `--ultrathink` | 最大深度分析（全MCP有効化） |
| `--brainstorm` | ブレインストーミングモード |
| `--delegate` | サブエージェント並列処理 |
| `--safe-mode` | 安全モード（最大検証） |

## 使用方法

```bash
# 基本使用
/sc:analyze src/

# フラグ付き使用
/sc:implement --think-hard "Add user authentication"

# 複合使用
/sc:task --delegate auto --validate "Refactor auth system"
```
