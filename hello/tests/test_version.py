"""Test version information."""

import subprocess
import sys
from hello import __version__


def test_version_exists():
    """Test that version can be imported."""
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert __version__ != "unknown"


def test_version_format():
    """Test version follows semantic versioning."""
    parts = __version__.split(".")
    assert len(parts) >= 2, "Version should have at least major.minor"
    assert all(part.isdigit() for part in parts), "Version parts should be numeric"


def test_cli_version_flag():
    """Test that CLI --version flag works."""
    result = subprocess.run(
        ["hello", "--version"],
        capture_output=True,
        text=True,
        check=False
    )

    # Check command succeeded
    assert result.returncode == 0, f"CLI failed with: {result.stderr}"

    # Check output contains version
    output = result.stdout.strip()
    assert "hello" in output.lower(), f"Expected 'hello' in output: {output}"
    assert __version__ in output, f"Expected version {__version__} in output: {output}"


def test_cli_version_shorthand():
    """Test that CLI -v flag works."""
    result = subprocess.run(
        ["hello", "-v"],
        capture_output=True,
        text=True,
        check=False
    )

    # Check command succeeded
    assert result.returncode == 0, f"CLI failed with: {result.stderr}"

    # Check output contains version
    output = result.stdout.strip()
    assert __version__ in output, f"Expected version {__version__} in output: {output}"


def test_cli_module_version():
    """Test running CLI as module with --version."""
    result = subprocess.run(
        [sys.executable, "-m", "hello.cli", "--version"],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode == 0, f"CLI module failed with: {result.stderr}"
    output = result.stdout.strip()
    assert __version__ in output, f"Expected version {__version__} in output: {output}"
