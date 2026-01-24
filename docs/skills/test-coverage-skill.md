# Test Coverage Skill

## 概要

テストカバレッジを分析し、80%以上のカバレッジを達成するために不足しているテストを生成するスキル。ユニット、インテグレーション、E2Eテストを包括的にカバーします。

## アクティベーショントリガー

- テストカバレッジが低い時
- カバレッジ目標を達成したい時
- 未テストのコードパスを特定したい時
- テストスイートを拡充したい時

## 使用方法

```bash
/test-coverage
```

## ワークフロー

### Step 1: カバレッジ付きテスト実行
```bash
npm test --coverage
# または
pnpm test --coverage
```

### Step 2: カバレッジレポート分析
`coverage/coverage-summary.json`を分析

### Step 3: 80%閾値未満のファイル特定

### Step 4: 各未カバーファイルに対して
- 未テストのコードパスを分析
- 関数用のユニットテストを生成
- API用のインテグレーションテストを生成
- クリティカルフロー用のE2Eテストを生成

### Step 5: 新しいテストがパスすることを確認

### Step 6: Before/Afterカバレッジメトリクスを表示

### Step 7: プロジェクト全体で80%+カバレッジを確保

## テスト生成の焦点

### ハッピーパスシナリオ
- 正常なユーザーフロー
- 期待される入力と出力
- 成功ケース

### エラーハンドリング
- 例外処理
- エラーメッセージ
- 失敗からの回復

### エッジケース
- null, undefined, empty
- 極端な値
- 特殊文字

### 境界条件
- 最小値/最大値
- 配列の境界
- タイムアウト

## カバレッジレポート形式

```json
{
  "total": {
    "lines": { "total": 1000, "covered": 750, "pct": 75 },
    "statements": { "total": 1200, "covered": 900, "pct": 75 },
    "functions": { "total": 150, "covered": 120, "pct": 80 },
    "branches": { "total": 200, "covered": 140, "pct": 70 }
  },
  "/src/utils/validation.ts": {
    "lines": { "total": 50, "covered": 30, "pct": 60 },
    "statements": { "total": 60, "covered": 36, "pct": 60 },
    "functions": { "total": 8, "covered": 5, "pct": 62.5 },
    "branches": { "total": 12, "covered": 6, "pct": 50 }
  }
}
```

## 出力例

```
📊 Coverage Analysis Report

Current Coverage: 75%
Target Coverage: 80%
Gap: 5%

📁 Files Below Threshold:

src/utils/validation.ts (60%)
├── Missing: validateEmail() error paths
├── Missing: validatePhone() edge cases
└── Action: Generate 4 additional tests

src/services/auth.ts (65%)
├── Missing: login() failure scenarios
├── Missing: refreshToken() edge cases
└── Action: Generate 6 additional tests

src/components/Form.tsx (70%)
├── Missing: submit handler tests
├── Missing: validation feedback tests
└── Action: Generate 3 additional tests

🧪 Tests Generated: 13
📈 Projected Coverage: 82%
```

## テスト優先順位

| 優先度 | カバレッジ | アクション |
|--------|-----------|-----------|
| 高 | 0-50% | 即座にテスト追加 |
| 中 | 50-70% | 重要パスをカバー |
| 低 | 70-80% | エッジケース追加 |

## カバレッジタイプ

| タイプ | 説明 | 重要度 |
|--------|------|--------|
| Lines | 実行された行数 | 高 |
| Statements | 実行された文の数 | 高 |
| Functions | 呼び出された関数数 | 中 |
| Branches | 実行された分岐数 | 高 |

## ベストプラクティス

1. **段階的改善** - 一度に全てをカバーしようとしない
2. **重要なパスを優先** - ビジネスロジックを先に
3. **エッジケースを忘れない** - 境界条件をテスト
4. **モックを適切に** - 外部依存をモック
5. **定期的に実行** - CIで継続的にチェック

## 成功指標

- 全体カバレッジ80%以上
- クリティカルファイルは90%以上
- すべての生成テストがパス
- Before/Afterで改善が確認できる
- CI/CDに統合されている
