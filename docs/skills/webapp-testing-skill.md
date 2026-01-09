---
name: webapp-testing
description: Playwrightを使用したローカルWebアプリケーションとのインタラクションとテストのためのツールキット。フロントエンド機能の検証、UI動作のデバッグ、ブラウザスクリーンショットのキャプチャ、ブラウザログの表示をサポート。
license: LICENSE.txtの完全な条件を参照
---

# Webアプリケーションテスト

ローカルWebアプリケーションをテストするには、ネイティブPython Playwrightスクリプトを作成する。

**利用可能なヘルパースクリプト**:
- `scripts/with_server.py` - サーバーライフサイクルを管理（複数サーバーをサポート）

**スクリプトは必ず最初に`--help`で実行して**使用方法を確認。カスタマイズされたソリューションが絶対に必要であることがわかるまでソースを読まない。これらのスクリプトは非常に大きくなる可能性があり、コンテキストウィンドウを汚染する。コンテキストウィンドウに取り込むのではなく、ブラックボックススクリプトとして直接呼び出すために存在する。

## 決定ツリー：アプローチの選択

```
ユーザータスク → 静的HTMLか？
    ├─ はい → HTMLファイルを直接読んでセレクタを特定
    │         ├─ 成功 → セレクタを使用してPlaywrightスクリプトを作成
    │         └─ 失敗/不完全 → 動的として扱う（下記）
    │
    └─ いいえ（動的webapp） → サーバーは既に起動中か？
        ├─ いいえ → 実行: python scripts/with_server.py --help
        │           ヘルパーを使用 + 簡略化されたPlaywrightスクリプトを作成
        │
        └─ はい → 偵察してからアクション:
            1. ナビゲートしてnetworkidleを待つ
            2. スクリーンショットを撮るかDOMを検査
            3. レンダリングされた状態からセレクタを特定
            4. 発見したセレクタでアクションを実行
```

## 例：with_server.pyの使用

サーバーを起動するには、まず`--help`を実行してからヘルパーを使用:

**単一サーバー:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**複数サーバー（例：バックエンド + フロントエンド）:**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

自動化スクリプトを作成するには、Playwrightロジックのみを含める（サーバーは自動管理される）:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # 常にヘッドレスモードでchromiumを起動
    page = browser.new_page()
    page.goto('http://localhost:5173') # サーバーは既に起動して準備完了
    page.wait_for_load_state('networkidle') # 重要：JSの実行を待つ
    # ... 自動化ロジック
    browser.close()
```

## 偵察してからアクションパターン

1. **レンダリングされたDOMを検査**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. 検査結果から**セレクタを特定**

3. 発見したセレクタを使用して**アクションを実行**

## よくある落とし穴

- 動的アプリで`networkidle`を待つ前にDOMを検査**しない**
- 検査前に`page.wait_for_load_state('networkidle')`を待つ**こと**

## ベストプラクティス

- **バンドルされたスクリプトをブラックボックスとして使用** - タスクを達成するために、`scripts/`で利用可能なスクリプトが役立つかどうかを検討。これらのスクリプトは、コンテキストウィンドウを乱雑にすることなく、一般的で複雑なワークフローを確実に処理する。`--help`で使用方法を確認し、直接呼び出す。
- 同期スクリプトには`sync_playwright()`を使用
- 完了したら必ずブラウザを閉じる
- 説明的なセレクタを使用：`text=`、`role=`、CSSセレクタ、またはID
- 適切な待機を追加：`page.wait_for_selector()`または`page.wait_for_timeout()`

## リファレンスファイル

- **examples/** - 一般的なパターンを示す例:
  - `element_discovery.py` - ページ上のボタン、リンク、入力の発見
  - `static_html_automation.py` - ローカルHTMLでのfile:// URLの使用
  - `console_logging.py` - 自動化中のコンソールログのキャプチャ
