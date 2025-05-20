"""Hellolib functions."""

def say_hello(name="World"):
    """Return a hellolib message.
    Args:
        name (str, optional): Name to greet. Defaults to "World".
    Returns:
        str: Hellolib message
    """
    return f"Hello, {name}!"

def say_goodbye(name="World"):
    """Return a goodbye message.
    Args:
        name (str, optional): Name to say goodbye to. Defaults to "World".
    Returns:
        str: Goodbye message
    """
    return f"Goodbye, {name}!"
