"""Simple greeting library."""

try:
    from importlib.metadata import version, PackageNotFoundError
    __version__ = version(__name__)
except (ImportError, PackageNotFoundError):
    __version__ = "unknown"

from hellolib.hello import (
    say_hello,
    say_goodbye,
    greet_multiple,
    format_greeting,
)

# Define public interface
__all__ = [
    "__version__",
    "say_hello",
    "say_goodbye",
    "greet_multiple",
    "format_greeting",
]
