"""Greeting functions demonstrating Python 3.10+ features."""


def say_hello(name: str = "World") -> str:
    """Return a greeting message.

    Args:
        name: Name to greet. Defaults to "World".

    Returns:
        Greeting message

    Examples:
        >>> say_hello()
        'Hello, World!'
        >>> say_hello("Python")
        'Hello, Python!'
    """
    return f"Hello, {name}!"


def say_goodbye(name: str = "World") -> str:
    """Return a goodbye message.

    Args:
        name: Name to say goodbye to. Defaults to "World".

    Returns:
        Goodbye message

    Examples:
        >>> say_goodbye()
        'Goodbye, World!'
        >>> say_goodbye("Python")
        'Goodbye, Python!'
    """
    return f"Goodbye, {name}!"


def greet_multiple(
    names: list[str] | tuple[str, ...],
    greeting: str = "Hello"
) -> list[str]:
    """Greet multiple people with modern type hints.

    Demonstrates Python 3.10+ features:
    - Union types with | operator (PEP 604)
    - Built-in generics like list[str], tuple[str, ...] (PEP 585)

    Args:
        names: List or tuple of names to greet
        greeting: Greeting word to use. Defaults to "Hello".

    Returns:
        List of greeting messages

    Examples:
        >>> greet_multiple(["Alice", "Bob"])
        ['Hello, Alice!', 'Hello, Bob!']
        >>> greet_multiple(("Charlie",), "Hi")
        ['Hi, Charlie!']
        >>> greet_multiple([])
        []
    """
    return [f"{greeting}, {name}!" for name in names]


def format_greeting(
    name: str,
    *,
    style: str | None = None,
    suffix: str = "!"
) -> str:
    """Format a greeting with various styles using pattern matching.

    Demonstrates Python 3.10+ features:
    - Union with None using | operator
    - Keyword-only arguments with *
    - Structural pattern matching (PEP 634)

    Args:
        name: Name to greet
        style: Greeting style ('formal', 'casual', or None for default)
        suffix: Punctuation to end with. Defaults to "!".

    Returns:
        Formatted greeting message

    Examples:
        >>> format_greeting("Alice")
        'Hello, Alice!'
        >>> format_greeting("Bob", style="formal")
        'Good day, Bob!'
        >>> format_greeting("Charlie", style="casual")
        'Hey, Charlie!'
        >>> format_greeting("Dave", style="casual", suffix=".")
        'Hey, Dave.'
    """
    match style:
        case "formal":
            greeting = "Good day"
        case "casual":
            greeting = "Hey"
        case None:
            greeting = "Hello"
        case _:
            greeting = "Hello"

    return f"{greeting}, {name}{suffix}"
