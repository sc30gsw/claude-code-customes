# Serena Skill

## 概要

構造化されたアプリ開発と問題解決のためのトークン効率の良いSerena MCPコマンド。デバッグ、設計、レビュー、実装のパターンを提供し、インテリジェントな開発支援を実現します。

## アクティベーショントリガー

- 複雑な問題解決が必要な時
- コードベースの分析が必要な時
- 実装タスクの計画と実行時
- デバッグセッションの開始時

## 使用方法

```bash
/serena <problem> [options]
```

## クイックリファレンス

```bash
/serena <problem> [options]           # 基本使用
/serena debug "memory leak in prod"   # デバッグパターン (5-8思考)
/serena design "auth system"          # 設計パターン (8-12思考)
/serena review "optimize this code"   # レビューパターン (4-7思考)
/serena implement "add feature X"     # 実装 (6-10思考)
```

## オプション

| オプション | 説明 | 例 |
|------------|------|-----|
| `-q` | クイックモード (3-5思考) | `/serena "fix button" -q` |
| `-d` | ディープモード (10-15思考) | `/serena "architecture design" -d` |
| `-c` | コードフォーカス分析 | `/serena "optimize performance" -c` |
| `-s` | ステップバイステップ実装 | `/serena "build dashboard" -s` |
| `-v` | 詳細出力 | `/serena "debug issue" -v` |
| `-r` | リサーチフェーズを含む | `/serena "choose framework" -r` |
| `-t` | 実装TODOを作成 | `/serena "new feature" -t` |

## Serena MCPツール優先

### プライマリ開発ツール
- `mcp__serena__get_symbols_overview` - プロジェクト分析
- `mcp__serena__search_for_pattern` - コード検索
- `mcp__serena__find_symbol` - シンボル管理
- `mcp__serena__replace_symbol_body` - コード修正

### メモリ＆学習
- `mcp__serena__write_memory` - 知識保存
- `mcp__serena__read_memory` - 経験取得
- `mcp__serena__think_about_task_adherence` - 進捗追跡

## 問題別テンプレート

### デバッグパターン (5-8思考)
1. 症状分析＆再現
2. エラーコンテキスト＆環境チェック
3. 根本原因仮説生成
4. 証拠収集＆検証
5. 解決策設計＆リスク評価

### 設計パターン (8-12思考)
1. 要件明確化
2. 制約＆前提条件
3. アーキテクチャオプション生成
4. オプション評価（長所/短所）
5. 技術選定
6. 実装フェーズ

### 実装パターン (6-10思考)
1. 機能仕様＆スコープ
2. 技術アプローチ選択
3. コンポーネント/モジュール設計
4. 依存関係＆統合
5. テスト戦略

## クロスコマンド統合

Serena MCPは他のコマンドと統合:

| コマンド | 統合 |
|----------|------|
| `/commit` | Git履歴 + 変更分析 |
| `/debug-error` | シンボル追跡 + パターン検索 |
| `/smart-think` | コードベースコンテキスト + メモリ |

## 使用例

### デバッグセッション
```bash
/serena debug "API returning 500 error on login" -v
```

出力:
```markdown
## Debug Session: API 500 Error

### Symptom Analysis
- Error occurs on login endpoint
- Started after recent deployment

### Root Cause Hypothesis
1. Database connection pool exhausted
2. Authentication service timeout
3. Invalid token validation

### Evidence Gathered
- Error logs show timeout at auth.service.ts:45
- Connection pool at 100% utilization

### Solution
- Increase pool size
- Add retry logic
- Implement circuit breaker
```

### 設計セッション
```bash
/serena design "notification system" -d
```

### 実装セッション
```bash
/serena implement "user profile page" -s -t
```

## ベストプラクティス

1. **問題分析から開始** - 具体的なアクションで終了
2. **深さとトークン効率のバランス**
3. **シンプルな問題には`-q`を使用**（約40%トークン節約）
4. **`--focus`で無関係な分析を回避**

## メモリ活用

### セッション間の継続性
```bash
# 前回のセッション情報を読み込み
/serena "continue auth implementation" -r
```

### 学習の蓄積
- 成功パターンを保存
- 失敗から学習
- プロジェクト固有の知識を蓄積

## 成功指標

- 問題が正確に分析される
- 適切な思考深度で処理される
- トークン使用が効率的
- 具体的なアクションが提案される
- 知識が蓄積される
