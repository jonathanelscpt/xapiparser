import argparse

import lxml.etree as etree

from xapiparser import __version__
from xapiparser import parse

parser = argparse.ArgumentParser(description='xAPI ssh expression parser.')
parser.add_argument('expression', metavar='expression', nargs='?',
                    help="xAPI ssh expression")
parser.add_argument('--version', action='version',
                    version='%(prog)s v{version}'.format(version=__version__))


def main(args=None):
    args = parser.parse_args(args=args)
    if not args.expression:
        parser.error("Error.  No xAPI ssh expression supplied.")
    print(etree.tostring(parse(args.expression), pretty_print=True, encoding='unicode'))
