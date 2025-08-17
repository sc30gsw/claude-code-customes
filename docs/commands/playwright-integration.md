# Playwright MCPインテグレーションコマンド

## `/e2e [対象] [オプション]` - E2Eテスト実行・動作検証
**説明**: Playwright MCPとSerenaツールを統合したアプリケーション動作テストと仕様検証。

**主要オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-s, --spec` | 仕様書との比較検証 | false |
| `-r, --report` | 詳細レポート生成 | false |
| `-i, --interactive` | インタラクティブモード | false |
| `-w, --wait` | 要素表示待機時間（秒） | 5 |
| `-d, --device` | デバイスエミュレーション | desktop |
| `--headless` | ヘッドレスモード | true |
| `--network` | ネットワーク監視 | false |

**使用例**:
```bash
# 基本ページテスト
/e2e https://myapp.com/login

# 仕様検証とレポート生成
/e2e /checkout -s -r

# モバイルデバイステスト
/e2e https://myapp.com -d mobile -r

# ネットワーク監視付きテスト
/e2e /api-heavy-page --network --console -r
```

**主な機能**:
- アプリケーション動作の自動検証
- 仕様書との動作比較
- インタラクティブテスト実行
- マルチデバイス対応
- 詳細なレポート生成

## `/web-analyzer [URL] [オプション]` - ウェブサイト分析・仕様抽出
**説明**: Playwright MCPとSerenaツールを使用したウェブサイト構造・UI・UXの分析と開発用参考資料の自動生成。

**主要オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-d, --deep` | 深層分析（複数ページ） | false |
| `-u, --ui-focus` | UI重点分析 | false |
| `-x, --ux-flow` | UXフロー分析 | false |
| `-t, --tech-stack` | 技術スタック検出 | false |
| `-c, --components` | コンポーネント仕様抽出 | false |
| `-m, --mobile` | モバイル版分析 | false |
| `-r, --report` | 詳細レポート生成 | false |
| `-s, --screenshots` | 各セクションのスクリーンショット | false |

**使用例**:
```bash
# 基本サイト分析
/web-analyzer https://example.com

# UI重点詳細分析
/web-analyzer https://design-system.com -u -c -s

# UXフローとモバイル分析
/web-analyzer https://ecommerce-site.com -x -m -r

# 完全競合分析
/web-analyzer https://competitor.com -d -u -x -t -c -m -r -s
```

**主な機能**:
- HTMLページ構造解析
- デザインシステム要素抽出
- UXフローの可視化
- 技術スタック検出
- Reactコンポーネント仕様生成
- 競合比較分析

## `/visual-regression [対象] [オプション]` - ビジュアルリグレッションテスト
**説明**: Playwright MCPとSerenaツールを統合したビジュアル変更検出と意図しない修正の防止。

**主要オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-b, --baseline` | ベースライン画像作成 | false |
| `-c, --compare` | 既存ベースラインとの比較 | true |
| `-f, --full-page` | フルページスクリーンショット | false |
| `-m, --mobile` | モバイル版同時テスト | false |
| `-d, --devices` | 複数デバイステスト | desktop |
| `-t, --threshold` | 差異許容閾値（%） | 0.2 |
| `-i, --ignore-regions` | 無視領域指定 | none |
| `-r, --report` | 詳細レポート生成 | false |
| `-a, --auto-update` | 差異発生時自動更新確認 | false |

**使用例**:
```bash
# 初期ベースライン画像作成
/visual-regression http://localhost:3000 -b -f

# 変更後の比較テスト
/visual-regression http://localhost:3000 -c -r

# マルチデバイステスト
/visual-regression /dashboard -m -d "desktop,tablet,mobile"

# 特定閾値での比較
/visual-regression /profile -c -t 0.5
```

**主な機能**:
- ベースライン画像管理
- 差異検出・比較
- マルチデバイス対応
- 動的コンテンツ除外
- 差異レポート生成
- CI/CD統合

## `/accessibility-test [対象] [オプション]` - アクセシビリティテスト
**説明**: Playwright MCPとSerenaツールを活用したWCAG 2.1/2.2準拠のアクセシビリティ検証。

**主要オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-l, --level` | WCAG準拠レベル | AA |
| `-s, --standard` | WCAGバージョン | 2.1 |
| `-k, --keyboard` | キーボードナビゲーションテスト | true |
| `-c, --color` | 色・コントラストテスト | true |
| `-t, --text` | テキスト・スクリーンリーダーテスト | true |
| `-f, --focus` | フォーカス管理テスト | true |
| `-a, --aria` | ARIA属性テスト | true |
| `-r, --report` | 詳細レポート生成 | false |
| `-i, --interactive` | インタラクティブ修正モード | false |
| `--screen-reader` | スクリーンリーダーシミュレーション | false |
| `--auto-fix` | 自動修正提案 | false |

**使用例**:
```bash
# 基本アクセシビリティテスト
/accessibility-test http://localhost:3000

# 厳格WCAG AAA準拠テスト
/accessibility-test /form -l AAA -s 2.2 -r

# キーボードナビゲーション重点テスト
/accessibility-test /dashboard -k -f --screen-reader

# インタラクティブ修正モード
/accessibility-test /signup -i --auto-fix -r
```

**主な機能**:
- WCAG準拠チェック
- キーボードナビゲーション検証
- 色・コントラスト分析
- ARIA属性検証
- スクリーンリーダーシミュレーション
- 自動修正提案
- インタラクティブ修正

## `/performance-monitor [対象] [オプション]` - パフォーマンス監視
**説明**: Playwright MCPとSerenaツールを統合したWebアプリケーションパフォーマンス測定と最適化提案。

**主要オプション**:
| オプション | 説明 | デフォルト |
|---------|------|----------|
| `-v, --vitals` | Core Web Vitals測定 | true |
| `-l, --lighthouse` | Lighthouse監査実行 | false |
| `-n, --network` | 詳細ネットワーク分析 | false |
| `-j, --javascript` | JavaScript実行時間分析 | false |
| `-m, --memory` | メモリ使用量監視 | false |
| `-c, --cpu` | CPU使用量測定 | false |
| `-r, --runs` | 測定回数 | 3 |
| `-d, --device` | デバイス条件設定 | desktop |
| `-t, --throttling` | ネットワーク/CPU制限 | none |
| `--report` | 詳細レポート生成 | false |
| `--baseline` | ベースライン比較 | false |
| `--alerts` | 閾値アラート設定 | false |

**使用例**:
```bash
# 基本パフォーマンス測定
/performance-monitor http://localhost:3000

# Core Web Vitals + Lighthouse監査
/performance-monitor /dashboard -v -l --report

# 詳細パフォーマンス分析
/performance-monitor /checkout -n -j -m -c

# モバイル環境測定
/performance-monitor https://myapp.com -d mobile -t "slow-3g"

# アラート付き監視
/performance-monitor https://production.com --alerts --report
```

**主な機能**:
- Core Web Vitals測定
- Lighthouse監査
- ネットワーク分析
- JavaScript実行分析
- メモリ使用量監視
- ベースライン比較
- パフォーマンス予算
- 最適化提案

## `/playwright-integration [オプション]` - Playwright統合診断
**説明**: Playwright MCPインテグレーションシステムの診断・設定確認・トラブルシューティング。

**主要オプション**:
| オプション | 説明 |
|---------|------|
| `--diagnose` | 全般的診断実行 |
| `--check-browser` | ブラウザ起動確認 |
| `--check-serena` | Serena統合確認 |
| `--performance-debug` | パフォーマンス診断 |
| `--config-validate` | 設定ファイル検証 |
| `--repair` | 自動修復実行 |

**使用例**:
```bash
# 全般的診断
/playwright-integration --diagnose

# ブラウザ診断
/playwright-integration --check-browser

# Serena統合診断
/playwright-integration --check-serena

# パフォーマンス問題診断
/playwright-integration --performance-debug
```

**主な機能**:
- 各コマンド動作確認
- Playwright MCP接続確認
- Serenaメモリ整合性チェック
- 設定ファイル検証
- 権限・セキュリティチェック
- 自動修復機能