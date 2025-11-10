#!/usr/bin/env python3
"""
Document Quality Analyzer
Analyzes Markdown documents and generates quality scores and improvement suggestions.
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
import requests


@dataclass
class QualityMetrics:
    """Quality metrics for a document"""
    structure_score: float = 0.0
    content_score: float = 0.0
    readability_score: float = 0.0
    link_health_score: float = 0.0
    overall_score: float = 0.0


@dataclass
class Issue:
    """Represents a quality issue in a document"""
    type: str
    severity: str  # critical, high, medium, low
    line: int = 0
    section: str = ""
    message: str = ""
    suggestion: str = ""


class DocumentAnalyzer:
    """Analyzes Markdown document quality"""

    def __init__(self, file_path: str, detailed: bool = False):
        self.file_path = Path(file_path)
        self.detailed = detailed
        self.content = ""
        self.lines = []
        self.issues: List[Issue] = []
        self.metrics = QualityMetrics()

    def load_document(self):
        """Load the document into memory"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')

    def analyze(self) -> Dict[str, Any]:
        """Run complete analysis"""
        self.load_document()

        # Run all analysis components
        self._analyze_structure()
        self._analyze_content()
        self._analyze_readability()
        self._analyze_links()

        # Calculate overall score
        self.metrics.overall_score = self._calculate_overall_score()

        return self._generate_report()

    def _analyze_structure(self):
        """Analyze document structure"""
        score = 100.0

        # Check for heading hierarchy
        headings = self._extract_headings()
        if not headings:
            self.issues.append(Issue(
                type="missing_headings",
                severity="critical",
                message="Document has no headings",
                suggestion="Add section headings to structure your document"
            ))
            score -= 30

        # Check heading levels are sequential
        for i, (level, text, line_num) in enumerate(headings):
            if i > 0:
                prev_level = headings[i-1][0]
                if level > prev_level + 1:
                    self.issues.append(Issue(
                        type="heading_hierarchy",
                        severity="medium",
                        line=line_num,
                        section=text,
                        message=f"Heading level skipped (from h{prev_level} to h{level})",
                        suggestion=f"Use h{prev_level+1} instead of h{level}"
                    ))
                    score -= 5

        # Check for Table of Contents (if document is long)
        if len(self.lines) > 100:
            if not self._has_toc():
                self.issues.append(Issue(
                    type="missing_toc",
                    severity="medium",
                    message="Long document without Table of Contents",
                    suggestion="Add a Table of Contents after the introduction"
                ))
                score -= 10

        # Check for document metadata (front matter)
        if not self._has_metadata():
            self.issues.append(Issue(
                type="missing_metadata",
                severity="low",
                message="No document metadata found",
                suggestion="Add metadata (title, date, author) at the top"
            ))
            score -= 5

        self.metrics.structure_score = max(0, score)

    def _analyze_content(self):
        """Analyze document content quality"""
        score = 100.0

        # Check for minimum content
        word_count = len(self.content.split())
        if word_count < 100:
            self.issues.append(Issue(
                type="insufficient_content",
                severity="high",
                message=f"Document is too short ({word_count} words)",
                suggestion="Expand document to at least 100 words"
            ))
            score -= 20

        # Check for code examples (if technical doc)
        code_blocks = re.findall(r'```[\s\S]*?```', self.content)
        headings = self._extract_headings()

        # Technical docs should have code examples
        tech_keywords = ['api', 'function', 'class', 'method', 'implementation', 'example']
        is_technical = any(kw in self.content.lower() for kw in tech_keywords)

        if is_technical and len(code_blocks) == 0:
            self.issues.append(Issue(
                type="missing_code_examples",
                severity="medium",
                message="Technical document without code examples",
                suggestion="Add code snippets to illustrate concepts"
            ))
            score -= 15

        # Check for placeholder text
        placeholders = re.findall(r'\b(TODO|TBD|FIXME|XXX|\[.*?\])\b', self.content)
        if placeholders:
            self.issues.append(Issue(
                type="placeholder_text",
                severity="high",
                message=f"Found {len(placeholders)} placeholder(s)",
                suggestion="Replace placeholder text with actual content"
            ))
            score -= 10

        # Check for lists and examples
        lists = re.findall(r'^[\*\-\+]\s', self.content, re.MULTILINE)
        if len(lists) < 3 and len(headings) > 3:
            self.issues.append(Issue(
                type="lack_of_examples",
                severity="low",
                message="Few lists or examples for documentation size",
                suggestion="Add bullet lists or numbered examples"
            ))
            score -= 5

        self.metrics.content_score = max(0, score)

    def _analyze_readability(self):
        """Analyze document readability"""
        score = 100.0

        # Check average sentence length
        sentences = re.split(r'[.!?]+', self.content)
        sentences = [s.strip() for s in sentences if s.strip()]

        if sentences:
            avg_words_per_sentence = sum(len(s.split()) for s in sentences) / len(sentences)

            if avg_words_per_sentence > 25:
                self.issues.append(Issue(
                    type="sentence_length",
                    severity="medium",
                    message=f"Average sentence too long ({avg_words_per_sentence:.1f} words)",
                    suggestion="Break long sentences into shorter ones"
                ))
                score -= 10

        # Check paragraph length
        paragraphs = [p for p in self.content.split('\n\n') if p.strip() and not p.startswith('#')]
        long_paragraphs = [p for p in paragraphs if len(p.split()) > 150]

        if long_paragraphs:
            self.issues.append(Issue(
                type="long_paragraphs",
                severity="low",
                message=f"Found {len(long_paragraphs)} very long paragraph(s)",
                suggestion="Break long paragraphs into smaller chunks"
            ))
            score -= 5

        # Check for technical term density
        total_words = len(self.content.split())
        tech_terms = re.findall(r'\b[A-Z]{2,}\b', self.content)  # Acronyms

        if total_words > 0:
            tech_density = len(tech_terms) / total_words
            if tech_density > 0.15:
                self.issues.append(Issue(
                    type="high_technical_density",
                    severity="low",
                    message="High density of technical terms/acronyms",
                    suggestion="Define acronyms and technical terms on first use"
                ))
                score -= 5

        self.metrics.readability_score = max(0, score)

    def _analyze_links(self):
        """Analyze link health"""
        score = 100.0

        # Extract all links
        md_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', self.content)

        if not md_links:
            # No penalty for no links, but note it
            self.metrics.link_health_score = 100.0
            return

        broken_links = 0

        for link_text, url in md_links:
            # Check internal links (anchors)
            if url.startswith('#'):
                anchor = url[1:].lower().replace(' ', '-')
                headings = self._extract_headings()
                heading_anchors = [h[1].lower().replace(' ', '-') for h in headings]

                if anchor not in heading_anchors:
                    self.issues.append(Issue(
                        type="broken_internal_link",
                        severity="high",
                        message=f"Broken internal link: {url}",
                        suggestion=f"Check that section '{link_text}' exists"
                    ))
                    broken_links += 1

            # Check local file references
            elif not url.startswith(('http://', 'https://', 'mailto:')):
                file_path = self.file_path.parent / url
                if not file_path.exists():
                    self.issues.append(Issue(
                        type="broken_file_link",
                        severity="high",
                        message=f"Broken file link: {url}",
                        suggestion="Check that the referenced file exists"
                    ))
                    broken_links += 1

        # Calculate score
        if md_links:
            broken_ratio = broken_links / len(md_links)
            score = 100 * (1 - broken_ratio)

        self.metrics.link_health_score = max(0, score)

    def _extract_headings(self) -> List[Tuple[int, str, int]]:
        """Extract all headings with their level, text, and line number"""
        headings = []
        for i, line in enumerate(self.lines, 1):
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append((level, text, i))
        return headings

    def _has_toc(self) -> bool:
        """Check if document has a Table of Contents"""
        toc_patterns = [
            r'##?\s+table\s+of\s+contents',
            r'##?\s+contents',
            r'##?\s+toc',
        ]
        content_lower = self.content.lower()
        return any(re.search(pattern, content_lower) for pattern in toc_patterns)

    def _has_metadata(self) -> bool:
        """Check if document has metadata/front matter"""
        # Check for YAML front matter
        if self.content.startswith('---'):
            return True

        # Check for common metadata patterns
        metadata_patterns = [
            r'^#+\s+metadata',
            r'^\*\*author\*\*:',
            r'^\*\*date\*\*:',
            r'^\*\*version\*\*:',
        ]

        first_lines = '\n'.join(self.lines[:20]).lower()
        return any(re.search(pattern, first_lines, re.MULTILINE) for pattern in metadata_patterns)

    def _calculate_overall_score(self) -> float:
        """Calculate weighted overall score"""
        weights = {
            'structure': 0.3,
            'content': 0.35,
            'readability': 0.2,
            'links': 0.15,
        }

        overall = (
            weights['structure'] * self.metrics.structure_score +
            weights['content'] * self.metrics.content_score +
            weights['readability'] * self.metrics.readability_score +
            weights['links'] * self.metrics.link_health_score
        )

        return round(overall, 1)

    def _generate_report(self) -> Dict[str, Any]:
        """Generate analysis report"""
        report = {
            'file': str(self.file_path),
            'quality_score': self.metrics.overall_score,
            'metrics': asdict(self.metrics),
            'issues': [asdict(issue) for issue in self.issues],
            'summary': {
                'total_issues': len(self.issues),
                'critical': sum(1 for i in self.issues if i.severity == 'critical'),
                'high': sum(1 for i in self.issues if i.severity == 'high'),
                'medium': sum(1 for i in self.issues if i.severity == 'medium'),
                'low': sum(1 for i in self.issues if i.severity == 'low'),
            }
        }

        if self.detailed:
            report['recommendations'] = self._generate_recommendations()

        return report

    def _generate_recommendations(self) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []

        # Priority recommendations based on scores
        if self.metrics.structure_score < 70:
            recommendations.append("Improve document structure: add clear headings and organize content logically")

        if self.metrics.content_score < 70:
            recommendations.append("Enhance content: add more examples, code snippets, and detailed explanations")

        if self.metrics.readability_score < 70:
            recommendations.append("Improve readability: shorten sentences and break up long paragraphs")

        if self.metrics.link_health_score < 70:
            recommendations.append("Fix broken links: verify all internal and external links work correctly")

        # Add specific recommendations from issues
        critical_issues = [i for i in self.issues if i.severity == 'critical']
        for issue in critical_issues[:3]:  # Top 3 critical
            if issue.suggestion:
                recommendations.append(f"CRITICAL: {issue.suggestion}")

        return recommendations


def main():
    parser = argparse.ArgumentParser(description='Analyze Markdown document quality')
    parser.add_argument('--file', required=True, help='Path to Markdown file')
    parser.add_argument('--detailed', action='store_true', help='Generate detailed analysis')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--format', choices=['json', 'text'], default='json', help='Output format')

    args = parser.parse_args()

    analyzer = DocumentAnalyzer(args.file, args.detailed)
    report = analyzer.analyze()

    if args.format == 'json':
        output = json.dumps(report, indent=2)
    else:
        # Text format
        output = f"""
Document Quality Report
=======================
File: {report['file']}
Overall Quality Score: {report['quality_score']}/100

Metrics:
--------
Structure:   {report['metrics']['structure_score']:.1f}/100
Content:     {report['metrics']['content_score']:.1f}/100
Readability: {report['metrics']['readability_score']:.1f}/100
Links:       {report['metrics']['link_health_score']:.1f}/100

Issues Summary:
---------------
Total: {report['summary']['total_issues']}
Critical: {report['summary']['critical']}
High: {report['summary']['high']}
Medium: {report['summary']['medium']}
Low: {report['summary']['low']}

{"Recommendations:" if args.detailed and 'recommendations' in report else ""}
{chr(10).join(f"- {r}" for r in report.get('recommendations', [])) if args.detailed else ""}
"""

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Report saved to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
