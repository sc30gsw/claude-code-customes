---
name: convert-to-md
description: Convert various file formats to Markdown using markitdown MCP, optimized for AI readability
---

# Convert to Markdown

Convert various file formats to Markdown using markitdown MCP, optimized for AI readability.

## Arguments
- `files`: Input files or directories to convert (required)

## Options
- `--recursive`, `-r`: Process subdirectories recursively
- `--filter <types>`: Filter by file types (e.g., pdf,docx,xlsx)
- `--combine`, `-c`: Combine multiple files into one markdown file
- `--toc`: Generate table of contents
- `--metadata`, `-m`: Include file metadata in output
- `--ai-optimize`: Optimize output for AI reading
- `--output`, `-o <path>`: Specify output directory or file
- `--verbose`, `-v`: Show detailed progress

## Examples

```bash
# Convert single file
/convert-to-md document.pdf

# Convert multiple files with AI optimization
/convert-to-md --ai-optimize file1.docx file2.xlsx

# Recursively convert directory with filtering
/convert-to-md --recursive --filter pdf,docx ./documents

# Combine files into one markdown with TOC
/convert-to-md --combine --toc *.pdf -o combined.md
```

## Workflow

1. Parse arguments and validate input files
2. Get file list based on patterns and filters
3. For each file:
   - Call `mcp__markitdown__convert_to_markdown` with file URI
   - Apply AI optimization if enabled
   - Save to output location
4. If `--combine`, merge all outputs with optional TOC
5. Report summary (successful/failed counts)

## AI Optimization Features

When `--ai-optimize` is enabled:
- Add file context headers (filename, original format)
- Add structure hints (headers, code blocks, tables)
- Clean up excessive whitespace
- Add reading notes for long documents
