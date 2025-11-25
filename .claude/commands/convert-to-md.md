---
allowed-tools: Read, Write, Bash, Glob, Grep, mcp__markitdown__convert_to_markdown, TodoWrite, Edit, WebFetch, mcp__serena__list_dir
description: Convert various file formats to Markdown using markitdown MCP, optimized for AI readability
---

# Convert to Markdown Command

## Description
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
/convert-to-markdown document.pdf

# Convert multiple files with AI optimization
/convert-to-markdown --ai-optimize file1.docx file2.xlsx

# Recursively convert directory with filtering
/convert-to-markdown --recursive --filter pdf,docx ./documents

# Combine files into one markdown with TOC
/convert-to-markdown --combine --toc *.pdf -o combined.md
```

## Implementation

```javascript
const fs = require('fs').promises;
const path = require('path');
const { glob } = require('glob');

async function main(args, { mcp }) {
    const options = parseArgs(args);
    
    try {
        const files = await getFileList(options);
        
        if (options.verbose) {
            console.log(`Found ${files.length} files to process`);
        }
        
        if (options.combine) {
            await processCombined(files, options, mcp);
        } else {
            await processIndividual(files, options, mcp);
        }
        
        console.log('✅ Conversion completed successfully!');
        
    } catch (error) {
        console.error('❌ Error during conversion:', error.message);
        process.exit(1);
    }
}

function parseArgs(args) {
    const options = {
        files: [],
        recursive: false,
        filter: null,
        combine: false,
        toc: false,
        metadata: false,
        aiOptimize: false,
        output: null,
        verbose: false
    };
    
    for (let i = 0; i < args.length; i++) {
        const arg = args[i];
        
        if (arg === '--recursive' || arg === '-r') {
            options.recursive = true;
        } else if (arg === '--filter') {
            options.filter = args[++i]?.split(',') || [];
        } else if (arg === '--combine' || arg === '-c') {
            options.combine = true;
        } else if (arg === '--toc') {
            options.toc = true;
        } else if (arg === '--metadata' || arg === '-m') {
            options.metadata = true;
        } else if (arg === '--ai-optimize') {
            options.aiOptimize = true;
        } else if (arg === '--output' || arg === '-o') {
            options.output = args[++i];
        } else if (arg === '--verbose' || arg === '-v') {
            options.verbose = true;
        } else if (!arg.startsWith('-')) {
            options.files.push(arg);
        }
    }
    
    if (options.files.length === 0) {
        throw new Error('No input files specified');
    }
    
    return options;
}

async function getFileList(options) {
    const allFiles = [];
    
    for (const input of options.files) {
        try {
            const stat = await fs.stat(input);
            
            if (stat.isDirectory()) {
                const pattern = options.recursive ? `${input}/**/*` : `${input}/*`;
                const files = await glob(pattern, { nodir: true });
                allFiles.push(...files);
            } else {
                // Handle glob patterns
                const files = await glob(input, { nodir: true });
                allFiles.push(...files);
            }
        } catch (error) {
            if (options.verbose) {
                console.warn(`⚠️ Could not access: ${input}`);
            }
        }
    }
    
    // Filter by file types if specified
    if (options.filter && options.filter.length > 0) {
        return allFiles.filter(file => {
            const ext = path.extname(file).toLowerCase().slice(1);
            return options.filter.includes(ext);
        });
    }
    
    return [...new Set(allFiles)]; // Remove duplicates
}

async function processIndividual(files, options, mcp) {
    const results = [];
    
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        
        if (options.verbose) {
            console.log(`📄 Processing (${i + 1}/${files.length}): ${file}`);
        }
        
        try {
            const result = await convertFile(file, options, mcp);
            results.push({ file, success: true, result });
            
            const outputPath = getOutputPath(file, options);
            await saveMarkdown(result.content, outputPath, options);
            
            if (options.verbose) {
                console.log(`✅ Saved: ${outputPath}`);
            }
            
        } catch (error) {
            results.push({ file, success: false, error: error.message });
            console.error(`❌ Failed to process ${file}: ${error.message}`);
        }
    }
    
    // Show summary
    const successful = results.filter(r => r.success).length;
    const failed = results.length - successful;
    
    console.log(`\n📊 Summary: ${successful} successful, ${failed} failed`);
    
    if (failed > 0) {
        console.log('\n❌ Failed files:');
        results.filter(r => !r.success).forEach(r => {
            console.log(`  - ${r.file}: ${r.error}`);
        });
    }
}

async function processCombined(files, options, mcp) {
    let combinedContent = '';
    const toc = [];
    
    if (options.toc) {
        combinedContent += '# Table of Contents\n\n';
    }
    
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        
        if (options.verbose) {
            console.log(`📄 Processing (${i + 1}/${files.length}): ${file}`);
        }
        
        try {
            const result = await convertFile(file, options, mcp);
            const fileName = path.basename(file);
            const anchor = fileName.toLowerCase().replace(/[^a-z0-9]/g, '-');
            
            if (options.toc) {
                toc.push(`- [${fileName}](#${anchor})`);
            }
            
            combinedContent += `\n\n---\n\n# ${fileName} {#${anchor}}\n\n`;
            
            if (options.metadata) {
                const stats = await fs.stat(file);
                combinedContent += `**File:** ${file}\n`;
                combinedContent += `**Size:** ${formatBytes(stats.size)}\n`;
                combinedContent += `**Modified:** ${stats.mtime.toISOString()}\n\n`;
            }
            
            combinedContent += result.content;
            
        } catch (error) {
            console.error(`❌ Failed to process ${file}: ${error.message}`);
            combinedContent += `\n\n**Error processing ${file}:** ${error.message}\n\n`;
        }
    }
    
    if (options.toc && toc.length > 0) {
        const tocContent = toc.join('\n') + '\n\n---';
        combinedContent = combinedContent.replace('# Table of Contents\n\n', `# Table of Contents\n\n${tocContent}\n\n`);
    }
    
    const outputPath = options.output || 'combined.md';
    await saveMarkdown(combinedContent, outputPath, options);
    
    console.log(`✅ Combined file saved: ${outputPath}`);
}

async function convertFile(filePath, options, mcp) {
    const fileUri = `file://${path.resolve(filePath)}`;
    
    try {
        const result = await mcp.call('mcp__markitdown__convert_to_markdown', {
            uri: fileUri
        });
        
        let content = result.content || result;
        
        if (options.aiOptimize) {
            content = optimizeForAI(content, filePath);
        }
        
        return { content, originalPath: filePath };
        
    } catch (error) {
        throw new Error(`MCP conversion failed: ${error.message}`);
    }
}

function optimizeForAI(content, filePath) {
    // Add file context header
    const fileName = path.basename(filePath);
    const ext = path.extname(filePath).toLowerCase();
    
    let optimized = `<!-- File: ${fileName} -->\n`;
    optimized += `<!-- Original Format: ${ext} -->\n`;
    optimized += `<!-- Converted for AI Reading -->\n\n`;
    
    // Clean up common markdown issues
    content = content
        .replace(/\n{3,}/g, '\n\n') // Reduce excessive line breaks
        .replace(/\t/g, '    ') // Convert tabs to spaces
        .trim();
    
    // Add structure hints for AI
    if (content.includes('##') || content.includes('#')) {
        optimized += '<!-- Document Structure: Hierarchical with headers -->\n\n';
    }
    
    if (content.includes('```') || content.includes('`')) {
        optimized += '<!-- Contains Code Blocks -->\n\n';
    }
    
    if (content.includes('|') && content.includes('---')) {
        optimized += '<!-- Contains Tables -->\n\n';
    }
    
    optimized += content;
    
    // Add summary section for long documents
    if (content.length > 5000) {
        const wordCount = content.split(/\s+/).length;
        optimized += `\n\n---\n\n<!-- AI Reading Notes -->\n`;
        optimized += `<!-- Word Count: ~${wordCount} words -->\n`;
        optimized += `<!-- Document Length: Long - Consider section-by-section analysis -->\n`;
    }
    
    return optimized;
}

function getOutputPath(inputPath, options) {
    if (options.output) {
        return options.output;
    }
    
    const dir = path.dirname(inputPath);
    const name = path.basename(inputPath, path.extname(inputPath));
    return path.join(dir, `${name}.md`);
}

async function saveMarkdown(content, outputPath, options) {
    // Ensure output directory exists
    const dir = path.dirname(outputPath);
    await fs.mkdir(dir, { recursive: true });
    
    await fs.writeFile(outputPath, content, 'utf8');
}

function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

module.exports = { main };
```