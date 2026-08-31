import pytest
from app.utils.ip_utils import is_valid_ipv4, normalize_mac_address, is_private_ip, parse_cidr_subnet

def test_ip_validation():
    assert is_valid_ipv4('192.168.1.1') is True
    assert is_valid_ipv4('10.0.0.254') is True
    assert is_valid_ipv4('999.999.999.999') is False
    assert is_valid_ipv4('not-an-ip') is False

def test_mac_normalization():
    assert normalize_mac_address('00-50-56-AB-CD-EF') == '00:50:56:AB:CD:EF'

def test_private_ip_detection():
    assert is_private_ip('192.168.1.5') is True
    assert is_private_ip('10.0.10.1') is True
    assert is_private_ip('172.16.0.1') is True
    assert is_private_ip('8.8.8.8') is False
