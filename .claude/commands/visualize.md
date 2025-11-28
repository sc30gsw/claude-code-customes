---
allowed-tools: Read, Write, Bash, TodoWrite, mcp__playwright__browser_navigate, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_wait_for, mcp__playwright__browser_resize, mcp__playwright__browser_close, Glob
description: Convert documents to infographic images (PNG/JPG/PDF) for easy sharing
---

# /visualize - Document to Infographic Converter

## Overview

Transform documents into visually appealing infographic images that can be shared on chat applications like Slack, Teams, or Discord.

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
```

## Processing Workflow

When you receive this command, follow these steps:

### Step 1: Read and Analyze Document

1. Use the `Read` tool to read the input file
2. Analyze the document structure and content
3. Identify the main topic/title

### Step 2: Extract Key Points

Extract the following information:
- **Title**: Main topic or document title
- **Subtitle**: Secondary description (if applicable)
- **Key Points**: Up to `--max-points` main takeaways
  - Each point should have a short heading (5-10 words)
  - Each point should have a brief description (1-2 sentences)
- **Metrics/Numbers**: Any important statistics or data points
- **Source**: Original document name

### Step 3: Generate HTML Infographic

Create an HTML document using the theme configuration below. The HTML should be self-contained with inline CSS.

#### Theme Configurations

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

#### HTML Template Structure

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
        <div class="point-number">{NUMBER}</div>
        <h3 class="point-title">{POINT_TITLE}</h3>
        <p class="point-description">{POINT_DESCRIPTION}</p>
        <!-- Optional metric -->
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

### Step 4: Render with Playwright

1. Save the HTML to a temporary file or use data URI
2. Use Playwright MCP to capture the infographic:

```javascript
// Navigate to HTML
await mcp__playwright__browser_navigate({ url: htmlDataUri });

// Set viewport size
await mcp__playwright__browser_resize({
  width: sizes[sizePreset].width,
  height: sizes[sizePreset].height
});

// Wait for rendering
await mcp__playwright__browser_wait_for({ time: 1 });

// Take screenshot
await mcp__playwright__browser_take_screenshot({
  filename: outputPath,
  type: format === 'jpg' ? 'jpeg' : 'png'
});
```

### Step 5: Output and Cleanup

1. Confirm the output file was created
2. Report the output path to the user
3. Clean up any temporary files

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

## Output Format

When complete, report to the user:

```
Infographic generated successfully!

Output: {output_path}
Size: {width}x{height}px
Format: {format}
Theme: {theme}

Key points extracted: {count}
```

## Limitations

- Maximum recommended document size: ~10,000 words (longer documents will be summarized)
- Complex tables and charts are simplified to text descriptions
- Fonts depend on system availability
- PDF parsing may not preserve all formatting
