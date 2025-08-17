# Claude Code 専門家システム

開発プロジェクトにおいて、Claude Codeの様々な専門家があなたの開発をサポートします。

## 基本的な使い方

### Serenaとの連携
常に最新のSerenaとの連携を行い、最適な開発環境を提供します。

### コンテキスト保持
過去の会話のコンテキストを保持し、継続的な開発支援を行います。

### 専門性
それぞれの専門家は特定の技術領域に特化しています。

---

## カテゴリ別専門家一覧

詳細な専門家情報については、以下のカテゴリ別ファイルを参照してください：

### [開発・設計専門家](./sub-agents/development-design.md)
- `/backend-architect` - バックエンド設計者
- `/frontend-developer` - フロントエンド開発者
- `/mobile-developer` - モバイル開発者

### [インフラ・運用専門家](./sub-agents/infrastructure-operations.md)
- `/cloud-architect` - クラウド設計者
- `/terraform-specialist` - Terraform専門家
- `/devops-engineer` - DevOps・CI/CD

### [品質・セキュリティ専門家](./sub-agents/quality-security.md)
- `/code-reviewer` - コードレビュー専門家
- `/testing-specialist` - テスト専門家
- `/security-engineer` - セキュリティ専門家

### [データ・検索専門家](./sub-agents/data-search.md)
- `/database-architect` - データベース設計者
- `/search-specialist` - 検索・情報収集専門家

### [UI/UX・デザイン専門家](./sub-agents/ui-ux-design.md)
- `/ui-ux-designer` - UI/UX設計者
- `/react-performance-optimization` - React最適化専門家

### [コマンド開発・運用支援](./sub-agents/command-development.md)
- `/command-expert` - CLIコマンド設計
- `/serena-expert` - Serena連携エキスパート

---

## 専門家選択ガイド

### 開発フェーズ別おすすめ専門家

| フェーズ | おすすめ専門家 |
|---------|-----------------|
| **要件定義** | search-specialist, ui-ux-designer |
| **設計** | backend-architect, frontend-developer, cloud-architect |
| **実装** | mobile-developer, database-architect, command-expert |
| **テスト** | testing-specialist, react-performance-optimization |
| **運用** | devops-engineer, terraform-specialist |
| **運用・保守** | security-engineer, code-reviewer |

### 課題別おすすめ専門家

| 課題分類 | おすすめ専門家 |
|-----------|-----------------|
| **パフォーマンス課題** | react-performance-optimization, database-architect |
| **セキュリティ課題** | security-engineer, code-reviewer |
| **インフラ課題** | cloud-architect, devops-engineer, terraform-specialist |
| **UI/UX課題** | ui-ux-designer, frontend-developer |
| **テスト課題** | testing-specialist, code-reviewer |

### 技術別おすすめ専門家

| 技術分野 | おすすめ専門家 |
|-------------|-----------------|
| **React/Next.js** | frontend-developer, react-performance-optimization |
| **Node.js/Express** | backend-architect, security-engineer |
| **モバイル** | mobile-developer, ui-ux-designer |
| **AWS/GCP/Azure** | cloud-architect, terraform-specialist, devops-engineer |
| **データベース** | database-architect, backend-architect |

---

## 専門性組み合わせ

### 複合専門性パターン

1. **フルスタック開発**:
   `backend-architect` + `frontend-developer` + `testing-specialist` + `code-reviewer`

2. **インフラ構築**:
   `cloud-architect` + `terraform-specialist` + `devops-engineer` + `security-engineer`

3. **パフォーマンス最適化**:
   `react-performance-optimization` + `database-architect` + `code-reviewer`

4. **セキュリティ強化**:
   `security-engineer` + `code-reviewer` + `testing-specialist`

### 継続的サポート

プロジェクトの各段階で継続的にサポートします。

- **code-reviewer**: コード品質の継続的改善
- **security-engineer**: セキュリティ対策の継続監視
- **react-performance-optimization**: React パフォーマンス最適化の継続改善
- **cloud-architect**: 運用環境最適化の継続改善

---

## 専門家一覧

| 専門家コマンド | カテゴリー | 主要領域 |
|-------------|---------|-------------|
| `/backend-architect` | 開発・設計 | API設計・マイクロサービス |
| `/frontend-developer` | 開発・設計 | React・モダンフロントエンド |
| `/mobile-developer` | 開発・設計 | React Native・Flutter・クロスプラットフォーム |
| `/cloud-architect` | インフラ・運用 | クラウド設計・コスト最適化 |
| `/terraform-specialist` | インフラ・運用 | Terraform・IaC・環境管理 |
| `/devops-engineer` | インフラ・運用 | CI/CD・運用自動化 |
| `/code-reviewer` | 品質・セキュリティ | コード品質・静的解析 |
| `/testing-specialist` | 品質・セキュリティ | テスト戦略・TDD |
| `/security-engineer` | 品質・セキュリティ | セキュリティ・脆弱性・コンプライアンス |
| `/database-architect` | データ・検索 | データベース設計・最適化 |
| `/search-specialist` | データ・検索 | 検索・情報収集・情報整理 |
| `/ui-ux-designer` | UI/UX・デザイン | ユーザビリティ・UX最適化 |
| `/react-performance-optimization` | UI/UX・デザイン | React パフォーマンス最適化 |
| `/command-expert` | コマンド開発・運用支援 | CLI コマンド設計・実装 |
| `/serena-expert` | コマンド開発・運用支援 | マルチスケール開発支援 |