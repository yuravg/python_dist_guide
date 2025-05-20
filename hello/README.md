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
python -m venv myenv

# Activate environment
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Building:
python -m build

# Install the package in development mode
pip install -e .

# Running tests
python -m unittest discover
```
