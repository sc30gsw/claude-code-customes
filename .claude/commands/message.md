---
allowed-tools: Read, Write, Glob, Grep, TodoWrite
description: Generate communication text for chat, email, tickets, reports, and more
---

# /message - Communication Text Generator

## Overview

Generate well-formatted communication text for various work scenarios: chat messages, business emails, issue tickets, progress reports, announcements, and task outlines.

## Usage

```bash
/message <input> [options]
```

## Arguments
- `input`: The content to transform into a message (required)
  - Can be: direct text in quotes, file path, or topic description

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--format` | `-f` | Output format | `chat` |
| `--lang` | `-l` | Output language (ja/en) | `ja` |
| `--length` | | Message length (short/medium/long) | `medium` |
| `--context` | `-c` | Additional context to include | none |
| `--output` | `-o` | Output file path (displays in console if omitted) | none |
| `--to` | `-t` | Recipient type (team/manager/client/external) | `team` |
| `--urgent` | `-u` | Mark as urgent | false |
| `--priority` | `-p` | Priority level (high/medium/low) | `medium` |

### Output Formats

| Format | Tone | Best For |
|--------|------|----------|
| `chat` | Casual | Slack, Teams, Discord messages |
| `email` | Formal | Business emails, professional communication |
| `ticket` | Technical | Jira, GitHub Issues, bug reports |
| `report` | Structured | Progress reports, weekly/monthly summaries |
| `announcement` | Informative | Company-wide notices, team announcements |
| `outline` | Actionable | Task checklists, work procedures |

### Recipient-Based Tone Adjustment (`--to`)

| Recipient | Tone | Characteristics |
|-----------|------|-----------------|
| `team` | Casual | Friendly, concise, informal |
| `manager` | Polite | Respectful, structured, professional |
| `client` | Formal | Very polite, detailed, professional |
| `external` | Business | First-contact appropriate, courteous |

### Urgency Options

**`--urgent` flag:**
- Japanese: Adds `【緊急】` or `【至急】` prefix
- English: Adds `[URGENT]` prefix

**`--priority` levels:**
- `high`: Emphasizes importance, requests prompt action
- `medium`: Standard tone (default)
- `low`: Indicates flexibility, "when you have time"

## Examples

```bash
# Chat message (formerly slack)
/message "Taking the day off tomorrow" --format chat

# Email to manager
/message "Weekly progress update" --format email --to manager

# Urgent announcement
/message "Server maintenance tonight" --format announcement --urgent

# Progress report
/message ./notes.md --format report --lang ja

# Task outline
/message "Implement user authentication" --format outline --context "Add OAuth2 support"

# High-priority client email
/message "Project status update" --format email --to client --priority high

# Jira ticket
/message "Login bug fix" --format ticket --context "Users cannot log in after password reset"
```

## Processing Workflow

When you receive this command, follow these steps:

### Step 1: Parse Input

1. If input is a file path (`.md`, `.txt`, etc.), use `Read` tool to get content
2. If input is quoted text, use it directly
3. Apply any `--context` as supplementary information

### Step 2: Apply Urgency Prefix

If `--urgent` is set, add appropriate prefix:
- Japanese: `【緊急】` or `【至急】`
- English: `[URGENT]`

If `--priority high`, emphasize urgency in the message body.

### Step 3: Determine Tone Based on Recipient

Adjust language formality based on `--to`:
- **team**: Casual, friendly (e.g., "Hey!", "Thanks!")
- **manager**: Polite, respectful (e.g., "お疲れ様です", "Thank you for your time")
- **client**: Formal, professional (e.g., "いつもお世話になっております", "I hope this email finds you well")
- **external**: Business formal (e.g., "初めてご連絡いたします", "I am reaching out to...")

### Step 4: Generate Based on Format

#### Chat Format (`--format chat`)
**Tone Guidelines:**
- Casual, friendly language
- Use bullet points for lists
- Emojis are welcome
- Keep it concise

**Structure:**
```
[Greeting - optional]

**[Topic/Title]**

- Point 1
- Point 2
- Point 3

[Closing - optional]
```

#### Email Format (`--format email`)
**Tone Guidelines:**
- Professional, polite language
- Use formal greetings and closings
- Structured paragraphs
- Clear subject line

**Structure (Japanese):**
```
件名: [Subject Line]

[宛名] 様

お疲れ様です。

[Introduction - purpose of email]

【[Section Header]】
・[Point 1]
・[Point 2]

[Closing statement]

よろしくお願いいたします。
```

**Structure (English):**
```
Subject: [Subject Line]

Dear [Recipient],

[Opening paragraph - purpose]

[Body - key points]

[Closing paragraph - next steps/call to action]

Best regards,
[Your name]
```

#### Ticket Format (`--format ticket`)
**Tone Guidelines:**
- Technical, precise language
- Structured sections
- Clear acceptance criteria
- Markdown formatting

**Structure:**
```markdown
## Summary
[Brief one-line description]

## Background
[Context and why this is needed]

## Requirements
- [Requirement 1]
- [Requirement 2]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Additional Notes
[Optional: technical details, links, references]
```

#### Report Format (`--format report`)
**Tone Guidelines:**
- Clear, structured presentation
- Data-driven where possible
- Action-oriented conclusions

**Structure (Japanese):**
```markdown
# [レポートタイトル]

**期間**: [対象期間]
**報告者**: [名前]
**報告日**: [日付]

## サマリー
[1-2文で要約]

## 実績
- [完了したこと1]
- [完了したこと2]

## 進行中
- [進行中のタスク1]
- [進行中のタスク2]

## 課題・懸念事項
- [課題があれば記載]

## 次のアクション
- [次にやること]
```

**Structure (English):**
```markdown
# [Report Title]

**Period**: [Date Range]
**Author**: [Name]
**Date**: [Date]

## Summary
[1-2 sentence overview]

## Completed
- [Achievement 1]
- [Achievement 2]

## In Progress
- [Ongoing task 1]
- [Ongoing task 2]

## Issues & Concerns
- [Any blockers or risks]

## Next Steps
- [Action items]
```

#### Announcement Format (`--format announcement`)
**Tone Guidelines:**
- Clear, informative
- Easy to scan
- Include all necessary details

**Structure (Japanese):**
```
【お知らせ】[タイトル]

[本文 - 何についてのお知らせか]

■ 詳細
・[ポイント1]
・[ポイント2]

■ 対象者
[誰に関係するか]

■ 期日・日程
[いつまでに何をするか]

ご不明点があれば、[連絡先]までお問い合わせください。
```

**Structure (English):**
```
[ANNOUNCEMENT] [Title]

[Brief description of what this is about]

Details:
- [Point 1]
- [Point 2]

Who this affects:
[Target audience]

Timeline:
[Relevant dates/deadlines]

Questions? Contact [contact info].
```

#### Outline Format (`--format outline`)
**Tone Guidelines:**
- Action-oriented
- Clear step-by-step structure
- Checkboxes for tracking

**Structure (Japanese):**
```markdown
# [タスク名] - 作業アウトライン

## 目的
[このタスクで達成すること]

## 前提条件
- [ ] [必要な準備1]
- [ ] [必要な準備2]

## 作業手順

### Step 1: [ステップ名]
- [ ] [具体的なアクション]
- [ ] [具体的なアクション]

### Step 2: [ステップ名]
- [ ] [具体的なアクション]
- [ ] [具体的なアクション]

### Step 3: [ステップ名]
- [ ] [具体的なアクション]

## 完了条件
- [ ] [何をもって完了とするか]

## 参考リンク
- [関連ドキュメント]
```

**Structure (English):**
```markdown
# [Task Name] - Work Outline

## Objective
[What this task should achieve]

## Prerequisites
- [ ] [Required preparation 1]
- [ ] [Required preparation 2]

## Procedure

### Step 1: [Step Name]
- [ ] [Specific action]
- [ ] [Specific action]

### Step 2: [Step Name]
- [ ] [Specific action]
- [ ] [Specific action]

### Step 3: [Step Name]
- [ ] [Specific action]

## Definition of Done
- [ ] [Completion criteria]

## References
- [Related documentation]
```

### Step 5: Adjust Length

Based on `--length`:
- **short**: 2-3 sentences, key points only
- **medium**: Standard format with reasonable detail
- **long**: Comprehensive coverage with full context

### Step 6: Generate Output

1. Generate the formatted message
2. If `--output` is specified, write to file using `Write` tool
3. Otherwise, display the message directly in the response

## Output Display Format

When complete, display the generated message:

```
Generated Message (format: chat, lang: ja, to: team)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Generated content here]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ready to copy!
```

If saved to file:
```
Message saved to: {output_path}
```

## Tips

- For chat, emojis help convey tone
- For email, always include a clear subject line
- For tickets, be specific about acceptance criteria
- For reports, include measurable outcomes where possible
- For announcements, highlight key dates/deadlines
- For outlines, break down into small actionable steps
- When converting from file input, summarize key points rather than copying everything
- Use `--to client` for external stakeholders to ensure maximum professionalism
