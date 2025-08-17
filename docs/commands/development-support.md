# 開発支援コマンド

## `/commit [オプション]` - インテリジェントなGitコミット自動化（Serena統合）
**説明**: Serena MCPを活用した高度なコミット自動化システム。変更内容の意味的分析、git履歴学習、コンテキスト認識によるコミットメッセージ生成を行います。

**主要オプション**:
| オプション | 短縮形 | 説明 | 例 |
|---------|-------|------|---------|
| `--no-verify` | | pre-commitチェックをスキップ | `/commit --no-verify` |
| `--analyze` | `-a` | Serena深層分析を有効化 | `/commit -a` |
| `--learning` | `-l` | git履歴パターンから学習 | `/commit -l` |
| `--scope` | `-s` | コミットスコープを設定 | `/commit -s feature` |
| `--batch` | `-b` | 複数の関連変更をグループ化 | `/commit -b` |
| `--interactive` | `-i` | インタラクティブなメッセージ調整 | `/commit -i` |
| `--semantic-grouping` | | 高度な変更グループ化を有効化 | `/commit --semantic-grouping` |
| `--impact-analysis` | | 変更の潜在的影響を分析 | `/commit --impact-analysis` |

**使用例**:
```bash
# 基本的なスマートコミット
/commit

# 機能開発での学習付きコミット
/commit --scope=feature --learning --analyze

# リファクタリングでの意味的グループ化
/commit --template=refactor --semantic-grouping

# 大規模変更での影響分析付きバッチコミット
/commit --batch --impact-analysis --interactive
```

**主な機能**:
- Serena MCPによるコードベース理解とパターン認識
- Git履歴からのコミット規約学習と適応
- conventional commitフォーマットでの絵文字付きメッセージ自動生成
- 変更の意味的分析による適切なコミット分割提案
- チーム固有のコミットパターンへの継続的適応

## `/debug-error "[エラー説明]" [オプション]` - インテリジェントデバッグシステム（Serena統合）
**説明**: Serena MCPを活用した高度なデバッグシステム。パターン認識、シンボル追跡、過去の解決例学習により効率的なエラー解決を実現します。

**主要オプション**:
| オプション | 短縮形 | 説明 | 例 |
|---------|-------|------|---------|
| `--analyze` | `-a` | Serena深層分析を有効化 | `/debug-error "crash" -a` |
| `--trace` | `-t` | コードフロー追跡 | `/debug-error "logic error" -t` |
| `--serena-deep` | `-s` | 完全なSerenaツールキット使用 | `/debug-error "complex bug" -s` |
| `--pattern-search` | `-p` | 類似エラーパターンを検索 | `/debug-error "timeout" -p` |
| `--memory` | `-m` | デバッグメモリを使用 | `/debug-error "recurring issue" -m` |
| `--interactive` | `-i` | ステップバイステップガイダンス | `/debug-error "unknown issue" -i` |
| `--implement` | | 修正を自動実装 | `/debug-error "known solution" --implement` |
| `--document` | `-d` | デバッグプロセスを文書化 | `/debug-error "complex issue" -d` |

**使用例**:
```bash
# パターン検索付き基本デバッグ
/debug-error "NullPointerException in UserService" --pattern-search

# Serena深層分析
/debug-error "performance degradation" --analyze --serena-deep

# コードフロー追跡とメモリ活用
/debug-error "auth flow broken" --trace --memory

# 複雑な問題のインタラクティブデバッグ
/debug-error "mysterious crash" --interactive --step-by-step
```

**主な機能**:
- Serena MCPによるシンボルレベルのエラー分析
- 過去のデバッグセッションからの学習とパターン適用
- コードベース全体での類似問題パターン検索
- 精密なコード修正とインパクト評価
- デバッグ専門知識の蓄積と再利用

## `/smart-think "[問題説明]" [オプション]` - 高度な多段階思考システム（Serena統合）
**説明**: Sequential Thinking MCPとSerena MCPを統合した高度な問題解決システム。4段階の思考モードで複雑な技術的意思決定をサポートします。

**思考モード**:
| モード | 予算範囲 | 思考数 | 信頼度 | 最適用途 |
|-------|---------|-------|--------|----------|
| `think` | 2,000-8,000 | 3-6 | 70-85% | 迅速な決定、シンプルな問題 |
| `think-hard` | 8,000-15,000 | 6-10 | 75-90% | 複雑な分析、設計決定 |
| `think-harder` | 15,000-25,000 | 10-15 | 80-95% | アーキテクチャ、重要な決定 |
| `ultrathink` | 25,000-50,000 | 15-25 | 85-98% | 研究レベル、複雑システム |

**主要オプション**:
| オプション | 短縮形 | 説明 | デフォルト | 例 |
|---------|-------|-------------|---------|----------|
| `--mode` | `-m` | 思考モード | `think` | `-m ultrathink` |
| `--budget` | `-b` | トークン予算 | 自動 | `-b 15000` |
| `--serena` | `-s` | Serena統合を使用 | false | `-s` |
| `--interactive` | `-i` | インタラクティブ改良 | false | `-i` |
| `--research` | `-r` | 調査フェーズを含む | false | `-r` |
| `--structured` | | 構造化出力 | false | `--structured` |
| `--confidence` | | 信頼度レベル表示 | false | `--confidence` |
| `--focus` | `-f` | 焦点領域 | なし | `-f security` |

**使用例**:
```bash
# デフォルト思考モード
/smart-think "Redux vs Zustandどちらを使うべきか？"

# コードベースコンテキスト付き深層分析
/smart-think "データベース移行戦略" -m think-harder --serena

# インタラクティブ問題解決
/smart-think "API設計アプローチ" -m think-hard --interactive

# 引用付き研究重点
/smart-think "技術選定" -m ultrathink --research --citations

# 予算制御付きクイック決定
/smart-think "CSSフレームワーク選択" -b 5000 --focus=frontend
```

**主な機能**:
- Sequential Thinking MCPによる構造化された仮説生成・検証
- Serena MCPによるコードベース認識型技術決定
- 証拠ベースの推論と信頼度追跡
- 複数視点からの包括的分析
- 実装ロードマップとリスク評価

## `/serena [問題] [オプション]` - 高効率な構造化問題解決
**説明**: トークン効率を重視した構造化された問題解決コマンド。複雑な開発問題の分析・設計・実装を段階的に行います。

**オプション**:
| オプション | 説明 | 使用例 |
|---------|------|-------|
| `-q` | クイックモード（3-5思考） | `/serena "ボタンを修正" -q` |
| `-d` | ディープモード（10-15思考） | `/serena "アーキテクチャ設計" -d` |
| `-c` | コード重点分析 | `/serena "パフォーマンス最適化" -c` |
| `-s` | ステップバイステップ実装 | `/serena "ダッシュボード構築" -s` |
| `-v` | 詳細出力（プロセス表示） | `/serena "問題デバッグ" -v` |
| `-r` | 調査フェーズ含む | `/serena "フレームワーク選択" -r` |
| `-t` | 実装TODOの作成 | `/serena "新機能" -t` |

**使用例**:
```bash
# 基本的な問題解決
/serena "ログインバグを修正"

# パターン指定
/serena debug "プロダクションでのメモリリーク"      # デバッグパターン（5-8思考）
/serena design "認証システム"                    # 設計パターン（8-12思考）
/serena review "このコードを最適化したい"           # レビューパターン（4-7思考）
/serena implement "機能Xを追加" -q               # クイックモード（3-5思考）

# 高度な組み合わせ
/serena "マイクロサービス設計" -d -r -v          # 深い調査と詳細出力
/serena "チャート付きダッシュボード" -s -t -c     # ステップ実装+TODO+コード重点
```

**主な機能**:
- 構造化された思考プロセスで問題を分析
- デバッグ、設計、レビュー、実装のパターン別最適化
- トークン効率を重視した高速処理
- MCPとSerenaツールとの統合

## `/test [対象] [オプション]` - 高度なテスト実装・実行
**説明**: 単体テストとE2Eテストの自動生成、実行、修正機能を提供する包括的なテストコマンド。

**基本オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-u` | 単体テストモード | ✅ |
| `-e` | E2Eテスト + アクセシビリティ属性注入 | - |
| `-r` | 自動実行・修正（最大10回試行） | - |
| `-v` | 詳細出力モード | - |
| `-c` | カバレッジ重視モード（90%+目標） | - |
| `-p` | パフォーマンステストモード | - |
| `-w` | ウォッチモード（ファイル変更時自動再実行） | - |
| `-f` | 高速モード（並列実行・キャッシュ） | - |

**高度なオプション**:
| オプション | 説明 | 例 |
|---------|------|---|
| `--skip-lint` | リンター実行をスキップ | `--skip-lint` |
| `--dry-run` | テスト設計のみ（ファイル作成なし） | `--dry-run` |
| `--parallel=N` | 並列実行数指定 | `--parallel=8` |
| `--timeout=N` | タイムアウト秒数指定 | `--timeout=60` |
| `--files=PATTERN` | Globパターンでファイル指定 | `--files="Button*"` |
| `--exclude=PATTERN` | Globパターンで除外 | `--exclude="*.test.*"` |
| `--include-deps` | 依存ファイルも含める | `--include-deps` |

**使用例**:
```bash
# 基本使用
/test UserService                    # 単体テスト生成・実行
/test LoginForm -e -r               # E2Eテスト生成・実行・修正
/test utils/auth -u -r -c           # 高カバレッジ単体テスト

# ファイルパターン指定
/test components --files="Button*" -u -r        # すべてのButtonコンポーネント
/test . --files="**/*.hook.ts" -u -c            # カスタムフック全て
/test api --files="**/*Controller.ts" --include-deps -u -r  # コントローラーと依存関係

# パフォーマンス・高速実行
/test heavyComponent -u -p -f --parallel=8      # 高速並列パフォーマンステスト
/test ActiveComponent -u -w -f                  # ウォッチモード + 高速実行
```

**主な機能**:
- Jest、Vitest、Cypress、Playwrightサポート
- テストの自動生成と実行
- 失敗テストの自動修正機能（最大10回試行）
- カバレッジレポート生成
- Globパターンによるファイル一括処理
- 依存関係の自動分析・包含

## `/tech-research "[トピック]" [オプション]` - 高度な技術調査（Serena統合強化版）
**説明**: Serena MCPによるコードベース認識型技術調査システム。既存の実装パターンを理解した上で、実装可能性と互換性を考慮した技術研究を行います。

**思考モード**:
| モード | トークン予算 | 深度 | 用途 |
|-------|------------|------|------|
| `think` | 10,000 | 標準分析 | 概要調査 |
| `think-hard` | 20,000 | 強化検証 | 詳細比較 |
| `think-harder` | 30,000 | 構造化推論 | 複雑な意思決定 |
| `ultrathink` | 50,000 | 最大深度 | 学術的批判分析 |

**基本オプション**:
| オプション | 説明 | デフォルト | 例 |
|---------|------|----------|---|
| `-m, --mode` | 思考モード | `think` | `-m ultrathink` |
| `-b, --budget` | トークン予算 | 自動 | `-b 25000` |
| `-o, --output` | 出力ファイル | `research-report.md` | `-o analysis.md` |
| `-f, --format` | 出力形式 | `markdown` | `-f json` |
| `--mcp` | 使用MCPツール | `all` | `--mcp "context7"` |

**Serena統合オプション**:
| オプション | 説明 | 例 | 用途 |
|---------|-------------|---------|----------|
| `--serena` | **Serena MCP統合を有効化** | `--serena` | **すべての技術調査で推奨** |
| `--serena-context` | 現在のコードベースコンテキストを含む | `--serena-context` | アーキテクチャ認識調査 |
| `--current-patterns` | 既存コードパターンを分析 | `--current-patterns` | パターンベース推奨 |
| `--implementation-plan` | 実装ロードマップを生成 | `--implementation-plan` | 実行可能な調査結果 |
| `--compatibility-check` | コードベース互換性チェック | `--compatibility-check` | 技術評価 |
| `--decision-history` | 過去の決定コンテキストを含む | `--decision-history` | 過去の調査の継続 |

**使用例（Serena統合強化）**:
```bash
# コードベース認識クイック調査（推奨デフォルト）
/tech-research "Redis vs Memcached for our app" --serena -d quick --compatibility-check

# パターン分析付き包括的調査
/tech-research "React アーキテクチャパターン" --serena -t comprehensive --current-patterns

# 実装計画付き技術評価
/tech-research "GraphQL導入戦略" --serena -m think-hard --implementation-plan --decision-history

# 実装ロードマップ付き学習
/tech-research "Rust for web development" --serena -t technical --mcp "context7" --implementation-plan

# 全機能統合での戦略的調査
/tech-research "マイクロサービスアーキテクチャ" --serena -m ultrathink --current-patterns --implementation-plan --compatibility-check
```

**主な機能（Serena統合強化）**:
- **Serena MCPによるコードベース認識型調査**（既存パターン理解）
- **実装可能性評価**（現在のアーキテクチャとの互換性）
- **パターンベース推奨**（成功した実装パターンの適用）
- **決定継続性**（過去の調査・決定との一貫性維持）
- WebSearch、WebFetch機能による最新情報収集
- Context7との連携によるライブラリドキュメント参照
- 実装ロードマップと移行戦略の自動生成
- 技術的負債と保守性を考慮した推奨

## `/spec:requirements [システム名] [オプション]` - 包括的要件定義
**説明**: プロジェクトの要件定義書を自動生成し、技術選定と改善提案も含めた包括的なドキュメントを作成。

**オプション**:
| オプション | 短縮形 | 説明 | 例 |
|---------|-------|------|---|
| `--app` | `-a` | アプリケーション名 | `-a "Web Store"` |
| `--function` | `-f` | 機能/特徴名 | `-f "認証"` |
| `--file` | - | 追加要件の入力ファイル | `--file existing-req.txt` |
| `--dir` | - | 追加要件のディレクトリ | `--dir requirements` |
| `--output` | `-o` | 出力ファイルパス | `-o specs.md` |
| `--tech` | `-t` | 技術スタック | `-t "react,nodejs,postgresql"` |
| `--priority` | `-p` | 優先度レベル | `-p high` |
| `--scope` | `-s` | スコープタイプ | `-s mvp` |
| `--suggest` | - | 改善提案含む | `--suggest` |
| `--examples` | - | 実装例含む | `--examples` |
| `--template` | - | テンプレートタイプ | `--template agile` |
| `--hearing` | - | インタラクティブモード | `--hearing` |

**使用例**:
```bash
# 基本的な要件定義
/spec:requirements "ECサイト" -a "Web Store" -t "react,nodejs"

# MVP版で提案付き
/spec:requirements "SNSアプリ" -s mvp -p medium --suggest

# エンタープライズ版で実装例付き
/spec:requirements "CRMシステム" -s enterprise -t "react,nodejs,postgresql" --examples --template agile

# 既存要件の取り込み
/spec:requirements "決済API" --file legacy-specs.txt -t "nodejs,mongodb"

# 抽象的要件に対するインタラクティブモード
/spec:requirements "モバイルアプリ" --hearing
/spec:requirements "業務システム" -p high --hearing --suggest
```

**主な機能**:
- 機能要件・非機能要件の詳細定義
- 技術スタックの推奨と選定理由
- 既存プロジェクト構造の分析と連携
- テンプレートベースでの高速生成（標準、アジャイル、ウォーターフォール）
- 改善提案とリスク分析
- インタラクティブな要件聞き取りモード