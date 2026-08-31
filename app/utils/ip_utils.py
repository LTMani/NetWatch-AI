import ipaddress
import re

OUI_VENDOR_DATABASE = {
    '00:50:56': 'VMware Virtual NIC',
    '00:0C:29': 'VMware Virtual NIC',
    '00:1A:11': 'Google Cloud Interface',
    'F0:9F:C2': 'Ubiquiti Networks',
    '00:15:5D': 'Microsoft Hyper-V',
    '00:1B:21': 'Intel Corporate',
    '3C:D9:2B': 'Hewlett Packard Enterprise',
    '00:26:08': 'Cisco Systems',
    '00:24:B2': 'Cisco Systems',
    'D8:67:D9': 'Dell Inc.',
    'B8:27:EB': 'Raspberry Pi Foundation',
    'DC:A6:32': 'Raspberry Pi Trading',
    '70:85:C2': 'Apple Inc.',
    'AC:DE:48': 'Apple Inc.',
    'F4:39:09': 'Samsung Electronics',
    '08:00:27': 'Oracle VirtualBox'
}

def is_valid_ipv4(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ipaddress.IPv4Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ipaddress.IPv6Address(ip_str.strip())
        return True
    except ipaddress.AddressValueError:
        return False

def is_private_ip(ip_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        return ip.is_private
    except ValueError:
        return False

def normalize_mac_address(mac_str: str) -> str:
    if not mac_str or not isinstance(mac_str, str):
        return ''
    clean = re.sub(r'[^a-fA-F0-9]', '', mac_str.strip())
    if len(clean) != 12:
        return mac_str.upper()
    return ':'.join(clean[i:i+2].upper() for i in range(0, 12, 2))

def lookup_mac_vendor(mac_str: str) -> str:
    norm = normalize_mac_address(mac_str)
    if len(norm) >= 8:
        prefix = norm[:8]
        return OUI_VENDOR_DATABASE.get(prefix, 'Enterprise Network Hardware')
    return 'Unknown Vendor'

def parse_cidr_subnet(cidr_str: str):
    try:
        net = ipaddress.ip_network(cidr_str.strip(), strict=False)
        return {
            'network_address': str(net.network_address),
            'netmask': str(net.netmask),
            'broadcast_address': str(net.broadcast_address),
            'total_hosts': net.num_addresses - 2 if net.num_addresses > 2 else net.num_addresses,
            'prefix_length': net.prefixlen,
            'is_private': net.is_private
        }
    except ValueError as e:
        raise ValueError(f'Invalid CIDR notation "{cidr_str}": {str(e)}')

def ip_in_subnet(ip_str: str, cidr_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str.strip())
        net = ipaddress.ip_network(cidr_str.strip(), strict=False)
        return ip in net
    except ValueError:
        return False
