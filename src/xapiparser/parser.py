import re
import shlex
from typing import List
from typing import Union

from lxml.etree import Element
from lxml.etree import SubElement

from xapiparser.exception import ParseError
from xapiparser.exception import UnsupportedError

COMMANDS = ('xCommand', 'xStatus', 'xConfiguration')
UNSUPPORTED = ('xGetxml', 'xEvent')
SSH_ONLY = ('Systemtools', 'Log', 'xPreferences', 'xFeedback', 'Echo')
INDEXED_TAG = r"\[(\d+)\]$"


def _rejoin(expr: List) -> str:
    return " ".join(expr)


def parse(cmd: str) -> Element:
    expr = shlex.split(cmd)
    return _XApiParser.parse(expr)


class _XApiParser:

    @staticmethod
    def parse(expr: List, root: Element = None, current: Union[Element, SubElement] = None) -> Element:
        try:
            # base case
            if root is None:
                if expr[0].lower() in [u.lower() for u in SSH_ONLY]:
                    raise UnsupportedError('CLI cmd is not supported in REST API')
                if expr[0].lower() in [u.lower() for u in UNSUPPORTED]:
                    raise NotImplementedError('cmd is not currently supported by xapiparser lib')
                if expr[0].lower() not in [c.lower() for c in COMMANDS]:
                    raise ParseError(f"Unknown command: {expr[0]}")
                root = Element(expr[0][1:])
                return _XApiParser.parse(expr[1:], root=root, current=root)

            # exit case: end of cmd reached
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
                    return _XApiParser.parse(expr[2:], root=root, current=current)
                # only trailing colon
                else:
                    child = SubElement(current, expr[0][:-1])
                    child.text = expr[1]
                    return _XApiParser.parse(expr[2:], root=root, current=current)

            # case: [indexed] tag with value
            elif re.search(INDEXED_TAG, expr[0]):
                tag = expr[0].split("[")[0]
                child = SubElement(current, tag)
                val = re.search(INDEXED_TAG, expr[0]).group(1)
                child.set("item", val)
                child.text = expr[1]
                return _XApiParser.parse(expr[2:], root=root, current=child)

            # case: final element
            elif len(expr) == 1:
                child = SubElement(current, expr[0])
                return _XApiParser.parse(expr[1:], root=root, current=child)

            # case: index as next element and subsequent values are provided
            elif expr[1].isdigit() and len(expr) > 2:
                child = SubElement(current, expr[0])
                child.set("item", expr[1])
                return _XApiParser.parse(expr[2:], root=root, current=child)

            # case: child element exists
            else:
                child = SubElement(current, expr[0])
                return _XApiParser.parse(expr[1:], root=root, current=child)

        except NotImplementedError as nie:
            raise nie
        except UnsupportedError as ue:
            raise ue
        except Exception:
            raise ParseError("Parsing failed")
