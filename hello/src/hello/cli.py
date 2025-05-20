"""Command-line interface for the hello package."""

import sys
import argparse
from hello.handlers.hi_handler import handle_hi
from hello.handlers.bay_handler import handle_bay
from hello.handlers.default_handler import handle_default

def main():
    """Execute the CLI application.

    Parses command line arguments and calls the appropriate handler.
    """
    parser = argparse.ArgumentParser(description='CLI greeting application')
    parser.add_argument('command', nargs='?', default='default',
                        help='Command to execute (hi, bay, or any other text)')

    args = parser.parse_args()

    # Map commands to their handlers
    handlers = {
        'hi': handle_hi,
        'bay': handle_bay,
    }

    # Get the appropriate handler or use the default
    handler = handlers.get(args.command, handle_default)

    # Execute the handler
    print(handler())

    return 0

if __name__ == "__main__":
    sys.exit(main())
