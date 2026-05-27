---
name: notion-bug-pr
description: Skill that pulls bug tickets (titles containing 「不具合」) from a Notion database, investigates root cause in a GitHub repo, applies fixes, and opens draft PRs. Supports three modes — daily recurring schedule, one-shot at a specific time, or immediate on-demand run. Takes three or four args: Notion database URL, repo path or name, and either HH:MM (daily), "once HH:MM" (one-shot), or "now" (immediate).
---

# notion-bug-pr

Fetches tickets whose title contains the substring 「不具合」 from a Notion database and automatically investigates, fixes, and opens draft PRs in the corresponding GitHub repository. PR 本文のテンプレート検出・スコア算出・Mermaid 生成は `/git-pr -p` に委譲し、作成後にタイトル上書きと Notion URL フッター追記を行う。 PR 本文のテンプレート検出・スコア算出・Mermaid 生成は `/git-pr -p` に委譲し、作成後にタイトル上書きと Notion URL フッター追記を行う。

## Usage

```
/notion-bug-pr <notion-database-url> <repo-path-or-name> <HH:MM>        # Daily at HH:MM (default)
/notion-bug-pr <notion-database-url> <repo-path-or-name> once <HH:MM>   # One-shot at HH:MM
/notion-bug-pr <notion-database-url> <repo-path-or-name> now             # Run immediately
```

| Argument | Description | Example |
|----------|-------------|---------|
| `<notion-database-url>` | Shared URL of the Notion database. | `https://www.notion.so/<workspace>/<db-id>?v=...` |
| `<repo-path-or-name>` | Absolute/relative local path, or repo name under `~/work`, `~/dev`, `~/projects`, etc. | `~/work/myapp` or `myapp` |
| `<HH:MM>` | Run time in 24-hour notation. | `22:00` |

Examples:

```
/notion-bug-pr https://www.notion.so/ws/abc123 ~/work/myapp 22:00
/notion-bug-pr https://www.notion.so/ws/abc123 myapp once 09:30
/notion-bug-pr https://www.notion.so/ws/abc123 myapp now
```

## Three execution modes

| Mode | Invocation | CronCreate | Description |
|------|-----------|------------|-------------|
| **daily** | `HH:MM` | `recurring: true, durable: true` | Fires every day until stopped. Auto-renews to avoid the 7-day expiry. |
| **once** | `once HH:MM` | `recurring: false` | Fires once at the specified time, then auto-deletes. |
| **now** | `now` | Not called | Skips scheduling and runs the bug-fix procedure immediately. |

Run mode is started by the remote agent when cron fires, or inline for `now`.

How to choose execution mode:
- Prompt contains `RUN_MODE=1` → **Run mode** (cron-triggered or inline for `now`)
- Otherwise → **Setup mode** (user typed the command)

## Setup mode procedure

Run when the user supplies all required arguments.

### 1. Validate arguments

- **Notion URL**: Ensure the domain is `notion.so` or `notion.site`. Extract and keep the database ID with a regex (`[0-9a-f]{32}` or hyphenated UUID).
- **Repo resolution**:
  - If the argument starts with `/` or `~`, or is a path containing `.` → resolve as a path (absolute with `realpath`).
  - Otherwise → check in order and use the first match:
    1. `$HOME/work/<name>`
    2. `$HOME/dev/<name>`
    3. `$HOME/projects/<name>`
    4. `$HOME/src/<name>`
    5. `$HOME/<name>`
  - After resolution, error if `.git/` is missing (not a Git repository).
- **Mode detection**:
  - 3rd arg is `now` → **now mode**; skip time validation, proceed to §4 (Run mode) immediately.
  - 3rd arg is `once` and 4th arg is a valid `HH:MM` → **once mode**.
  - 3rd arg matches `HH:MM` pattern → **daily mode**.
  - Otherwise → show error with usage and stop.
- **Time validation** (daily and once modes): Parse `HH:MM`. `HH` must be 0–23, `MM` 0–59. On failure, show an error and stop.

### 2. Register cron (daily and once modes only)

#### Daily mode

Convert `HH:MM` to cron `M H * * *` (e.g. `22:00` → `0 22 * * *`).

Before registering, call `CronList` and delete any existing jobs whose `prompt` contains both `RUN_MODE=1 MODE=daily` and the resolved repo path, using `CronDelete <id>` for each match. This prevents job accumulation when the user re-runs setup.

Call `CronCreate`:

- `schedule`: e.g. `"0 22 * * *"`
- `recurring`: `true`
- `durable`: `true`
- `prompt`: Build from the template below

```
RUN_MODE=1 MODE=daily /notion-bug-pr <resolved-full-path> <Notion DB URL>

You are running in Run mode. Execute the Run Mode procedure documented in the notion-bug-pr SKILL.md.
Repo: <resolved-full-path>
Notion DB URL: <Notion DB URL>
```

#### Once mode

Determine the fire date:
- Parse the current local time.
- If `HH:MM` is later than now today → use today's date: `DD`, `MM`-of-month.
- If `HH:MM` has already passed today → use tomorrow's date.
- Build cron: `"<min> <hour> <dom> <mon> *"` (all four values pinned).

Call `CronCreate`:

- `schedule`: e.g. `"30 9 16 5 *"`
- `recurring`: `false`
- `durable`: `true`
- `prompt`: Build from the template below

```
RUN_MODE=1 MODE=once /notion-bug-pr <resolved-full-path> <Notion DB URL>

You are running in Run mode (one-shot). Execute the Run Mode procedure documented in the notion-bug-pr SKILL.md.
Repo: <resolved-full-path>
Notion DB URL: <Notion DB URL>
```

> **Important**: Expand and embed the Notion URL and repo absolute path as literal text in `prompt`. Do not pass them as separate arguments later.

### 3. Now mode — run immediately

When the 3rd argument is `now`, skip cron registration. Instead, set internal markers `RUN_MODE=1 MODE=now` and immediately execute the Run mode procedure (§4 onward) inline in this same session.

Print before starting:

```
▶ Running on-demand now — results below.
```

### 4. Completion message (daily and once modes)

Include the return value from `CronCreate` (job ID) and output the appropriate message:

**Daily:**
```
✅ Registered daily bug-PR job

  Job ID   : <id>
  Schedule : every day at HH:MM
  Repository: <absolute-path>
  Notion DB: <URL>

To stop: CronDelete <id>
To list jobs: CronList
```

**Once:**
```
✅ Scheduled one-shot bug-PR run

  Job ID   : <id>
  Fires at : YYYY-MM-DD HH:MM
  Repository: <absolute-path>
  Notion DB: <URL>

(Auto-deletes after firing. To cancel early: CronDelete <id>)
```

## Run mode procedure

When cron fires (or `now` mode is invoked), the agent runs with `RUN_MODE=1`.

### 1. Parse arguments

Extract from the prompt:
- Repo absolute path
- Notion DB URL
- `MODE` value (`daily`, `once`, or `now`)

### 2. Fetch 「不具合」 tickets from Notion

Use tools from the Notion MCP server (`mcp__claude_ai_Notion__*`). Pick concrete tool names from what is available at runtime:

- First run `ToolSearch` with `query: "notion"` and load available Notion MCP tools (search / database query / page fetch), excluding auth-only tools.
- On auth errors, tell the user to use `mcp__claude_ai_Notion__authenticate` and stop.

#### 2-1. Identify the target database(s)

Fetch the URL with `notion-fetch`. Check `metadata.type` in the response:

- **`type == "database"`**: Use that database's data source URL directly.
- **`type == "page"`**: Parse the fetched page content for `<database ... data-source-url="collection://...">` tags. Collect **only** the inline database(s) listed on that page. Do **not** search the parent database, sibling databases, or any other database not explicitly embedded on the page.

#### 2-2. Query for bug tickets

For each identified data source, inspect the schema first (via `notion-fetch` on the `collection://` URL):

- **If a `不具合チケット` checkbox property exists**: use `不具合チケット = '__YES__'` as the primary filter. This is more reliable than title-text search.
- **Otherwise**: filter by title (usually `名前` or `Name`) containing 「不具合」.

Exclude tickets where the status property equals any of: 「完了」, 「却下」, `Done`, `Closed`, `Rejected`. Only process tickets in active/open statuses (e.g. 「進行中」, 「開始前」, `In Progress`, `Open`, `Todo`).

- For each matched ticket, fetch its full body content (reproduction steps, expected/actual behavior, etc.).
- Record the **Notion page ID** (32-char hex, strip hyphens) and **full page URL** for each ticket — both are needed for duplicate detection.

### 3. Prepare the repository

```bash
cd <repo-path>
git fetch origin
git checkout main 2>/dev/null || git checkout master
git pull --rebase --autostash
```

If neither `main` nor `master` exists, get the default branch with `git remote show origin | grep 'HEAD branch'`.

### 4. Process every ticket in order

Loop. For each ticket:

#### 4-1. Investigation

- Read the ticket body and summarize symptoms and repro steps.
- Search the repo with Grep / Read / Serena MCP and narrow likely root-cause locations.
- State the fix approach in one paragraph (for the PR body later).

#### 4-1.5. Duplicate PR detection

Before creating a branch or making any changes, check whether a PR for this ticket already exists:

1. Extract the Notion page ID (`<page-id>`, 32-char hex without hyphens) and the full page URL (`<page-url>`).
2. Run both searches:
   ```bash
   gh pr list --state all --limit 50 --search "<page-id>"
   gh pr list --state all --limit 50 --search "<page-url>"
   ```
3. If either search returns a result → **skip this ticket**. Record skip reason as `duplicate PR exists: <existing-pr-url>`.
4. If no results → continue to §4-2.

#### 4-2. Branch and fix

- Branch name: `fix/<slug>-<ticket-short-id>`
  - slug: Alphanumeric from the title after removing Japanese characters and symbols; if none, use `bug`
  - short-id: First 8 characters of the Notion page ID
- Fix commit:
  ```bash
  git checkout -b <branch>
  # edit files
  git add <files>
  git commit -m "fix: <short description>

  Refs: <notion-page-url>"
  ```
  The commit message **must** include `Refs: <notion-page-url>` so the Notion URL is embedded in git history.
- If a fix is not feasible (unclear spec, unknown root cause after investigation, tests needed but cannot be written, etc.), skip the ticket and record the reason.

#### 4-3. PR 本文生成は /git-pr に委譲

PR テンプレートの検出・セクション穴埋め・スコア算出・Mermaid 生成はすべて `/git-pr -p` 側で行う。ここでは何もしない。§4-4 で `/git-pr -p` を呼び出す。

#### 4-4. Open PR

1. **Invoke `/git-pr -p`** via the Skill tool (`skill: "git-pr"`, `args: "-p"`). The `-p` flag handles `git push -u origin <branch>`, so do not run a separate `git push`.

2. **Retrieve the PR number and URL**:
   ```bash
   PR_NUM=$(gh pr view --json number -q '.number')
   PR_URL=$(gh pr view --json url -q '.url')
   ```

3. **Override the title** to preserve the ticket link:
   ```bash
   gh pr edit "$PR_NUM" --title "fix: <ticket title>"
   ```

4. **Append the Notion footer** so §4-1.5 duplicate detection keeps working:
   ```bash
   gh pr view "$PR_NUM" --json body -q '.body' > /tmp/notion-bug-pr-body.md
   printf '\n\n---\n🔗 Notion ticket: %s\n' "<notion-page-url>" >> /tmp/notion-bug-pr-body.md
   gh pr edit "$PR_NUM" --body-file /tmp/notion-bug-pr-body.md
   rm -f /tmp/notion-bug-pr-body.md
   ```
   This preserves the badges, score tables, and Mermaid diagram generated by `/git-pr`, appending only the Notion URL at the end.

5. **Fallback if `/git-pr -p` fails** (non-zero exit or `gh pr view` returns nothing): do **not** skip the ticket — fall back to the legacy flow:
   ```bash
   git push -u origin <branch>
   gh pr create --draft \
     --title "fix: <ticket title>" \
     --body "## Bug summary

   <symptoms from Notion ticket>

   ## Root cause

   <investigation notes>

   ## What changed

   <files changed and how>

   ## Impact / testing

   <affected areas and tests>

   ---
   🔗 Notion ticket: <notion-page-url>"
   ```
   Record `⚠️ /git-pr fallback used: <reason>` in the completion report.

6. **Record the PR URL** on success; continue to §4-5.

#### 4-5. Cleanup

- `git checkout main` (or the default branch used for the next ticket)

### 5. Completion report

After all tickets, print a summary:

```
📊 Run complete

  Tickets processed: N
  PRs opened: X
  Skipped: Y

PRs:
  - <title> → <pr-url>
  - ...

Skip reasons:
  - <title>: <reason>
  - ...
```

### 6. Cron auto-renewal (daily mode only)

After the completion report, **if and only if `MODE=daily`**, re-register the daily cron to prevent the 7-day auto-expiry from stopping the job:

1. Call `CronList` to get all active jobs.
2. For each job whose `prompt` contains both `RUN_MODE=1 MODE=daily` and the repo path from the current run context, call `CronDelete <id>`. This removes all previous instances before creating a fresh one.
3. Call `CronCreate` with the same `schedule`, `recurring: true`, `durable: true`, and the same `prompt`.
4. On success: silently continue (do not print extra output).
5. On failure: append to the report:
   ```
   ⚠️ Cron re-registration failed: <reason>
      Please re-run /notion-bug-pr to restore the daily schedule.
   ```

`once` and `now` modes skip this step entirely.

## Error handling

| Situation | Action |
|-----------|--------|
| Notion MCP auth expired | Point user to `mcp__claude_ai_Notion__authenticate` and stop. Do not authenticate on their behalf. |
| `gh` not authenticated | Record the ticket from the error, skip, report at the end. |
| Repo is not a Git repository | Reject registration in Setup mode; in Run mode skip all and report. |
| Neither `main` nor `master` | Get default branch via `git remote show origin`. Abort if that fails. |
| Ticket status is 却下 / Closed / Rejected | Skip silently — do not process rejected tickets. |
| Ticket body does not allow a fix | Skip and include reason in the report. |
| Duplicate PR detected via `gh pr list --search` | Skip. Reason: `duplicate PR exists: <url>`. Branch-name check alone is no longer sufficient. |
| Cron re-registration fails (daily mode) | Append warning to report; do not abort. |
| `/git-pr -p` execution fails | Fall back to plain `gh pr create --draft` and create the PR with a minimal body. Record `⚠️ /git-pr fallback used: <reason>` in the completion report. |

## Related skills

- `/git-pr`: Directly invoked in §4-4 via the Skill tool (`skill: "git-pr"`, `args: "-p"`). Handles push + body generation + draft PR creation. `/notion-bug-pr` only post-processes the result: title override and Notion footer append. On failure, `/notion-bug-pr` falls back to a plain `gh pr create --draft` without invoking `/git-pr`.
- `/schedule`: For longer-lived or externally managed schedules, consider `/schedule` instead of the session-bound `CronCreate`.
- Stop daily job: `CronDelete <id>` or `/schedule` management commands.

## Notes

- This skill creates **draft** PRs. A human must review before merge.
- **7-day expiry**: `CronCreate` recurring jobs auto-expire after 7 days. This skill mitigates this with two measures: `durable: true` (survives Claude restarts) and auto-renewal at the end of every daily Run mode execution.
- Duplicate PR detection uses `gh pr list --search` with the Notion ticket ID/URL, so it catches existing PRs even if the original branch was deleted or a different branch name was used.
- Commits should follow minimal-diff rules; no drive-by refactors.
- `/git-pr` auto-generates the PR title; this skill always overrides it with `fix: <ticket title>` via `gh pr edit --title` to preserve the explicit link to the Notion ticket.
- The Notion URL footer (`---\n🔗 Notion ticket: <url>`) is non-negotiable — it is the anchor for `§4-1.5` duplicate detection. `/git-pr` does not include it, so it is appended post-hoc via `gh pr edit --body-file`. If `/git-pr` fails and the fallback is used, the footer is embedded directly in the `gh pr create --body` string.
