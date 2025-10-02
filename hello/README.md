# Hello

A simple Python CLI package for greeting commands.

## Installation (system-wide)

```bash
pipx install hello
```

## Usage

After installation, you can use the package from the command line:

```bash
hello hi         # Outputs: Hello
hello bay        # Outputs: Good-bay
hello anything   # Outputs: Have a nice day
hello --help     # Shows help information
```

## Development

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
python -m unittest discover  # Or: pytes

# Building:
python -m build
```
