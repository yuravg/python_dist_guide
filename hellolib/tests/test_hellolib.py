"""Tests for the hellolib package."""

from hellolib.hello import (
    say_hello,
    say_goodbye,
    greet_multiple,
    format_greeting,
)


def test_say_hello_default() -> None:
    """Test say_hello with default arguments."""
    assert say_hello() == "Hello, World!"


def test_say_hello_custom() -> None:
    """Test say_hello with custom name."""
    assert say_hello("Python") == "Hello, Python!"


def test_say_hello_empty_string() -> None:
    """Test say_hello with empty string."""
    assert say_hello("") == "Hello, !"


def test_say_goodbye_default() -> None:
    """Test say_goodbye with default arguments."""
    assert say_goodbye() == "Goodbye, World!"


def test_say_goodbye_custom() -> None:
    """Test say_goodbye with custom name."""
    assert say_goodbye("Python") == "Goodbye, Python!"


def test_return_types() -> None:
    """Test that functions return strings."""
    assert isinstance(say_hello(), str)
    assert isinstance(say_goodbye(), str)


# Tests for Python 3.10+ features
def test_greet_multiple_list() -> None:
    """Test greet_multiple with list (demonstrates list[str] type hint)."""
    result = greet_multiple(["Alice", "Bob"])
    assert result == ["Hello, Alice!", "Hello, Bob!"]


def test_greet_multiple_tuple() -> None:
    """Test greet_multiple with tuple (demonstrates tuple[str, ...] type hint)."""
    result = greet_multiple(("Charlie",))
    assert result == ["Hello, Charlie!"]


def test_greet_multiple_empty() -> None:
    """Test greet_multiple with empty list."""
    assert greet_multiple([]) == []


def test_greet_multiple_custom_greeting() -> None:
    """Test greet_multiple with custom greeting."""
    result = greet_multiple(["Dave"], greeting="Hi")
    assert result == ["Hi, Dave!"]


def test_format_greeting_default() -> None:
    """Test format_greeting with default style."""
    assert format_greeting("Alice") == "Hello, Alice!"


def test_format_greeting_formal() -> None:
    """Test format_greeting with formal style (demonstrates pattern matching)."""
    assert format_greeting("Bob", style="formal") == "Good day, Bob!"


def test_format_greeting_casual() -> None:
    """Test format_greeting with casual style (demonstrates pattern matching)."""
    assert format_greeting("Charlie", style="casual") == "Hey, Charlie!"


def test_format_greeting_custom_suffix() -> None:
    """Test format_greeting with custom suffix."""
    assert format_greeting("Dave", style="casual", suffix=".") == "Hey, Dave."


def test_format_greeting_unknown_style() -> None:
    """Test format_greeting with unknown style (demonstrates default case)."""
    assert format_greeting("Eve", style="unknown") == "Hello, Eve!"
