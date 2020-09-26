import re
import shlex

from lxml.etree import Element
from lxml.etree import SubElement

from xapiparser.exception import ParseError
from xapiparser.exception import UnsupportedError

COMMANDS = ('xCommand', 'xStatus', 'xConfiguration')
UNSUPPORTED = ('xGetxml', 'xEvent')
SSH_ONLY = ('Systemtools', 'Log', 'xPreferences', 'xFeedback', 'Echo')
INDEXED_TAG = r"\[(\d+)\]$"


def _rejoin(expr):
    return " ".join(expr)


def parse(expression):
    return _XApiParser.parse(expression)


class _XApiParser:

    @staticmethod
    def parse(expression, root=None, current=None):
        try:
            expr = shlex.split(expression)

            # base case
            if root is None:
                if expr[0].lower() in [u.lower() for u in SSH_ONLY]:
                    raise UnsupportedError('CLI expression is not supported in REST API')
                if expr[0].lower() in [u.lower() for u in UNSUPPORTED]:
                    raise UnsupportedError('Expression is not currently supported by xapiparser')
                if expr[0].lower() not in [c.lower() for c in COMMANDS]:
                    raise ParseError(f"Unknown command: {expr[0]}")
                root = Element(expr[0][1:])
                return _XApiParser.parse(_rejoin(expr[1:]), root=root, current=root)

            # exit case: end of expression reached
            elif not expr:
                return root

            # case: sub-element with text
            elif expr[0][-1] == ":":
                # [indexed] tag with value and trailing colon
                if re.search(INDEXED_TAG, expr[0][:-1]):
                    tag = expr[0][:-1].split("[")[0]
                    child = SubElement(current, tag)
                    val = re.search(INDEXED_TAG, expr[0][:-1]).group(1)
                    child.set("item", val)
                    child.text = expr[1]
                    return _XApiParser.parse(_rejoin(expr[2:]), root=root, current=current)
                # only trailing colon
                else:
                    child = SubElement(current, expr[0][:-1])
                    child.text = expr[1]
                    return _XApiParser.parse(_rejoin(expr[2:]), root=root, current=current)

            # case: [indexed] tag with value
            elif re.search(INDEXED_TAG, expr[0]):
                tag = expr[0].split("[")[0]
                child = SubElement(current, tag)
                val = re.search(INDEXED_TAG, expr[0]).group(1)
                child.set("item", val)
                child.text = expr[1]
                return _XApiParser.parse(_rejoin(expr[2:]), root=root, current=child)

            # case: index as next element and subsequent values are provided
            elif expr[1].isdigit() and expr[2]:
                child = SubElement(current, expr[0])
                child.set("item", expr[1])
                return _XApiParser.parse(_rejoin(expr[2:]), root=root, current=child)

            # case: basic child element
            else:
                child = SubElement(current, expr[0])
                return _XApiParser.parse(_rejoin(expr[1:]), root=root, current=child)

        except Exception:
            raise ParseError("Parsing failed")
