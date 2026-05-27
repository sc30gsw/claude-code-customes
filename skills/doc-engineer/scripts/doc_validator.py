#!/usr/bin/env python3
"""
Document Validator
Validates Markdown documents against quality rules and structural requirements.
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Set
from dataclasses import dataclass, asdict


@dataclass
class ValidationResult:
    """Result of a validation check"""
    check_type: str
    passed: bool
    severity: str
    message: str
    line: int = 0
    details: str = ""


class DocumentValidator:
    """Validates Markdown document structure and content"""

    def __init__(self, file_path: str, rules_path: Optional[str] = None):
        self.file_path = Path(file_path)
        self.rules = self._load_rules(rules_path) if rules_path else self._default_rules()
        self.content = ""
        self.lines = []
        self.results: List[ValidationResult] = []

    def _load_rules(self, rules_path: str) -> Dict:
        """Load validation rules from JSON file"""
        with open(rules_path, 'r') as f:
            return json.load(f)

    def _default_rules(self) -> Dict:
        """Default validation rules"""
        return {
            "required_sections": [],
            "max_heading_level": 6,
            "require_toc": False,
            "require_metadata": False,
            "check_links": True,
            "check_code_fences": True,
            "allow_todo": False,
        }

    def load_document(self):
        """Load the document"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')

    def validate(self, checks: List[str] = None) -> Dict[str, Any]:
        """Run validation checks"""
        self.load_document()

        if checks is None or 'structure' in checks:
            self._validate_structure()

        if checks is None or 'links' in checks:
            self._validate_links()

        if checks is None or 'consistency' in checks:
            self._validate_consistency()

        if checks is None or 'completeness' in checks:
            self._validate_completeness()

        return self._generate_report()

    def _validate_structure(self):
        """Validate document structure"""

        # Check heading hierarchy
        headings = self._extract_headings()

        if not headings:
            self.results.append(ValidationResult(
                check_type="structure",
                passed=False,
                severity="critical",
                message="Document has no headings"
            ))
            return

        # Check heading levels don't skip
        for i, (level, text, line_num) in enumerate(headings):
            if i > 0:
                prev_level = headings[i-1][0]
                if level > prev_level + 1:
                    self.results.append(ValidationResult(
                        check_type="structure",
                        passed=False,
                        severity="warning",
                        message=f"Heading level skipped: h{prev_level} → h{level}",
                        line=line_num,
                        details=text
                    ))

            # Check heading level doesn't exceed max
            if level > self.rules.get('max_heading_level', 6):
                self.results.append(ValidationResult(
                    check_type="structure",
                    passed=False,
                    severity="warning",
                    message=f"Heading level too deep: h{level}",
                    line=line_num,
                    details=text
                ))

        # Check required sections
        required_sections = self.rules.get('required_sections', [])
        heading_texts = [text.lower() for _, text, _ in headings]

        for required in required_sections:
            if required.lower() not in heading_texts:
                self.results.append(ValidationResult(
                    check_type="structure",
                    passed=False,
                    severity="high",
                    message=f"Missing required section: {required}"
                ))

        # Check TOC if required
        if self.rules.get('require_toc', False) and not self._has_toc():
            self.results.append(ValidationResult(
                check_type="structure",
                passed=False,
                severity="medium",
                message="Missing Table of Contents"
            ))

        # Check metadata if required
        if self.rules.get('require_metadata', False) and not self._has_metadata():
            self.results.append(ValidationResult(
                check_type="structure",
                passed=False,
                severity="medium",
                message="Missing document metadata"
            ))

    def _validate_links(self):
        """Validate all links in the document"""

        # Extract all Markdown links
        md_links = re.finditer(r'\[([^\]]+)\]\(([^\)]+)\)', self.content)

        for match in md_links:
            link_text = match.group(1)
            url = match.group(2)
            line_num = self.content[:match.start()].count('\n') + 1

            # Internal anchor links
            if url.startswith('#'):
                anchor = url[1:].lower().replace(' ', '-')
                headings = self._extract_headings()
                heading_anchors = [h[1].lower().replace(' ', '-') for h in headings]

                if anchor not in heading_anchors:
                    self.results.append(ValidationResult(
                        check_type="links",
                        passed=False,
                        severity="high",
                        message=f"Broken internal link: {url}",
                        line=line_num,
                        details=link_text
                    ))

            # Local file references
            elif not url.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                # Remove anchor if present
                file_url = url.split('#')[0]
                file_path = self.file_path.parent / file_url

                if not file_path.exists():
                    self.results.append(ValidationResult(
                        check_type="links",
                        passed=False,
                        severity="high",
                        message=f"Broken file link: {url}",
                        line=line_num,
                        details=f"File not found: {file_path}"
                    ))

            # External URLs (basic check, not making HTTP requests)
            elif url.startswith(('http://', 'https://')):
                # Just validate URL format
                if not self._is_valid_url(url):
                    self.results.append(ValidationResult(
                        check_type="links",
                        passed=False,
                        severity="medium",
                        message=f"Invalid URL format: {url}",
                        line=line_num
                    ))

        # Check for reference-style links
        ref_links = re.finditer(r'^\[([^\]]+)\]:\s*(.+)$', self.content, re.MULTILINE)
        defined_refs = set()

        for match in ref_links:
            ref_name = match.group(1)
            defined_refs.add(ref_name.lower())

        # Find link usages
        link_usages = re.finditer(r'\[([^\]]+)\]\[([^\]]*)\]', self.content)

        for match in link_usages:
            ref_name = match.group(2) or match.group(1)
            if ref_name.lower() not in defined_refs:
                line_num = self.content[:match.start()].count('\n') + 1
                self.results.append(ValidationResult(
                    check_type="links",
                    passed=False,
                    severity="high",
                    message=f"Undefined reference link: {ref_name}",
                    line=line_num
                ))

    def _validate_consistency(self):
        """Validate consistency across document"""

        # Check code fence language tags
        if self.rules.get('check_code_fences', True):
            code_fences = re.finditer(r'^```(\w*)\s*$', self.content, re.MULTILINE)

            for match in code_fences:
                if not match.group(1):  # Empty language tag
                    line_num = self.content[:match.start()].count('\n') + 1
                    self.results.append(ValidationResult(
                        check_type="consistency",
                        passed=False,
                        severity="low",
                        message="Code fence without language tag",
                        line=line_num,
                        details="Add language tag for syntax highlighting (e.g., ```python)"
                    ))

        # Check for mismatched code fences
        opening_fences = len(re.findall(r'^```', self.content, re.MULTILINE))
        if opening_fences % 2 != 0:
            self.results.append(ValidationResult(
                check_type="consistency",
                passed=False,
                severity="critical",
                message="Unmatched code fences (odd number of ```)",
                details=f"Found {opening_fences} code fence markers"
            ))

        # Check list marker consistency
        self._check_list_consistency()

    def _validate_completeness(self):
        """Validate document completeness"""

        # Check for TODO/TBD markers
        if not self.rules.get('allow_todo', False):
            todo_patterns = r'\b(TODO|TBD|FIXME|XXX)\b'
            todos = re.finditer(todo_patterns, self.content)

            for match in todos:
                line_num = self.content[:match.start()].count('\n') + 1
                self.results.append(ValidationResult(
                    check_type="completeness",
                    passed=False,
                    severity="high",
                    message=f"Placeholder text found: {match.group(1)}",
                    line=line_num,
                    details="Replace with actual content"
                ))

        # Check for empty sections
        headings = self._extract_headings()

        for i, (level, text, line_num) in enumerate(headings):
            next_line = headings[i + 1][2] if i + 1 < len(headings) else len(self.lines)
            section_content = '\n'.join(self.lines[line_num:next_line]).strip()

            # Remove the heading itself
            section_content = re.sub(r'^#+\s+.+$', '', section_content, flags=re.MULTILINE).strip()

            if not section_content:
                self.results.append(ValidationResult(
                    check_type="completeness",
                    passed=False,
                    severity="medium",
                    message=f"Empty section: {text}",
                    line=line_num,
                    details="Add content to this section"
                ))

        # Check minimum content length
        word_count = len(self.content.split())
        min_words = self.rules.get('min_word_count', 100)

        if word_count < min_words:
            self.results.append(ValidationResult(
                check_type="completeness",
                passed=False,
                severity="medium",
                message=f"Document too short: {word_count} words (minimum: {min_words})"
            ))

    def _check_list_consistency(self):
        """Check list marker consistency"""
        list_blocks = []
        in_list = False
        list_start = 0
        list_markers = set()

        for i, line in enumerate(self.lines):
            # Detect list item
            if re.match(r'^\s*[-*+]\s', line):
                if not in_list:
                    in_list = True
                    list_start = i
                    list_markers = set()

                marker = re.match(r'^\s*([-*+])', line).group(1)
                list_markers.add(marker)

            elif in_list and line.strip() == '':
                # End of list block
                if len(list_markers) > 1:
                    self.results.append(ValidationResult(
                        check_type="consistency",
                        passed=False,
                        severity="low",
                        message=f"Inconsistent list markers: {list_markers}",
                        line=list_start + 1,
                        details="Use consistent markers within a list (-, *, or +)"
                    ))
                in_list = False

    def _extract_headings(self) -> List:
        """Extract all headings"""
        headings = []
        for i, line in enumerate(self.lines, 1):
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append((level, text, i))
        return headings

    def _has_toc(self) -> bool:
        """Check if document has TOC"""
        toc_patterns = [
            r'##?\s+table\s+of\s+contents',
            r'##?\s+contents',
            r'##?\s+toc',
        ]
        content_lower = self.content.lower()
        return any(re.search(pattern, content_lower) for pattern in toc_patterns)

    def _has_metadata(self) -> bool:
        """Check if document has metadata"""
        # YAML front matter
        if self.content.startswith('---'):
            return True

        # Metadata section
        metadata_patterns = [
            r'^#+\s+metadata',
            r'^\*\*author\*\*:',
            r'^\*\*date\*\*:',
            r'^\*\*version\*\*:',
        ]

        first_lines = '\n'.join(self.lines[:20]).lower()
        return any(re.search(pattern, first_lines, re.MULTILINE) for pattern in metadata_patterns)

    def _is_valid_url(self, url: str) -> bool:
        """Basic URL validation"""
        from urllib.parse import urlparse

        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def _generate_report(self) -> Dict[str, Any]:
        """Generate validation report"""
        passed = all(r.passed for r in self.results)

        report = {
            'file': str(self.file_path),
            'passed': passed,
            'total_checks': len(self.results),
            'failed_checks': sum(1 for r in self.results if not r.passed),
            'results': [asdict(r) for r in self.results],
            'summary': {
                'critical': sum(1 for r in self.results if not r.passed and r.severity == 'critical'),
                'high': sum(1 for r in self.results if not r.passed and r.severity == 'high'),
                'medium': sum(1 for r in self.results if not r.passed and r.severity == 'medium'),
                'low': sum(1 for r in self.results if not r.passed and r.severity == 'low'),
            }
        }

        return report


def main():
    parser = argparse.ArgumentParser(description='Validate Markdown document')
    parser.add_argument('--file', required=True, help='Path to Markdown file')
    parser.add_argument('--check', choices=['structure', 'links', 'consistency', 'completeness'],
                       help='Specific check to run')
    parser.add_argument('--rules', help='Path to validation rules JSON file')
    parser.add_argument('--full', action='store_true', help='Run all validation checks')
    parser.add_argument('--output', help='Output JSON file path')

    args = parser.parse_args()

    validator = DocumentValidator(args.file, args.rules)

    checks = None
    if args.check:
        checks = [args.check]
    elif args.full:
        checks = ['structure', 'links', 'consistency', 'completeness']

    report = validator.validate(checks)

    output = json.dumps(report, indent=2)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Validation report saved to {args.output}")
    else:
        print(output)

    # Exit with error code if validation failed
    exit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
