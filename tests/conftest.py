import lxml.etree as etree
import pytest


@pytest.fixture
def strip_whitespace():
    return etree.XMLParser(remove_blank_text=True)
