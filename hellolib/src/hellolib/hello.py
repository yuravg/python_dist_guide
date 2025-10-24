"""Greeting functions."""


def say_hello(name="World"):
    """Return a greeting message.

    Args:
        name (str, optional): Name to greet. Defaults to "World".

    Returns:
        str: Greeting message

    Examples:
        >>> say_hello()
        'Hello, World!'
        >>> say_hello("Python")
        'Hello, Python!'
    """
    return f"Hello, {name}!"


def say_goodbye(name="World"):
    """Return a goodbye message.

    Args:
        name (str, optional): Name to say goodbye to. Defaults to "World".

    Returns:
        str: Goodbye message

    Examples:
        >>> say_goodbye()
        'Goodbye, World!'
        >>> say_goodbye("Python")
        'Goodbye, Python!'
    """
    return f"Goodbye, {name}!"
