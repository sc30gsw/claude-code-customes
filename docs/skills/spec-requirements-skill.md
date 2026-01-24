# Spec Requirements Skill

## 概要

技術選定と改善提案を含む包括的な要件定義書を生成するスキル。EARS形式の受け入れ基準、プロダクトバックログ形式、リバースエンジニアリングモードをサポートします。

## アクティベーショントリガー

- 新しいプロジェクトの要件定義が必要な時
- 既存システムから要件を抽出したい時
- プロダクトバックログを作成したい時
- 技術選定を文書化したい時

## 使用方法

```bash
/spec:requirements <system_name> [options]
```

## オプション

| オプション | 短縮形 | 説明 | 例 |
|------------|--------|------|-----|
| `--mode` | `-m` | モード (new-creation/reverse-engineering) | `-m reverse-engineering` |
| `--backlog` | `-b` | プロダクトバックログ形式を有効化 | `--backlog` |
| `--epic` | `-e` | バックログ構造用のエピック名 | `-e "User Management Epic"` |
| `--story-points` | | ストーリーポイント見積もりを含む | `--story-points` |
| `--app` | `-a` | アプリケーション名 | `-a "Web Store"` |
| `--function` | `-f` | 機能/フィーチャー名 | `-f "Authentication"` |
| `--output` | `-o` | 出力ファイルパス | `-o specs.md` |
| `--tech` | `-t` | 技術スタック | `-t "react,nodejs,postgresql"` |
| `--priority` | `-p` | 優先度レベル | `-p high` |
| `--scope` | `-s` | スコープタイプ | `-s mvp` |
| `--suggest` | | 改善提案を含む | `--suggest` |
| `--examples` | | 実装例を含む | `--examples` |
| `--template` | | テンプレートタイプ | `--template agile` |
| `--hearing` | | インタラクティブ明確化モード | `--hearing` |

## テンプレート

| テンプレート | 説明 |
|--------------|------|
| `standard` | EARS形式の汎用テンプレート |
| `agile` | 受け入れ基準付きユーザーストーリー形式 |
| `waterfall` | 詳細仕様書 |
| `product-backlog` | エピック、フィーチャー、ストーリー付きバックログ |

## Serena MCP ツール優先

### ファイル操作
- `mcp__serena__find_file` → `Read`（フォールバック）
- `mcp__serena__search_for_pattern` → `Grep`（フォールバック）
- `mcp__serena__list_dir` → `LS`（フォールバック）

### コード分析
- `mcp__serena__get_symbols_overview`
- `mcp__serena__find_referencing_symbols`

### Context7統合
技術ドキュメント用:
- Frontend: React, Vue, Angular
- Backend: Node.js, Express, FastAPI
- Database: PostgreSQL, MongoDB, Redis

## モード

### 新規作成モード（デフォルト）
仕様とユーザー入力から要件を生成

### リバースエンジニアリングモード
既存コードベースを分析して要件を抽出:
1. コンポーネント検出（コントローラー、サービス、モデル）
2. フィーチャー抽出（ユーザー向け機能）
3. ユーザーストーリー生成（機能からストーリーへ）

## EARS形式

受け入れ基準はEARS (Easy Approach to Requirements Syntax)を使用:
- WHEN [event] THEN [system] SHALL [response]
- IF [precondition] THEN [system] SHALL [response]
- WHILE [condition] THE SYSTEM SHALL [behavior]
- WHERE [context] THE SYSTEM SHALL [behavior]

## 使用例

```bash
# 基本的な要件
/spec:requirements "E-commerce Platform" -a "Web Store" -t "react,nodejs"

# 提案付きMVP
/spec:requirements "Social Media App" -s mvp --suggest

# インタラクティブヒアリングモード
/spec:requirements "Mobile App" --hearing

# バックログ付きリバースエンジニアリング
/spec:requirements "User Management" -m reverse-engineering -b -e "Auth Epic"

# 例付きエンタープライズ
/spec:requirements "CRM System" -s enterprise -t "react,nodejs,postgresql" --examples
```

## 出力構造

1. **ヘッダー情報**: タイムスタンプ、システム名、優先度、スコープ
2. **機能要件**: コア機能、ユーザーシナリオ（EARS形式）
3. **非機能要件**: パフォーマンス、セキュリティ、可用性
4. **技術仕様**: アーキテクチャ、技術スタック、統合
5. **追加セクション**: 例、提案（有効時）

## 出力例

```markdown
# Requirements Definition: E-commerce Platform

## Header
- Generated: 2024-01-20T10:30:00Z
- Priority: HIGH
- Scope: MVP

## Functional Requirements

### FR-001: User Authentication
**WHEN** user submits login form with valid credentials
**THEN** system **SHALL** create session and redirect to dashboard

**Acceptance Criteria:**
- WHEN user enters valid email and password THEN system SHALL authenticate within 2 seconds
- IF credentials are invalid THEN system SHALL display error message
- WHILE session is active THE SYSTEM SHALL maintain authentication state

### FR-002: Product Catalog
...

## Non-Functional Requirements

### NFR-001: Performance
- Page load time < 3 seconds
- API response time < 500ms

### NFR-002: Security
- HTTPS required
- Password hashing with bcrypt
```

## 成功指標

- 要件が明確に文書化される
- EARS形式の受け入れ基準が含まれる
- 技術仕様が具体的
- 優先度とスコープが明確
- 実装可能なレベルの詳細度
