"""Simple greeting library."""

try:
    from importlib.metadata import version, PackageNotFoundError
    __version__ = version(__name__)
except (ImportError, PackageNotFoundError):
    __version__ = "unknown"

# Define public interface
__all__ = ["__version__"]
