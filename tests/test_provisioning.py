import lxml.etree as etree
import pytest

from xapiparser import parse


def test_conf_ipstack(strip_whitespace):
    cmd = 'xConfiguration Conference 1 CallProtocolIPStack: IPv4'
    xapi = """
    <Configuration>
        <Conference item="1">
            <CallProtocolIPStack>IPv4</CallProtocolIPStack>
        </Conference>
    </Configuration>
    """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_autoanswer_mode(strip_whitespace):
    cmd = 'xConfiguration Conference 1 AutoAnswer Mode: ON'
    xapi = """
        <Configuration>
            <Conference item="1">
                <AutoAnswer>
                    <Mode>ON</Mode>
                </AutoAnswer>
            </Conference>
        </Configuration>
        """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_autoanswer_mute(strip_whitespace):
    cmd = 'xConfiguration Conference 1 AutoAnswer Mute: ON'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <AutoAnswer>
                        <Mute>ON</Mute>
                    </AutoAnswer>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_autoanswer_fecc(strip_whitespace):
    cmd = 'xConfiguration Conference 1 FarEndControl Mode: OFF'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <FarEndControl>
                        <Mode>OFF</Mode>
                    </FarEndControl>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_autoanswer_encryption(strip_whitespace):
    cmd = 'xConfiguration Conference 1 Encryption Mode: BestEffort'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <Encryption>
                        <Mode>BestEffort</Mode>
                    </Encryption>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_call_protocol(strip_whitespace):
    cmd = 'xConfiguration Conference 1 DefaultCall Protocol: H323'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <DefaultCall>
                        <Protocol>H323</Protocol>
                    </DefaultCall>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_call_rate(strip_whitespace):
    cmd = 'xConfiguration Conference 1 DefaultCall Rate: 1152'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <DefaultCall>
                        <Rate>1152</Rate>
                    </DefaultCall>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_video_bw_mode(strip_whitespace):
    cmd = 'xConfiguration Conference 1 VideoBandwidth Mode: Dynamic'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <VideoBandwidth>
                        <Mode>Dynamic</Mode>
                    </VideoBandwidth>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_conf_video_bw_pchan(strip_whitespace):
    cmd = 'xConfiguration Conference 1 VideoBandwidth PresentationChannel Weight: 5'
    xapi = """
            <Configuration>
                <Conference item="1">
                    <VideoBandwidth>
                        <PresentationChannel>
                            <Weight>5</Weight>
                        </PresentationChannel>
                    </VideoBandwidth>
                </Conference>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_h323_mode(strip_whitespace):
    cmd = 'xConfiguration H323 Profile 1 CallSetup Mode: Gatekeeper '
    xapi = """
            <Configuration>
                <H323>
                    <Profile item="1">
                        <CallSetup>
                            <Mode>Gatekeeper</Mode>
                        </CallSetup>
                    </Profile>
                </H323>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_h323_gk_discovery(strip_whitespace):
    cmd = 'xConfiguration H323 Profile 1 Gatekeeper Discovery: Manual'
    xapi = """
            <Configuration>
                <H323>
                    <Profile item="1">
                        <Gatekeeper>
                            <Discovery>Manual</Discovery>
                        </Gatekeeper>
                    </Profile>
                </H323>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_h323_gk_addr(strip_whitespace):
    cmd = 'xConfiguration H323 Profile 1 Gatekeeper Address: vcs.sample.lab'
    xapi = """
            <Configuration>
                <H323>
                    <Profile item="1">
                        <Gatekeeper>
                            <Address>vcs.sample.lab</Address>
                        </Gatekeeper>
                    </Profile>
                </H323>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_h323_alias(strip_whitespace):
    cmd = 'xConfiguration H323 Profile 1 H323Alias E164: ""'
    xapi = """
            <Configuration>
                <H323>
                    <Profile item="1">
                        <H323Alias>
                            <E164></E164>
                        </H323Alias>
                    </Profile>
                </H323>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    # do not collapse empty tags to prevent false negative
    assert etree.tostring(expected, method="c14n") == etree.tostring(parsed, method="c14n")


def test_h323_port_allocation(strip_whitespace):
    cmd = 'xConfiguration H323 Profile 1 PortAllocation: Static'
    xapi = """
            <Configuration>
                <H323>
                    <Profile item="1">
                        <PortAllocation>Static</PortAllocation>
                    </Profile>
                </H323>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_ipv4(strip_whitespace):
    cmd = 'xConfiguration Network 1 IPv4 Assignment: DHCP'
    xapi = """
            <Configuration>
                <Network item="1">
                    <IPv4>
                        <Assignment>DHCP</Assignment>
                    </IPv4>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_qos_mode(strip_whitespace):
    cmd = 'xConfiguration Network 1 QoS Mode: Diffserv'
    xapi = """
            <Configuration>
                <Network item="1">
                    <QoS>
                        <Mode>Diffserv</Mode>
                    </QoS>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_qos_ds_audio(strip_whitespace):
    cmd = 'xConfiguration Network 1 QoS Diffserv Audio: 46'
    xapi = """
            <Configuration>
                <Network item="1">
                    <QoS>
                        <Diffserv>
                            <Audio>46</Audio>
                        </Diffserv>
                    </QoS>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_qos_ds_video(strip_whitespace):
    cmd = 'xConfiguration Network 1 QoS Diffserv Video: 34'
    xapi = """
            <Configuration>
                <Network item="1">
                    <QoS>
                        <Diffserv>
                            <Video>34</Video>
                        </Diffserv>
                    </QoS>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_qos_ds_data(strip_whitespace):
    cmd = 'xConfiguration Network 1 QoS Diffserv Data: 22'
    xapi = """
            <Configuration>
                <Network item="1">
                    <QoS>
                        <Diffserv>
                            <Data>22</Data>
                        </Diffserv>
                    </QoS>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_qos_ds_sig(strip_whitespace):
    cmd = 'xConfiguration Network 1 QoS Diffserv Signalling: 40'
    xapi = """
            <Configuration>
                <Network item="1">
                    <QoS>
                        <Diffserv>
                            <Signalling>40</Signalling>
                        </Diffserv>
                    </QoS>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_8021x_mode(strip_whitespace):
    cmd = 'xConfiguration Network 1 IEEE8021X Mode: Off'
    xapi = """
            <Configuration>
                <Network item="1">
                    <IEEE8021X>
                        <Mode>Off</Mode>
                    </IEEE8021X>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_8021x_tls(strip_whitespace):
    cmd = 'xConfiguration Network 1 IEEE8021X TlsVerify: Off'
    xapi = """
            <Configuration>
                <Network item="1">
                    <IEEE8021X>
                        <TlsVerify>Off</TlsVerify>
                    </IEEE8021X>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_net_8021x_use_cert(strip_whitespace):
    cmd = 'xConfiguration Network 1 IEEE8021X UseClientCertificate: Off'
    xapi = """
            <Configuration>
                <Network item="1">
                    <IEEE8021X>
                        <UseClientCertificate>Off</UseClientCertificate>
                    </IEEE8021X>
                </Network>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_h323_mode(strip_whitespace):
    cmd = 'xConfiguration NetworkServices H323 Mode: On'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <H323>
                        <Mode>On</Mode>
                    </H323>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_http_mode(strip_whitespace):
    cmd = 'xConfiguration NetworkServices HTTP Mode: On'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <HTTP>
                        <Mode>On</Mode>
                    </HTTP>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_https_mode(strip_whitespace):
    cmd = 'xConfiguration NetworkServices HTTPS Mode: On'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <HTTPS>
                        <Mode>On</Mode>
                    </HTTPS>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_sip_mode(strip_whitespace):
    cmd = 'xConfiguration NetworkServices SIP Mode: Off'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <SIP>
                        <Mode>Off</Mode>
                    </SIP>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_ntp_mode(strip_whitespace):
    cmd = 'xConfiguration NetworkServices NTP Mode: Manual'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <NTP>
                        <Mode>Manual</Mode>
                    </NTP>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_netserv_ntp_addr(strip_whitespace):
    cmd = 'xConfiguration NetworkServices NTP Address: ""'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <NTP>
                        <Address></Address>
                    </NTP>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    # do not collapse empty tags to prevent false negative
    assert etree.tostring(expected, method="c14n") == etree.tostring(parsed, method="c14n")


def test_netserv_snmp_host(strip_whitespace):
    cmd = 'xConfiguration NetworkServices SNMP Host 1 Address: tms.sample.lab'
    xapi = """
            <Configuration>
                <NetworkServices>
                    <SNMP>
                        <Host item="1">
                            <Address>tms.sample.lab</Address>
                        </Host>
                    </SNMP>
                </NetworkServices>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_phonebook_server(strip_whitespace):
    cmd = 'xConfiguration Phonebook Server 1 ID: default'
    xapi = """
            <Configuration>
                <Phonebook>
                    <Server item="1">
                        <ID>default</ID>
                    </Server>
                </Phonebook>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_phonebook_server_type(strip_whitespace):
    cmd = 'xConfiguration Phonebook Server 1 Type: TMS'
    xapi = """
            <Configuration>
                <Phonebook>
                    <Server item="1">
                        <Type>TMS</Type>
                    </Server>
                </Phonebook>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_phonebook_server_url(strip_whitespace):
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


def test_provisioning_mode(strip_whitespace):
    cmd = 'xConfiguration Provisioning Mode: TMS'
    xapi = """
            <Configuration>
                <Provisioning>
                    <Mode>TMS</Mode>
                </Provisioning>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_provisioning_external_manager_addr(strip_whitespace):
    cmd = 'xConfiguration Provisioning ExternalManager Address: ""'
    xapi = """
            <Configuration>
                <Provisioning>
                    <ExternalManager>
                        <Address></Address>
                    </ExternalManager>
                </Provisioning>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    # do not collapse empty tags to prevent false negative
    assert etree.tostring(expected, method="c14n") == etree.tostring(parsed, method="c14n")


def test_provisioning_external_manager_protocol(strip_whitespace):
    cmd = 'xConfiguration Provisioning ExternalManager Protocol: HTTP'
    xapi = """
            <Configuration>
                <Provisioning>
                    <ExternalManager>
                        <Protocol>HTTP</Protocol>
                    </ExternalManager>
                </Provisioning>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_provisioning_external_manager_path(strip_whitespace):
    cmd = 'xConfiguration Provisioning ExternalManager Path: "tms/public/external/management/SystemManagementService.asmx"'  # noqa
    xapi = """
            <Configuration>
                <Provisioning>
                    <ExternalManager>
                        <Path>tms/public/external/management/SystemManagementService.asmx</Path>
                    </ExternalManager>
                </Provisioning>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_standby_control(strip_whitespace):
    cmd = 'xConfiguration Standby Control: On'
    xapi = """
            <Configuration>
                <Standby>
                    <Control>On</Control>
                </Standby>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_standby_delay(strip_whitespace):
    cmd = 'xConfiguration Standby Delay: 3'
    xapi = """
            <Configuration>
                <Standby>
                    <Delay>3</Delay>
                </Standby>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_standby_boot_action(strip_whitespace):
    cmd = 'xConfiguration Standby BootAction: DefaultCameraPosition'
    xapi = """
            <Configuration>
                <Standby>
                    <BootAction>DefaultCameraPosition</BootAction>
                </Standby>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_standby_standby_action(strip_whitespace):
    cmd = 'xConfiguration Standby StandbyAction: PrivacyPosition'
    xapi = """
            <Configuration>
                <Standby>
                    <StandbyAction>PrivacyPosition</StandbyAction>
                </Standby>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_standby_wakeup_action(strip_whitespace):
    cmd = 'xConfiguration Standby WakeupAction: DefaultCameraPosition'
    xapi = """
            <Configuration>
                <Standby>
                    <WakeupAction>DefaultCameraPosition</WakeupAction>
                </Standby>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_systemunit_lang(strip_whitespace):
    cmd = 'xConfiguration SystemUnit MenuLanguage: English'
    xapi = """
            <Configuration>
                <SystemUnit>
                    <MenuLanguage>English</MenuLanguage>
                </SystemUnit>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_time_zone(strip_whitespace):
    cmd = 'xConfiguration Time Zone: "Europe/Paris"'
    xapi = """
            <Configuration>
                <Time>
                    <Zone>Europe/Paris</Zone>
                </Time>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_time_time_format(strip_whitespace):
    cmd = 'xConfiguration Time TimeFormat: 24H'
    xapi = """
            <Configuration>
                <Time>
                    <TimeFormat>24H</TimeFormat>
                </Time>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_time_date_format(strip_whitespace):
    cmd = 'xConfiguration Time DateFormat: DD_MM_YY'
    xapi = """
            <Configuration>
                <Time>
                    <DateFormat>DD_MM_YY</DateFormat>
                </Time>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_ui_touchpanel_default(strip_whitespace):
    cmd = 'xConfiguration UserInterface TouchPanel DefaultPanel: ContactList'
    xapi = """
            <Configuration>
                <UserInterface>
                    <TouchPanel>
                        <DefaultPanel>ContactList</DefaultPanel>
                    </TouchPanel>
                </UserInterface>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_ui_user_preferences(strip_whitespace):
    cmd = 'xConfiguration UserInterface UserPreferences: Off'
    xapi = """
            <Configuration>
                <UserInterface>
                    <UserPreferences>Off</UserPreferences>
                </UserInterface>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)


def test_video_default_presentation_source(strip_whitespace):
    cmd = 'xConfiguration Video DefaultPresentationSource: 2'
    xapi = """
            <Configuration>
                <Video>
                    <DefaultPresentationSource>2</DefaultPresentationSource>
                </Video>
            </Configuration>
            """
    expected = etree.XML(xapi, parser=strip_whitespace)
    parsed = parse(cmd)
    assert etree.tostring(expected) == etree.tostring(parsed)
