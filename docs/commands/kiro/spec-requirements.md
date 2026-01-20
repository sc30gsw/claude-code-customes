# Kiro Spec Requirements Command

## 概要

仕様に対する包括的な要件を生成するコマンド。EARS（Easy Approach to Requirements Syntax）形式で受け入れ基準を定義します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:spec-requirements` |
| 引数 | `<feature-name>` |
| 用途 | 要件ドキュメントの生成 |
| 許可ツール | Bash, Glob, Grep, LS, Read, Write, Edit, MultiEdit, Update, WebSearch, WebFetch |

## EARS形式パターン

### 基本パターン
- `WHEN [event/condition] THEN [system] SHALL [response]`
- `IF [precondition/state] THEN [system] SHALL [response]`
- `WHILE [ongoing condition] THE [system] SHALL [continuous behavior]`
- `WHERE [location/context] THE [system] SHALL [contextual behavior]`

### 複合パターン
- `WHEN [event] AND [additional condition] THEN [system] SHALL [response]`
- `IF [condition] AND [additional condition] THEN [system] SHALL [response]`

## 要件ドキュメント構造

```markdown
# Requirements Document

## Introduction
[機能とビジネス価値の要約]

## Requirements

### Requirement 1: [主要な目標領域]
**Objective:** As a [role], I want [feature], so that [benefit]

#### Acceptance Criteria
1. WHEN [event] THEN [system] SHALL [response]
2. IF [precondition] THEN [system] SHALL [response]

### Requirement 2: [次の主要領域]
...
```

## 使用例

```bash
# 要件を生成
/kiro:spec-requirements user-authentication

# 要件を確認後、設計フェーズへ
/kiro:spec-design user-authentication -y
```

## コンテキスト検証

実行前に以下を確認：
- アーキテクチャコンテキスト: `.kiro/steering/structure.md`
- 技術的制約: `.kiro/steering/tech.md`
- プロダクトコンテキスト: `.kiro/steering/product.md`

## 次のフェーズ

要件生成後：
- **要件がOKな場合**: `/kiro:spec-design <feature-name> -y`
- **修正が必要な場合**: 変更を要求し、再度このコマンドを実行
