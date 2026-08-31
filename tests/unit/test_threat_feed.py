import pytest
from app.data.threat_intelligence_feed import check_threat_ioc
from app.data.oui_hardware_vendors import get_extended_vendor
from app.data.mitre_attack_matrix import MITRE_NETWORK_MATRIX

def test_threat_ioc_lookup():
    ioc = check_threat_ioc('198.51.1.1')
    assert ioc is not None
    assert ioc['category'] == 'C2_SERVER'
    assert ioc['threat_score'] >= 90

def test_threat_ioc_clean():
    ioc = check_threat_ioc('8.8.8.8')
    assert ioc is None

def test_oui_vendor_lookup():
    vendor = get_extended_vendor('00:00:0C')
    assert 'Cisco' in vendor

def test_mitre_matrix():
    assert 'T1071.001' in MITRE_NETWORK_MATRIX
    assert MITRE_NETWORK_MATRIX['T1071.001']['tactic'] == 'Command and Control'
