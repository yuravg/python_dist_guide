"""Tests for the hello package."""

from unittest.mock import patch
import pytest
from hello.cli import main
from hello.handlers.hi_handler import handle_hi
from hello.handlers.bay_handler import handle_bay
from hello.handlers.default_handler import handle_default
from hello.handlers.info_handler import handle_info


def test_handle_hi() -> None:
    """Test the hi handler."""
    assert handle_hi() == "Hello"


def test_handle_bay() -> None:
    """Test the bay handler."""
    assert handle_bay() == "Good-bay"


def test_handle_default() -> None:
    """Test the default handler."""
    assert handle_default() == "Have a nice day"


@patch("sys.argv", ["hello", "hi"])
def test_cli_hi(capsys: pytest.CaptureFixture[str]) -> None:
    """Test CLI with 'hi' command."""
    result = main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello"
    assert result == 0


@patch("sys.argv", ["hello", "bay"])
def test_cli_bay(capsys: pytest.CaptureFixture[str]) -> None:
    """Test CLI with 'bay' command."""
    result = main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Good-bay"
    assert result == 0


@patch("sys.argv", ["hello", "unknown"])
def test_cli_default(capsys: pytest.CaptureFixture[str]) -> None:
    """Test CLI with an unknown command."""
    result = main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Have a nice day"
    assert result == 0


@patch("sys.argv", ["hello"])
def test_cli_no_command(capsys: pytest.CaptureFixture[str]) -> None:
    """Test CLI with no command (should use default)."""
    result = main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Have a nice day"
    assert result == 0


# Tests for info_handler demonstrating Python 3.10+ pattern matching
def test_info_handler_none() -> None:
    """Test info handler with None."""
    assert handle_info(None) == "No information requested"


def test_info_handler_empty() -> None:
    """Test info handler with empty list."""
    assert handle_info([]) == "No information requested"


def test_info_handler_version() -> None:
    """Test info handler requesting version."""
    assert handle_info(["version"]) == "Version: 1.0.0"


def test_info_handler_python() -> None:
    """Test info handler requesting Python version."""
    assert handle_info(["python"]) == "Python: 3.10+"


def test_info_handler_help() -> None:
    """Test info handler requesting help."""
    assert handle_info(["help"]) == "Available info: version, python, author, help"


def test_info_handler_author() -> None:
    """Test info handler with author contact (demonstrates pattern with capture)."""
    result = handle_info(["author", "test@example.com"])
    assert result == "Contact: author at test@example.com"


def test_info_handler_config() -> None:
    """Test info handler with config (demonstrates wildcard pattern)."""
    result = handle_info(["config", "debug", "verbose"])
    assert result == "Configuration: debug, verbose"


def test_info_handler_config_empty() -> None:
    """Test info handler with config but no items."""
    result = handle_info(["config"])
    assert result == "Configuration: none"


def test_info_handler_too_many_args() -> None:
    """Test info handler with too many arguments (demonstrates guard clause)."""
    result = handle_info(["a", "b", "c", "d"])
    assert result == "Too many arguments (got 4, expected ≤ 3)"


def test_info_handler_unknown() -> None:
    """Test info handler with unknown request (demonstrates catch-all)."""
    result = handle_info(["unknown", "request"])
    assert result == "Unknown info request: unknown, request"
