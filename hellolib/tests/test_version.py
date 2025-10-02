"""Test version information."""

from hellolib import __version__

def test_version_exists():
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert __version__ != "unknown"


def test_version_format():
    """Test version follows semantic versioning."""
    parts = __version__.split(".")
    assert len(parts) >= 2, "Version should have at least major.minor"
    assert all(part.isdigit() for part in parts), "Version parts should be numeric"
