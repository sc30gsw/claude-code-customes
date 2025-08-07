# Claude Commands カスタムコマンド集

このリポジトリには、Claude Codeで使用できるカスタムコマンドが含まれています。

## Kiroコマンドシステム

Kiroは、仕様駆動開発（Spec-Driven Development）とテスト駆動開発（TDD）をサポートするコマンドシステムです。

### 利用可能なコマンド

#### 基本ワークフロー

1. **`/kiro:steering`** - プロジェクトのステアリングドキュメントを生成/更新
   - プロジェクト概要、技術スタック、構造を文書化

2. **`/kiro:spec-init [詳細な機能説明]`** - 新しい仕様を初期化
   - 機能の詳細説明から仕様ディレクトリを作成

3. **`/kiro:spec-requirements [機能名]`** - 要件定義を生成
   - EARS形式で要件とユーザーストーリーを作成

4. **`/kiro:spec-design [機能名]`** - 技術設計書を生成
   - アーキテクチャ、データモデル、APIを設計

5. **`/kiro:spec-test [機能名] [オプション]`** - テスト仕様を生成 **(新機能)**
   - TDD用のテスト仕様を自動生成
   - 単体テスト、コンポーネントテスト、フックテスト、APIテスト、E2Eテストをサポート

6. **`/kiro:spec-tasks [機能名]`** - 実装タスクを生成
   - 詳細な実装ステップを作成

7. **`/kiro:spec-status [機能名]`** - 仕様の進捗状況を表示
   - 各フェーズの完了状況を確認

### spec-testコマンドの詳細

#### 基本使用法
```bash
/kiro:spec-test feature-name
```

#### オプション
- `--test-lib=[jest|vitest|mocha]` - 単体テストフレームワーク（デフォルト: vitest）
- `--ui-lib=[testing-library|enzyme]` - UIテストライブラリ（デフォルト: testing-library）
- `--e2e-lib=[playwright|cypress|puppeteer]` - E2Eテストフレームワーク（デフォルト: playwright）
- `--api-lib=[supertest|axios-mock]` - APIテストライブラリ（デフォルト: supertest）
- `--coverage=[数値]` - カバレッジ目標パーセンテージ（デフォルト: 80）
- `--mock-strategy=[manual|auto]` - モック生成戦略（デフォルト: auto）

#### 生成される内容
- **テスト仕様書** - 包括的なテスト戦略ドキュメント
- **単体テスト仕様** - ビジネスロジックとユーティリティのテスト
- **コンポーネントテスト仕様** - Reactコンポーネントのテスト
- **フックテスト仕様** - カスタムフックのテスト
- **APIテスト仕様** - エンドポイントのテスト
- **E2Eテスト仕様** - ユーザーワークフローのテスト
- **モック仕様** - テストデータとサービスモック
- **CI/CD設定** - GitHub Actionsワークフロー

#### TDDワークフロー
1. **Red Phase** - 失敗するテストを先に書く
2. **Green Phase** - テストを通す最小限のコードを実装
3. **Refactor Phase** - テストを維持しながらコードを改善

### ディレクトリ構造

```
.kiro/
├── steering/              # プロジェクト全体の方針
│   ├── product.md        # 製品概要
│   ├── tech.md          # 技術スタック
│   └── structure.md     # プロジェクト構造
└── specs/               # 機能仕様
    └── [feature-name]/
        ├── requirements.md    # 要件定義
        ├── design.md         # 技術設計
        ├── tasks.md          # 実装タスク
        ├── tests/            # テスト仕様
        │   ├── test-spec.md  # テスト仕様書
        │   ├── unit/         # 単体テスト
        │   ├── component/    # コンポーネントテスト
        │   ├── hook/         # フックテスト
        │   ├── api/          # APIテスト
        │   └── e2e/          # E2Eテスト
        └── spec.json         # メタデータと承認状態
```

### 推奨ワークフロー

1. プロジェクト初期化
   ```bash
   /kiro:steering
   ```

2. 新機能の仕様作成
   ```bash
   /kiro:spec-init "ユーザー認証機能を実装したい。メールアドレスとパスワードでログインできるようにする"
   ```

3. 要件定義
   ```bash
   /kiro:spec-requirements user-authentication
   ```

4. 技術設計
   ```bash
   /kiro:spec-design user-authentication
   ```

5. **テスト仕様生成（TDD）**
   ```bash
   /kiro:spec-test user-authentication --test-lib=vitest --e2e-lib=playwright
   ```

6. 実装タスク生成
   ```bash
   /kiro:spec-tasks user-authentication
   ```

7. 進捗確認
   ```bash
   /kiro:spec-status user-authentication
   ```

### 特徴

- **仕様駆動開発**: 要件から実装まで体系的に管理
- **TDD対応**: テストファーストアプローチをサポート
- **自動承認**: インタラクティブな承認プロセス
- **多言語対応**: 日本語/英語での仕様生成
- **柔軟な設定**: プロジェクトに合わせてカスタマイズ可能

---

## その他の利用可能なコマンド

### 開発支援コマンド

#### `/serena [問題] [オプション]` - 高効率な構造化問題解決
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

#### `/test [対象] [オプション]` - 高度なテスト実装・実行
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

#### `/tech-research "[トピック]" [オプション]` - 高度な技術調査
**説明**: 最新技術動向の調査、比較分析、ベストプラクティスの調査を行う高度なリサーチコマンド。

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

**調査オプション**:
| オプション | 説明 | 値 | 例 |
|---------|------|---|---|
| `-d, --depth` | 検索深度 | `quick\|standard\|deep\|exhaustive` | `-d deep` |
| `-t, --template` | レポートテンプレート | `overview\|comprehensive\|academic\|technical` | `-t academic` |
| `-i, --iterations` | 最大反復回数 | 数値 | `-i 10` |
| `-c, --confidence` | 信頼度閾値 | 0-1 | `-c 0.9` |
| `--sources` | 引用文献含む | Boolean | `--sources` |
| `--diagrams` | 図表生成 | Boolean | `--diagrams` |
| `-l, --language` | 出力言語 | `en\|ja\|es\|fr\|de\|zh` | `-l ja` |

**MCPツール組み合わせ**:
| ツール | 用途 | 適用場面 |
|-------|------|---------|
| `context7` | ライブラリドキュメント・例 | フレームワーク調査、API文書 |
| `sequential` | ステップ別推論 | 複雑な分析・アルゴリズム |
| `playwright` | Web自動化 | ライブテスト・スクリーンショット |
| `serena` | 構造化問題解決 | 実装計画 |

**使用例**:
```bash
# クイック調査
/tech-research "Redis vs Memcached" -d quick -t overview

# 包括的分析
/tech-research "React 18新機能" -t comprehensive -m think-hard

# 学術的調査
/tech-research "機械学習トレンド" -t academic --sources --diagrams -c 0.95

# 技術実装重点
/tech-research "REST API設計" -t technical -m think-harder

# MCPツール組み合わせ
/tech-research "Next.js 14機能" --mcp "context7"                    # ドキュメント調査
/tech-research "量子コンピューティング" --mcp "sequential" -m ultrathink  # 複雑分析
/tech-research "UI フレームワーク 2024" --mcp "playwright,context7" --diagrams  # ライブ調査
```

**主な機能**:
- WebSearch、WebFetch機能による最新情報収集
- 4段階の思考モード（think、think-hard、think-harder、ultrathink）
- 技術仕様書やベストプラクティスの調査
- 図表やダイアグラムの自動生成
- Context7との連携によるライブラリドキュメント参照
- 引用文献・信頼度評価機能

#### `/spec:requirements [システム名] [オプション]` - 包括的要件定義
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

**値のオプション**:
- **priority**: `low`, `medium`, `high`, `critical`
- **scope**: `mvp`, `full`, `enterprise`
- **template**: `standard`, `agile`, `waterfall`

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

### Git・GitHub連携コマンド

#### `/git:pr [オプション]` - インテリジェントなプルリクエスト生成
**説明**: 変更内容を自動分析してプルリクエストの説明文を生成し、GitHub上にPRを自動作成。

**オプション**:
| オプション | 説明 | 動作 |
|---------|------|------|
| （オプションなし） | 標準PR作成 | PR説明生成 → 自動作成 |
| `-p` | プッシュ後PR作成 | ブランチをプッシュ → PR作成 |
| `-u` | 既存PR更新のみ | PR説明のみ更新（作成なし） |

**標準動作フロー**:
1. Serenaオンボーディング実行
2. Git変更内容の自動分析（`git diff`, `git log`）
3. PRテンプレート読み込み（`.github/pull_request_template.md`）
4. Context7 MCPでドキュメントURL取得
5. Mermaid図表を含むPR説明生成（日本語）
6. `gh pr create --draft` でドラフトPR作成
7. 成功パターンをメモリに保存

**使用例**:
```bash
# 標準PR作成
/git:pr                    # 変更分析 → PR説明生成 → 作成

# ブランチプッシュ後PR作成
/git:pr -p                 # git push → 変更分析 → PR作成

# 既存PR更新
/git:pr -u                 # 既存PR説明のみ更新
```

**主な機能**:
- Git変更履歴の自動分析（`git diff`, `git log`, `git status`）
- コミットメッセージからの意図推定
- プルリクエストテンプレートとの連携
- Serena MCPによる高速ファイル分析・シンボル解析
- Context7連携による関連ドキュメントURL取得
- Mermaid図表による変更の可視化
- GitHub APIを使用した自動PR作成・更新

#### `/dependabot-check [URL]` - セキュリティ脆弱性解決
**説明**: Dependabotアラートを分析し、セキュリティ脆弱性の解決戦略を提供。

**URL形式**:
| URL種類 | 形式 | 用途 |
|---------|------|------|
| **Dependabotアラート** | `https://github.com/owner/repo/security/dependabot/[number]` | セキュリティアラート分析 |
| **Dependabot PR** | `https://github.com/owner/repo/pull/[number]` | 依存関係更新PR分析 |

**分析内容**:
1. **アラート情報収集**: GitHub APIでアラート詳細を取得
2. **脆弱性評価**: CVSS スコア、影響範囲、攻撃ベクターの分析
3. **依存関係分析**: 影響を受けるパッケージとバージョンの特定
4. **修正戦略策定**: 更新手順、代替手法、回避策の提案
5. **自動化スクリプト生成**: 修正用コマンド・スクリプトの生成

**使用例**:
```bash
# Dependabotセキュリティアラート分析
/dependabot-check https://github.com/owner/repo/security/dependabot/123

# Dependabot PR分析
/dependabot-check https://github.com/owner/repo/pull/456

# ローカルプロジェクトでのパッケージ脆弱性チェック
/dependabot-check  # package.jsonから脆弱性検出
```

**主な機能**:
- GitHub Security Advisoryの詳細分析
- CVSS スコアに基づく脆弱性リスク評価
- 影響範囲の可視化（依存関係ツリー）
- 修正優先度の自動判定
- 複数修正手法の比較提示（メジャーアップデート、パッチ適用、代替パッケージ）
- 修正後の影響評価・テスト提案
- 自動化された修正スクリプト・コマンド生成

### UI/UX設計コマンド

#### `/ui-advice [要件]` - UI/UXデザインパターン提案
**説明**: UI/UXの専門知識に基づき、デザインパターンの提案とテキストワイヤーフレームを生成。

**提案内容**:
1. **デザインパターン提案**: 要件に適した3-5種類のパターンを提示
2. **パターン説明**: 各パターンの特徴・メリット・デメリット・適用場面
3. **テキストワイヤーフレーム**: ASCII形式でレイアウト構造を可視化
4. **推奨提案**: 状況に応じた最適パターンの選択理由

**考慮要素**:
- **アクセシビリティ**: WCAG準拠、スクリーンリーダー対応
- **レスポンシブデザイン**: モバイルファースト、ブレークポイント設計
- **ユーザビリティ**: 認知負荷軽減、直感的な操作性
- **視覚デザイン**: 階層構造、視覚的重要度、ブランド一貫性

**対応要件例**:
| 要件カテゴリ | 例 |
|------------|---|
| **フォーム系** | ログインフォーム、登録画面、検索フォーム |
| **ナビゲーション系** | メニュー、パンくずリスト、タブ |
| **データ表示系** | ダッシュボード、テーブル、カード |
| **インタラクション系** | モーダル、ドロップダウン、ツールチップ |
| **レスポンシブ系** | モバイル対応、タブレット最適化 |

**使用例**:
```bash
# 基本的なUI要素
/ui-advice "ログインフォーム"
/ui-advice "商品一覧カード"
/ui-advice "管理画面ダッシュボード"

# 複雑なインタラクション
/ui-advice "多段階フォーム"
/ui-advice "データテーブルのフィルタリング"
/ui-advice "リアルタイム通知システム"

# レスポンシブ・アクセシビリティ重視
/ui-advice "モバイル対応のナビゲーション"
/ui-advice "視覚障害者対応の検索インターフェース"
```

**主な機能**:
- 世界的に認知されたデザインパターンライブラリに基づく提案
- 3-5種類のデザインパターン提案（Material Design、Apple HIG、独自パターン等）
- 各パターンの特徴・メリット・デメリット・実装複雑度の詳細説明
- ASCII形式のテキストワイヤーフレーム生成
- 状況に応じた最適パターンの推奨とその理由
- WCAG、モバイルファースト、ユーザビリティを考慮した設計指針

---

## 全コマンド一覧

| コマンド | カテゴリ | 説明 |
|---------|---------|------|
| `/kiro:steering` | Kiro基本 | プロジェクトステアリング文書の生成・更新 |
| `/kiro:spec-init` | Kiro基本 | 新機能仕様の初期化 |
| `/kiro:spec-requirements` | Kiro基本 | EARS形式要件定義の生成 |
| `/kiro:spec-design` | Kiro基本 | 技術設計書の生成 |
| `/kiro:spec-test` | Kiro基本 | TDDテスト仕様の生成 |
| `/kiro:spec-tasks` | Kiro基本 | 実装タスクの生成 |
| `/kiro:spec-status` | Kiro基本 | 仕様進捗の表示 |
| `/serena` | 開発支援 | 構造化問題解決・デバッグ・設計 |
| `/test` | 開発支援 | 高度なテスト実装・実行・修正 |
| `/tech-research` | 開発支援 | 技術調査・比較分析・ベストプラクティス |
| `/spec:requirements` | 開発支援 | 包括的要件定義書の生成 |
| `/git:pr` | Git・GitHub | インテリジェントなPR生成 |
| `/dependabot-check` | Git・GitHub | セキュリティ脆弱性解決 |
| `/ui-advice` | UI/UX | デザインパターン提案・ワイヤーフレーム |

