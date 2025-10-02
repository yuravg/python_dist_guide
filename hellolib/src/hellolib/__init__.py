"""Simple hellolib package."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("hellolib")
except PackageNotFoundError:
    __version__ = "unknown"

# Define public interface
__all__ = ["__version__"]
