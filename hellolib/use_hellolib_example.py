#!/usr/bin/env python3

from hellolib.hello import say_hello;

# Default hellolib
print(say_hello());  # Outputs: Hello, World!

# Custom hellolib
print(say_hello("Python"));  # Outputs: Hello, Python!

# For goodbye messages
from hellolib.hello import say_goodbye
print(say_goodbye("Friend"));  # Outputs: Goodbye, Friend!
