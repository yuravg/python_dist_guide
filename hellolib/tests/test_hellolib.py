"""Tests for the hellolib package."""

import unittest
from hellolib.hello import say_hello, say_goodbye


class TestHellolib(unittest.TestCase):
    """Test case for hellolib functions."""

    def test_say_hello_default(self):
        """Test say_hello with default arguments."""
        self.assertEqual(say_hello(), "Hello, World!")

    def test_say_hello_custom(self):
        """Test say_hello with custom name."""
        self.assertEqual(say_hello("Python"), "Hello, Python!")

    def test_say_hello_empty_string(self):
        """Test say_hello with empty string."""
        self.assertEqual(say_hello(""), "Hello, !")

    def test_say_goodbye_default(self):
        """Test say_goodbye with default arguments."""
        self.assertEqual(say_goodbye(), "Goodbye, World!")

    def test_say_goodbye_custom(self):
        """Test say_goodbye with custom name."""
        self.assertEqual(say_goodbye("Python"), "Goodbye, Python!")

    def test_return_types(self):
        """Test that functions return strings."""
        self.assertIsInstance(say_hello(), str)
        self.assertIsInstance(say_goodbye(), str)


if __name__ == "__main__":
    unittest.main()
