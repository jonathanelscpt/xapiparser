import lxml.etree as etree
import pytest

from xapiparser import parse
from xapiparser.cli import main
from xapiparser.exception import ParseError
from xapiparser.exception import UnsupportedError


def test_main(strip_whitespace):
    main(['xCommand Audio Volume Set Level: 50'])


def test_simple(strip_whitespace):
    cmd = 'xConfiguration Conference Encryption Mode'
    xapi = """
        <Configuration>
            <Conference>
                <Encryption>
                    <Mode></Mode>
                </Encryption>
            </Conference>
        </Configuration>
        """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_tag_val(strip_whitespace):
    cmd = 'xCommand Audio Volume Set Level: 50'
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
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_multiple_key_value(strip_whitespace):
    cmd = 'xCommand Dial Number: "12345" Protocol: H323'
    xapi = """
    <Command>
        <Dial>
            <Number>12345</Number>
            <Protocol>H323</Protocol>
        </Dial>
    </Command>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_item_attribute(strip_whitespace):
    cmd = "xConfiguration Video Input Connector 2 InputSourceType: camera"
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
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_attribute_suffixes(strip_whitespace):
    cmd = 'xCommand HttpFeedback Register FeedbackSlot: 2 ServerUrl: https://status.oops.com/ Format: JSON ' \
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
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_whitespace_attribute(strip_whitespace):
    cmd = "xConfiguration NetworkServices SNMP SystemContact: '43.51, 1.81'"
    xapi = """
    <Configuration>
        <NetworkServices>
            <SNMP>
                <SystemContact>43.51, 1.81</SystemContact>
            </SNMP>
        </NetworkServices>
    </Configuration>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_empty_attribute(strip_whitespace):
    cmd = 'xConfiguration Phonebook Server 1 URL: ""'
    xapi = """
            <Configuration>
                <Phonebook>
                    <Server item="1">
                        <URL></URL>
                    </Server>
                </Phonebook>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    # do not collapse empty tags to prevent false negative
    assert etree.tostring(expected, method="c14n") == etree.tostring(parsed, method="c14n")


def test_not_implemented_error():
    with pytest.raises(NotImplementedError):
        parse('xgetxml /Configuration/Video/Layout/Scaling | resultId="mytag _ 2"')


def test_unsupported__error_ssh_only_cmd():
    with pytest.raises(UnsupportedError):
        parse("systemtools license list")


def test_parse_error():
    with pytest.raises(ParseError):
        parse("not valid xapi ssh cmd")

def test_null_attribute(strip_whitespace):
    cmd = 'xConfiguration Phonebook Server 1 URL:'
    with pytest.raises(ParseError):
        parse(cmd)
