# Dev3000統合開発支援コマンド

## `/dev-3000 [アクション] [対象] [オプション]` - 包括的開発支援システム（dev3000 + Playwright + Serena統合）
**説明**: dev3000の統合ログ機能、Playwrightのブラウザ自動化、SerenaのコードインテリジェンスとSequential Thinkingの高度な分析能力を組み合わせた、完全な開発ワークフロー管理システムです。

## 主要機能

### 🔧 Dev3000統合 - 統合開発環境
- **統合ログ表示**: サーバー＋ブラウザログを単一タイムラインで管理
- **自動エラー検出**: AIによるエラーパターン認識
- **リアルタイム監視**: インテリジェントアラート付きライブログ監視
- **ブラウザ制御**: Chrome DevTools Protocol経由の直接制御
- **パフォーマンス追跡**: レスポンス時間とリソース使用量の監視

### 🎯 Playwright統合 - E2Eテスト・ブラウザ自動化
- **視覚的回帰テスト**: 自動スクリーンショット比較
- **アクセシビリティテスト**: WCAG準拠検証
- **クロスブラウザテスト**: 複数ブラウザ互換性チェック
- **パフォーマンステスト**: ページロードと操作タイミング測定
- **ユーザージャーニーテスト**: 完全なワークフロー検証

### 🧠 Serena統合 - コードインテリジェンス
- **スマートコード分析**: パターン認識とベストプラクティス提案
- **自動バグ修正**: 一般的な問題の自動解決
- **パフォーマンス推奨**: データ駆動型最適化提案
- **テスト生成**: 自動テストケース作成
- **ドキュメント生成**: 動作分析からのコードドキュメント生成

### 🔍 Sequential Thinking統合 - 高度分析
- **体系的デバッグ**: 段階的問題解決アプローチ
- **根本原因分析**: 複雑な問題の多段階推論
- **最適化戦略**: 構造化された最適化アプローチ
- **証拠ベース推論**: データと証拠に基づく決定支援

## アクション一覧

### ログ分析・モニタリング
| アクション | 説明 | 主要オプション | 例 |
|----------|------|-------------|---|
| `logs` | ログ表示・分析 | `--filter`, `--watch`, `--last` | `/dev logs --filter "ERROR" --watch` |
| `errors` | ブラウザエラー分析 | `--last`, `--context`, `--analyze` | `/dev errors --last 1h --context 5` |
| `monitor` | リアルタイム監視 | `--watch`, `--type`, `--threshold` | `/dev monitor --watch --type memory` |

### デバッグ・問題解決
| アクション | 説明 | 主要オプション | 例 |
|----------|------|-------------|---|
| `debug` | 特定問題のデバッグ | `--fix`, `--interactive`, `--analyze` | `/dev debug "login fails" --fix --interactive` |
| `analyze` | コード分析 | `--file`, `--performance`, `--suggestions` | `/dev analyze --file auth.js --suggestions` |
| `fix` | 自動修正 | `--type`, `--dry-run`, `--validate` | `/dev fix --type "unused-variables" --dry-run` |

### パフォーマンス最適化
| アクション | 説明 | 主要オプション | 例 |
|----------|------|-------------|---|
| `perf` | パフォーマンス分析 | `--component`, `--analyze`, `--optimize` | `/dev perf --component Dashboard --analyze` |

### E2Eテスト・ブラウザ自動化
| アクション | 説明 | 主要オプション | 例 |
|----------|------|-------------|---|
| `e2e` | E2Eテスト実行 | `--scenario`, `--record`, `--verify` | `/dev e2e --scenario login --record` |
| `screenshot` | スクリーンショット取得 | `--selector`, `--full-page`, `--save` | `/dev screenshot --selector #main --save` |
| `browse` | ブラウザ自動化 | `--action`, `--target`, `--value` | `/dev browse --action click --target #submit` |

## 共通オプション

### 基本オプション
| オプション | 短縮形 | 説明 | 例 |
|---------|-------|------|---|
| `--watch` | `-w` | リアルタイム監視 | `/dev logs -w` |
| `--filter` | `-f` | パターンフィルタ | `/dev logs -f "ERROR"` |
| `--last` | `-l` | 最新N件表示 | `/dev logs -l 100` |
| `--context` | `-c` | 前後の行数 | `/dev errors -c 5` |
| `--analyze` | `-a` | Serena深層分析 | `/dev perf -a` |
| `--interactive` | `-i` | インタラクティブモード | `/dev debug -i` |
| `--verbose` | `-v` | 詳細出力 | `/dev debug -v` |

### 高度なオプション
| オプション | 説明 | 例 |
|---------|------|---|
| `--fix` | 自動修正試行 | `/dev debug "auth error" --fix` |
| `--record` | セッション記録 | `/dev e2e -r session.log` |
| `--dry-run` | 実行せずにプレビュー | `/dev fix --dry-run` |
| `--session` | セッション管理 | `/dev monitor --session start` |
| `--baseline` | パフォーマンスベースライン | `/dev monitor --baseline` |
| `--compare` | 比較実行 | `/dev screenshot --compare --baseline` |

## 使用例

### 基本的な使用パターン

#### 1. エラー調査とデバッグ
```bash
# 最新のエラーを前後5行のコンテキストと共に表示
/dev errors --last 50 --context 5

# 特定のエラーパターンを検索
/dev logs --filter "TypeError.*Cannot read" --context 3

# リアルタイムでエラーを監視
/dev logs --watch --filter "ERROR|WARN"

# 具体的な問題をインタラクティブにデバッグ
/dev debug "ログインボタンが機能しない" --fix --interactive
```

#### 2. パフォーマンス分析と最適化
```bash
# ダッシュボードコンポーネントのパフォーマンス分析
/dev perf --analyze --component Dashboard

# メモリリーク検出
/dev monitor --watch --type memory

# バンドルサイズ分析と提案
/dev analyze --bundle --suggestions

# パフォーマンスベースラインの設定
/dev monitor --performance --baseline
```

#### 3. E2Eテストとスクリーンショット
```bash
# 現在の状態のフルページスクリーンショット
/dev screenshot --full-page --save error-state.png

# ユーザー登録シナリオのE2Eテスト
/dev e2e --scenario "user-registration" --record

# インタラクティブなブラウザ操作
/dev browse --action navigate --target "http://localhost:3000"
/dev browse --action click --target "#login-button"
/dev browse --action type --target "#email" --value "test@example.com"
```

#### 4. コード分析と自動修正
```bash
# 認証コンポーネントの分析と改善提案
/dev analyze --file src/components/Auth.js --suggestions

# パフォーマンスボトルネックの検出
/dev analyze --performance --pattern "heavy-computation"

# 未使用変数の自動修正（ドライラン）
/dev fix --type "unused-variables" --dry-run
```

### 高度なワークフロー例

#### 完全なデバッグワークフロー
```bash
# 1. 初期エラー調査
/dev errors --analyze --context 10

# 2. コードコンテキスト分析
/dev analyze --error-location --trace-dependencies

# 3. ブラウザ状態キャプチャ
/dev screenshot --error-state --accessibility

# 4. 体系的デバッグ
/dev debug "具体的なエラーメッセージ" --interactive --fix

# 5. 修正検証
/dev e2e --verify-fix --scenario error-reproduction
```

#### パフォーマンス最適化ワークフロー
```bash
# 1. パフォーマンスベースライン設定
/dev monitor --performance --baseline

# 2. ボトルネック特定
/dev perf --analyze --profile --hotspots

# 3. 最適化計画
/dev analyze --optimize --strategy

# 4. 最適化実装
/dev fix --performance --apply-optimizations

# 5. 改善検証
/dev monitor --performance --compare-baseline
```

#### E2E開発ワークフロー
```bash
# 1. 開発監視
/dev logs --watch --filter "development"

# 2. リアルタイムテスト
/dev e2e --interactive --record

# 3. 視覚的検証
/dev screenshot --compare --baseline

# 4. パフォーマンス検証
/dev monitor --e2e --performance-budget
```

## 統合ワークフローパターン

### 他のコマンドとの連携
```bash
# Debug → Think → Fix ワークフロー
/dev debug "複雑な問題" --analyze
/smart-think "最適化戦略" --serena --use-debug-context
/dev fix --apply-strategy --validate

# E2E → Debug → Optimize ワークフロー
/dev e2e --scenario critical-path --record
/dev analyze --e2e-results --bottlenecks
/dev perf --optimize --e2e-validated

# Monitor → Alert → Auto-fix ワークフロー
/dev monitor --watch --auto-fix --threshold high
```

### セッション管理
```bash
# 包括的監視セッション開始
/dev monitor --session start --record session-2024-01-15

# 以前のセッション再開
/dev monitor --session resume session-2024-01-15

# デバッグ状態の保存
/dev debug --save-state critical-bug-investigation

# デバッグ状態の読み込み
/dev debug --load-state critical-bug-investigation
```

## ベストプラクティス

### 効果的なデバッグ
1. **統合ログから開始**: 常に `logs` アクションから問題調査を始める
2. **パターン検索の活用**: 特定の問題には `--filter` オプションを使用
3. **視覚的コンテキストのキャプチャ**: UI関連の問題では必ずスクリーンショットを取得
4. **体系的思考の適用**: 複雑な問題にはSequential Thinking機能を活用
5. **解決策の保存**: 成功したデバッグアプローチはSerenaメモリに保存

### パフォーマンス最適化
1. **ベースライン確立**: 最適化前に必ず測定
2. **ボトルネックに集中**: Serenaを使って実際のパフォーマンス問題を特定
3. **変更の検証**: Playwright E2Eテストで機能性を確保
4. **継続監視**: dev3000リアルタイム監視を使用
5. **改善の文書化**: 最適化の効果を時系列で追跡

### E2Eテスト戦略
1. **クリティカルパス優先**: コアユーザージャーニーに集中
2. **視覚的検証の包含**: スクリーンショット比較を含める
3. **パフォーマンス予算**: パフォーマンス閾値の設定と監視
4. **アクセシビリティ準拠**: すべてのテストにアクセシビリティチェックを含める
5. **クロスブラウザカバレッジ**: 複数ブラウザ・デバイスでのテスト

## トラブルシューティング

### よくある問題
| 問題 | 解決方法 | 予防策 |
|------|---------|--------|
| "Dev3000接続エラー" | dev3000サーバーの再起動 | dev3000の自動起動設定 |
| "ブラウザ自動化失敗" | Playwrightブラウザの再インストール | 定期的なブラウザ更新 |
| "パフォーマンス分析エラー" | 部分的結果での安全な失敗 | メモリとCPUリソースの監視 |
| "大きなログファイル" | 自動的なクリーンアップ実行 | ログローテーション設定 |

### パフォーマンスのヒント
1. **適切なモードの選択**: 複雑さに応じてモードを選択、必要に応じてエスカレーション
2. **フォーカスエリアの使用**: 特定のフォーカスパラメータでスコープクリープを防止
3. **MCP統合の活用**: 技術的コンテキストにSerena、知識にContext7を使用
4. **決定の文書化**: 重要な分析を再利用・参照のために保存
5. **反復的アプローチ**: 進化する要件にはインタラクティブモードを使用

## システム要件

### 前提条件
- dev3000 MCPサーバー（localhost:3000で実行）
- Playwright MCP（ブラウザ自動化用）
- Serena MCP（コードインテリジェンス用）
- Sequential Thinking MCP（複雑分析用）

### 依存関係
- **dev3000 MCP**: 統合ログとブラウザ制御
- **Playwright MCP**: E2Eテストとブラウザ自動化
- **Serena MCP**: コード分析とインテリジェント修正
- **Sequential Thinking MCP**: 複雑問題解決推論

## 今後の拡張予定

### 計画中の機能
- **モバイルテスト**: React NativeとモバイルWebテストの統合
- **視覚AI**: AI駆動の視覚的回帰検出
- **予測デバッグ**: ML基盤の問題予測
- **チーム分析**: 開発チームの生産性インサイト
- **カスタム統合**: カスタムMCPサーバー向けプラグインシステム
- **クラウド統合**: クラウドベースのテストと監視

### リアルタイムコラボレーション
- **セッション共有**: チームメンバーとのデバッグセッション共有
- **ライブ監視**: 同じアプリケーションを複数の開発者で監視
- **協調デバッグ**: 共有デバッグコンテキストと発見事項
- **知識ベース**: チーム全体のデバッグパターン認識

### 機械学習統合
- **パターン学習**: 成功したデバッグセッションからの学習
- **予測分析**: 問題が発生する前の予測
- **自動最適化**: 学習済み最適化の自動適用
- **スマートアラート**: 履歴データに基づくインテリジェントアラート閾値

## 関連コマンド

### 連携推奨コマンド
- `/smart-think`: 複雑な問題の戦略的思考
- `/debug-error`: 集中的エラーデバッグ
- `/test`: 自動テスト生成・実行
- `/commit`: インテリジェントGitコミット
- `/serena`: 構造化問題解決

### 統合例
```bash
# 包括的開発サイクル
/dev monitor --session development
/dev debug "discovered-issue" --analyze
/smart-think "resolution-strategy" --serena
/dev fix --implement-strategy
/test --validate-fix
/commit --include-analysis
```

このコマンドにより、dev3000の強力な統合機能に加え、Playwright、Serena、Sequential Thinkingとの連携を活用した、包括的で効率的な開発支援環境が実現されます。