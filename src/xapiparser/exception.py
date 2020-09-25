class ParseError(ValueError):
    """Parsing error"""


class UnsupportedError(ValueError):
    """SSH commands that don't have api equivalent"""
