import argparse
import sys

import lxml.etree as etree

from xapiparser import __version__
from xapiparser import parse

parser = argparse.ArgumentParser(description='xAPI ssh expression parser.')
parser.add_argument('expression', metavar='expression', nargs='?',
                    help="xAPI ssh expression")
parser.add_argument('--version', action="store_true",
                    help="version")


def main(args=None):
    args = parser.parse_args(args=args)
    if args.version:
        print(f"version: {__version__}")
        sys.exit()
    if not args.expression:
        print("Error.  No xAPI ssh expression supplied.")
        sys.exit(1)
    print(etree.tostring(parse(args.expression[0]), pretty_print=True, encoding='unicode'))
