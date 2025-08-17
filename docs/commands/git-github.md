# Git・GitHub連携コマンド

## `/git:pr [オプション]` - インテリジェントなプルリクエスト生成
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

## `/git:commit [オプション]` - 高度なGitコミット自動化（Serena MCP統合）
**説明**: Serena MCPを統合した高度なコミット自動化システム。変更内容の意味的分析とコンテキスト認識によるコミットメッセージ生成。

**主な機能**:
- Serena MCPによるコードベース理解とパターン認識
- Git履歴からのコミット規約学習と適応
- conventional commitフォーマットでの絵文字付きメッセージ自動生成
- 変更の意味的分析による適切なコミット分割提案
- チーム固有のコミットパターンへの継続的適応

## `/dependabot-check [URL]` - セキュリティ脆弱性解決
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