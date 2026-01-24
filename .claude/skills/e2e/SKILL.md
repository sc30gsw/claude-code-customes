---
name: e2e
description: Generate and run end-to-end tests with Playwright. Creates test journeys, runs tests, captures screenshots/videos/traces, and uploads artifacts.
---

# E2E Command

This skill invokes the **e2e-runner** agent to generate, maintain, and execute end-to-end tests using Playwright.

## What This Skill Does

1. **Generate Test Journeys** - Create Playwright tests for user flows
2. **Run E2E Tests** - Execute tests across browsers
3. **Capture Artifacts** - Screenshots, videos, traces on failures
4. **Upload Results** - HTML reports and JUnit XML
5. **Identify Flaky Tests** - Quarantine unstable tests

## When to Use

Use `/e2e` when:
- Testing critical user journeys (login, trading, payments)
- Verifying multi-step flows work end-to-end
- Testing UI interactions and navigation
- Validating integration between frontend and backend
- Preparing for production deployment

## How It Works

The e2e-runner agent will:

1. **Analyze user flow** and identify test scenarios
2. **Generate Playwright test** using Page Object Model pattern
3. **Run tests** across multiple browsers (Chrome, Firefox, Safari)
4. **Capture failures** with screenshots, videos, and traces
5. **Generate report** with results and artifacts
6. **Identify flaky tests** and recommend fixes

## Test Artifacts

**On All Tests:**
- HTML Report with timeline and results
- JUnit XML for CI integration

**On Failure Only:**
- Screenshot of the failing state
- Video recording of the test
- Trace file for debugging
- Network logs
- Console logs

## Browser Configuration

Tests run on multiple browsers by default:
- Chromium (Desktop Chrome)
- Firefox (Desktop)
- WebKit (Desktop Safari)
- Mobile Chrome (optional)

## Best Practices

**DO:**
- Use Page Object Model for maintainability
- Use data-testid attributes for selectors
- Wait for API responses, not arbitrary timeouts
- Test critical user journeys end-to-end
- Run tests before merging to main

**DON'T:**
- Use brittle selectors (CSS classes can change)
- Test implementation details
- Run tests against production
- Ignore flaky tests

## Quick Commands

```bash
npx playwright test                    # Run all E2E tests
npx playwright test --headed           # Run in headed mode
npx playwright test --debug            # Debug test
npx playwright show-report             # View report
```
