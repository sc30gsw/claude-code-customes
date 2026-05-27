#!/usr/bin/env python3
"""
Document Workflow Manager
Manages end-to-end document creation workflow from draft to publication.
"""

import json
import argparse
from pathlib import Path
from typing import Dict, Optional
from template_generator import TemplateGenerator
from doc_analyzer import DocumentAnalyzer
from doc_improver import DocumentImprover
from doc_validator import DocumentValidator


class DocumentWorkflow:
    """Manages complete document creation workflow"""

    def __init__(self, target_quality: int = 80):
        self.target_quality = target_quality
        self.workflow_state = {}

    def create_complete_document(
        self,
        doc_type: str,
        output_path: str,
        context: Dict = None
    ) -> Dict:
        """
        Create a complete, publication-ready document.

        Phases:
        1. Template Generation
        2. Structure Validation
        3. Content Development
        4. Quality Check
        5. Improvement Application
        6. Final Validation
        """

        print(f"\n{'='*60}")
        print(f"Document Workflow: Creating {doc_type}")
        print(f"{'='*60}\n")

        # Phase 1: Template Generation
        print("Phase 1: Generating template...")
        self._phase_1_generate(doc_type, output_path, context)

        # Phase 2: Structure Validation
        print("\nPhase 2: Validating structure...")
        self._phase_2_validate_structure(output_path)

        # Phase 3: Content Development
        print("\nPhase 3: Developing content...")
        # This phase typically requires human input
        print("  → Template created. Add your content to the document.")
        print("  → Run workflow again with --improve flag when content is ready.")

        # Phase 4: Quality Check
        print("\nPhase 4: Quality check...")
        quality_report = self._phase_4_quality_check(output_path)

        # Phase 5: Improvement Application (if needed)
        if quality_report['quality_score'] < self.target_quality:
            print(f"\nPhase 5: Applying improvements (current: {quality_report['quality_score']}, target: {self.target_quality})...")
            self._phase_5_apply_improvements(output_path)

            # Re-check quality
            quality_report = self._phase_4_quality_check(output_path)

        # Phase 6: Final Validation
        print("\nPhase 6: Final validation...")
        validation_report = self._phase_6_final_validation(output_path)

        # Summary
        print(f"\n{'='*60}")
        print("Workflow Complete!")
        print(f"{'='*60}")
        print(f"Document: {output_path}")
        print(f"Quality Score: {quality_report['quality_score']}/100")
        print(f"Validation: {'✓ PASSED' if validation_report['passed'] else '✗ FAILED'}")
        print(f"Status: {'Ready for review' if quality_report['quality_score'] >= self.target_quality else 'Needs improvement'}")
        print(f"{'='*60}\n")

        return {
            'output_path': output_path,
            'quality_score': quality_report['quality_score'],
            'validation_passed': validation_report['passed'],
            'ready_for_review': quality_report['quality_score'] >= self.target_quality,
        }

    def improve_existing_document(
        self,
        input_path: str,
        output_path: Optional[str] = None
    ) -> Dict:
        """
        Improve an existing document to meet quality target.
        """

        if output_path is None:
            output_path = str(Path(input_path).with_suffix('.improved.md'))

        print(f"\n{'='*60}")
        print(f"Document Workflow: Improving {input_path}")
        print(f"{'='*60}\n")

        # Analyze current state
        print("Analyzing current document...")
        analyzer = DocumentAnalyzer(input_path, detailed=True)
        initial_report = analyzer.analyze()

        print(f"Current Quality Score: {initial_report['quality_score']}/100")
        print(f"Target Quality Score: {self.target_quality}/100")

        # Generate improvements
        print("\nGenerating improvements...")
        improver = DocumentImprover(input_path)
        improvements = improver.analyze_and_suggest()

        auto_applicable = [imp for imp in improvements if imp.auto_applicable]
        print(f"  → Found {len(improvements)} improvements")
        print(f"  → {len(auto_applicable)} can be auto-applied")

        # Apply improvements
        if auto_applicable:
            print("\nApplying auto-applicable improvements...")
            content = improver.apply_improvements([imp.id for imp in auto_applicable])

            with open(output_path, 'w') as f:
                f.write(content)

            print(f"  → Saved improved document to {output_path}")

        # Re-analyze
        print("\nRe-analyzing improved document...")
        analyzer = DocumentAnalyzer(output_path, detailed=True)
        final_report = analyzer.analyze()

        print(f"New Quality Score: {final_report['quality_score']}/100")
        print(f"Improvement: +{final_report['quality_score'] - initial_report['quality_score']:.1f}")

        # Final validation
        print("\nRunning final validation...")
        validator = DocumentValidator(output_path)
        validation_report = validator.validate()

        print(f"\n{'='*60}")
        print("Improvement Complete!")
        print(f"{'='*60}")
        print(f"Original: {input_path} ({initial_report['quality_score']}/100)")
        print(f"Improved: {output_path} ({final_report['quality_score']}/100)")
        print(f"Validation: {'✓ PASSED' if validation_report['passed'] else '✗ FAILED'}")
        print(f"{'='*60}\n")

        return {
            'input_path': input_path,
            'output_path': output_path,
            'initial_score': initial_report['quality_score'],
            'final_score': final_report['quality_score'],
            'improvement': final_report['quality_score'] - initial_report['quality_score'],
            'validation_passed': validation_report['passed'],
        }

    def _phase_1_generate(self, doc_type: str, output_path: str, context: Dict):
        """Phase 1: Generate template"""
        generator = TemplateGenerator(doc_type, context)
        generator.save(output_path)
        print(f"  ✓ Template generated: {output_path}")

    def _phase_2_validate_structure(self, file_path: str):
        """Phase 2: Validate basic structure"""
        validator = DocumentValidator(file_path)
        report = validator.validate(['structure'])

        if report['passed']:
            print(f"  ✓ Structure validation passed")
        else:
            print(f"  ⚠ Structure validation found issues:")
            for result in report['results']:
                if not result['passed']:
                    print(f"    - {result['message']}")

    def _phase_4_quality_check(self, file_path: str) -> Dict:
        """Phase 4: Run quality analysis"""
        analyzer = DocumentAnalyzer(file_path, detailed=True)
        report = analyzer.analyze()

        print(f"  ✓ Quality Score: {report['quality_score']}/100")
        print(f"    - Structure: {report['metrics']['structure_score']:.1f}")
        print(f"    - Content: {report['metrics']['content_score']:.1f}")
        print(f"    - Readability: {report['metrics']['readability_score']:.1f}")
        print(f"    - Links: {report['metrics']['link_health_score']:.1f}")

        if report['summary']['total_issues'] > 0:
            print(f"  ⚠ Found {report['summary']['total_issues']} issues:")
            print(f"    - Critical: {report['summary']['critical']}")
            print(f"    - High: {report['summary']['high']}")
            print(f"    - Medium: {report['summary']['medium']}")
            print(f"    - Low: {report['summary']['low']}")

        return report

    def _phase_5_apply_improvements(self, file_path: str):
        """Phase 5: Apply improvements"""
        improver = DocumentImprover(file_path)
        improvements = improver.analyze_and_suggest()

        auto_applicable = [imp for imp in improvements if imp.auto_applicable]

        if auto_applicable:
            print(f"  → Applying {len(auto_applicable)} improvements...")
            content = improver.apply_improvements([imp.id for imp in auto_applicable])

            with open(file_path, 'w') as f:
                f.write(content)

            print(f"  ✓ Improvements applied")
        else:
            print(f"  ⚠ No auto-applicable improvements found")
            print(f"  → Manual improvements needed: {len(improvements)}")

    def _phase_6_final_validation(self, file_path: str) -> Dict:
        """Phase 6: Final comprehensive validation"""
        validator = DocumentValidator(file_path)
        report = validator.validate()

        if report['passed']:
            print(f"  ✓ All validation checks passed")
        else:
            print(f"  ⚠ Validation issues found:")
            for result in report['results']:
                if not result['passed'] and result['severity'] in ['critical', 'high']:
                    print(f"    - [{result['severity'].upper()}] {result['message']}")

        return report


def main():
    parser = argparse.ArgumentParser(description='Document workflow management')

    subparsers = parser.add_subparsers(dest='command', help='Workflow command')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create new document')
    create_parser.add_argument('--type', required=True,
                              choices=['technical-spec', 'requirements', 'adr', 'rfc', 'readme', 'coding-rules', 'article'],
                              help='Document type')
    create_parser.add_argument('--output', required=True, help='Output file path')
    create_parser.add_argument('--project', help='Project name')
    create_parser.add_argument('--author', help='Author name')
    create_parser.add_argument('--title', help='Document title')
    create_parser.add_argument('--context', help='JSON file with context data')
    create_parser.add_argument('--target-quality', type=int, default=80,
                              help='Target quality score (0-100)')
    create_parser.add_argument('--complete', action='store_true',
                              help='Run complete workflow (template only by default)')

    # Improve command
    improve_parser = subparsers.add_parser('improve', help='Improve existing document')
    improve_parser.add_argument('--file', required=True, help='Input file path')
    improve_parser.add_argument('--output', help='Output file path')
    improve_parser.add_argument('--target-quality', type=int, default=80,
                               help='Target quality score (0-100)')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    workflow = DocumentWorkflow(target_quality=args.target_quality)

    if args.command == 'create':
        # Load context
        context = {}
        if args.context:
            with open(args.context, 'r') as f:
                context = json.load(f)

        # Override with command-line arguments
        if args.project:
            context['project_name'] = args.project
        if args.author:
            context['author'] = args.author
        if args.title:
            context['title'] = args.title

        if args.complete:
            result = workflow.create_complete_document(args.type, args.output, context)
        else:
            # Just generate template
            print(f"\nGenerating {args.type} template...")
            workflow._phase_1_generate(args.type, args.output, context)
            print(f"✓ Template created: {args.output}")
            print("\nNext steps:")
            print("1. Add your content to the template")
            print("2. Run: python doc_workflow.py improve --file <your-file>")

    elif args.command == 'improve':
        result = workflow.improve_existing_document(args.file, args.output)


if __name__ == '__main__':
    main()
