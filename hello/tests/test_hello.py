"""Tests for the hello package."""

import unittest
import io
import sys
from unittest.mock import patch
from hello.cli import main
from hello.handlers.hi_handler import handle_hi
from hello.handlers.bay_handler import handle_bay
from hello.handlers.default_handler import handle_default

class TestHandlers(unittest.TestCase):
    """Test case for handler functions."""

    def test_handle_hi(self):
        """Test the hi handler."""
        self.assertEqual(handle_hi(), "Hello")

    def test_handle_bay(self):
        """Test the bay handler."""
        self.assertEqual(handle_bay(), "Good-bay")

    def test_handle_default(self):
        """Test the default handler."""
        self.assertEqual(handle_default(), "Have a nice day")

class TestCLI(unittest.TestCase):
    """Test case for CLI functionality."""

    @patch('sys.argv', ['hello', 'hi'])
    def test_cli_hi(self):
        """Test CLI with 'hi' command."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello")

    @patch('sys.argv', ['hello', 'bay'])
    def test_cli_bay(self):
        """Test CLI with 'bay' command."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Good-bay")

    @patch('sys.argv', ['hello', 'unknown'])
    def test_cli_default(self):
        """Test CLI with an unknown command."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Have a nice day")

if __name__ == "__main__":
    unittest.main()
