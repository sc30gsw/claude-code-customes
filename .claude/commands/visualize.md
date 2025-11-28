---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_wait_for, mcp__playwright__browser_resize, mcp__playwright__browser_close, Glob
description: Convert documents to infographic images (PNG/JPG/PDF) for easy sharing
---

# /visualize - Document to Infographic Converter

## Overview

Transform documents into visually appealing infographic images that can be shared on chat applications like Slack, Teams, or Discord. Supports both quick summaries and detailed multi-section documents.

## Usage

```bash
/visualize <input-file> [options]
```

## Arguments
- `input-file`: Path to the document to visualize (required)
  - Supported formats: `.md`, `.txt`, `.pdf`

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output file path | `{input}-infographic.png` |
| `--format` | `-f` | Output format (png/jpg/pdf) | `png` |
| `--theme` | `-t` | Visual theme | `business` |
| `--size` | `-s` | Image size preset | `chat` |
| `--max-points` | `-m` | Maximum key points to extract | `6` |
| `--lang` | `-l` | Output language (ja/en) | `ja` |
| `--title` | | Custom title (overrides auto-extraction) | auto |
| `--style` | | Output style (summary/visual/detailed) | `summary` |
| `--audience` | `-a` | Target audience (executive/team/technical) | `team` |
| `--diagram` | `-d` | Include Mermaid diagrams | `false` |
| `--icons` | | Show icons for key points | `true` |
| `--sections` | | Number of sections (detailed style) | `auto` |

### Themes

| Theme | Description | Best For |
|-------|-------------|----------|
| `business` | Professional blue tones, clean layout | Work presentations |
| `modern` | Vibrant colors, gradient backgrounds | Marketing materials |
| `tech` | Dark accents, monospace fonts | Technical documentation |
| `minimal` | White space, simple typography | Clean summaries |
| `dark` | Dark background, high contrast | Screen-friendly viewing |

### Size Presets

| Preset | Dimensions | Best For |
|--------|------------|----------|
| `chat` | 1200x630px | Slack, Teams, Discord sharing |
| `slide` | 1920x1080px | Presentations |
| `a4` | 2480x3508px | Print (A4 portrait) |
| `square` | 1080x1080px | Social media |

### Output Styles

| Style | Description | Use Case | Understanding Level |
|-------|-------------|----------|---------------------|
| `summary` | Single page, concise overview | Quick sharing, chat previews | Surface (what exists) |
| `visual` | Diagram + context explanation | Understanding documents | **Deep (why & how)** |
| `detailed` | Multi-section document with TOC | Formal reports | Comprehensive (everything) |

### Target Audience

| Audience | Tone | Content Focus |
|----------|------|---------------|
| `executive` | High-level, minimal jargon | Business impact, KPIs, ROI |
| `team` | Balanced, practical | Action items, timelines, deliverables |
| `technical` | Detailed, technical depth | Architecture, implementation, APIs |

## Examples

```bash
# Basic usage - convert PDF to infographic
/visualize ./docs/report.pdf

# Specify theme and size
/visualize ./notes.md --theme modern --size slide

# Output as JPEG with custom filename
/visualize ./spec.txt -o ./output/summary.jpg -f jpg

# Japanese output with custom title
/visualize ./meeting.md --lang ja --title "会議サマリー"

# Technical documentation style
/visualize ./api-docs.md --theme tech --max-points 8

# Detailed multi-section infographic
/visualize ./spec.md --style detailed --sections 4

# Executive summary for leadership
/visualize ./quarterly-report.pdf --audience executive --style summary

# Visual style - diagram with context explanation (NEW)
/visualize ./architecture.md --style visual

# Visual style for process understanding
/visualize ./workflow.md --style visual --theme modern

# Technical documentation with diagrams (detailed)
/visualize ./api-spec.md --audience technical --diagram --style detailed

# Team-friendly document with diagrams
/visualize ./process.md --diagram --theme modern --size slide

# PDF output for formal report
/visualize ./project-plan.md --style detailed --format pdf --audience team
```

## Processing Workflow

When you receive this command, follow these steps:

### Step 1: Read and Analyze Document

1. Use the `Read` tool to read the input file
2. Analyze the document structure and content
3. Identify the main topic/title
4. Determine appropriate diagram types (if `--diagram` is set)

### Step 2: Extract Key Points Based on Audience

Extract information adapted to the target audience:

#### For `executive` audience:
- **Focus**: Business impact, ROI, strategic implications
- **Metrics**: KPIs, percentages, financial figures
- **Language**: Non-technical, decision-focused
- **Structure**: Bottom-line first, then supporting evidence

#### For `team` audience:
- **Focus**: Actionable items, responsibilities, timelines
- **Metrics**: Progress indicators, milestones
- **Language**: Balanced technical/business terms
- **Structure**: Context → Details → Action items

#### For `technical` audience:
- **Focus**: Implementation details, architecture, APIs
- **Metrics**: Performance stats, technical specifications
- **Language**: Technical terminology, code references
- **Structure**: Overview → Technical deep-dive → Integration notes

### Step 3: Generate Mermaid Diagrams (if --diagram)

Analyze content to auto-select appropriate diagram type:

| Content Pattern | Diagram Type | Example |
|-----------------|--------------|---------|
| Process/workflow description | `flowchart` | Step-by-step procedures |
| Time-based data | `gantt` | Project timelines |
| Data structure | `erDiagram` | Database schemas |
| System communication | `sequence` | API interactions |
| Class/component structure | `classDiagram` | Architecture overview |

#### Mermaid Generation Template

```javascript
// Flowchart example
const flowchartTemplate = `
flowchart TD
    A[{START_NODE}] --> B[{STEP_1}]
    B --> C[{STEP_2}]
    C --> D[{END_NODE}]
`;

// Sequence diagram example
const sequenceTemplate = `
sequenceDiagram
    participant A as {ACTOR_1}
    participant B as {ACTOR_2}
    A->>B: {ACTION_1}
    B-->>A: {RESPONSE}
`;

// Gantt chart example
const ganttTemplate = `
gantt
    title {TITLE}
    dateFormat YYYY-MM-DD
    section {SECTION_1}
    {TASK_1} :a1, {START}, {DURATION}
`;
```

### Step 4: Select Icon for Each Point (if --icons)

| Category | Icon | Usage |
|----------|------|-------|
| Success/Complete | ✓ | Achievements, completed items |
| Warning/Caution | ⚠ | Risks, concerns |
| Information | ℹ | General information |
| Important | ⭐ | Key highlights |
| Time | 🕐 | Deadlines, schedules |
| Person | 👤 | Team members, stakeholders |
| Settings | ⚙ | Configuration, setup |
| Data | 📊 | Statistics, metrics |
| Document | 📄 | References, documentation |
| Communication | 💬 | Discussions, feedback |

### Step 5: Generate HTML Based on Style

#### Summary Style (`--style summary`)

Single-page layout with concise overview:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    .infographic {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      background: {BACKGROUND};
      font-family: {FONT_FAMILY};
      padding: 40px;
      display: flex;
      flex-direction: column;
    }

    .header {
      text-align: center;
      margin-bottom: 30px;
    }

    .title {
      font-size: 48px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 10px;
    }

    .subtitle {
      font-size: 24px;
      color: {TEXT};
      opacity: 0.8;
    }

    .content {
      flex: 1;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      align-content: start;
    }

    .point-card {
      background: {SURFACE};
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      border-left: 4px solid {ACCENT};
    }

    .point-icon {
      font-size: 28px;
      margin-bottom: 12px;
    }

    .point-number {
      width: 36px;
      height: 36px;
      background: {PRIMARY};
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      margin-bottom: 12px;
    }

    .point-title {
      font-size: 20px;
      font-weight: 600;
      color: {TEXT};
      margin-bottom: 8px;
    }

    .point-description {
      font-size: 16px;
      color: {TEXT};
      opacity: 0.8;
      line-height: 1.5;
    }

    .metric {
      font-size: 28px;
      font-weight: 700;
      color: {ACCENT};
      margin-top: 12px;
    }

    .footer {
      margin-top: auto;
      padding-top: 20px;
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: {TEXT};
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <div class="infographic">
    <header class="header">
      <h1 class="title">{TITLE}</h1>
      <p class="subtitle">{SUBTITLE}</p>
    </header>

    <main class="content">
      <!-- Repeat for each key point -->
      <div class="point-card">
        <div class="point-icon">{ICON}</div>
        <div class="point-number">{NUMBER}</div>
        <h3 class="point-title">{POINT_TITLE}</h3>
        <p class="point-description">{POINT_DESCRIPTION}</p>
        <div class="metric">{METRIC}</div>
      </div>
    </main>

    <footer class="footer">
      <span>Source: {SOURCE_NAME}</span>
      <span>Generated: {DATE}</span>
    </footer>
  </div>
</body>
</html>
```

#### Visual Style (`--style visual`)

**Understanding-focused layout with diagram + context explanation:**

The visual style focuses on helping readers understand "why" and "how", not just "what exists". It features:
- **Main diagram**: Visualizes structure, flow, or relationships
- **Context explanation**: 2-3 sentences explaining the diagram (not bullet points)
- **Key point cards**: Supplementary highlights

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    .visual-infographic {
      width: {WIDTH}px;
      background: {BACKGROUND};
      font-family: {FONT_FAMILY};
      padding: 30px;
    }

    .header {
      margin-bottom: 25px;
    }

    .title {
      font-size: 28px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 8px;
    }

    .overview {
      font-size: 15px;
      color: {TEXT};
      opacity: 0.8;
      line-height: 1.5;
    }

    .diagram-container {
      background: {SURFACE};
      border-radius: 12px;
      padding: 25px;
      margin-bottom: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .diagram-area {
      background: white;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 250px;
    }

    .context-explanation {
      background: linear-gradient(135deg, {PRIMARY}08, {ACCENT}08);
      border-left: 4px solid {ACCENT};
      border-radius: 0 12px 12px 0;
      padding: 20px;
      margin-bottom: 20px;
    }

    .context-text {
      font-size: 15px;
      color: {TEXT};
      line-height: 1.8;
    }

    .key-points {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
    }

    .point-card {
      background: {SURFACE};
      border-radius: 10px;
      padding: 16px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    .point-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }

    .point-icon {
      font-size: 20px;
    }

    .point-title {
      font-size: 14px;
      font-weight: 600;
      color: {PRIMARY};
    }

    .point-description {
      font-size: 13px;
      color: {TEXT};
      opacity: 0.8;
      line-height: 1.5;
    }

    .footer {
      margin-top: 25px;
      padding-top: 15px;
      border-top: 1px solid rgba(0,0,0,0.1);
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: {TEXT};
      opacity: 0.5;
    }
  </style>
</head>
<body>
  <div class="visual-infographic">
    <header class="header">
      <h1 class="title">{TITLE}</h1>
      <p class="overview">{OVERVIEW_TEXT}</p>
    </header>

    <div class="diagram-container">
      <div class="diagram-area">
        <div class="mermaid">
          {MERMAID_CODE}
        </div>
      </div>
    </div>

    <div class="context-explanation">
      <p class="context-text">{CONTEXT_EXPLANATION}</p>
    </div>

    <div class="key-points">
      <div class="point-card">
        <div class="point-header">
          <span class="point-icon">{ICON_1}</span>
          <span class="point-title">{POINT_TITLE_1}</span>
        </div>
        <p class="point-description">{POINT_DESC_1}</p>
      </div>
      <div class="point-card">
        <div class="point-header">
          <span class="point-icon">{ICON_2}</span>
          <span class="point-title">{POINT_TITLE_2}</span>
        </div>
        <p class="point-description">{POINT_DESC_2}</p>
      </div>
      <div class="point-card">
        <div class="point-header">
          <span class="point-icon">{ICON_3}</span>
          <span class="point-title">{POINT_TITLE_3}</span>
        </div>
        <p class="point-description">{POINT_DESC_3}</p>
      </div>
    </div>

    <footer class="footer">
      <span>Source: {SOURCE_NAME}</span>
      <span>Generated: {DATE}</span>
    </footer>
  </div>

  <script>
    mermaid.initialize({ startOnLoad: true, theme: 'default' });
  </script>
</body>
</html>
```

**Visual Style Generation Logic:**

1. **Extract visualizable structure**: Identify flows, relationships, or hierarchies from the document
2. **Select diagram type**: Choose the most appropriate Mermaid diagram based on content
3. **Generate context explanation**: Create 2-3 sentences explaining "why" and "how" (not bullet points)
4. **Create key point cards**: Extract 3-4 supplementary highlights

**Key differences from summary:**
- summary: Extracts bullet points ("what exists")
- visual: **Identifies structure/flow** → **Generates contextual explanation** ("why & how")

#### Detailed Style (`--style detailed`)

Multi-section layout with comprehensive coverage:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: {FONT_FAMILY};
      background: {BACKGROUND};
      color: {TEXT};
    }

    .page {
      width: {WIDTH}px;
      min-height: {HEIGHT}px;
      padding: 60px;
      background: {SURFACE};
      margin-bottom: 20px;
      page-break-after: always;
    }

    /* Cover Page */
    .cover {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      height: {HEIGHT}px;
    }

    .cover-title {
      font-size: 64px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 20px;
    }

    .cover-subtitle {
      font-size: 28px;
      color: {TEXT};
      opacity: 0.8;
      margin-bottom: 40px;
    }

    .cover-meta {
      font-size: 18px;
      color: {TEXT};
      opacity: 0.6;
    }

    /* Table of Contents */
    .toc {
      padding: 40px;
    }

    .toc-title {
      font-size: 36px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 30px;
      border-bottom: 3px solid {ACCENT};
      padding-bottom: 15px;
    }

    .toc-item {
      display: flex;
      justify-content: space-between;
      padding: 15px 0;
      border-bottom: 1px solid rgba(0,0,0,0.1);
      font-size: 20px;
    }

    .toc-number {
      color: {ACCENT};
      font-weight: 600;
      margin-right: 15px;
    }

    /* Section Pages */
    .section-header {
      margin-bottom: 40px;
    }

    .section-number {
      font-size: 18px;
      color: {ACCENT};
      font-weight: 600;
      margin-bottom: 10px;
    }

    .section-title {
      font-size: 42px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 15px;
    }

    .section-subtitle {
      font-size: 20px;
      color: {TEXT};
      opacity: 0.7;
    }

    .section-content {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 30px;
    }

    .content-card {
      background: {BACKGROUND};
      border-radius: 16px;
      padding: 30px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .card-icon {
      font-size: 32px;
      margin-bottom: 15px;
    }

    .card-title {
      font-size: 22px;
      font-weight: 600;
      color: {TEXT};
      margin-bottom: 12px;
    }

    .card-description {
      font-size: 16px;
      color: {TEXT};
      opacity: 0.8;
      line-height: 1.6;
    }

    /* Diagram Container */
    .diagram-container {
      grid-column: span 2;
      background: white;
      border-radius: 16px;
      padding: 30px;
      text-align: center;
    }

    .mermaid {
      margin: 20px auto;
    }

    /* Conclusion Page */
    .conclusion {
      padding: 40px;
    }

    .conclusion-title {
      font-size: 36px;
      font-weight: 700;
      color: {PRIMARY};
      margin-bottom: 30px;
    }

    .summary-box {
      background: linear-gradient(135deg, {PRIMARY}15, {ACCENT}15);
      border-radius: 16px;
      padding: 30px;
      margin-bottom: 30px;
    }

    .next-steps {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }

    .step-card {
      background: {BACKGROUND};
      border-radius: 12px;
      padding: 25px;
      text-align: center;
    }

    .step-number {
      width: 40px;
      height: 40px;
      background: {PRIMARY};
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      margin: 0 auto 15px;
    }

    /* Footer */
    .page-footer {
      position: absolute;
      bottom: 30px;
      left: 60px;
      right: 60px;
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: {TEXT};
      opacity: 0.5;
    }
  </style>
</head>
<body>
  <!-- Cover Page -->
  <div class="page cover">
    <h1 class="cover-title">{TITLE}</h1>
    <p class="cover-subtitle">{SUBTITLE}</p>
    <p class="cover-meta">{DATE} | {AUTHOR}</p>
  </div>

  <!-- Table of Contents -->
  <div class="page toc">
    <h2 class="toc-title">Table of Contents</h2>
    <!-- Repeat for each section -->
    <div class="toc-item">
      <span><span class="toc-number">1.</span> {SECTION_TITLE}</span>
      <span>{PAGE_NUMBER}</span>
    </div>
  </div>

  <!-- Section Pages -->
  <div class="page">
    <div class="section-header">
      <p class="section-number">Section {N}</p>
      <h2 class="section-title">{SECTION_TITLE}</h2>
      <p class="section-subtitle">{SECTION_DESCRIPTION}</p>
    </div>

    <div class="section-content">
      <!-- Content cards -->
      <div class="content-card">
        <div class="card-icon">{ICON}</div>
        <h3 class="card-title">{CARD_TITLE}</h3>
        <p class="card-description">{CARD_DESCRIPTION}</p>
      </div>

      <!-- Optional: Mermaid diagram -->
      <div class="diagram-container">
        <div class="mermaid">
          {MERMAID_CODE}
        </div>
      </div>
    </div>

    <div class="page-footer">
      <span>{TITLE}</span>
      <span>Page {N}</span>
    </div>
  </div>

  <!-- Conclusion Page -->
  <div class="page conclusion">
    <h2 class="conclusion-title">まとめ / Conclusion</h2>

    <div class="summary-box">
      <p>{SUMMARY_TEXT}</p>
    </div>

    <h3 style="margin-bottom: 20px; color: {PRIMARY};">Next Steps</h3>
    <div class="next-steps">
      <div class="step-card">
        <div class="step-number">1</div>
        <p>{NEXT_STEP_1}</p>
      </div>
      <div class="step-card">
        <div class="step-number">2</div>
        <p>{NEXT_STEP_2}</p>
      </div>
      <div class="step-card">
        <div class="step-number">3</div>
        <p>{NEXT_STEP_3}</p>
      </div>
    </div>

    <div class="page-footer">
      <span>Source: {SOURCE_NAME}</span>
      <span>Generated: {DATE}</span>
    </div>
  </div>

  <script>
    mermaid.initialize({ startOnLoad: true, theme: 'default' });
  </script>
</body>
</html>
```

### Step 6: Theme Configurations

```javascript
const themes = {
  business: {
    primary: '#2563eb',
    secondary: '#1e40af',
    background: '#f8fafc',
    surface: '#ffffff',
    text: '#1e293b',
    accent: '#3b82f6',
    fontFamily: "'Segoe UI', 'Hiragino Sans', sans-serif"
  },
  modern: {
    primary: '#8b5cf6',
    secondary: '#7c3aed',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    surface: 'rgba(255,255,255,0.95)',
    text: '#1e1b4b',
    accent: '#a78bfa',
    fontFamily: "'Poppins', 'Hiragino Sans', sans-serif"
  },
  tech: {
    primary: '#10b981',
    secondary: '#059669',
    background: '#0f172a',
    surface: '#1e293b',
    text: '#f1f5f9',
    accent: '#34d399',
    fontFamily: "'JetBrains Mono', 'Source Han Code JP', monospace"
  },
  minimal: {
    primary: '#374151',
    secondary: '#1f2937',
    background: '#ffffff',
    surface: '#f9fafb',
    text: '#111827',
    accent: '#6b7280',
    fontFamily: "'Inter', 'Hiragino Sans', sans-serif"
  },
  dark: {
    primary: '#f59e0b',
    secondary: '#d97706',
    background: '#18181b',
    surface: '#27272a',
    text: '#fafafa',
    accent: '#fbbf24',
    fontFamily: "'SF Pro Display', 'Hiragino Sans', sans-serif"
  }
};

const sizes = {
  chat: { width: 1200, height: 630 },
  slide: { width: 1920, height: 1080 },
  a4: { width: 2480, height: 3508 },
  square: { width: 1080, height: 1080 }
};
```

### Step 7: Render with Playwright

1. Save the HTML to a temporary file
2. Use Playwright MCP to capture the infographic:

```javascript
// Navigate to HTML
await mcp__playwright__browser_navigate({ url: htmlFilePath });

// Set viewport size
await mcp__playwright__browser_resize({
  width: sizes[sizePreset].width,
  height: sizes[sizePreset].height
});

// Wait for Mermaid rendering (if diagrams included)
await mcp__playwright__browser_wait_for({ time: 2 });

// Take screenshot
await mcp__playwright__browser_take_screenshot({
  filename: outputPath,
  type: format === 'jpg' ? 'jpeg' : 'png',
  fullPage: style === 'detailed'  // Full page for detailed style
});
```

### Step 8: Output and Cleanup

1. Confirm the output file was created
2. Report the output path to the user
3. Clean up any temporary files (HTML)

## Detailed Style Structure

```
┌─────────────────────────────────────┐
│  [Cover Page]                       │
│  Title + Subtitle                   │
│  Date + Author                      │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Table of Contents]                │
│  1. Overview                        │
│  2. Background                      │
│  3. Details                         │
│  4. Conclusion                      │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Section 1: Overview]              │
│  • Key points                       │
│  • Highlights                       │
│  📊 [Optional Diagram]              │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Section 2-N: Detail Sections]     │
│  • Topic details                    │
│  • Charts/Icons                     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│  [Conclusion]                       │
│  • Summary                          │
│  • Next Steps                       │
└─────────────────────────────────────┘
```

## Error Handling

### Unsupported File Format
```
Supported formats: .md, .txt, .pdf
Provided: {extension}
```

### File Not Found
```
File not found: {path}
Please check the file path and try again.
```

### Playwright Error
```
Failed to capture screenshot.
Ensure Playwright MCP is properly configured.
```

### Mermaid Rendering Error
```
Warning: Mermaid diagram failed to render.
Generating infographic without diagram.
```

## Output Format

When complete, report to the user:

```
Infographic generated successfully!

Output: {output_path}
Size: {width}x{height}px
Format: {format}
Theme: {theme}
Style: {style}
Audience: {audience}

Key points extracted: {count}
Diagrams included: {yes/no}
Sections: {count} (detailed only)
```

## Limitations

- Maximum recommended document size: ~10,000 words (longer documents will be summarized)
- Complex tables and charts are simplified to text descriptions
- Fonts depend on system availability
- PDF parsing may not preserve all formatting
- Mermaid diagrams require internet connection for CDN
- Detailed style works best with `slide` or `a4` size presets
