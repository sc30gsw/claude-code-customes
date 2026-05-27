#!/usr/bin/env python3
"""
Document Improver
Generates and applies improvement suggestions to Markdown documents.
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from doc_analyzer import DocumentAnalyzer, Issue


@dataclass
class Improvement:
    """Represents a document improvement"""
    id: int
    type: str
    priority: str  # critical, high, medium, low
    impact: str  # high, medium, low
    effort: str  # high, medium, low
    section: str
    line_start: int
    line_end: int
    current_text: str
    improved_text: str
    rationale: str
    auto_applicable: bool = True


class DocumentImprover:
    """Improves document quality through automated suggestions"""

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = ""
        self.lines = []
        self.improvements: List[Improvement] = []
        self.improvement_id = 1

    def load_document(self):
        """Load the document into memory"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')

    def analyze_and_suggest(self) -> List[Improvement]:
        """Analyze document and generate improvement suggestions"""
        self.load_document()

        # Run analyzer first to identify issues
        analyzer = DocumentAnalyzer(str(self.file_path), detailed=True)
        analysis_report = analyzer.analyze()

        # Generate improvements based on issues
        self._suggest_structure_improvements(analyzer)
        self._suggest_content_enhancements()
        self._suggest_readability_improvements()
        self._suggest_consistency_improvements()

        return self.improvements

    def _suggest_structure_improvements(self, analyzer: DocumentAnalyzer):
        """Suggest structural improvements"""

        # Add TOC if missing and document is long
        if len(self.lines) > 100 and not analyzer._has_toc():
            toc_content = self._generate_toc()
            self.improvements.append(Improvement(
                id=self.improvement_id,
                type="add_toc",
                priority="high",
                impact="medium",
                effort="low",
                section="Table of Contents",
                line_start=0,
                line_end=0,
                current_text="[No TOC]",
                improved_text=toc_content,
                rationale="Long documents benefit from a Table of Contents for navigation",
                auto_applicable=True
            ))
            self.improvement_id += 1

        # Add metadata if missing
        if not analyzer._has_metadata():
            metadata = self._generate_metadata()
            self.improvements.append(Improvement(
                id=self.improvement_id,
                type="add_metadata",
                priority="medium",
                impact="low",
                effort="low",
                section="Document Metadata",
                line_start=0,
                line_end=0,
                current_text="[No metadata]",
                improved_text=metadata,
                rationale="Metadata helps track document version, author, and purpose",
                auto_applicable=True
            ))
            self.improvement_id += 1

        # Fix heading hierarchy issues
        headings = analyzer._extract_headings()
        for i, (level, text, line_num) in enumerate(headings):
            if i > 0:
                prev_level = headings[i-1][0]
                if level > prev_level + 1:
                    suggested_level = prev_level + 1
                    current = '#' * level + ' ' + text
                    improved = '#' * suggested_level + ' ' + text

                    self.improvements.append(Improvement(
                        id=self.improvement_id,
                        type="fix_heading_hierarchy",
                        priority="medium",
                        impact="medium",
                        effort="low",
                        section=text,
                        line_start=line_num - 1,
                        line_end=line_num - 1,
                        current_text=current,
                        improved_text=improved,
                        rationale=f"Heading levels should be sequential (h{prev_level} → h{suggested_level}, not h{level})",
                        auto_applicable=True
                    ))
                    self.improvement_id += 1

    def _suggest_content_enhancements(self):
        """Suggest content improvements"""

        # Find sections that are too short
        headings = self._extract_all_headings()

        for i, (level, text, line_num) in enumerate(headings):
            # Calculate section length
            start_line = line_num
            end_line = headings[i + 1][2] if i + 1 < len(headings) else len(self.lines)

            section_content = '\n'.join(self.lines[start_line:end_line])
            word_count = len(section_content.split())

            # If section is very short (< 20 words), suggest expansion
            if word_count < 20 and word_count > 0:
                self.improvements.append(Improvement(
                    id=self.improvement_id,
                    type="expand_section",
                    priority="medium",
                    impact="high",
                    effort="medium",
                    section=text,
                    line_start=start_line,
                    line_end=end_line,
                    current_text=f"[{word_count} words]",
                    improved_text=f"[Expand to at least 50 words with examples]",
                    rationale="Sections should provide sufficient detail and examples",
                    auto_applicable=False  # Requires manual content creation
                ))
                self.improvement_id += 1

        # Suggest adding code examples for technical sections
        tech_keywords = ['api', 'function', 'method', 'class', 'implementation', 'usage']
        code_blocks = re.findall(r'```[\s\S]*?```', self.content)

        if any(kw in self.content.lower() for kw in tech_keywords) and len(code_blocks) < 2:
            self.improvements.append(Improvement(
                id=self.improvement_id,
                type="add_code_examples",
                priority="high",
                impact="high",
                effort="medium",
                section="Code Examples",
                line_start=0,
                line_end=0,
                current_text="[No code examples]",
                improved_text="[Add 2-3 code examples with explanations]",
                rationale="Technical documentation should include code examples",
                auto_applicable=False
            ))
            self.improvement_id += 1

    def _suggest_readability_improvements(self):
        """Suggest readability improvements"""

        # Find long sentences
        for i, line in enumerate(self.lines):
            # Skip headings, code blocks, lists
            if re.match(r'^#+ |```|^\s*[-*+]\s', line):
                continue

            sentences = re.split(r'[.!?]+', line)
            for sentence in sentences:
                words = sentence.split()
                if len(words) > 30:
                    self.improvements.append(Improvement(
                        id=self.improvement_id,
                        type="split_long_sentence",
                        priority="low",
                        impact="medium",
                        effort="low",
                        section=f"Line {i+1}",
                        line_start=i,
                        line_end=i,
                        current_text=sentence[:100] + "...",
                        improved_text="[Split into 2-3 shorter sentences]",
                        rationale=f"Sentence is too long ({len(words)} words). Aim for under 25 words.",
                        auto_applicable=False
                    ))
                    self.improvement_id += 1

        # Find long paragraphs
        paragraphs = self.content.split('\n\n')
        current_line = 0

        for para in paragraphs:
            para_lines = para.count('\n') + 1
            words = len(para.split())

            if words > 150:
                self.improvements.append(Improvement(
                    id=self.improvement_id,
                    type="break_long_paragraph",
                    priority="low",
                    impact="medium",
                    effort="low",
                    section=f"Paragraph at line {current_line+1}",
                    line_start=current_line,
                    line_end=current_line + para_lines,
                    current_text=para[:100] + "...",
                    improved_text="[Break into 2-3 smaller paragraphs]",
                    rationale=f"Paragraph is too long ({words} words). Break into smaller chunks.",
                    auto_applicable=False
                ))
                self.improvement_id += 1

            current_line += para_lines + 1

    def _suggest_consistency_improvements(self):
        """Suggest consistency improvements"""

        # Check for consistent code fence language tags
        code_blocks = re.finditer(r'```(\w*)\n', self.content)
        untagged_blocks = []

        for match in code_blocks:
            if not match.group(1):  # No language tag
                line_num = self.content[:match.start()].count('\n')
                untagged_blocks.append(line_num)

        if untagged_blocks:
            self.improvements.append(Improvement(
                id=self.improvement_id,
                type="add_code_fence_tags",
                priority="low",
                impact="low",
                effort="low",
                section="Code Blocks",
                line_start=untagged_blocks[0],
                line_end=untagged_blocks[-1],
                current_text="```",
                improved_text="```python  # or appropriate language",
                rationale="Code blocks should have language tags for proper syntax highlighting",
                auto_applicable=False
            ))
            self.improvement_id += 1

        # Check for TODO/TBD placeholders
        placeholders = re.finditer(r'\b(TODO|TBD|FIXME|XXX)\b', self.content)
        for match in placeholders:
            line_num = self.content[:match.start()].count('\n')
            self.improvements.append(Improvement(
                id=self.improvement_id,
                type="remove_placeholder",
                priority="high",
                impact="high",
                effort="medium",
                section=f"Line {line_num+1}",
                line_start=line_num,
                line_end=line_num,
                current_text=self.lines[line_num],
                improved_text="[Replace with actual content]",
                rationale="Remove placeholder text and add real content",
                auto_applicable=False
            ))
            self.improvement_id += 1

    def _extract_all_headings(self) -> List:
        """Extract all headings"""
        headings = []
        for i, line in enumerate(self.lines):
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append((level, text, i))
        return headings

    def _generate_toc(self) -> str:
        """Generate Table of Contents"""
        headings = self._extract_all_headings()
        toc = "## Table of Contents\n\n"

        for level, text, _ in headings:
            if level == 1:  # Skip h1 (usually document title)
                continue
            indent = "  " * (level - 2)
            anchor = text.lower().replace(' ', '-').replace('[^a-z0-9-]', '')
            toc += f"{indent}- [{text}](#{anchor})\n"

        return toc + "\n"

    def _generate_metadata(self) -> str:
        """Generate document metadata"""
        from datetime import datetime

        metadata = f"""---
title: {self.file_path.stem.replace('-', ' ').title()}
date: {datetime.now().strftime('%Y-%m-%d')}
version: 1.0.0
status: Draft
---

"""
        return metadata

    def apply_improvements(self, improvement_ids: List[int]) -> str:
        """Apply selected improvements and return modified content"""
        modified_lines = self.lines.copy()

        # Sort improvements by line number (reverse to avoid line number shifts)
        improvements_to_apply = [
            imp for imp in self.improvements
            if imp.id in improvement_ids and imp.auto_applicable
        ]
        improvements_to_apply.sort(key=lambda x: x.line_start, reverse=True)

        for improvement in improvements_to_apply:
            if improvement.type == "add_toc":
                # Insert TOC after first heading
                insert_pos = 1 if modified_lines else 0
                toc_lines = improvement.improved_text.split('\n')
                modified_lines[insert_pos:insert_pos] = toc_lines

            elif improvement.type == "add_metadata":
                # Insert metadata at the beginning
                metadata_lines = improvement.improved_text.split('\n')
                modified_lines[0:0] = metadata_lines

            elif improvement.type == "fix_heading_hierarchy":
                # Replace heading line
                modified_lines[improvement.line_start] = improvement.improved_text

        return '\n'.join(modified_lines)

    def save_improved_document(self, output_path: Optional[str] = None):
        """Save improved document"""
        if output_path is None:
            output_path = str(self.file_path.with_suffix('.improved.md'))

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.apply_improvements([imp.id for imp in self.improvements if imp.auto_applicable]))

        return output_path


def main():
    parser = argparse.ArgumentParser(description='Improve Markdown document quality')
    parser.add_argument('--file', required=True, help='Path to Markdown file')
    parser.add_argument('--analyze', action='store_true', help='Analyze and show suggestions only')
    parser.add_argument('--apply-all', action='store_true', help='Apply all auto-applicable improvements')
    parser.add_argument('--apply-ids', help='Apply specific improvements by ID (comma-separated)')
    parser.add_argument('--priority', choices=['critical', 'high', 'medium', 'low'],
                       help='Filter by priority level')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--format', choices=['json', 'text'], default='text', help='Output format')

    args = parser.parse_args()

    improver = DocumentImprover(args.file)
    improvements = improver.analyze_and_suggest()

    # Filter by priority if specified
    if args.priority:
        improvements = [imp for imp in improvements if imp.priority == args.priority]

    if args.analyze:
        # Show improvements
        if args.format == 'json':
            output = json.dumps([asdict(imp) for imp in improvements], indent=2)
        else:
            output = f"\nDocument Improvement Suggestions\n{'='*50}\n\n"
            for imp in improvements:
                output += f"[{imp.id}] {imp.type.upper()} - Priority: {imp.priority}\n"
                output += f"    Section: {imp.section}\n"
                output += f"    Impact: {imp.impact} | Effort: {imp.effort}\n"
                output += f"    Rationale: {imp.rationale}\n"
                output += f"    Auto-applicable: {imp.auto_applicable}\n\n"

        print(output)

    elif args.apply_all:
        # Apply all auto-applicable improvements
        auto_improvements = [imp.id for imp in improvements if imp.auto_applicable]
        content = improver.apply_improvements(auto_improvements)

        output_file = args.output or str(Path(args.file).with_suffix('.improved.md'))
        with open(output_file, 'w') as f:
            f.write(content)

        print(f"Applied {len(auto_improvements)} improvements to {output_file}")

    elif args.apply_ids:
        # Apply specific improvements
        ids = [int(x.strip()) for x in args.apply_ids.split(',')]
        content = improver.apply_improvements(ids)

        output_file = args.output or str(Path(args.file).with_suffix('.improved.md'))
        with open(output_file, 'w') as f:
            f.write(content)

        print(f"Applied {len(ids)} improvements to {output_file}")

    else:
        print("Use --analyze to see suggestions, --apply-all or --apply-ids to apply improvements")


if __name__ == '__main__':
    main()
