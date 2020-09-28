import argparse

import lxml.etree as etree

from xapiparser import __version__
from xapiparser import parse

parser = argparse.ArgumentParser(description='xAPI ssh command parser.')
parser.add_argument('command', metavar='command', nargs=1,
                    help="xAPI ssh command")
parser.add_argument('--version', action='version',
                    version='%(prog)s v{version}'.format(version=__version__))


def main(args=None):
    args = parser.parse_args(args=args)
    print(etree.tostring(parse(args.command[0]), pretty_print=True, encoding='unicode'))
