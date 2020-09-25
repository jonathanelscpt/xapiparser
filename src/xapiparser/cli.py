import argparse
import sys

from xapiparser import __version__
from xapiparser import parse

parser = argparse.ArgumentParser(description='xAPI ssh expression parser.')
parser.add_argument('expression', metavar='expression', nargs=argparse.ZERO_OR_MORE,
                    help="xAPI ssh expression")
parser.add_argument('--version', metavar='version', action="store_true",
                    help="version")


def main(args=None):
    args = parser.parse_args(args=args)
    if args.version:
        print(f"version: {__version__}")
        sys.exit()
    print(parse(args.expression))
