# Sprint 1 Retrospective — Personal Finance Tracker

## What Went Well

- Successfully implemented core account and transaction functionality
- Set up a working CI/CD pipeline using GitHub Actions
- Maintained incremental commits, avoiding “big-bang” commits
- Integrated unit testing early in the development process

---

## What Didn’t Go Well

- Initial CI pipeline failed due to missing test detection
- Minor issues with project structure and import paths
- Time spent debugging pipeline configuration

---

## Lessons Learned

- CI pipelines require proper test structure to function correctly
- Running tests locally before pushing prevents pipeline failures
- Clean project structure is essential for scalability

---

## Improvements for Sprint 2

### 1. Improve Development Workflow

- Always run tests locally before pushing changes
- Use smaller, more frequent commits

### 2. Enhance Code Structure

- Organize modules more clearly
- Introduce additional abstraction where necessary

### 3. Expand Testing Coverage

- Add more edge case tests
- Include validation and error-handling tests

---

## Action Plan for Sprint 2

- Implement category-based transactions
- Add savings goals functionality
- Introduce JSON data persistence
- Improve reporting features
