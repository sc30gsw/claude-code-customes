# 📝 doc-engineerスキル - 技術ドキュメントの作成・改善・品質管理

Claude CodeでMarkdown形式の技術ドキュメントを作成し、品質を自動的に分析・改善できるプロフェッショナルスキルです。

## 🎯 概要

doc-engineerスキルは、技術ドキュメントのライフサイクル全体をカバーします：

| 操作タイプ | 機能 | 主要ツール |
|-----------|------|-----------|
| 📝 **作成** | 7種類のテンプレートから新規作成 | template_generator.py |
| 🔍 **分析** | 4次元品質評価システム | doc_analyzer.py |
| ✨ **改善** | AI駆動の自動改善提案・適用 | doc_improver.py |
| ✅ **検証** | 包括的なドキュメント検証 | doc_validator.py |
| 🔄 **ワークフロー** | エンドツーエンド自動化 | doc_workflow.py |

### 主な特徴

- ✅ **7種類の専門テンプレート**: 技術仕様、要件定義、README、ADR、RFC、コーディング規則、技術記事
- ✅ **4次元品質評価**: 構造(75点)、コンテンツ(70点)、可読性(65点)、リンク健全性(80点)
- ✅ **自動改善システム**: 優先度マトリクスに基づく改善提案と適用
- ✅ **厳格な検証**: 構造、リンク、一貫性、完全性、フォーマットの5軸検証
- ✅ **EARS形式サポート**: 要件記述のベストプラクティス準拠

### 品質スコアリング

```
Overall Quality Score = 加重平均
├─ Structure Score (30%)    - 見出し階層、セクション完全性、TOC整合性
├─ Content Score (30%)      - 情報完全性、明確性、例示、コードスニペット
├─ Readability Score (25%)  - 文の複雑さ、段落の長さ、技術用語密度
└─ Link Health (15%)        - 内部リンク有効性、外部URL到達可能性

目標: 総合スコア ≥ 80点（高品質ドキュメント）
```

## 🚀 クイックスタート

### テンプレートから新規作成

```bash
# 技術仕様書のテンプレート生成
python .claude/skills/doc-engineer/scripts/template_generator.py \
  --type technical-spec \
  --project "User Authentication System" \
  --author "Development Team" \
  --stack "Node.js, PostgreSQL, Redis" \
  --output auth-spec.md
```

### 既存ドキュメントの品質分析

```bash
# 詳細分析レポート生成
python .claude/skills/doc-engineer/scripts/doc_analyzer.py \
  --file README.md \
  --detailed

# 出力例:
# Quality Score: 62/100
# - Structure: 58/100 (missing sections: Installation, Contributing)
# - Content: 65/100 (needs more examples)
# - Readability: 70/100 (some paragraphs too long)
# - Link Health: 55/100 (3 broken links found)
```

### 自動改善の適用

```bash
# 高優先度の改善を自動適用
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file README.md \
  --apply-all \
  --priority high

# 品質目標を指定して改善
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file README.md \
  --target-quality 85 \
  --interactive
```

## 📖 ワークフロー解説

### 📋 ワークフロー決定木

```
何をしたい？
├─ 新規ドキュメント作成 → CREATEワークフロー
│  └─ 7フェーズ: コンテキスト収集 → テンプレート → 開発 → 検証 → 改善 → 検証 → 公開準備
│
├─ 既存ドキュメント編集 → EDITワークフロー
│  └─ ロード → 分析 → 編集 → 検証 → 改善確認
│
└─ ドキュメント品質向上 → IMPROVEワークフロー
   └─ 分析 → 改善提案 → 適用（一括/選択/対話） → 検証 → レポート
```

---

## 🆕 ワークフロー1: CREATE（新規作成）

### 7フェーズのエンドツーエンドワークフロー

```bash
# 完全自動ワークフロー
python .claude/skills/doc-engineer/scripts/doc_workflow.py \
  --mode create \
  --type technical-spec \
  --project "Payment Gateway API" \
  --author "API Team" \
  --output payment-spec.md
```

#### Phase 1: Context Gathering（コンテキスト収集）
- プロジェクト名、バージョン、著者情報
- 技術スタック、アーキテクチャパターン
- 要件、制約、ステークホルダー

#### Phase 2: Template Generation（テンプレート生成）
- ドキュメントタイプに応じた構造作成
- メタデータ自動注入（`{PROJECT_NAME}`, `{VERSION}`, `{DATE}`等）
- セクションプレースホルダー配置

#### Phase 3: Content Development（コンテンツ開発）
- セクションごとの詳細化
- 例示とコードスニペット追加
- 図表、リンクの追加

#### Phase 4: Quality Check（品質チェック）
- バリデータ実行（構造、リンク、完全性）
- アナライザ実行（4次元品質評価）
- 問題の特定と優先度付け

#### Phase 5: Improvement Application（改善適用）
- 高優先度問題の自動修正
- コンテンツ拡充、可読性向上
- 欠落セクションの追加

#### Phase 6: Final Validation（最終検証）
- 品質目標達成確認（デフォルト: ≥80点）
- 全検証項目の再チェック
- リンク健全性の最終確認

#### Phase 7: Publication Prep（公開準備）
- レビューチェックリスト生成
- 変更履歴記録
- 配布準備完了

### 実行例

```bash
# 技術仕様書を完全自動作成
python .claude/skills/doc-engineer/scripts/doc_workflow.py \
  --mode create \
  --type technical-spec \
  --project "Microservices Platform" \
  --author "Architecture Team" \
  --stack "Docker, Kubernetes, gRPC, PostgreSQL" \
  --version "1.0.0" \
  --target-quality 85 \
  --output platform-spec.md

# 結果: 品質スコア87点の技術仕様書が生成される
```

---

## ✏️ ワークフロー2: EDIT（編集）

### 既存ドキュメントの編集フロー

```bash
# Step 1: ロードと分析
python .claude/skills/doc-engineer/scripts/doc_analyzer.py \
  --file existing-doc.md \
  --detailed

# Step 2: 編集範囲の特定
# - 構造的編集: セクション追加・削除・再配置
# - コンテンツ編集: テキスト追加・更新・削除
# - フォーマット編集: スタイル統一、リンク修正

# Step 3: 編集適用（手動またはスクリプト）
# Markdown直接編集

# Step 4: 変更の検証
python .claude/skills/doc-engineer/scripts/doc_validator.py \
  --file existing-doc.md \
  --full

# Step 5: 改善確認
python .claude/skills/doc-engineer/scripts/doc_analyzer.py \
  --file existing-doc.md
```

### 構造的編集の例

```markdown
# Before
## Installation
## Usage

# After（セクション追加）
## Installation
## Configuration
## Usage
## Troubleshooting
## FAQ
```

---

## ✨ ワークフロー3: IMPROVE（品質向上）

### 改善優先度マトリクス

```
Impact  │
 High   │ [Critical]         [High Priority]
        │ - 必須セクション追加  - 例示追加
        │ - 壊れたリンク修正    - 説明拡充
        │
 Medium │ [Medium Priority]   [Medium Priority]
        │ - 可読性向上         - フォーマット統一
        │ - 段落分割           - 用語統一
        │
 Low    │ [Low Priority]      [Optional]
        │ - 軽微な修正         - スタイル調整
        │ - 任意の改善         - 装飾的変更
        └─────────────────────────────────
              Low      Medium      High
                      Effort
```

### 一括改善の実行

```bash
# すべての改善を自動適用
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file document.md \
  --apply-all \
  --priority high

# Before: Quality Score 62/100
# After:  Quality Score 89/100
```

### 選択的改善

```bash
# 改善提案をリスト表示（適用はしない）
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file document.md \
  --suggest-only

# 出力:
# [HIGH] Add missing section: Installation (Impact: 15 points)
# [HIGH] Fix 3 broken links (Impact: 12 points)
# [MEDIUM] Add code examples to Usage section (Impact: 8 points)
# [MEDIUM] Split long paragraphs in Overview (Impact: 5 points)
# [LOW] Unify heading capitalization (Impact: 2 points)

# 特定カテゴリのみ改善
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file document.md \
  --category structure \
  --apply-all
```

### 対話的改善

```bash
# 各改善を確認しながら適用
python .claude/skills/doc-engineer/scripts/doc_improver.py \
  --file document.md \
  --interactive

# プロンプト例:
# [HIGH] Add missing section: Installation
# Impact: +15 points | Effort: Medium
# Apply this improvement? [Y/n/skip]:
```

---

## 📚 テンプレート詳細

### 1. Technical Specification（技術仕様書）

**用途**: システムアーキテクチャ、API仕様、技術設計

**必須セクション**:
- Overview（概要）
- Architecture（アーキテクチャ）
- Requirements（要件）
- API Specification（API仕様）
- Data Models（データモデル）
- Security Considerations（セキュリティ考慮事項）
- Performance Requirements（性能要件）
- Testing Strategy（テスト戦略）

**生成例**:

```bash
python scripts/template_generator.py \
  --type technical-spec \
  --project "E-Commerce Platform API" \
  --author "Backend Team" \
  --version "2.0.0" \
  --stack "FastAPI, PostgreSQL, Redis, Docker" \
  --output ecommerce-api-spec.md
```

### 2. Requirements Document（要件定義書）

**用途**: 機能要件、非機能要件、受入基準

**EARS形式サポート**:
- **Ubiquitous**: システムは常に〜すべき
- **Event-driven**: 〜の場合、システムは〜すべき
- **State-driven**: 〜の状態では、システムは〜すべき
- **Optional**: 〜を提供すべき（オプション）
- **Unwanted**: システムは〜してはならない

**必須セクション**:
- Introduction（導入）
- Functional Requirements（機能要件）
- Non-Functional Requirements（非機能要件）
- Acceptance Criteria（受入基準）

**生成例**:

```bash
python scripts/template_generator.py \
  --type requirements \
  --project "Mobile Banking App" \
  --author "Product Team" \
  --output banking-requirements.md
```

**EARS形式の例**:

```markdown
## Functional Requirements

### FR-001: User Authentication
**Type**: Event-driven
**Description**: WHEN a user enters valid credentials, the system SHALL authenticate the user within 2 seconds.

### FR-002: Data Encryption
**Type**: Ubiquitous
**Description**: The system SHALL encrypt all sensitive data at rest using AES-256.

### FR-003: Offline Mode
**Type**: Optional
**Description**: The system SHOULD provide offline access to cached data.

### FR-004: Unauthorized Access
**Type**: Unwanted
**Description**: The system SHALL NOT allow access without valid authentication.
```

### 3. README

**用途**: プロジェクト概要、インストール、使用方法

**必須セクション**:
- Installation（インストール）
- Usage（使用方法）

**推奨セクション**:
- Features（機能）
- Getting Started（はじめに）
- Configuration（設定）
- Contributing（貢献）
- License（ライセンス）

**生成例**:

```bash
python scripts/template_generator.py \
  --type readme \
  --project "awesome-library" \
  --author "Open Source Contributors" \
  --output README.md
```

### 4. ADR（Architecture Decision Record）

**用途**: アーキテクチャ決定の記録と理由

**必須セクション**:
- Status（状態: Proposed/Accepted/Deprecated/Superseded）
- Context（コンテキスト）
- Decision（決定内容）
- Consequences（結果・影響）

**生成例**:

```bash
python scripts/template_generator.py \
  --type adr \
  --project "ADR-001: Use PostgreSQL for Primary Database" \
  --author "Architecture Team" \
  --output adr/001-postgresql-choice.md
```

**ADRの例**:

```markdown
# ADR-001: Use PostgreSQL for Primary Database

## Status
Accepted

## Context
We need to select a primary database for our microservices platform. Key requirements:
- ACID compliance
- JSON support
- Full-text search
- Strong community support
- Horizontal scalability options

## Decision
We will use PostgreSQL 14+ as our primary relational database.

## Consequences

### Positive
- Strong ACID guarantees
- Excellent JSON/JSONB support
- Rich ecosystem of extensions (PostGIS, pg_trgm)
- Active community and extensive documentation

### Negative
- Higher operational complexity than managed NoSQL solutions
- Vertical scaling limitations without partitioning
- Requires more DBA expertise

### Neutral
- Need to implement connection pooling (PgBouncer)
- Will use TimescaleDB extension for time-series data
```

### 5. RFC（Request for Comments）

**用途**: 技術提案、設計ドラフト、標準化文書

**必須セクション**:
- Abstract（要約）
- Motivation（動機）
- Proposal（提案）
- Detailed Design（詳細設計）
- Alternatives（代替案）
- Unresolved Questions（未解決の問題）

**生成例**:

```bash
python scripts/template_generator.py \
  --type rfc \
  --project "RFC-003: Standardize API Error Handling" \
  --author "API Working Group" \
  --output rfc/003-error-handling.md
```

### 6. Coding Rules（コーディング規則）

**用途**: コーディング標準、ベストプラクティス、レビューチェックリスト

**必須セクション**:
- Principles（原則）
- Naming Conventions（命名規則）
- Code Style（コードスタイル）
- Best Practices（ベストプラクティス）
- Code Review Checklist（コードレビューチェックリスト）

**生成例**:

```bash
python scripts/template_generator.py \
  --type coding-rules \
  --project "TypeScript Coding Standards" \
  --author "Engineering Team" \
  --stack "TypeScript, React, Node.js" \
  --output coding-standards.md
```

### 7. Article（技術記事）

**用途**: ブログ記事、技術解説、チュートリアル

**必須セクション**:
- Introduction（導入）
- Implementation（実装）
- Conclusion（まとめ）

**推奨セクション**:
- Prerequisites（前提知識）
- Step-by-Step Guide（ステップバイステップガイド）
- Code Examples（コード例）
- Common Pitfalls（よくある落とし穴）
- Further Reading（参考資料）

**生成例**:

```bash
python scripts/template_generator.py \
  --type article \
  --project "Building a GraphQL API with TypeScript" \
  --author "Tech Blog Team" \
  --output articles/graphql-typescript-guide.md
```

---

## 🔧 品質ルール詳細

### structure-rules.json（構造要件）

各ドキュメントタイプの構造基準:

| ドキュメント | 必須セクション数 | 見出しレベル | TOC必須 | メタデータ必須 |
|------------|----------------|-------------|---------|---------------|
| technical-spec | 5+ | h1-h4 | ✅ | ✅ |
| requirements | 4+ | h1-h3 | ❌ | ✅ |
| adr | 4+ | h1-h3 | ❌ | ❌ |
| rfc | 5+ | h1-h4 | ✅ | ✅ |
| readme | 3+ | h1-h3 | ❌ | ❌ |
| coding-rules | 4+ | h1-h3 | ✅ | ✅ |
| article | 3+ | h1-h3 | ❌ | ✅ |

**検証項目**:
- ✅ 必須セクションがすべて存在
- ✅ 見出しレベルがスキップされていない（h1 → h3は❌）
- ✅ TOCとコンテンツが一致
- ✅ メタデータが完全

### style-guide.json（スタイルガイド）

**フォーマット規則**:

```json
{
  "heading_style": "ATX",           // # 形式（Setext形式は非推奨）
  "code_fence": "backticks",        // ``` 使用（~~~ は非推奨）
  "code_language": "required",      // 言語タグ必須
  "link_style": "inline",           // [text](url) 形式
  "max_line_length": 120,           // 最大行長
  "trailing_newline": true          // ファイル末尾改行必須
}
```

**用語統一**:

```json
{
  "uppercase_terms": [
    "API", "URL", "HTTP", "HTTPS", "JSON", "XML",
    "SQL", "HTML", "CSS", "ID", "OK", "UI", "UX"
  ],
  "american_english": true,         // colour → color
  "avoid_abbreviations": [
    "etc", "e.g.", "i.e."          // そのまま書く
  ]
}
```

**ベストプラクティス**:

```json
{
  "max_sentence_length": 25,        // 最大単語数/文
  "max_paragraph_length": 150,      // 最大単語数/段落
  "prefer_active_voice": true,      // 能動態優先
  "use_present_tense": true         // 現在時制使用
}
```

### completeness-checklist.json（完全性チェックリスト）

**メタデータ要件**:

```markdown
---
title: "Document Title"              # 必須、最大100文字
author: "Author Name"                # 必須、名前またはメール
date: "2025-01-15"                   # 必須、YYYY-MM-DD形式
version: "1.0.0"                     # 必須、セマンティックバージョニング
status: "Draft"                      # 任意: Draft|Review|Approved|Published|Deprecated
---
```

**品質ゲート**:

| メトリクス | 最小値 | 推奨値 |
|-----------|-------|-------|
| Overall Quality | 70 | 80 |
| Structure Score | 75 | 85 |
| Content Score | 70 | 80 |
| Readability Score | 65 | 75 |
| Link Health | 80 | 95 |

**問題許容数**:

| 優先度 | 最大許容数 |
|-------|-----------|
| Critical | 0 |
| High | 2 |
| Medium | 5 |
| Low | 無制限 |

---

## 💼 実用例

### 例1: 技術仕様書をゼロから作成

```bash
# Step 1: テンプレート生成
python scripts/template_generator.py \
  --type technical-spec \
  --project "Real-time Chat Service" \
  --author "Platform Team" \
  --version "1.0.0" \
  --stack "WebSocket, Redis, MongoDB, Docker" \
  --output chat-service-spec.md

# Step 2: コンテンツ開発（手動編集）
# セクションごとに詳細を追加:
# - Architecture: システム図、コンポーネント説明
# - API Specification: エンドポイント定義
# - Data Models: スキーマ定義

# Step 3: 品質チェック
python scripts/doc_analyzer.py --file chat-service-spec.md --detailed

# 出力:
# Quality Score: 68/100
# Issues:
# - [HIGH] Missing section: Testing Strategy
# - [MEDIUM] No code examples in API Specification
# - [MEDIUM] 2 paragraphs exceed 150 words

# Step 4: 自動改善
python scripts/doc_improver.py \
  --file chat-service-spec.md \
  --apply-all \
  --priority high

# Step 5: 最終検証
python scripts/doc_validator.py --file chat-service-spec.md --full

# 結果:
# ✅ All validations passed
# Quality Score: 87/100
# Status: Ready for review
```

### 例2: 既存READMEの品質改善

```bash
# 現状分析
python scripts/doc_analyzer.py --file README.md --detailed

# 出力:
# Quality Score: 58/100
# Structure: 45/100
#   - Missing sections: Installation, Configuration, Contributing
#   - No table of contents
# Content: 60/100
#   - Usage section needs examples
#   - No troubleshooting information
# Readability: 65/100
#   - 5 sentences exceed 25 words
#   - 3 paragraphs exceed 150 words
# Link Health: 60/100
#   - 2 broken external links
#   - 1 broken internal link

# 改善提案の確認
python scripts/doc_improver.py --file README.md --suggest-only

# 提案リスト:
# [HIGH] Add missing section: Installation (+12 points)
# [HIGH] Add missing section: Configuration (+12 points)
# [HIGH] Fix 3 broken links (+15 points)
# [MEDIUM] Add code examples to Usage (+8 points)
# [MEDIUM] Add table of contents (+6 points)
# [MEDIUM] Split long paragraphs (+5 points)
# [LOW] Add badges to header (+2 points)

# 高優先度のみ自動適用
python scripts/doc_improver.py \
  --file README.md \
  --apply-all \
  --priority high

# 再分析
python scripts/doc_analyzer.py --file README.md

# 改善結果:
# Quality Score: 89/100 (+31 points)
# Structure: 85/100 (+40 points)
# Content: 88/100 (+28 points)
# Readability: 90/100 (+25 points)
# Link Health: 95/100 (+35 points)
```

### 例3: 要件定義書の作成（EARS形式）

```bash
# テンプレート生成
python scripts/template_generator.py \
  --type requirements \
  --project "Healthcare Portal" \
  --author "Product Management" \
  --version "1.0.0" \
  --output healthcare-requirements.md

# 生成されたテンプレートに要件を追加（EARS形式）
```

```markdown
## Functional Requirements

### FR-001: Patient Data Access
**Type**: Event-driven
**Priority**: High
**Description**: WHEN a healthcare provider logs in with valid credentials, the system SHALL display the patient dashboard within 3 seconds.

### FR-002: Data Encryption
**Type**: Ubiquitous
**Priority**: Critical
**Description**: The system SHALL encrypt all patient health information using AES-256 encryption both at rest and in transit.

### FR-003: HIPAA Compliance
**Type**: Ubiquitous
**Priority**: Critical
**Description**: The system SHALL comply with all HIPAA regulations for patient data handling and storage.

### FR-004: Appointment Scheduling
**Type**: Event-driven
**Priority**: High
**Description**: WHEN a patient selects an available time slot, the system SHALL confirm the appointment within 2 seconds and send a confirmation email within 30 seconds.

### FR-005: Offline Viewing
**Type**: Optional
**Priority**: Medium
**Description**: The system SHOULD allow healthcare providers to view cached patient data when offline.

### FR-006: Unauthorized Data Export
**Type**: Unwanted
**Priority**: Critical
**Description**: The system SHALL NOT allow export of patient data without explicit authorization and audit logging.

## Non-Functional Requirements

### NFR-001: Performance
**Category**: Performance
**Description**: The system SHALL support 1000 concurrent users with response times under 2 seconds for 95% of requests.

### NFR-002: Availability
**Category**: Reliability
**Description**: The system SHALL maintain 99.9% uptime during business hours (6 AM - 10 PM EST).

### NFR-003: Security Audit
**Category**: Security
**Description**: The system SHALL log all data access attempts with timestamp, user ID, and action type.
```

```bash
# 検証
python scripts/doc_validator.py --file healthcare-requirements.md --full

# 品質チェック
python scripts/doc_analyzer.py --file healthcare-requirements.md

# 結果:
# Quality Score: 92/100
# - EARS format compliance: ✅
# - All required metadata: ✅
# - Acceptance criteria defined: ✅
```

### 例4: ドキュメントディレクトリの一括品質チェック

```bash
# ディレクトリ全体を再帰的に分析
python scripts/doc_analyzer.py \
  --directory docs/ \
  --recursive \
  --output quality-report.json

# JSON出力例:
# {
#   "summary": {
#     "total_documents": 15,
#     "average_quality": 72.3,
#     "documents_below_threshold": 5
#   },
#   "documents": [
#     {
#       "path": "docs/api-spec.md",
#       "quality_score": 88,
#       "status": "good"
#     },
#     {
#       "path": "docs/README.md",
#       "quality_score": 58,
#       "status": "needs_improvement",
#       "issues": [...]
#     }
#   ]
# }

# 低品質ドキュメントのみ抽出
jq '.documents[] | select(.quality_score < 70)' quality-report.json

# 低品質ドキュメントを一括改善
for doc in $(jq -r '.documents[] | select(.quality_score < 70) | .path' quality-report.json); do
  python scripts/doc_improver.py \
    --file "$doc" \
    --target-quality 80 \
    --apply-all \
    --priority high
done

# 再分析
python scripts/doc_analyzer.py --directory docs/ --recursive

# 結果:
# Average Quality: 72.3 → 84.6 (+12.3 points)
# Documents below threshold: 5 → 0
```

---

## 📊 品質メトリクス詳細

### Structure Score（構造スコア）

**計算方法**:

```python
structure_score = weighted_average([
    (heading_hierarchy_score, 0.30),    # 見出し階層の適切性
    (section_completeness_score, 0.40), # 必須セクション存在
    (toc_consistency_score, 0.20),      # TOCとコンテンツの一致
    (metadata_completeness_score, 0.10) # メタデータの完全性
])
```

**評価基準**:

| スコア | 評価 | 状態 |
|-------|------|------|
| 90-100 | Excellent | 完璧な構造 |
| 80-89 | Good | 軽微な改善のみ |
| 70-79 | Fair | 改善推奨 |
| 60-69 | Poor | 改善必要 |
| 0-59 | Critical | 大幅な改善必要 |

### Content Score（コンテンツスコア）

**計算方法**:

```python
content_score = weighted_average([
    (information_completeness, 0.40),   # 情報の完全性
    (clarity_score, 0.30),              # 明確性
    (examples_score, 0.20),             # 例示の充実度
    (code_snippets_score, 0.10)         # コードスニペット
])
```

**ペナルティ**:
- プレースホルダーテキスト: -5点/箇所（TODO, TBD, FIXME, XXX）
- 空セクション: -10点/箇所
- 疎なセクション（<50語）: -3点/箇所

### Readability Score（可読性スコア）

**計算方法**:

```python
readability_score = weighted_average([
    (sentence_complexity, 0.40),        # 文の複雑さ
    (paragraph_length, 0.30),           # 段落の長さ
    (technical_density, 0.20),          # 技術用語密度
    (active_voice_ratio, 0.10)          # 能動態使用率
])
```

**ペナルティ**:
- 長い文（>25語）: -2点/文
- 長い段落（>150語）: -3点/段落
- 高い技術用語密度（>30%）: -5点

### Link Health（リンク健全性）

**計算方法**:

```python
link_health = (valid_links / total_links) * 100

valid_links = internal_valid + external_valid
```

**検証**:
- ✅ 内部リンク: セクションID、アンカーの存在確認
- ✅ 外部リンク: HTTPステータスコード200確認（タイムアウト: 5秒）

---

## 🛠️ スクリプト詳細

### doc_analyzer.py（品質分析）

**基本使用法**:

```bash
# 簡易分析
python scripts/doc_analyzer.py --file document.md

# 詳細分析
python scripts/doc_analyzer.py --file document.md --detailed

# ディレクトリ分析
python scripts/doc_analyzer.py --directory docs/ --recursive

# JSON出力
python scripts/doc_analyzer.py --file document.md --output report.json
```

**出力形式**:

```json
{
  "overall_quality": 78,
  "scores": {
    "structure": 82,
    "content": 75,
    "readability": 76,
    "link_health": 80
  },
  "issues": [
    {
      "type": "structure",
      "severity": "high",
      "message": "Missing required section: Testing Strategy",
      "location": "N/A"
    },
    {
      "type": "readability",
      "severity": "medium",
      "message": "Sentence exceeds 25 words",
      "location": "Line 45"
    }
  ],
  "recommendations": [
    "Add Testing Strategy section",
    "Split long sentences for better readability"
  ]
}
```

### doc_improver.py（自動改善）

**基本使用法**:

```bash
# 改善提案のみ（適用しない）
python scripts/doc_improver.py --file document.md --suggest-only

# 全改善を自動適用
python scripts/doc_improver.py --file document.md --apply-all

# 高優先度のみ適用
python scripts/doc_improver.py --file document.md --apply-all --priority high

# 品質目標を指定
python scripts/doc_improver.py --file document.md --target-quality 85

# 対話的改善
python scripts/doc_improver.py --file document.md --interactive

# カテゴリ指定
python scripts/doc_improver.py --file document.md --category structure --apply-all
```

**改善カテゴリ**:
- `structure`: セクション追加・再配置、階層改善
- `content`: 例示追加、説明拡充、コードスニペット
- `readability`: 文・段落分割、簡略化
- `consistency`: 用語統一、フォーマット統一
- `links`: リンク修正、追加

### doc_validator.py（検証）

**基本使用法**:

```bash
# 基本検証
python scripts/doc_validator.py --file document.md

# 完全検証（すべてのチェック）
python scripts/doc_validator.py --file document.md --full

# 特定カテゴリのみ
python scripts/doc_validator.py --file document.md --checks structure,links

# JSON出力
python scripts/doc_validator.py --file document.md --output validation.json
```

**検証カテゴリ**:

| カテゴリ | 検証項目 |
|---------|---------|
| structure | 必須セクション、見出し階層、TOC一致 |
| links | 内部リンク有効性、外部URL到達可能性 |
| consistency | 用語統一、フォーマット統一 |
| completeness | メタデータ完全性、プレースホルダー検出 |
| format | Markdown構文、コードフェンス、画像パス |

### doc_workflow.py（エンドツーエンド）

**基本使用法**:

```bash
# 新規作成ワークフロー
python scripts/doc_workflow.py \
  --mode create \
  --type technical-spec \
  --project "Project Name" \
  --author "Author Name" \
  --output document.md

# 改善ワークフロー
python scripts/doc_workflow.py \
  --mode improve \
  --file existing.md \
  --target-quality 85

# カスタムワークフロー
python scripts/doc_workflow.py \
  --mode create \
  --type requirements \
  --project "Healthcare Portal" \
  --author "PM Team" \
  --target-quality 90 \
  --skip-phases 6,7  # Phase 6,7をスキップ
```

### template_generator.py（テンプレート生成）

**基本使用法**:

```bash
# 基本生成
python scripts/template_generator.py \
  --type technical-spec \
  --project "Project Name" \
  --output spec.md

# 完全なメタデータ指定
python scripts/template_generator.py \
  --type requirements \
  --project "Mobile App" \
  --author "Product Team" \
  --version "2.1.0" \
  --stack "React Native, Firebase, GraphQL" \
  --date "2025-01-15" \
  --output requirements.md
```

**メタデータ変数**:
- `{PROJECT_NAME}`: プロジェクト名
- `{VERSION}`: バージョン
- `{DATE}`: 日付（YYYY-MM-DD）
- `{AUTHOR}`: 著者名
- `{TECH_STACK}`: 技術スタック

---

## ⚙️ 高度な機能

### カスタムテンプレートの作成

```bash
# テンプレートディレクトリに新規追加
.claude/skills/doc-engineer/templates/custom-design-doc.md
```

```markdown
---
title: "{PROJECT_NAME} Design Document"
author: "{AUTHOR}"
date: "{DATE}"
version: "{VERSION}"
type: "design-doc"
---

# {PROJECT_NAME} Design Document

## Executive Summary
[Brief overview of the design]

## System Context
[System boundaries and external interfaces]

## Design Goals
[Primary objectives and constraints]

## High-Level Design
[Architecture diagrams and component descriptions]

## Detailed Design
[Component-level design details]

## Data Flow
[Data flow diagrams and descriptions]

## Interface Specifications
[API and integration point specifications]

## Quality Attributes
[Performance, security, scalability considerations]

## Implementation Plan
[Phases, milestones, dependencies]
```

```python
# template_generator.pyにカスタムタイプを追加
TEMPLATE_TYPES = {
    # ... existing types ...
    'design-doc': {
        'template': 'custom-design-doc.md',
        'required_sections': [
            'Executive Summary',
            'System Context',
            'Design Goals',
            'High-Level Design',
            'Detailed Design'
        ]
    }
}
```

### 品質ルールのカスタマイズ

```json
// quality-rules/custom-structure-rules.json
{
  "design-doc": {
    "required_sections": [
      "Executive Summary",
      "System Context",
      "Design Goals",
      "High-Level Design",
      "Detailed Design",
      "Data Flow",
      "Interface Specifications"
    ],
    "heading_levels": ["h1", "h2", "h3", "h4"],
    "min_sections": 7,
    "toc_required": true,
    "metadata_required": true
  }
}
```

### エージェント統合

#### technical-writerエージェントとの統合

doc-engineerスキルは`technical-writer`エージェント呼び出し時に自動的に活用されます：

```bash
# technical-writerエージェント呼び出し例
# エージェントがdoc-engineerスキルを内部的に使用:
# 1. テンプレート生成
# 2. コンテンツ開発
# 3. 品質評価と改善
# 4. 検証
```

#### requirements-analystエージェントとの統合

`requirements-analyst`エージェントは要件定義書作成時にdoc-engineerを使用：

```bash
# requirements-analystエージェント呼び出し例
# 自動的に:
# 1. EARS形式テンプレート生成
# 2. 要件の構造化
# 3. 完全性基準に対する検証
```

---

## ⚠️ トラブルシューティング

### よくある問題

#### 問題1: 依存関係エラー

```bash
# エラー: ModuleNotFoundError: No module named 'markdown'

# 解決策: 依存関係をインストール
pip install markdown>=3.4.0 beautifulsoup4>=4.12 requests>=2.31 jsonschema>=4.19
```

#### 問題2: 品質スコアが低い

```bash
# 症状: Quality Score: 45/100

# デバッグ手順:
# 1. 詳細分析で問題を特定
python scripts/doc_analyzer.py --file document.md --detailed

# 2. カテゴリ別スコアを確認
# Output:
# Structure: 30/100 (missing 3 required sections)
# Content: 50/100 (needs examples and details)
# Readability: 55/100 (long sentences and paragraphs)
# Link Health: 45/100 (5 broken links)

# 3. 高優先度問題から順に解決
python scripts/doc_improver.py --file document.md --apply-all --priority high

# 4. 再評価
python scripts/doc_analyzer.py --file document.md
# Expected: Score improves to 75-85/100
```

#### 問題3: 検証エラー

```bash
# エラー: Validation failed: Invalid heading hierarchy

# デバッグ:
python scripts/doc_validator.py --file document.md --full --verbose

# Output:
# [ERROR] Heading level skip: h1 → h3 at line 25
# [ERROR] Missing required section: Installation
# [WARNING] TOC does not match content

# 修正:
# 1. h2を追加してh1 → h2 → h3の階層にする
# 2. Installationセクションを追加
# 3. TOCを再生成
```

### デバッグのヒント

| 問題 | デバッグ方法 | ツール |
|------|------------|--------|
| 低い構造スコア | 必須セクションと見出し階層を確認 | `doc_analyzer.py --detailed` |
| 低いコンテンツスコア | プレースホルダー、空セクションを検索 | `grep -E "TODO\|TBD\|FIXME" document.md` |
| 低い可読性スコア | 長い文・段落を特定 | `doc_analyzer.py --detailed` |
| リンクエラー | 壊れたリンクのリストを取得 | `doc_validator.py --checks links` |
| フォーマットエラー | Markdown構文をチェック | `markdownlint document.md` |

---

## 🛠️ 開発者向け情報

### スキルファイル構成

```
doc-engineer/
├── SKILL.md                          # スキル概要（使用方法、ワークフロー）
├── LICENSE.txt                       # プロプライエタリライセンス
├── quality-rules/                    # 品質検証ルール（3ファイル）
│   ├── structure-rules.json         # 構造要件定義
│   ├── style-guide.json             # スタイルガイド
│   └── completeness-checklist.json  # 完全性チェックリスト
├── scripts/                          # Python自動化スクリプト（5ファイル）
│   ├── doc_analyzer.py              # 品質分析エンジン
│   ├── doc_improver.py              # 改善提案・適用エンジン
│   ├── doc_validator.py             # 検証エンジン
│   ├── doc_workflow.py              # エンドツーエンドワークフロー
│   └── template_generator.py        # テンプレート生成
└── templates/                        # ドキュメントテンプレート（7種類）
    ├── technical-spec.md
    ├── requirements.md
    ├── readme.md
    ├── adr.md
    ├── rfc.md
    ├── coding-rules.md
    └── article.md
```

### 依存関係

#### Pythonライブラリ

```bash
pip install markdown>=3.4.0       # Markdownパース
pip install beautifulsoup4>=4.12  # HTML/XML操作
pip install requests>=2.31        # URL検証
pip install jsonschema>=4.19      # JSON検証
```

#### オプションツール

```bash
# 高度なMarkdown変換
brew install pandoc  # macOS
apt-get install pandoc  # Ubuntu

# 追加リンティング
npm install -g markdownlint-cli
```

### カスタマイズと拡張

#### カスタム品質メトリクスの追加

```python
# scripts/doc_analyzer.py にカスタムスコア追加

def calculate_custom_score(document):
    """カスタム品質メトリクス"""
    # 例: 図表の数をスコア化
    diagrams = len(re.findall(r'!\[.*?\]\(.*?\)', document))
    diagram_score = min(diagrams * 10, 100)  # 最大100点

    return diagram_score

# Overall scoreの計算に追加
overall_score = weighted_average([
    (structure_score, 0.25),
    (content_score, 0.25),
    (readability_score, 0.20),
    (link_health, 0.15),
    (custom_score, 0.15)  # カスタムスコア追加
])
```

#### カスタム改善ルールの追加

```python
# scripts/doc_improver.py にカスタム改善ルール追加

def add_diagram_suggestions(document):
    """図表追加の提案"""
    suggestions = []

    # Architectureセクションに図がない場合
    if 'Architecture' in document and '![' not in document:
        suggestions.append({
            'priority': 'high',
            'category': 'content',
            'message': 'Add architecture diagram to Architecture section',
            'impact': 10,
            'effort': 'medium'
        })

    return suggestions
```

---

## 📚 参考資料

### スキル関連ドキュメント

- **SKILL.md**: ワークフロー概要と使用ガイド
- **quality-rules/**: 品質基準とチェックリスト定義
- **templates/**: 7種類のドキュメントテンプレート

### 外部リソース

- [EARS形式（Easy Approach to Requirements Syntax）](https://www.iaria.org/conferences2012/filesREQUIRE12/Tutorial%20EARS.pdf)
- [Markdown Guide](https://www.markdownguide.org/)
- [Semantic Versioning](https://semver.org/)
- [Architecture Decision Records (ADR)](https://adr.github.io/)

### ベストプラクティス

- **Plain Language Guidelines**: わかりやすい技術文書の書き方
- **Google Developer Documentation Style Guide**: Googleのドキュメントスタイル
- **Microsoft Writing Style Guide**: Microsoftのライティングガイド

---

## 🎓 まとめ

doc-engineerスキルは、技術ドキュメントの作成から品質保証まで、ライフサイクル全体をカバーする包括的なツールセットです。

### 使い分けのポイント

| シナリオ | 推奨アプローチ |
|---------|-------------|
| 📝 新規ドキュメント作成 | CREATEワークフロー（7フェーズ） |
| ✏️ 既存ドキュメント編集 | EDITワークフロー |
| ✨ 品質向上 | IMPROVEワークフロー |
| 🔍 品質分析のみ | doc_analyzer.py |
| ✅ 検証のみ | doc_validator.py |

### 品質目標

| ドキュメントタイプ | 最小スコア | 推奨スコア |
|------------------|-----------|-----------|
| 内部ドキュメント | 70 | 80 |
| 公開ドキュメント | 80 | 90 |
| クリティカル仕様 | 85 | 95 |

### 次のステップ

1. **学習**: テンプレートを確認し、品質ルールを理解
2. **実践**: 既存ドキュメントで品質分析を試す
3. **応用**: カスタムテンプレートと品質ルールを作成
4. **最適化**: ワークフローを自動化し、CI/CDに統合

doc-engineerスキルを使って、プロフェッショナルで高品質な技術ドキュメントを効率的に作成しましょう！
