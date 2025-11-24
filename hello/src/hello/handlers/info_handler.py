"""Handler demonstrating advanced Python 3.10+ features.

This handler showcases structural pattern matching capabilities
introduced in Python 3.10 (PEP 634).
"""


def handle_info(args: list[str] | None = None) -> str:
    """Process info command with structural pattern matching.

    Demonstrates Python 3.10+ features:
    - Union types with | operator (PEP 604)
    - Built-in generics like list[str] (PEP 585)
    - Structural pattern matching (PEP 634)

    Args:
        args: List of arguments to process. Defaults to None.

    Returns:
        Information message based on the arguments

    Examples:
        >>> handle_info(None)
        'No information requested'
        >>> handle_info([])
        'No information requested'
        >>> handle_info(['version'])
        'Version: 1.0.0'
        >>> handle_info(['python'])
        'Python: 3.10+'
        >>> handle_info(['author', 'email'])
        'Contact: author at email'
    """
    match args:
        # Match None or empty list
        case None | []:
            return "No information requested"

        # Match single item patterns
        case ["version"]:
            return "Version: 1.0.0"

        case ["python"]:
            return "Python: 3.10+"

        case ["help"]:
            return "Available info: version, python, author, help"

        # Match two items for contact info
        case ["author", email]:
            return f"Contact: author at {email}"

        # Match list with specific first element
        case ["config", *rest]:
            config_items = ", ".join(rest) if rest else "none"
            return f"Configuration: {config_items}"

        # Catch-all with guard (if clause)
        case [first, *_] if len(args) > 3:
            return f"Too many arguments (got {len(args)}, expected ≤ 3)"

        # Final catch-all
        case _:
            items = ", ".join(args) if isinstance(args, list) else str(args)
            return f"Unknown info request: {items}"
