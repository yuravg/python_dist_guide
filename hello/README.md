# Hello

A simple Python CLI application for greeting commands.

## Installation

### System-wide Installation (Recommended for CLI tools)
```bash
pipx install hello
```

### Regular Installation
```bash
pip install hello
```

## Usage

After installation, you can use the package from the command line:
```bash
hello hi         # Outputs: Hello
hello bay        # Outputs: Good-bay
hello anything   # Outputs: Have a nice day
hello --version  # Shows version information
hello --help     # Shows help information
```

## Development

```bash
# Create and activate environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run all tests
pytest

# Run tests with coverage
pytest --cov=hello --cov-report=html

# Run specific test
pytest tests/test_hello.py -v

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build distribution
python -m build

# Clean up
deactivate
rm -rf .venv
```

## Testing the Built Package

###  Test environment
```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the wheel
pip install ./dist/hello-1.0.0-py3-none-any.whl

# Test commands
hello hi
hello bay
hello --version

# Clean up
deactivate
rm -rf test_env
```

### System-wide Installation
```bash
# Install with pipx for testing
pipx install ./dist/hello-1.0.0-py3-none-any.whl

# Test commands
hello hi
hello bay
hello --version

# Uninstall
pipx uninstall hello
```
