# Kiro Spec Status Command

## 概要

仕様の現在のステータスと進捗を表示するコマンド。各フェーズの完了状況、品質メトリクス、次のアクションを提供します。

## 基本情報

| 項目 | 値 |
|------|-----|
| コマンド | `/kiro:spec-status` |
| 引数 | `<feature-name>` |
| 用途 | 仕様の進捗確認 |
| 許可ツール | Bash, Read, Glob, Write, Edit, MultiEdit, Update |

## 表示内容

### 1. 仕様の概要
- フィーチャー名と説明
- 作成日と最終更新日
- 現在のフェーズ（requirements/design/tasks/implementation）
- 全体の完了率

### 2. フェーズステータス

```markdown
✅ **Requirements Phase**: [completion %]
  - 要件数: [number]
  - 受け入れ基準定義: [yes/no]
  - 要件カバレッジ: [complete/partial/missing]

✅ **Design Phase**: [completion %]
  - アーキテクチャ文書化: [yes/no]
  - コンポーネント定義: [yes/no]
  - 図の作成: [yes/no]
  - 統合計画: [yes/no]

✅ **Tasks Phase**: [completion %]
  - 総タスク数: [number]
  - 完了タスク: [number]
  - 残りタスク: [number]
  - ブロックされたタスク: [number]
```

### 3. 実装進捗
- タスク完了の内訳
- 現在のブロッカーや問題
- 完了までの推定時間
- 必要な次のアクション

### 4. 品質メトリクス
- 要件カバレッジ: [percentage]
- 設計の完全性: [percentage]
- タスク粒度: [適切/大きすぎ/小さすぎ]
- 依存関係解決: [yes/no]

### 5. 推奨事項
- 次に取るべきステップ
- 対処すべき潜在的な問題
- 改善提案
- 完了すべき欠落要素

### 6. Steeringアライメント
- アーキテクチャ一貫性: [aligned/misaligned]
- 技術スタック準拠: [compliant/non-compliant]
- プロダクト要件整合: [aligned/misaligned]

## 使用例

```bash
# 特定の仕様のステータスを確認
/kiro:spec-status user-authentication

# すべての仕様を一覧表示
ls .kiro/specs/
```

## タスク完了追跡

tasks.mdのチェックボックスステータスを解析：
- `- [x]` - 完了
- `- [ ]` - 保留

完了率と次の未完了タスクを表示します。
