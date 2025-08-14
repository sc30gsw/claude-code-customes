---
description: Generate comprehensive test specifications for TDD implementation
allowed-tools: Bash, Read, Write, Edit, MultiEdit, Update, Glob, Grep, LS, WebSearch, WebFetch, mcp__serena__check_onboarding_performed, mcp__serena__delete_memory, mcp__serena__find_file, mcp__serena__find_referencing_symbols, mcp__serena__find_symbol, mcp__serena__get_symbols_overview, mcp__serena__insert_after_symbol, mcp__serena__insert_before_symbol, mcp__serena__list_dir, mcp__serena__list_memories, mcp__serena__onboarding, mcp__serena__read_memory, mcp__serena__remove_project, mcp__serena__replace_regex, mcp__serena__replace_symbol_body, mcp__serena__restart_language_server, mcp__serena__search_for_pattern, mcp__serena__switch_modes, mcp__serena__think_about_collected_information, mcp__serena__think_about_task_adherence, mcp__serena__think_about_whether_you_are_done, mcp__serena__write_memory
argument-hint: <feature-name>
---

# Test Specification Generation

Generate comprehensive test specifications for feature: **$ARGUMENTS**

Optional parameters:
- `--test-lib=[jest|vitest|mocha]` - Unit test framework (default: vitest)
- `--ui-lib=[testing-library|enzyme]` - UI testing library (default: testing-library)
- `--e2e-lib=[playwright|cypress|puppeteer]` - E2E test framework (default: playwright)
- `--api-lib=[supertest|axios-mock]` - API testing library (default: supertest)
- `--coverage=[number]` - Target coverage percentage (default: 80)
- `--mock-strategy=[manual|auto]` - Mock generation strategy (default: auto)

## Interactive Approval: Requirements & Design Review

**CRITICAL**: Test specifications can only be generated after both requirements and design are reviewed and approved.

### Prerequisites Verification
- Requirements document: @.kiro/specs/$ARGUMENTS/requirements.md
- Design document: @.kiro/specs/$ARGUMENTS/design.md
- Spec metadata: @.kiro/specs/$ARGUMENTS/spec.json

**Interactive Approval Process**:
1. **Check if documents exist** - Verify that requirements.md and design.md have been generated
2. **Prompt for requirements review** - Ask user: "requirements.mdをレビューしましたか？ [y/N]"
3. **Prompt for design review** - Ask user: "design.mdをレビューしましたか？ [y/N]"
4. **If both 'y' (yes)**: Proceed with test specification generation
5. **If any 'N' (no)**: Stop execution and instruct user to review respective documents first

## Context Analysis

### Requirements Foundation
- Requirements document: @.kiro/specs/$ARGUMENTS/requirements.md
- EARS format requirements for test case derivation
- User stories for acceptance test scenarios
- Acceptance criteria for test assertion generation

### Design Foundation
- Design document: @.kiro/specs/$ARGUMENTS/design.md
- Component architecture for test structure
- API endpoints for API test generation
- Data models for test data generation
- UI components for component test planning

### Existing Test Context
- Current test specs: @.kiro/specs/$ARGUMENTS/tests/
- Test metadata: @.kiro/specs/$ARGUMENTS/spec.json

## Task: Generate TDD Test Specifications

**CRITICAL**: Generate test specifications that follow Test-Driven Development principles, ensuring tests are written before implementation.

### 1. Test Specification Structure

Create test directory structure:
```
.kiro/specs/$ARGUMENTS/tests/
├── test-spec.md           # Main test specification document
├── unit/                  # Unit test specifications
│   ├── services.test.md   # Service layer tests
│   ├── utils.test.md      # Utility function tests
│   └── models.test.md     # Data model tests
├── component/             # Component test specifications
│   ├── [Component].test.md # Individual component tests
│   └── integration.test.md # Component integration tests
├── hook/                  # Custom hook test specifications
│   └── [Hook].test.md     # Individual hook tests
├── api/                   # API test specifications
│   ├── endpoints.test.md  # Endpoint tests
│   └── integration.test.md # API integration tests
├── e2e/                   # E2E test specifications
│   ├── workflows.test.md  # User workflow tests
│   └── scenarios.test.md  # Complete scenario tests
├── mocks/                 # Mock specifications
│   ├── data.mock.md       # Test data mocks
│   └── services.mock.md   # Service mocks
└── coverage.config.md     # Coverage configuration

```

### 2. Main Test Specification Document (test-spec.md)

Generate comprehensive test specification in the language specified in spec.json:

```markdown
# Test Specification Document

## Overview
[Test strategy overview based on requirements and design]

## Test Framework Configuration
- **Unit Test Framework**: [Selected framework]
- **UI Testing Library**: [Selected library]
- **E2E Framework**: [Selected framework]
- **API Testing Library**: [Selected library]
- **Coverage Target**: [Coverage percentage]%

## Requirements Traceability Matrix

| Requirement ID | Test Type | Test Case ID | Coverage Status |
|---------------|-----------|--------------|-----------------|
| REQ-1.1 | Unit | TC-U-001 | ✅ Planned |
| REQ-1.2 | Component | TC-C-001 | ✅ Planned |
| REQ-2.1 | API | TC-A-001 | ✅ Planned |
| REQ-3.1 | E2E | TC-E-001 | ✅ Planned |

## Test Strategy

### Unit Testing Strategy
- **Scope**: Business logic, utilities, data transformations
- **Approach**: Test-first development (Red-Green-Refactor)
- **Isolation**: Mock all external dependencies
- **Coverage Goal**: ≥[coverage]% line coverage

### Component Testing Strategy  
- **Scope**: React components, UI behavior, user interactions
- **Approach**: Behavior-driven testing
- **Rendering**: Use testing library render methods
- **User Events**: Simulate real user interactions

### Hook Testing Strategy
- **Scope**: Custom React hooks
- **Approach**: renderHook with act for state changes
- **Isolation**: Test hooks independently from components
- **Coverage**: All hook paths and edge cases

### API Testing Strategy
- **Scope**: REST endpoints, GraphQL resolvers
- **Approach**: Contract testing with request/response validation
- **Data**: Use fixtures and factories for test data
- **Authentication**: Test both authenticated and public endpoints

### E2E Testing Strategy
- **Scope**: Complete user workflows
- **Approach**: User journey testing
- **Environment**: Test against staging environment
- **Data Management**: Database seeding and cleanup

## Test Execution Plan

### Phase 1: Foundation Tests (TDD Red Phase)
1. Write failing unit tests for core business logic
2. Write failing API contract tests
3. Write failing component tests for UI elements

### Phase 2: Implementation (TDD Green Phase)
1. Implement minimum code to pass unit tests
2. Implement API endpoints to pass contract tests
3. Implement components to pass UI tests

### Phase 3: Integration Tests (TDD Refactor Phase)
1. Write integration tests between components
2. Write API integration tests
3. Refactor code while keeping tests green

### Phase 4: E2E Tests
1. Write E2E tests for critical user paths
2. Write E2E tests for edge cases
3. Performance and load testing

## Mock Strategy

### Data Mocks
- User data fixtures
- API response mocks
- Database seed data

### Service Mocks
- External API mocks
- Authentication service mocks
- Database connection mocks

## CI/CD Integration

### Test Pipeline
```yaml
test:
  - lint
  - unit-tests
  - component-tests
  - api-tests
  - e2e-tests
  - coverage-report
```

### Coverage Gates
- Minimum coverage: [coverage]%
- Build fails if coverage drops
- Coverage trend reporting
```

### 3. Unit Test Specifications

For each unit identified in design, generate test specifications:

```markdown
# Unit Test: [ServiceName]

## Test Suite: [ServiceName]Service

### Setup
```[language]
// Mock dependencies
const mockRepository = jest.fn();
const mockLogger = jest.fn();
```

### Test Cases

#### TC-U-001: [Method] should [expected behavior] when [condition]
**Requirement**: REQ-X.X
**Given**: [Initial state]
**When**: [Action taken]
**Then**: [Expected result]

```[language]
test('should [expected behavior] when [condition]', () => {
  // Arrange
  const input = [test data];
  const expected = [expected result];
  
  // Act
  const result = service.[method](input);
  
  // Assert
  expect(result).toEqual(expected);
});
```

#### TC-U-002: [Method] should handle errors when [error condition]
**Requirement**: REQ-X.X
**Given**: [Error state]
**When**: [Error action]
**Then**: [Error handling]

### Edge Cases
- Null/undefined inputs
- Empty collections
- Boundary values
- Concurrent operations
```

### 4. Component Test Specifications

For each component in design:

```markdown
# Component Test: [ComponentName]

## Test Suite: [ComponentName] Component

### Setup
```[language]
import { render, screen, fireEvent } from '@testing-library/react';
import { [ComponentName] } from './[ComponentName]';
```

### Test Cases

#### TC-C-001: Should render with default props
**Requirement**: REQ-X.X
**Visual**: Component displays correctly

```[language]
test('renders with default props', () => {
  render(<[ComponentName] />);
  expect(screen.getByRole('[role]')).toBeInTheDocument();
});
```

#### TC-C-002: Should handle user interaction
**Requirement**: REQ-X.X
**Interaction**: User clicks/types/selects

```[language]
test('handles [interaction] correctly', async () => {
  const handleClick = jest.fn();
  render(<[ComponentName] onClick={handleClick} />);
  
  fireEvent.click(screen.getByRole('button'));
  expect(handleClick).toHaveBeenCalledWith([expected args]);
});
```

### Accessibility Tests
- ARIA labels
- Keyboard navigation
- Screen reader compatibility
```

### 5. Hook Test Specifications

For custom hooks:

```markdown
# Hook Test: [useHookName]

## Test Suite: [useHookName] Hook

### Test Cases

#### TC-H-001: Should initialize with default state
**Requirement**: REQ-X.X

```[language]
test('initializes with default state', () => {
  const { result } = renderHook(() => useHookName());
  expect(result.current.state).toBe(defaultState);
});
```

#### TC-H-002: Should update state on action
**Requirement**: REQ-X.X

```[language]
test('updates state when action is called', () => {
  const { result } = renderHook(() => useHookName());
  
  act(() => {
    result.current.action(newValue);
  });
  
  expect(result.current.state).toBe(newValue);
});
```
```

### 6. API Test Specifications

For each API endpoint:

```markdown
# API Test: [Endpoint]

## Test Suite: [Method] /api/[resource]

### Test Cases

#### TC-A-001: Should return [status] for valid request
**Requirement**: REQ-X.X
**Endpoint**: [Method] /api/[resource]

```[language]
test('[Method] /api/[resource] returns [status]', async () => {
  const response = await request(app)
    .[method]('/api/[resource]')
    .send([request body])
    .expect([status]);
    
  expect(response.body).toMatchObject([expected response]);
});
```

#### TC-A-002: Should validate request parameters
**Requirement**: REQ-X.X
**Validation**: Input validation rules

### Authentication Tests
- Authenticated requests
- Permission checks
- Token validation
```

### 7. E2E Test Specifications

For user workflows:

```markdown
# E2E Test: [Workflow Name]

## Test Suite: [Workflow] User Journey

### Test Scenarios

#### TC-E-001: Complete [workflow] successfully
**Requirement**: REQ-X.X
**User Story**: As a [user], I want to [action], so that [outcome]

```[language]
test('user completes [workflow] successfully', async ({ page }) => {
  // Navigate to starting point
  await page.goto('/[start-url]');
  
  // Step 1: [Action]
  await page.click('[selector]');
  await expect(page).toHaveURL('/[expected-url]');
  
  // Step 2: [Action]
  await page.fill('[input]', '[value]');
  await page.click('[submit]');
  
  // Verify outcome
  await expect(page.locator('[result]')).toContainText('[expected]');
});
```

### Critical User Paths
1. Authentication flow
2. Main feature workflow
3. Data CRUD operations
4. Error recovery paths
```

### 8. Mock Specifications

Generate mock data and service specifications:

```markdown
# Mock Specifications

## Data Mocks

### User Data Factory
```[language]
export const createMockUser = (overrides = {}) => ({
  id: faker.datatype.uuid(),
  email: faker.internet.email(),
  name: faker.name.fullName(),
  ...overrides
});
```

### API Response Mocks
```[language]
export const mockApiResponses = {
  success: { status: 200, data: [...] },
  error: { status: 400, error: 'Bad Request' },
  unauthorized: { status: 401, error: 'Unauthorized' }
};
```

## Service Mocks

### External Service Mock
```[language]
jest.mock('./external-service', () => ({
  fetchData: jest.fn().mockResolvedValue(mockData),
  sendNotification: jest.fn().mockResolvedValue({ sent: true })
}));
```
```

### 9. Coverage Configuration

Generate coverage configuration:

```markdown
# Coverage Configuration

## Jest Coverage Config
```javascript
module.exports = {
  collectCoverage: true,
  coverageDirectory: 'coverage',
  coverageThreshold: {
    global: {
      branches: [coverage],
      functions: [coverage],
      lines: [coverage],
      statements: [coverage]
    }
  },
  collectCoverageFrom: [
    'src/**/*.{js,jsx,ts,tsx}',
    '!src/**/*.test.{js,jsx,ts,tsx}',
    '!src/**/index.{js,ts}',
    '!src/**/*.mock.{js,ts}'
  ],
  coverageReporters: ['text', 'lcov', 'html']
};
```

## CI/CD Integration

### GitHub Actions Workflow
```yaml
name: Test Suite
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit
      
      - name: Run component tests
        run: npm run test:component
      
      - name: Run API tests
        run: npm run test:api
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/lcov.info
```

## NPM Scripts
```json
{
  "scripts": {
    "test": "jest",
    "test:unit": "jest --testPathPattern=unit",
    "test:component": "jest --testPathPattern=component",
    "test:hook": "jest --testPathPattern=hook",
    "test:api": "jest --testPathPattern=api",
    "test:e2e": "playwright test",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "test:ci": "jest --ci --coverage --maxWorkers=2"
  }
}
```
```

### 10. Update Metadata

Update spec.json with test phase:
```json
{
  "phase": "test-specifications-generated",
  "approvals": {
    "requirements": {
      "generated": true,
      "approved": true
    },
    "design": {
      "generated": true,
      "approved": true
    },
    "tests": {
      "generated": true,
      "approved": false
    }
  },
  "updated_at": "current_timestamp"
}
```

---

## INTERACTIVE APPROVAL FOR NEXT PHASE (Not included in document)
## Next Phase: Interactive Approval


After generating design.md, review the test and choose:

**If design looks good:**
Run `/kiro:spec-tasks $ARGUMENTS -y` to proceed to tasks phase

**If design needs modification:**
Request changes, then re-run this command after modifications

The `-y` flag auto-approves test and generates tasks directly, streamlining the workflow while maintaining review enforcement.

### Test Specification Review Process
After generating test specifications, the implementation phase can begin with TDD approach:

### TDD Implementation Workflow
**Red Phase**: Write failing tests based on specifications
**Green Phase**: Write minimum code to pass tests
**Refactor Phase**: Improve code while keeping tests green

### Review Checklist (for user reference):
- [ ] Test cases cover all requirements
- [ ] Test structure follows project conventions
- [ ] Mock strategy is appropriate
- [ ] Coverage targets are realistic
- [ ] CI/CD integration is configured

## Instructions

1. **Verify prerequisites** - Ensure requirements.md and design.md exist and are approved
2. **Parse command options** - Extract test framework preferences from arguments
3. **Analyze requirements** - Map each EARS requirement to test cases
4. **Analyze design** - Extract components, APIs, and services for testing
5. **Generate test specifications** - Create comprehensive test documentation
6. **Create test file structure** - Organize tests by type and component
7. **Generate mock specifications** - Define test data and service mocks
8. **Configure coverage settings** - Set up coverage targets and reporting
9. **Create CI/CD integration** - Generate workflow files for automated testing
10. **Update metadata** - Track test specification generation in spec.json

Generate test specifications that enable true Test-Driven Development with comprehensive coverage and clear traceability to requirements.