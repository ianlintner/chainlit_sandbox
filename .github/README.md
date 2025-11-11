# GitHub Workflows and CI/CD

This repository uses GitHub Actions for continuous integration and code quality checks.

## Workflows

### 1. Python Linting (`lint.yml`)
Runs on every push and pull request to `main` and `develop` branches.

**Checks:**
- **flake8**: Python syntax errors and undefined names
- **black**: Code formatting consistency
- **isort**: Import statement organization
- **mypy**: Static type checking

**Local Usage:**
```bash
# Install linting tools
pip install flake8 black isort mypy

# Run checks
flake8 . --exclude=.git,__pycache__,.chainlit,venv,env
black --check .
isort --check-only .
mypy . --ignore-missing-imports
```

### 2. Python Tests (`test.yml`)
Runs on every push and pull request to `main` and `develop` branches.

**Features:**
- Tests against Python 3.10, 3.11, and 3.12
- Runs structure validation test
- Executes pytest with coverage reporting
- Uploads coverage to Codecov

**Local Usage:**
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov pytest-mock

# Run tests
python test_structure.py
pytest --verbose --cov=. --cov-report=term-missing
```

### 3. Security Checks (`security.yml`)
Runs on:
- Every push and pull request to `main` and `develop`
- Weekly schedule (Mondays at 9:00 AM UTC)

**Checks:**
- **safety**: Known vulnerabilities in dependencies
- **bandit**: Security issues in Python code
- **TruffleHog**: Secret scanning in git history

**Local Usage:**
```bash
# Install security tools
pip install safety bandit

# Run checks
safety check
bandit -r . --exclude ./.git,./venv,./env,./__pycache__,./.chainlit
```

### 4. Code Quality (`code-quality.yml`)
Runs on every push and pull request to `main` and `develop` branches.

**Metrics:**
- **radon**: Cyclomatic complexity and maintainability index
- **pylint**: Comprehensive code quality checks
- **grep**: TODO and FIXME tracking

**Local Usage:**
```bash
# Install quality tools
pip install radon pylint

# Run checks
radon cc . -a -nb
radon mi . -nb
pylint app.py test_structure.py
```

## GitHub Copilot Agents

This repository includes specialized Copilot agents in `.github/agents/`:

### 1. Code Reviewer (`code-reviewer.md`)
Expert in Python and AI chatbot application code review.

**Focus Areas:**
- Chainlit integration patterns
- OpenAI API usage and error handling
- Security (API keys, environment variables)
- Async/await patterns
- Test coverage

### 2. Test Engineer (`test-engineer.md`)
Specialist in Python testing and AI application testing.

**Focus Areas:**
- Unit and integration tests
- Mocking external dependencies
- Async function testing
- Chainlit component testing
- Edge case and error scenario testing

### 3. Documentation Specialist (`documentation-specialist.md`)
Expert in technical documentation and user guides.

**Focus Areas:**
- Setup instructions
- API documentation
- Architecture explanations
- Code comments and docstrings
- Contributing guidelines

## CI/CD Best Practices

### For Contributors

1. **Before Pushing Code:**
   ```bash
   # Run all checks locally
   black .
   isort .
   flake8 .
   python test_structure.py
   pytest
   ```

2. **Writing Tests:**
   - Add tests for new features
   - Mock external API calls (OpenAI)
   - Ensure tests are isolated and deterministic
   - Follow existing test patterns

3. **Code Quality:**
   - Keep functions small and focused
   - Add docstrings for public functions
   - Handle errors gracefully
   - Secure API keys in environment variables

### CI Workflow Status

Add badges to README to show workflow status:

```markdown
![Python Linting](https://github.com/ianlintner/chainlit_sandbox/workflows/Python%20Linting/badge.svg)
![Python Tests](https://github.com/ianlintner/chainlit_sandbox/workflows/Python%20Tests/badge.svg)
![Security Checks](https://github.com/ianlintner/chainlit_sandbox/workflows/Security%20Checks/badge.svg)
![Code Quality](https://github.com/ianlintner/chainlit_sandbox/workflows/Code%20Quality/badge.svg)
```

## Configuration Files

- **`pyproject.toml`**: Configuration for pytest, coverage, black, isort, and mypy
- **`.github/workflows/`**: CI/CD workflow definitions
- **`.github/agents/`**: GitHub Copilot agent configurations

## Troubleshooting

### Failed Linting
If linting fails, run locally and fix issues:
```bash
black . --exclude='/(\.git|__pycache__|\.chainlit|venv|env)/'
isort .
```

### Failed Tests
Check test output for specific failures:
```bash
pytest -v --tb=short
```

### Security Alerts
Review bandit report and address high-severity issues:
```bash
bandit -r . -ll
```

## Adding New Workflows

1. Create a new `.yml` file in `.github/workflows/`
2. Define triggers (push, pull_request, schedule)
3. Add jobs with appropriate steps
4. Test locally before committing
5. Document in this file

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Agents](https://github.com/features/copilot)
- [pytest Documentation](https://docs.pytest.org/)
- [flake8 Rules](https://flake8.pycqa.org/en/latest/user/error-codes.html)
