# Dependabot Check Skill

## 概要

Dependabotセキュリティアドバイザリを分析し、解決戦略を提供するスキル。脆弱性のあるパッケージを特定し、適切な更新方法を提案します。

## アクティベーショントリガー

- DependabotのセキュリティアラートURLを受け取った時
- 依存パッケージのセキュリティ脆弱性を調査する時
- `npm audit` や `pnpm audit` で脆弱性が検出された時

## 使用方法

```bash
/dependabot-check <dependabot_url>
```

## ワークフロー

### Step 1: アドバイザリ情報の取得

URLタイプに応じて適切なコマンドを使用：
- `/security/dependabot/[number]` を含む場合: `gh api /repos/[owner]/[repo]/dependabot/alerts/[number]`
- `/pull/` を含む場合: `gh pr view [url] --json title,body,commits`
- GitHub Security Advisory ID (GHSA-xxxx) を含む場合: `gh api /advisories/[GHSA-ID]`

### Step 2: 現在のプロジェクト状態を確認

```bash
git status
pnpm list --depth=0    # 直接依存関係を確認
pnpm why [package]     # 依存関係ツリーを確認
```

### Step 3: 依存関係の分析

1. **直接依存 vs 間接依存を確認**
   - package.jsonにパッケージが存在するか確認
   - 存在する場合: 直接依存
   - 存在しない場合: 間接依存

2. **依存関係ツリーを分析**
   - `pnpm why [package-name]` を使用
   - 親パッケージを特定

### Step 4: 解決戦略

**直接依存の場合：**
```bash
pnpm update [package-name]
# または package.json のバージョンを変更後
pnpm install
```

**間接依存の場合：**
1. 親パッケージの更新がマイナー/パッチ（低リスク）か メジャー（高リスク）かを確認
2. マイナー/パッチ更新の場合: 親パッケージを直接更新
3. メジャー更新の場合: pnpm overridesの使用を検討

```json
{
  "pnpm": {
    "overrides": {
      "[package-name]": "^[safe-version]"
    }
  }
}
```

## 出力フォーマット

```markdown
## 🚨 Dependabot Advisory 分析

**参照URL**: [url]

### 脆弱なパッケージ
- **パッケージ名**: [name] ([直接/間接])
- **現在のバージョン**: [current] → **推奨**: [recommended]
- **重大度**: [level]

### 🔧 解決戦略
- **親パッケージ**: [parent] ([current] → [required])
- **更新レベル**: [Major/Minor/Patch]
- **推奨方法**: [approach]

### 📋 チェックリスト
- [ ] ロックファイルの変更を確認
- [ ] 依存関係のソースを特定
- [ ] 破壊的変更を確認
```

## ベストプラクティス

1. **事前確認** - 更新前に現在の依存関係ツリーを把握
2. **段階的更新** - 一度に複数のパッケージを更新しない
3. **テスト実行** - 更新後に必ずテストを実行
4. **ロックファイル確認** - 意図しない変更がないか確認
5. **CI確認** - PRを作成してCIが通過することを確認
