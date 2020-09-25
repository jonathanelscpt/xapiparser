import lxml.etree as etree
import pytest

from xapiparser import parse


@pytest.fixture
def strip_whitespace():
    return etree.XMLParser(remove_blank_text=True)


def test_basic(strip_whitespace):
    expression = 'xCommand Audio Volume Set Level: 50'
    xapi = """
    <Command>
        <Audio>
            <Volume>
                <Set>
                    <Level>50</Level>
                </Set>
            </Volume>
        </Audio>
    </Command>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(expression)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_item_attribute(strip_whitespace):
    expression = "xConfiguration Video Input Connector 2 InputSourceType: camera"
    xapi = """
    <Configuration>
        <Video>
            <Input>
                <Connector item="2">
                    <InputSourceType>camera</InputSourceType>
                </Connector>
            </Input>
        </Video>
    </Configuration>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(expression)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_key_value(strip_whitespace):
    expression = 'xCommand Dial Number: "12345" Protocol: H323'
    xapi = """
    <Command>
        <Dial>
            <Number>12345</Number>
            <Protocol>H323</Protocol>
        </Dial>
    </Command>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(expression)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_attribute_suffix_with_value(strip_whitespace):
    expression = 'xCommand HttpFeedback Register FeedbackSlot: 2 ServerUrl: https://status.oops.com/ Format: JSON ' \
                 'Expression[1]: /Event/UserInterface/Message/Prompt/Response ' \
                 'Expression[2]: /Event/UserInterface/Message/TextInput/Response/text ' \
                 'Expression[3]: /Event/CallDisconnect'
    xapi = """
    <Command>
        <HttpFeedback>
            <Register>
                <FeedbackSlot>2</FeedbackSlot>
                <ServerUrl>https://status.oops.com/</ServerUrl>
                <Format>JSON</Format>
                <Expression item="1">/Event/UserInterface/Message/Prompt/Response</Expression>
                <Expression item="2">/Event/UserInterface/Message/TextInput/Response/text</Expression>
                <Expression item="3">/Event/CallDisconnect</Expression>
            </Register>
        </HttpFeedback>
    </Command>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(expression)
    assert etree.tostring(expected) == etree.tostring(parsed)
