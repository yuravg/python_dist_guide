"""Command-line interface for the hello package."""

import sys
import argparse
from hello.handlers.hi_handler import handle_hi
from hello.handlers.bay_handler import handle_bay
from hello.handlers.default_handler import handle_default
from hello import __version__


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser.

    Returns:
        argparse.ArgumentParser: Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="hello",  # Use command name, not module name (__name__ would be "hello.cli")
        description="A simple greeting CLI application",
        epilog="Examples:\n"
               "  hello              # Default greeting\n"
               "  hello hi           # Say hello\n"
               "  hello bay          # Say goodbye\n"
               "  hello --version    # Show version",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show program version and exit"
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="default",
        help="Command to execute: 'hi', 'bay', or any other text for default message"
    )

    return parser


def main():
    """Main entry point for CLI.

    Returns:
        int: Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args()

    # Map commands to their handlers
    handlers = {
        "hi": handle_hi,
        "bay": handle_bay,
    }

    try:
        # Get the appropriate handler or use the default
        handler = handlers.get(args.command, handle_default)
        # Execute the handler and print result
        print(handler())
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
