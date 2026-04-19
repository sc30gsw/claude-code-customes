---
name: visualize
description: Convert documents to infographic images (PNG/JPG/PDF) for easy sharing
---

# Visualize: Document to Infographic Converter

Transform documents into visually appealing infographic images for sharing on chat applications like Slack, Teams, or Discord.

## Usage

```bash
/visualize <input-file> [options]
```

## Arguments
- `input-file`: Path to the document (required)
- Supported formats: `.md`, `.txt`, `.pdf`

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output file path | `{input}-infographic.png` |
| `--format` | `-f` | Output format (png/jpg/pdf) | `png` |
| `--theme` | `-t` | Visual theme | `business` |
| `--size` | `-s` | Image size preset | `chat` |
| `--max-points` | `-m` | Maximum key points | `6` |
| `--lang` | `-l` | Output language (ja/en) | `ja` |
| `--style` | | Output style (summary/visual/detailed) | `summary` |
| `--audience` | `-a` | Target audience | `team` |
| `--diagram` | `-d` | Include Mermaid diagrams | `false` |
| `--visual-type` | `-vt` | Visual format (diagram/cards/comic/auto) | `auto` |
| `--panels` | `-p` | Panel count for comic (2-6) | `3` |

## Themes

| Theme | Description | Best For |
|-------|-------------|----------|
| `business` | Professional blue tones | Work presentations |
| `modern` | Vibrant gradients | Marketing materials |
| `tech` | Dark accents, monospace | Technical documentation |
| `minimal` | White space, simple | Clean summaries |
| `dark` | Dark background | Screen-friendly |

## Size Presets

| Preset | Dimensions | Best For |
|--------|------------|----------|
| `chat` | 1200x630px | Slack, Teams, Discord |
| `slide` | 1920x1080px | Presentations |
| `a4` | 2480x3508px | Print (A4 portrait) |
| `square` | 1080x1080px | Social media |

## Output Styles

| Style | Description | Understanding Level |
|-------|-------------|---------------------|
| `summary` | Single page, concise | Surface (what exists) |
| `visual` | Diagram + context | **Deep (why & how)** |
| `detailed` | Multi-section with TOC | Comprehensive |

## Visual Types (visual style only)

| Type | Best For |
|------|----------|
| `diagram` | Flows, processes, API, data structures |
| `cards` | Feature lists, comparisons |
| `comic` | User journeys, tutorials, before/after |
| `auto` | Auto-select based on content |

## Examples

```bash
# Basic usage
/visualize ./docs/report.pdf

# Theme and size
/visualize ./notes.md --theme modern --size slide

# Visual style with diagram
/visualize ./architecture.md --style visual --visual-type diagram

# Comic format (4 panels)
/visualize ./tutorial.md --style visual --visual-type comic --panels 4

# Executive summary
/visualize ./quarterly-report.pdf --audience executive --style summary

# Technical with diagrams
/visualize ./api-spec.md --audience technical --diagram --style detailed
```

## Processing Workflow

1. **Read and Analyze**: Parse document structure
2. **Extract Key Points**: Based on target audience
3. **Generate Diagrams**: If `--diagram` enabled (Mermaid)
4. **Select Icons**: Lucide SVG icons for categories
5. **Generate HTML**: Based on style template
6. **Render with Playwright**: Capture as image
7. **Output and Report**: Save file and report results

## Audience Adaptation

### Executive
- Business impact, ROI, strategic implications
- Non-technical language, decision-focused

### Team
- Actionable items, responsibilities, timelines
- Balanced technical/business terms

### Technical
- Implementation details, architecture, APIs
- Technical terminology, code references
