# Contributing to Goal-Seeking AI Chatbot

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and considerate in all interactions. This is a parody project meant to be fun and educational.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- OpenAI API key (for running the chatbot)

### Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/chainlit_sandbox.git
   cd chainlit_sandbox
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Install runtime dependencies
   pip install -r requirements.txt
   
   # Install development dependencies
   pip install -r requirements-dev.txt
   ```

4. **Set Up Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

5. **Verify Installation**
   ```bash
   python test_structure.py
   pytest
   ```

## Development Workflow

### Before Making Changes

1. **Create a New Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Run Tests**
   ```bash
   python test_structure.py
   pytest -v
   ```

### Making Changes

1. **Write Code**
   - Follow PEP 8 style guidelines
   - Keep functions focused and small
   - Add docstrings to public functions
   - Handle errors gracefully

2. **Write Tests**
   - Add unit tests for new features
   - Maintain or improve code coverage
   - Mock external API calls
   - Test edge cases

3. **Format Code**
   ```bash
   # Auto-format with black
   black .
   
   # Sort imports
   isort .
   ```

4. **Run Linters**
   ```bash
   # Check for errors
   flake8 .
   
   # Type checking
   mypy . --ignore-missing-imports
   ```

5. **Run Tests**
   ```bash
   # Run all tests
   pytest -v
   
   # Run with coverage
   pytest --cov=. --cov-report=term-missing
   ```

### Committing Changes

1. **Stage Changes**
   ```bash
   git add .
   ```

2. **Commit with Descriptive Message**
   ```bash
   git commit -m "Add feature: brief description
   
   - Detailed point 1
   - Detailed point 2"
   ```

3. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

### Submitting a Pull Request

1. **Create Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

2. **PR Checklist**
   - [ ] Tests pass locally
   - [ ] Code is formatted (black, isort)
   - [ ] Linting passes (flake8)
   - [ ] New tests added for new features
   - [ ] Documentation updated if needed
   - [ ] PR description explains changes

3. **Respond to Feedback**
   - Address reviewer comments
   - Push additional commits as needed
   - Request re-review when ready

## Types of Contributions

### Bug Fixes
- Check existing issues or create a new one
- Include steps to reproduce
- Add tests that verify the fix

### New Features
- Open an issue to discuss the feature first
- Ensure it aligns with project goals
- Add comprehensive tests
- Update documentation

### Documentation
- Fix typos or unclear instructions
- Add examples or clarifications
- Update outdated information

### Tests
- Improve test coverage
- Add edge case tests
- Fix flaky tests

### Code Quality
- Refactor complex code
- Improve error handling
- Optimize performance

## Testing Guidelines

### Unit Tests
- Test individual functions in isolation
- Mock external dependencies (OpenAI API)
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

### Example Test
```python
def test_function_name_describes_scenario():
    # Arrange
    input_data = "test input"
    expected_output = "expected result"
    
    # Act
    actual_output = function_to_test(input_data)
    
    # Assert
    assert actual_output == expected_output
```

### Running Specific Tests
```bash
# Run specific test file
pytest tests/test_app.py -v

# Run specific test class
pytest tests/test_app.py::TestPromptStructure -v

# Run specific test
pytest tests/test_app.py::TestPromptStructure::test_system_prompt_exists -v
```

## Code Style

### Python Style Guide
- Follow PEP 8
- Maximum line length: 127 characters
- Use descriptive variable names
- Add type hints where helpful

### Naming Conventions
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Private: `_leading_underscore`

### Documentation
- Add docstrings to public functions
- Use Google-style docstrings
- Include examples for complex functions

### Example Docstring
```python
async def example_function(param1: str, param2: int) -> dict:
    """Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Dictionary containing result data
        
    Raises:
        ValueError: If param2 is negative
    """
    pass
```

## GitHub Copilot Agents

This repository uses specialized GitHub Copilot agents:

- **Code Reviewer**: Reviews code for quality, security, and best practices
- **Test Engineer**: Helps write comprehensive tests
- **Documentation Specialist**: Improves documentation clarity

These agents are configured in `.github/agents/` and can assist with development.

## CI/CD Workflows

All pull requests automatically run:

1. **Linting** (flake8, black, isort, mypy)
2. **Tests** (pytest across Python 3.10, 3.11, 3.12)
3. **Security Checks** (safety, bandit, TruffleHog)
4. **Code Quality** (radon, pylint)

Ensure all checks pass before requesting review.

## Project Structure

```
chainlit_sandbox/
├── .github/
│   ├── agents/              # Copilot agent configurations
│   ├── workflows/           # CI/CD workflows
│   └── README.md            # CI/CD documentation
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Unit tests
├── app.py                   # Main chatbot application
├── test_structure.py        # Structure validation
├── requirements.txt         # Runtime dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml          # Tool configurations
├── README.md               # User documentation
└── CONTRIBUTING.md         # This file
```

## Questions?

- Open an issue for questions about contributing
- Check existing issues and PRs for similar topics
- Review the [README](.github/README.md) for CI/CD details

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎮💰🚀
