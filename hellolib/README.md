# Hellolib

A simple Python package for hellolib messages.

## Usage

```bash
# Create environment:
python -m venv .venv       # Or: python3 -m venv .venv

# Activate environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package in development mode
pip install -e .

# Install Development Dependencies
python -m pip install --upgrade pip
pip install build pytest pytest-cov

# Running tests
pytes

# Building:
python -m build

# Checking (without installation)
python -c "from hellolib.hello import say_hello; print(say_hello('Python Wheel'))"

# Installation
pip install ./dist/hellolib-0.1.0-py3-none-any.whl
```
