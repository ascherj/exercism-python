# Exercism Python Track

This repository contains solutions to Exercism Python track exercises.

## Setup

This project uses `uv` for dependency management.

### Dependencies

- pytest - Testing framework
- pytest-cache - Caching plugin for pytest
- pytest-subtests - Subtest support for pytest
- pytest-pylint - Pylint integration for pytest

### Running Tests

```bash
# Run tests for a specific exercise
uv run pytest <exercise-name>/

# Run tests with pylint checks
uv run pytest --pylint

# Run all tests
uv run pytest
```

### Environment

To activate the virtual environment:
```bash
source .venv/bin/activate
```

## Exercises

Each exercise is in its own directory with:
- Implementation file (e.g., `leap.py`)
- Test file (e.g., `leap_test.py`)
- README with exercise instructions