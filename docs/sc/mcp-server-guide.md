# SuperClaude MCP サーバーガイド

## 概要
MCPサーバー（Model Context Protocol）は、SuperClaudeの拡張機能を提供する外部Node.jsプロセスです。Claude Codeの機能を大幅に拡張し、専門的なタスクに特化した処理能力を提供します。

## 📋 MCP サーバー一覧

### 1. **Context7** (`--c7` / `--context7`)
- **専門分野**: 公式ライブラリドキュメントとパターン取得
- **主要機能**:
  - 最新の公式ドキュメント取得
  - フレームワーク固有のベストプラクティス
  - バージョン固有の実装パターン
- **自動発動条件**: 
  - `import`, `require`, `from`, `use`文
  - React, Vue, Angular, Next.js等のフレームワーク名
  - ライブラリ固有の質問

### 2. **Sequential** (`--seq` / `--sequential`)
- **専門分野**: 複数ステップの構造化推論
- **主要機能**:
  - 仮説検証アプローチ
  - 多段階問題解決
  - 証拠ベースの分析
- **自動発動条件**:
  - 複雑なデバッグシナリオ
  - アーキテクチャ分析
  - システム設計課題

### 3. **Magic** (`--magic`)
- **専門分野**: モダンUIコンポーネント生成
- **主要機能**:
  - 21st.devパターンベースのUI生成
  - アクセシビリティ準拠コンポーネント
  - モダンデザインシステム統合
- **必要条件**: APIキーが必要
- **自動発動条件**:
  - `/ui`コマンド
  - UIコンポーネントリクエスト
  - フロントエンド開発タスク

### 4. **Playwright** (`--play` / `--playwright`)
- **専門分野**: ブラウザ自動化とE2Eテスト
- **主要機能**:
  - 実ブラウザでの自動テスト
  - 視覚的回帰テスト
  - アクセシビリティ監査
- **自動発動条件**:
  - ブラウザテストリクエスト
  - E2Eシナリオ
  - 視覚的検証が必要なタスク

### 5. **Morphllm** (`--morph` / `--morphllm`)
- **専門分野**: 一括コード変換とパターン適用
- **主要機能**:
  - 大規模なコードベース変換
  - パターンベースの編集
  - スタイル強制適用
- **必要条件**: APIキーが必要
- **自動発動条件**:
  - 一括変換タスク
  - パターンベースの編集
  - 複数ファイルの同期変更

### 6. **Serena** (`--serena`)
- **専門分野**: セマンティックコード理解とセッション永続化
- **主要機能**:
  - シンボルレベルの操作
  - プロジェクトメモリ管理
  - 大規模コードベースナビゲーション
- **自動発動条件**:
  - シンボル操作
  - プロジェクトメモリが必要なタスク
  - 大規模コードベース（>50ファイル）

## 🔧 セットアップと設定

### システム要件
- **Node.js**: 16以上（ほとんどのサーバーで必要）
- **Claude Code**: 最新版
- **SuperClaude**: v4.0.8以上

### インストール確認
```bash
# SuperClaudeがインストールされているかチェック
SuperClaude --version

# MCPサーバーの状態確認
SuperClaude mcp-status
```

### 設定ファイル: `~/.claude.json`
MCPサーバーの設定は`~/.claude.json`ファイルで管理されます：

```json
{
  "mcpServers": {
    "context7": {
      "enabled": true,
      "command": "node",
      "args": ["/path/to/context7/server.js"]
    },
    "sequential-thinking": {
      "enabled": true,
      "command": "node", 
      "args": ["/path/to/sequential/server.js"]
    },
    "magic": {
      "enabled": true,
      "command": "node",
      "args": ["/path/to/magic/server.js"],
      "env": {
        "MAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### APIキー設定（Magic & Morphllm）
```bash
# Magic APIキー設定
export MAGIC_API_KEY="your_magic_api_key"

# Morphllm APIキー設定  
export MORPHLLM_API_KEY="your_morphllm_api_key"
```

## 🎯 使用パターン

### 単一サーバー使用
```bash
# Context7のみを使用
/sc:implement "React認証システム" --c7

# Sequential思考のみを使用
/sc:troubleshoot "複雑なバグ" --seq

# Magicのみを使用
/sc:ui "ダッシュボード" --magic
```

### 複数サーバー連携
```bash
# ドキュメント取得 → 分析 → UI生成
/sc:implement "認証フロー" --c7 --seq --magic

# 分析 → セッション保存 → 一括変換
/sc:analyze codebase/ --seq --serena --morph
```

### 自動サーバー選択
```bash
# 適切なサーバーが自動選択される
/sc:implement "React + TypeScript ログインフォーム"
# → Context7 (React docs) + Magic (UI) が自動発動
```

## 🔍 各サーバーの詳細使用方法

### Context7 活用パターン

#### 公式ドキュメント取得
```bash
# React Hooks の最新パターン取得
/sc:implement "useEffect データフェッチ" --c7

# Next.js 14の新機能使用
/sc:implement "App Router移行" --c7
```

#### バージョン固有の実装
```bash
# 特定バージョンの実装パターン
/sc:analyze "Vue 3 Composition API移行" --c7
```

### Sequential 活用パターン

#### 複雑な問題の体系的解決
```bash
# 多層問題の分析
/sc:troubleshoot "本番パフォーマンス劣化" --seq

# アーキテクチャ設計
/sc:analyze "マイクロサービス設計" --seq --think-hard
```

#### 仮説検証アプローチ
```bash
# 根本原因分析
/sc:troubleshoot "メモリリーク" --seq --introspect
```

### Magic 活用パターン

#### モダンUIコンポーネント生成
```bash
# アクセシビリティ準拠コンポーネント
/sc:ui "データテーブル" --magic --focus accessibility

# レスポンシブデザイン
/sc:ui "管理画面レイアウト" --magic --style tailwind
```

#### デザインシステム統合
```bash
# 一貫性のあるUIパターン
/sc:ui "フォームバリデーション" --magic --c7
```

### Playwright 活用パターン

#### E2Eテスト作成
```bash
# ユーザーフロー全体のテスト
/sc:test "ログイン→ダッシュボード→ログアウト" --play

# クロスブラウザテスト
/sc:test --type e2e --play --coverage
```

#### アクセシビリティ監査
```bash
# WCAG準拠チェック
/sc:analyze "UIアクセシビリティ" --play --focus accessibility
```

### Morphllm 活用パターン

#### 大規模コードベース変換
```bash
# 一括リファクタリング
/sc:improve legacy-code/ --morph --type modernization

# パターン適用
/sc:improve "console.log → logger" --morph
```

### Serena 活用パターン

#### プロジェクトメモリ管理
```bash
# セッション保存・復元
/sc:save "進行中の認証機能実装"
/sc:load "認証機能実装"

# プロジェクト記録
/sc:analyze architecture/ --serena
```

#### シンボルレベル操作
```bash
# 関数名の一括変更
/sc:refactor "getUserData → fetchUserData" --serena

# 依存関係分析
/sc:analyze "クラス依存関係" --serena
```

## 🚀 最適化された組み合わせ

### Web開発フルスタック
```bash
# 設計 → 実装 → テスト の完全フロー
/sc:workflow "Eコマースサイト" --c7 --seq
/sc:implement "フロントエンド" --magic --c7
/sc:implement "バックエンドAPI" --c7 --seq
/sc:test --type e2e --play
```

### レガシーシステム現代化
```bash
# 分析 → 変換 → 検証
/sc:analyze legacy/ --seq --serena --ultrathink
/sc:improve legacy/ --morph --type modernization
/sc:test --type integration --fix
```

### 学習・研究開発
```bash
# 学習 → 実験 → 文書化
/sc:learn "GraphQL" --c7 --seq
/sc:experiment "GraphQL実装" --magic --c7
/sc:document --type tutorial
```

## ⚠️ トラブルシューティング

### 一般的な問題

#### サーバーが起動しない
```bash
# Node.jsバージョン確認
node --version  # 16以上が必要

# サーバー状態確認
SuperClaude mcp-status

# 再起動
SuperClaude mcp-restart
```

#### APIキーエラー
```bash
# 環境変数確認
echo $MAGIC_API_KEY
echo $MORPHLLM_API_KEY

# 設定ファイル確認
cat ~/.claude.json
```

#### パフォーマンス問題
```bash
# 重いサーバーを無効化
/sc:analyze --no-mcp  # 全サーバー無効

# 軽量サーバーのみ使用
/sc:analyze --c7  # Context7のみ
```

### デバッグ方法
```bash
# 詳細ログ表示
/sc:analyze --verbose

# MCPサーバーログ確認
SuperClaude mcp-logs

# 設定リセット
SuperClaude mcp-reset
```

## 🎨 カスタマイゼーション

### カスタムサーバー追加
```json
{
  "mcpServers": {
    "custom-server": {
      "enabled": true,
      "command": "node",
      "args": ["/path/to/custom/server.js"],
      "env": {
        "CUSTOM_CONFIG": "value"
      }
    }
  }
}
```

### サーバー無効化
```json
{
  "mcpServers": {
    "magic": {
      "enabled": false
    }
  }
}
```

MCPサーバーシステムにより、SuperClaudeは単純なコマンドラインツールから、包括的な開発プラットフォームに変貌します。各サーバーの特性を理解し、適切に組み合わせることで、開発効率を劇的に向上させることができます。