# Hellolib

A simple Python package for greeting messages.

## Installation
```bash
pip install hellolib
```

## Usage
```python
from hellolib.hello import say_hello, say_goodbye

print(say_hello())              # Hello, World!
print(say_hello("Python"))      # Hello, Python!
print(say_goodbye("Friend"))    # Goodbye, Friend!
```

## Development
```bash
# Create and activate environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=hellolib --cov-report=html

# Build distribution
python -m build

# Clean up
deactivate
rm -rf .venv
```

## Testing the Built Package
```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the wheel
pip install ./dist/hellolib-1.1.0-py3-none-any.whl

# Test it
python -c "from hellolib.hello import say_hello; print(say_hello('Wheel'))"

# Clean up
deactivate
rm -rf test_env
```
