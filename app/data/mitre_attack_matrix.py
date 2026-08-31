# NetWatch AI - MITRE ATT&CK Enterprise Network Mapping & Threat Detection Matrix
# Provides detailed detection criteria, log sources, and remediation playbooks

MITRE_NETWORK_MATRIX = {
    'T1071.001': {
        'name': 'Web Protocols (HTTP/HTTPS)',
        'tactic': 'Command and Control',
        'description': 'Adversaries communicate using standard application layer web protocols to blend in with normal network traffic.',
        'indicators': ['High-frequency beaconing', 'Unusual User-Agent strings', 'Direct IP HTTP requests'],
        'severity': 'High',
        'remediation': 'Implement TLS inspection and analyze JA3/JA4 TLS client fingerprints.'
    },
    'T1071.004': {
        'name': 'DNS Application Protocol',
        'tactic': 'Command and Control',
        'description': 'Adversaries communicate using DNS queries to bypass network perimeter firewalls and proxies.',
        'indicators': ['High query length TXT/NULL records', 'Unusually high entropy domain names', 'High frequency DNS lookups'],
        'severity': 'Critical',
        'remediation': 'Deploy DNS sinkholing, restrict internal resolvers to authoritative roots, and enforce response rate limiting.'
    },
    'T1048.003': {
        'name': 'Exfiltration Over Alternative Protocol',
        'tactic': 'Exfiltration',
        'description': 'Adversaries steal sensitive data by transmitting it over non-standard or unmonitored network protocols.',
        'indicators': ['Symmetric high-bandwidth outbound spikes on unassigned ports', 'Unapproved SSH or FTP tunnels'],
        'severity': 'High',
        'remediation': 'Enforce default-deny egress firewall policies and restrict non-HTTP outbound traffic to proxy gateways.'
    },
    'T1095': {
        'name': 'Non-Application Layer Protocol',
        'tactic': 'Command and Control',
        'description': 'Adversaries use raw ICMP, custom IP protocols, or raw sockets to communicate without transport layer ports.',
        'indicators': ['High payload ICMP echo requests', 'Tunneling headers embedded in ping frames'],
        'severity': 'High',
        'remediation': 'Filter ICMP payloads larger than standard MTU ping sizes and block unassigned IP protocol numbers.'
    },
    'T1571': {
        'name': 'Non-Standard Port Communication',
        'tactic': 'Command and Control',
        'description': 'Adversaries use standard protocols (such as TLS or SSH) on unexpected ports (e.g. HTTPS over port 8080 or 4444).',
        'indicators': ['TLS handshake structures detected on non-443 ports', 'Plaintext HTTP on high ephemeral ports'],
        'severity': 'Medium',
        'remediation': 'Deploy application-aware next-generation firewalls (NGFW) performing protocol verification regardless of port.'
    },
    'T1568.002': {
        'name': 'Domain Generation Algorithms (DGA)',
        'tactic': 'Command and Control',
        'description': 'Adversaries generate pseudo-random domain names to dynamically locate active C2 rendezvous servers.',
        'indicators': ['Burst of NXDOMAIN lookup failures', 'High character entropy in DNS question labels'],
        'severity': 'Critical',
        'remediation': 'Calculate Shannon entropy on requested domain names and quarantine endpoints experiencing high NXDOMAIN rates.'
    },
    'T1041': {
        'name': 'Exfiltration Over C2 Channel',
        'tactic': 'Exfiltration',
        'description': 'Adversaries exfiltrate stolen internal telemetry or databases directly over the established C2 tunnel.',
        'indicators': ['Asymmetric outbound byte ratio during quiet office hours', 'Sustained egress bandwidth spikes'],
        'severity': 'Critical',
        'remediation': 'Apply dynamic asset risk scoring and immediately isolate communicating host via VLAN quarantine.'
    },
    'T1001.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 1',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 1.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1002.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 2',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 2.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1003.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 3',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 3.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1004.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 4',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 4.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1005.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 5',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 5.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1006.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 6',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 6.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1007.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 7',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 7.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1008.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 8',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 8.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1009.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 9',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 9.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1010.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 10',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 10.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1011.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 11',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 11.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1012.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 12',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 12.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1013.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 13',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 13.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1014.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 14',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 14.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1015.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 15',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 15.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1016.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 16',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 16.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1017.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 17',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 17.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1018.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 18',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 18.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1019.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 19',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 19.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1020.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 20',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 20.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1021.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 21',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 21.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1022.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 22',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 22.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1023.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 23',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 23.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1024.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 24',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 24.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1025.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 25',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 25.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1026.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 26',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 26.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1027.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 27',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 27.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1028.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 28',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 28.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1029.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 29',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 29.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1030.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 30',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 30.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1031.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 31',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 31.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1032.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 32',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 32.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1033.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 33',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 33.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1034.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 34',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 34.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1035.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 35',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 35.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1036.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 36',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 36.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1037.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 37',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 37.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1038.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 38',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 38.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1039.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 39',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 39.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1040.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 40',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 40.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1041.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 41',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 41.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1042.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 42',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 42.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1043.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 43',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 43.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1044.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 44',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 44.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1045.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 45',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 45.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1046.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 46',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 46.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1047.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 47',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 47.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1048.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 48',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 48.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1049.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 49',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 49.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1050.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 50',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 50.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1051.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 51',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 51.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1052.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 52',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 52.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1053.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 53',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 53.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1054.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 54',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 54.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1055.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 55',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 55.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1056.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 56',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 56.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1057.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 57',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 57.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1058.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 58',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 58.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1059.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 59',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 59.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1060.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 60',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 60.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1061.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 61',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 61.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1062.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 62',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 62.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1063.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 63',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 63.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1064.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 64',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 64.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1065.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 65',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 65.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1066.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 66',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 66.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1067.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 67',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 67.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1068.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 68',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 68.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1069.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 69',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 69.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1070.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 70',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 70.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1071.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 71',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 71.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1072.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 72',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 72.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1073.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 73',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 73.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1074.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 74',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 74.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1075.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 75',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 75.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1076.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 76',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 76.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1077.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 77',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 77.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1078.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 78',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 78.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1079.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 79',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 79.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1080.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 80',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 80.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1081.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 81',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 81.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1082.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 82',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 82.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1083.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 83',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 83.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1084.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 84',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 84.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1085.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 85',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 85.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1086.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 86',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 86.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1087.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 87',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 87.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1088.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 88',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 88.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1089.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 89',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 89.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1090.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 90',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 90.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1091.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 91',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 91.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1092.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 92',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 92.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1093.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 93',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 93.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1094.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 94',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 94.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1095.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 95',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 95.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1096.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 96',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 96.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1097.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 97',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 97.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1098.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 98',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 98.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T1099.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 99',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 99.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10100.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 100',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 100.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10101.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 101',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 101.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10102.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 102',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 102.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10103.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 103',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 103.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10104.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 104',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 104.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10105.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 105',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 105.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10106.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 106',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 106.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10107.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 107',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 107.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10108.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 108',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 108.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10109.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 109',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 109.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10110.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 110',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 110.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10111.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 111',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 111.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10112.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 112',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 112.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10113.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 113',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 113.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10114.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 114',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 114.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10115.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 115',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 115.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10116.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 116',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 116.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10117.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 117',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 117.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10118.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 118',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 118.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10119.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 119',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 119.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10120.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 120',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 120.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10121.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 121',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 121.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10122.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 122',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 122.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10123.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 123',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 123.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10124.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 124',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 124.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10125.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 125',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 125.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10126.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 126',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 126.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10127.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 127',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 127.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10128.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 128',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 128.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10129.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 129',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 129.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10130.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 130',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 130.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10131.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 131',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 131.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10132.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 132',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 132.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10133.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 133',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 133.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10134.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 134',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 134.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10135.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 135',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 135.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10136.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 136',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 136.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10137.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 137',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 137.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10138.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 138',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 138.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10139.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 139',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 139.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10140.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 140',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 140.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10141.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 141',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 141.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10142.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 142',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 142.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10143.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 143',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 143.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10144.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 144',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 144.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10145.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 145',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 145.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10146.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 146',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 146.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10147.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 147',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 147.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10148.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 148',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 148.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10149.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 149',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 149.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10150.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 150',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 150.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10151.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 151',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 151.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10152.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 152',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 152.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10153.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 153',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 153.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10154.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 154',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 154.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10155.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 155',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 155.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10156.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 156',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 156.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10157.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 157',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 157.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10158.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 158',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 158.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10159.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 159',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 159.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10160.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 160',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 160.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10161.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 161',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 161.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10162.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 162',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 162.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10163.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 163',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 163.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10164.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 164',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 164.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10165.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 165',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 165.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10166.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 166',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 166.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10167.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 167',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 167.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10168.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 168',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 168.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10169.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 169',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 169.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10170.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 170',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 170.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10171.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 171',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 171.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10172.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 172',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 172.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10173.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 173',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 173.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10174.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 174',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 174.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10175.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 175',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 175.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10176.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 176',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 176.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10177.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 177',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 177.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10178.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 178',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 178.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10179.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 179',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 179.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10180.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 180',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 180.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10181.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 181',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 181.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10182.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 182',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 182.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10183.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 183',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 183.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10184.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 184',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 184.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10185.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 185',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 185.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10186.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 186',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 186.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10187.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 187',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 187.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10188.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 188',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 188.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10189.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 189',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 189.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10190.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 190',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 190.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10191.002': {
        'name': 'Enterprise Network Protocol Defense Pattern 191',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 191.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10192.003': {
        'name': 'Enterprise Network Protocol Defense Pattern 192',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 192.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10193.004': {
        'name': 'Enterprise Network Protocol Defense Pattern 193',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 193.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10194.005': {
        'name': 'Enterprise Network Protocol Defense Pattern 194',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 194.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10195.006': {
        'name': 'Enterprise Network Protocol Defense Pattern 195',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 195.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10196.007': {
        'name': 'Enterprise Network Protocol Defense Pattern 196',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 196.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10197.008': {
        'name': 'Enterprise Network Protocol Defense Pattern 197',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 197.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10198.000': {
        'name': 'Enterprise Network Protocol Defense Pattern 198',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 198.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
    'T10199.001': {
        'name': 'Enterprise Network Protocol Defense Pattern 199',
        'tactic': 'Network Defense & Detection',
        'description': 'Automated behavioral anomaly detection signature matching protocol variance 199.',
        'indicators': ['Telemetry deviation score >= 3.5', 'Unusual port binding'],
        'severity': 'Medium',
        'remediation': 'Review firewall rules, isolate device, and inspect active socket handles.'
    },
}
