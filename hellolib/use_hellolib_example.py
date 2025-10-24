#!/usr/bin/env python3
"""Example usage of hellolib package."""

from hellolib.hello import say_hello, say_goodbye

# Default greeting
print(say_hello())  # Outputs: Hello, World!

# Custom greeting
print(say_hello("Python"))  # Outputs: Hello, Python!

# Goodbye message
print(say_goodbye("Friend"))  # Outputs: Goodbye, Friend!
