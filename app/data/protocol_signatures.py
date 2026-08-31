# NetWatch AI - Enterprise Master Protocol Signatures & Network Port Registry
# Maps IANA port assignments, RFC protocol specifications, and transport layer header signatures

IANA_PROTOCOL_REGISTRY = {
    20: {
        'service_name': 'FTP-DATA',
        'transport': 'TCP',
        'full_name': 'File Transfer Protocol (Data)',
        'description': 'Standard file transfer data channel.'
    },
    21: {
        'service_name': 'FTP-CONTROL',
        'transport': 'TCP',
        'full_name': 'File Transfer Protocol (Control)',
        'description': 'Authentication and command channel for FTP.'
    },
    22: {
        'service_name': 'SSH',
        'transport': 'TCP',
        'full_name': 'Secure Shell',
        'description': 'Encrypted command-line and SFTP communication.'
    },
    23: {
        'service_name': 'TELNET',
        'transport': 'TCP',
        'full_name': 'Telnet Protocol',
        'description': 'Unencrypted terminal communication - flags high security warning.'
    },
    25: {
        'service_name': 'SMTP',
        'transport': 'TCP',
        'full_name': 'Simple Mail Transfer Protocol',
        'description': 'Outbound electronic mail routing.'
    },
    53: {
        'service_name': 'DNS',
        'transport': 'UDP/TCP',
        'full_name': 'Domain Name System',
        'description': 'Domain name resolution queries and zone transfers.'
    },
    67: {
        'service_name': 'DHCP-SERVER',
        'transport': 'UDP',
        'full_name': 'Dynamic Host Configuration Protocol',
        'description': 'Server listening port for IP lease assignment.'
    },
    68: {
        'service_name': 'DHCP-CLIENT',
        'transport': 'UDP',
        'full_name': 'Dynamic Host Configuration Protocol',
        'description': 'Client listening port for DHCP responses.'
    },
    69: {
        'service_name': 'TFTP',
        'transport': 'UDP',
        'full_name': 'Trivial File Transfer Protocol',
        'description': 'Unauthenticated lightweight file transfer.'
    },
    80: {
        'service_name': 'HTTP',
        'transport': 'TCP',
        'full_name': 'Hypertext Transfer Protocol',
        'description': 'Plaintext World Wide Web traffic.'
    },
    110: {
        'service_name': 'POP3',
        'transport': 'TCP',
        'full_name': 'Post Office Protocol v3',
        'description': 'Legacy email retrieval protocol.'
    },
    123: {
        'service_name': 'NTP',
        'transport': 'UDP',
        'full_name': 'Network Time Protocol',
        'description': 'Clock synchronization across network devices.'
    },
    137: {
        'service_name': 'NETBIOS-NS',
        'transport': 'UDP',
        'full_name': 'NetBIOS Name Service',
        'description': 'Windows name resolution protocol.'
    },
    138: {
        'service_name': 'NETBIOS-DGM',
        'transport': 'UDP',
        'full_name': 'NetBIOS Datagram Service',
        'description': 'Windows SMB browsing service.'
    },
    139: {
        'service_name': 'NETBIOS-SSN',
        'transport': 'TCP',
        'full_name': 'NetBIOS Session Service',
        'description': 'Windows file and printer sharing.'
    },
    143: {
        'service_name': 'IMAP',
        'transport': 'TCP',
        'full_name': 'Internet Message Access Protocol',
        'description': 'Email mailbox synchronization.'
    },
    161: {
        'service_name': 'SNMP',
        'transport': 'UDP',
        'full_name': 'Simple Network Management Protocol',
        'description': 'Network device monitoring queries.'
    },
    162: {
        'service_name': 'SNMP-TRAP',
        'transport': 'UDP',
        'full_name': 'SNMP Trap',
        'description': 'Asynchronous telemetry alerts from switches and routers.'
    },
    179: {
        'service_name': 'BGP',
        'transport': 'TCP',
        'full_name': 'Border Gateway Protocol',
        'description': 'Core autonomous system routing protocol.'
    },
    389: {
        'service_name': 'LDAP',
        'transport': 'TCP',
        'full_name': 'Lightweight Directory Access Protocol',
        'description': 'Enterprise user directory queries.'
    },
    443: {
        'service_name': 'HTTPS',
        'transport': 'TCP',
        'full_name': 'HTTP over TLS/SSL',
        'description': 'Encrypted web application traffic.'
    },
    445: {
        'service_name': 'MICROSOFT-DS',
        'transport': 'TCP',
        'full_name': 'Microsoft Directory Services (SMB)',
        'description': 'Modern Windows file sharing protocol.'
    },
    514: {
        'service_name': 'SYSLOG',
        'transport': 'UDP',
        'full_name': 'System Logging Protocol',
        'description': 'Centralized system event logging.'
    },
    636: {
        'service_name': 'LDAPS',
        'transport': 'TCP',
        'full_name': 'LDAP over TLS',
        'description': 'Encrypted directory service queries.'
    },
    993: {
        'service_name': 'IMAPS',
        'transport': 'TCP',
        'full_name': 'IMAP over TLS',
        'description': 'Encrypted email synchronization.'
    },
    995: {
        'service_name': 'POP3S',
        'transport': 'TCP',
        'full_name': 'POP3 over TLS',
        'description': 'Encrypted email retrieval.'
    },
    1433: {
        'service_name': 'MSSQL',
        'transport': 'TCP',
        'full_name': 'Microsoft SQL Server',
        'description': 'Database server communication.'
    },
    1521: {
        'service_name': 'ORACLE',
        'transport': 'TCP',
        'full_name': 'Oracle Database Listener',
        'description': 'Enterprise database queries.'
    },
    3306: {
        'service_name': 'MYSQL',
        'transport': 'TCP',
        'full_name': 'MySQL Database Server',
        'description': 'Open source relational database traffic.'
    },
    3389: {
        'service_name': 'RDP',
        'transport': 'TCP',
        'full_name': 'Remote Desktop Protocol',
        'description': 'Windows graphical remote desktop session.'
    },
    5432: {
        'service_name': 'POSTGRESQL',
        'transport': 'TCP',
        'full_name': 'PostgreSQL Database',
        'description': 'Relational database client connections.'
    },
    6379: {
        'service_name': 'REDIS',
        'transport': 'TCP',
        'full_name': 'Redis In-Memory Store',
        'description': 'Key-value cache and pub/sub message broker.'
    },
    8080: {
        'service_name': 'HTTP-ALT',
        'transport': 'TCP',
        'full_name': 'HTTP Alternate / Proxy',
        'description': 'Development and proxy server port.'
    },
    8443: {
        'service_name': 'HTTPS-ALT',
        'transport': 'TCP',
        'full_name': 'HTTPS Alternate',
        'description': 'Secondary TLS administrative interface.'
    },
    9200: {
        'service_name': 'ELASTICSEARCH',
        'transport': 'TCP',
        'full_name': 'Elasticsearch REST API',
        'description': 'Log search and analytics cluster communication.'
    },
    1000: {
        'service_name': 'ENTERPRISE-SERVICE-1000',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1000',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1000.'
    },
    1001: {
        'service_name': 'ENTERPRISE-SERVICE-1001',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1001',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1001.'
    },
    1002: {
        'service_name': 'ENTERPRISE-SERVICE-1002',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1002',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1002.'
    },
    1003: {
        'service_name': 'ENTERPRISE-SERVICE-1003',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1003',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1003.'
    },
    1004: {
        'service_name': 'ENTERPRISE-SERVICE-1004',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1004',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1004.'
    },
    1005: {
        'service_name': 'ENTERPRISE-SERVICE-1005',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1005',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1005.'
    },
    1006: {
        'service_name': 'ENTERPRISE-SERVICE-1006',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1006',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1006.'
    },
    1007: {
        'service_name': 'ENTERPRISE-SERVICE-1007',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1007',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1007.'
    },
    1008: {
        'service_name': 'ENTERPRISE-SERVICE-1008',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1008',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1008.'
    },
    1009: {
        'service_name': 'ENTERPRISE-SERVICE-1009',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1009',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1009.'
    },
    1010: {
        'service_name': 'ENTERPRISE-SERVICE-1010',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1010',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1010.'
    },
    1011: {
        'service_name': 'ENTERPRISE-SERVICE-1011',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1011',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1011.'
    },
    1012: {
        'service_name': 'ENTERPRISE-SERVICE-1012',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1012',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1012.'
    },
    1013: {
        'service_name': 'ENTERPRISE-SERVICE-1013',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1013',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1013.'
    },
    1014: {
        'service_name': 'ENTERPRISE-SERVICE-1014',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1014',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1014.'
    },
    1015: {
        'service_name': 'ENTERPRISE-SERVICE-1015',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1015',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1015.'
    },
    1016: {
        'service_name': 'ENTERPRISE-SERVICE-1016',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1016',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1016.'
    },
    1017: {
        'service_name': 'ENTERPRISE-SERVICE-1017',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1017',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1017.'
    },
    1018: {
        'service_name': 'ENTERPRISE-SERVICE-1018',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1018',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1018.'
    },
    1019: {
        'service_name': 'ENTERPRISE-SERVICE-1019',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1019',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1019.'
    },
    1020: {
        'service_name': 'ENTERPRISE-SERVICE-1020',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1020',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1020.'
    },
    1021: {
        'service_name': 'ENTERPRISE-SERVICE-1021',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1021',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1021.'
    },
    1022: {
        'service_name': 'ENTERPRISE-SERVICE-1022',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1022',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1022.'
    },
    1023: {
        'service_name': 'ENTERPRISE-SERVICE-1023',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1023',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1023.'
    },
    1024: {
        'service_name': 'ENTERPRISE-SERVICE-1024',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1024',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1024.'
    },
    1025: {
        'service_name': 'ENTERPRISE-SERVICE-1025',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1025',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1025.'
    },
    1026: {
        'service_name': 'ENTERPRISE-SERVICE-1026',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1026',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1026.'
    },
    1027: {
        'service_name': 'ENTERPRISE-SERVICE-1027',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1027',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1027.'
    },
    1028: {
        'service_name': 'ENTERPRISE-SERVICE-1028',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1028',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1028.'
    },
    1029: {
        'service_name': 'ENTERPRISE-SERVICE-1029',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1029',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1029.'
    },
    1030: {
        'service_name': 'ENTERPRISE-SERVICE-1030',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1030',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1030.'
    },
    1031: {
        'service_name': 'ENTERPRISE-SERVICE-1031',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1031',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1031.'
    },
    1032: {
        'service_name': 'ENTERPRISE-SERVICE-1032',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1032',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1032.'
    },
    1033: {
        'service_name': 'ENTERPRISE-SERVICE-1033',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1033',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1033.'
    },
    1034: {
        'service_name': 'ENTERPRISE-SERVICE-1034',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1034',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1034.'
    },
    1035: {
        'service_name': 'ENTERPRISE-SERVICE-1035',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1035',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1035.'
    },
    1036: {
        'service_name': 'ENTERPRISE-SERVICE-1036',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1036',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1036.'
    },
    1037: {
        'service_name': 'ENTERPRISE-SERVICE-1037',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1037',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1037.'
    },
    1038: {
        'service_name': 'ENTERPRISE-SERVICE-1038',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1038',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1038.'
    },
    1039: {
        'service_name': 'ENTERPRISE-SERVICE-1039',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1039',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1039.'
    },
    1040: {
        'service_name': 'ENTERPRISE-SERVICE-1040',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1040',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1040.'
    },
    1041: {
        'service_name': 'ENTERPRISE-SERVICE-1041',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1041',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1041.'
    },
    1042: {
        'service_name': 'ENTERPRISE-SERVICE-1042',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1042',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1042.'
    },
    1043: {
        'service_name': 'ENTERPRISE-SERVICE-1043',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1043',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1043.'
    },
    1044: {
        'service_name': 'ENTERPRISE-SERVICE-1044',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1044',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1044.'
    },
    1045: {
        'service_name': 'ENTERPRISE-SERVICE-1045',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1045',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1045.'
    },
    1046: {
        'service_name': 'ENTERPRISE-SERVICE-1046',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1046',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1046.'
    },
    1047: {
        'service_name': 'ENTERPRISE-SERVICE-1047',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1047',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1047.'
    },
    1048: {
        'service_name': 'ENTERPRISE-SERVICE-1048',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1048',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1048.'
    },
    1049: {
        'service_name': 'ENTERPRISE-SERVICE-1049',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1049',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1049.'
    },
    1050: {
        'service_name': 'ENTERPRISE-SERVICE-1050',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1050',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1050.'
    },
    1051: {
        'service_name': 'ENTERPRISE-SERVICE-1051',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1051',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1051.'
    },
    1052: {
        'service_name': 'ENTERPRISE-SERVICE-1052',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1052',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1052.'
    },
    1053: {
        'service_name': 'ENTERPRISE-SERVICE-1053',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1053',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1053.'
    },
    1054: {
        'service_name': 'ENTERPRISE-SERVICE-1054',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1054',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1054.'
    },
    1055: {
        'service_name': 'ENTERPRISE-SERVICE-1055',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1055',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1055.'
    },
    1056: {
        'service_name': 'ENTERPRISE-SERVICE-1056',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1056',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1056.'
    },
    1057: {
        'service_name': 'ENTERPRISE-SERVICE-1057',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1057',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1057.'
    },
    1058: {
        'service_name': 'ENTERPRISE-SERVICE-1058',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1058',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1058.'
    },
    1059: {
        'service_name': 'ENTERPRISE-SERVICE-1059',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1059',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1059.'
    },
    1060: {
        'service_name': 'ENTERPRISE-SERVICE-1060',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1060',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1060.'
    },
    1061: {
        'service_name': 'ENTERPRISE-SERVICE-1061',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1061',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1061.'
    },
    1062: {
        'service_name': 'ENTERPRISE-SERVICE-1062',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1062',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1062.'
    },
    1063: {
        'service_name': 'ENTERPRISE-SERVICE-1063',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1063',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1063.'
    },
    1064: {
        'service_name': 'ENTERPRISE-SERVICE-1064',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1064',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1064.'
    },
    1065: {
        'service_name': 'ENTERPRISE-SERVICE-1065',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1065',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1065.'
    },
    1066: {
        'service_name': 'ENTERPRISE-SERVICE-1066',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1066',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1066.'
    },
    1067: {
        'service_name': 'ENTERPRISE-SERVICE-1067',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1067',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1067.'
    },
    1068: {
        'service_name': 'ENTERPRISE-SERVICE-1068',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1068',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1068.'
    },
    1069: {
        'service_name': 'ENTERPRISE-SERVICE-1069',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1069',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1069.'
    },
    1070: {
        'service_name': 'ENTERPRISE-SERVICE-1070',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1070',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1070.'
    },
    1071: {
        'service_name': 'ENTERPRISE-SERVICE-1071',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1071',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1071.'
    },
    1072: {
        'service_name': 'ENTERPRISE-SERVICE-1072',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1072',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1072.'
    },
    1073: {
        'service_name': 'ENTERPRISE-SERVICE-1073',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1073',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1073.'
    },
    1074: {
        'service_name': 'ENTERPRISE-SERVICE-1074',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1074',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1074.'
    },
    1075: {
        'service_name': 'ENTERPRISE-SERVICE-1075',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1075',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1075.'
    },
    1076: {
        'service_name': 'ENTERPRISE-SERVICE-1076',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1076',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1076.'
    },
    1077: {
        'service_name': 'ENTERPRISE-SERVICE-1077',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1077',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1077.'
    },
    1078: {
        'service_name': 'ENTERPRISE-SERVICE-1078',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1078',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1078.'
    },
    1079: {
        'service_name': 'ENTERPRISE-SERVICE-1079',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1079',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1079.'
    },
    1080: {
        'service_name': 'ENTERPRISE-SERVICE-1080',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1080',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1080.'
    },
    1081: {
        'service_name': 'ENTERPRISE-SERVICE-1081',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1081',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1081.'
    },
    1082: {
        'service_name': 'ENTERPRISE-SERVICE-1082',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1082',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1082.'
    },
    1083: {
        'service_name': 'ENTERPRISE-SERVICE-1083',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1083',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1083.'
    },
    1084: {
        'service_name': 'ENTERPRISE-SERVICE-1084',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1084',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1084.'
    },
    1085: {
        'service_name': 'ENTERPRISE-SERVICE-1085',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1085',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1085.'
    },
    1086: {
        'service_name': 'ENTERPRISE-SERVICE-1086',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1086',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1086.'
    },
    1087: {
        'service_name': 'ENTERPRISE-SERVICE-1087',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1087',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1087.'
    },
    1088: {
        'service_name': 'ENTERPRISE-SERVICE-1088',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1088',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1088.'
    },
    1089: {
        'service_name': 'ENTERPRISE-SERVICE-1089',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1089',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1089.'
    },
    1090: {
        'service_name': 'ENTERPRISE-SERVICE-1090',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1090',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1090.'
    },
    1091: {
        'service_name': 'ENTERPRISE-SERVICE-1091',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1091',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1091.'
    },
    1092: {
        'service_name': 'ENTERPRISE-SERVICE-1092',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1092',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1092.'
    },
    1093: {
        'service_name': 'ENTERPRISE-SERVICE-1093',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1093',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1093.'
    },
    1094: {
        'service_name': 'ENTERPRISE-SERVICE-1094',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1094',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1094.'
    },
    1095: {
        'service_name': 'ENTERPRISE-SERVICE-1095',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1095',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1095.'
    },
    1096: {
        'service_name': 'ENTERPRISE-SERVICE-1096',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1096',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1096.'
    },
    1097: {
        'service_name': 'ENTERPRISE-SERVICE-1097',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1097',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1097.'
    },
    1098: {
        'service_name': 'ENTERPRISE-SERVICE-1098',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1098',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1098.'
    },
    1099: {
        'service_name': 'ENTERPRISE-SERVICE-1099',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1099',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1099.'
    },
    1100: {
        'service_name': 'ENTERPRISE-SERVICE-1100',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1100',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1100.'
    },
    1101: {
        'service_name': 'ENTERPRISE-SERVICE-1101',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1101',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1101.'
    },
    1102: {
        'service_name': 'ENTERPRISE-SERVICE-1102',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1102',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1102.'
    },
    1103: {
        'service_name': 'ENTERPRISE-SERVICE-1103',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1103',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1103.'
    },
    1104: {
        'service_name': 'ENTERPRISE-SERVICE-1104',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1104',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1104.'
    },
    1105: {
        'service_name': 'ENTERPRISE-SERVICE-1105',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1105',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1105.'
    },
    1106: {
        'service_name': 'ENTERPRISE-SERVICE-1106',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1106',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1106.'
    },
    1107: {
        'service_name': 'ENTERPRISE-SERVICE-1107',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1107',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1107.'
    },
    1108: {
        'service_name': 'ENTERPRISE-SERVICE-1108',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1108',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1108.'
    },
    1109: {
        'service_name': 'ENTERPRISE-SERVICE-1109',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1109',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1109.'
    },
    1110: {
        'service_name': 'ENTERPRISE-SERVICE-1110',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1110',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1110.'
    },
    1111: {
        'service_name': 'ENTERPRISE-SERVICE-1111',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1111',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1111.'
    },
    1112: {
        'service_name': 'ENTERPRISE-SERVICE-1112',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1112',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1112.'
    },
    1113: {
        'service_name': 'ENTERPRISE-SERVICE-1113',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1113',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1113.'
    },
    1114: {
        'service_name': 'ENTERPRISE-SERVICE-1114',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1114',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1114.'
    },
    1115: {
        'service_name': 'ENTERPRISE-SERVICE-1115',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1115',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1115.'
    },
    1116: {
        'service_name': 'ENTERPRISE-SERVICE-1116',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1116',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1116.'
    },
    1117: {
        'service_name': 'ENTERPRISE-SERVICE-1117',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1117',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1117.'
    },
    1118: {
        'service_name': 'ENTERPRISE-SERVICE-1118',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1118',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1118.'
    },
    1119: {
        'service_name': 'ENTERPRISE-SERVICE-1119',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1119',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1119.'
    },
    1120: {
        'service_name': 'ENTERPRISE-SERVICE-1120',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1120',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1120.'
    },
    1121: {
        'service_name': 'ENTERPRISE-SERVICE-1121',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1121',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1121.'
    },
    1122: {
        'service_name': 'ENTERPRISE-SERVICE-1122',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1122',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1122.'
    },
    1123: {
        'service_name': 'ENTERPRISE-SERVICE-1123',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1123',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1123.'
    },
    1124: {
        'service_name': 'ENTERPRISE-SERVICE-1124',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1124',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1124.'
    },
    1125: {
        'service_name': 'ENTERPRISE-SERVICE-1125',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1125',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1125.'
    },
    1126: {
        'service_name': 'ENTERPRISE-SERVICE-1126',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1126',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1126.'
    },
    1127: {
        'service_name': 'ENTERPRISE-SERVICE-1127',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1127',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1127.'
    },
    1128: {
        'service_name': 'ENTERPRISE-SERVICE-1128',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1128',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1128.'
    },
    1129: {
        'service_name': 'ENTERPRISE-SERVICE-1129',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1129',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1129.'
    },
    1130: {
        'service_name': 'ENTERPRISE-SERVICE-1130',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1130',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1130.'
    },
    1131: {
        'service_name': 'ENTERPRISE-SERVICE-1131',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1131',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1131.'
    },
    1132: {
        'service_name': 'ENTERPRISE-SERVICE-1132',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1132',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1132.'
    },
    1133: {
        'service_name': 'ENTERPRISE-SERVICE-1133',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1133',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1133.'
    },
    1134: {
        'service_name': 'ENTERPRISE-SERVICE-1134',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1134',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1134.'
    },
    1135: {
        'service_name': 'ENTERPRISE-SERVICE-1135',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1135',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1135.'
    },
    1136: {
        'service_name': 'ENTERPRISE-SERVICE-1136',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1136',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1136.'
    },
    1137: {
        'service_name': 'ENTERPRISE-SERVICE-1137',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1137',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1137.'
    },
    1138: {
        'service_name': 'ENTERPRISE-SERVICE-1138',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1138',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1138.'
    },
    1139: {
        'service_name': 'ENTERPRISE-SERVICE-1139',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1139',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1139.'
    },
    1140: {
        'service_name': 'ENTERPRISE-SERVICE-1140',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1140',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1140.'
    },
    1141: {
        'service_name': 'ENTERPRISE-SERVICE-1141',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1141',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1141.'
    },
    1142: {
        'service_name': 'ENTERPRISE-SERVICE-1142',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1142',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1142.'
    },
    1143: {
        'service_name': 'ENTERPRISE-SERVICE-1143',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1143',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1143.'
    },
    1144: {
        'service_name': 'ENTERPRISE-SERVICE-1144',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1144',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1144.'
    },
    1145: {
        'service_name': 'ENTERPRISE-SERVICE-1145',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1145',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1145.'
    },
    1146: {
        'service_name': 'ENTERPRISE-SERVICE-1146',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1146',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1146.'
    },
    1147: {
        'service_name': 'ENTERPRISE-SERVICE-1147',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1147',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1147.'
    },
    1148: {
        'service_name': 'ENTERPRISE-SERVICE-1148',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1148',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1148.'
    },
    1149: {
        'service_name': 'ENTERPRISE-SERVICE-1149',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1149',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1149.'
    },
    1150: {
        'service_name': 'ENTERPRISE-SERVICE-1150',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1150',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1150.'
    },
    1151: {
        'service_name': 'ENTERPRISE-SERVICE-1151',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1151',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1151.'
    },
    1152: {
        'service_name': 'ENTERPRISE-SERVICE-1152',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1152',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1152.'
    },
    1153: {
        'service_name': 'ENTERPRISE-SERVICE-1153',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1153',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1153.'
    },
    1154: {
        'service_name': 'ENTERPRISE-SERVICE-1154',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1154',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1154.'
    },
    1155: {
        'service_name': 'ENTERPRISE-SERVICE-1155',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1155',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1155.'
    },
    1156: {
        'service_name': 'ENTERPRISE-SERVICE-1156',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1156',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1156.'
    },
    1157: {
        'service_name': 'ENTERPRISE-SERVICE-1157',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1157',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1157.'
    },
    1158: {
        'service_name': 'ENTERPRISE-SERVICE-1158',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1158',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1158.'
    },
    1159: {
        'service_name': 'ENTERPRISE-SERVICE-1159',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1159',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1159.'
    },
    1160: {
        'service_name': 'ENTERPRISE-SERVICE-1160',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1160',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1160.'
    },
    1161: {
        'service_name': 'ENTERPRISE-SERVICE-1161',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1161',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1161.'
    },
    1162: {
        'service_name': 'ENTERPRISE-SERVICE-1162',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1162',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1162.'
    },
    1163: {
        'service_name': 'ENTERPRISE-SERVICE-1163',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1163',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1163.'
    },
    1164: {
        'service_name': 'ENTERPRISE-SERVICE-1164',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1164',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1164.'
    },
    1165: {
        'service_name': 'ENTERPRISE-SERVICE-1165',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1165',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1165.'
    },
    1166: {
        'service_name': 'ENTERPRISE-SERVICE-1166',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1166',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1166.'
    },
    1167: {
        'service_name': 'ENTERPRISE-SERVICE-1167',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1167',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1167.'
    },
    1168: {
        'service_name': 'ENTERPRISE-SERVICE-1168',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1168',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1168.'
    },
    1169: {
        'service_name': 'ENTERPRISE-SERVICE-1169',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1169',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1169.'
    },
    1170: {
        'service_name': 'ENTERPRISE-SERVICE-1170',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1170',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1170.'
    },
    1171: {
        'service_name': 'ENTERPRISE-SERVICE-1171',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1171',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1171.'
    },
    1172: {
        'service_name': 'ENTERPRISE-SERVICE-1172',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1172',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1172.'
    },
    1173: {
        'service_name': 'ENTERPRISE-SERVICE-1173',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1173',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1173.'
    },
    1174: {
        'service_name': 'ENTERPRISE-SERVICE-1174',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1174',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1174.'
    },
    1175: {
        'service_name': 'ENTERPRISE-SERVICE-1175',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1175',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1175.'
    },
    1176: {
        'service_name': 'ENTERPRISE-SERVICE-1176',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1176',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1176.'
    },
    1177: {
        'service_name': 'ENTERPRISE-SERVICE-1177',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1177',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1177.'
    },
    1178: {
        'service_name': 'ENTERPRISE-SERVICE-1178',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1178',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1178.'
    },
    1179: {
        'service_name': 'ENTERPRISE-SERVICE-1179',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1179',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1179.'
    },
    1180: {
        'service_name': 'ENTERPRISE-SERVICE-1180',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1180',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1180.'
    },
    1181: {
        'service_name': 'ENTERPRISE-SERVICE-1181',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1181',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1181.'
    },
    1182: {
        'service_name': 'ENTERPRISE-SERVICE-1182',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1182',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1182.'
    },
    1183: {
        'service_name': 'ENTERPRISE-SERVICE-1183',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1183',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1183.'
    },
    1184: {
        'service_name': 'ENTERPRISE-SERVICE-1184',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1184',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1184.'
    },
    1185: {
        'service_name': 'ENTERPRISE-SERVICE-1185',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1185',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1185.'
    },
    1186: {
        'service_name': 'ENTERPRISE-SERVICE-1186',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1186',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1186.'
    },
    1187: {
        'service_name': 'ENTERPRISE-SERVICE-1187',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1187',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1187.'
    },
    1188: {
        'service_name': 'ENTERPRISE-SERVICE-1188',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1188',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1188.'
    },
    1189: {
        'service_name': 'ENTERPRISE-SERVICE-1189',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1189',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1189.'
    },
    1190: {
        'service_name': 'ENTERPRISE-SERVICE-1190',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1190',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1190.'
    },
    1191: {
        'service_name': 'ENTERPRISE-SERVICE-1191',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1191',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1191.'
    },
    1192: {
        'service_name': 'ENTERPRISE-SERVICE-1192',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1192',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1192.'
    },
    1193: {
        'service_name': 'ENTERPRISE-SERVICE-1193',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1193',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1193.'
    },
    1194: {
        'service_name': 'ENTERPRISE-SERVICE-1194',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1194',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1194.'
    },
    1195: {
        'service_name': 'ENTERPRISE-SERVICE-1195',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1195',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1195.'
    },
    1196: {
        'service_name': 'ENTERPRISE-SERVICE-1196',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1196',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1196.'
    },
    1197: {
        'service_name': 'ENTERPRISE-SERVICE-1197',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1197',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1197.'
    },
    1198: {
        'service_name': 'ENTERPRISE-SERVICE-1198',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1198',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1198.'
    },
    1199: {
        'service_name': 'ENTERPRISE-SERVICE-1199',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1199',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1199.'
    },
    1200: {
        'service_name': 'ENTERPRISE-SERVICE-1200',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1200',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1200.'
    },
    1201: {
        'service_name': 'ENTERPRISE-SERVICE-1201',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1201',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1201.'
    },
    1202: {
        'service_name': 'ENTERPRISE-SERVICE-1202',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1202',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1202.'
    },
    1203: {
        'service_name': 'ENTERPRISE-SERVICE-1203',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1203',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1203.'
    },
    1204: {
        'service_name': 'ENTERPRISE-SERVICE-1204',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1204',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1204.'
    },
    1205: {
        'service_name': 'ENTERPRISE-SERVICE-1205',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1205',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1205.'
    },
    1206: {
        'service_name': 'ENTERPRISE-SERVICE-1206',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1206',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1206.'
    },
    1207: {
        'service_name': 'ENTERPRISE-SERVICE-1207',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1207',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1207.'
    },
    1208: {
        'service_name': 'ENTERPRISE-SERVICE-1208',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1208',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1208.'
    },
    1209: {
        'service_name': 'ENTERPRISE-SERVICE-1209',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1209',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1209.'
    },
    1210: {
        'service_name': 'ENTERPRISE-SERVICE-1210',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1210',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1210.'
    },
    1211: {
        'service_name': 'ENTERPRISE-SERVICE-1211',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1211',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1211.'
    },
    1212: {
        'service_name': 'ENTERPRISE-SERVICE-1212',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1212',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1212.'
    },
    1213: {
        'service_name': 'ENTERPRISE-SERVICE-1213',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1213',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1213.'
    },
    1214: {
        'service_name': 'ENTERPRISE-SERVICE-1214',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1214',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1214.'
    },
    1215: {
        'service_name': 'ENTERPRISE-SERVICE-1215',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1215',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1215.'
    },
    1216: {
        'service_name': 'ENTERPRISE-SERVICE-1216',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1216',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1216.'
    },
    1217: {
        'service_name': 'ENTERPRISE-SERVICE-1217',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1217',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1217.'
    },
    1218: {
        'service_name': 'ENTERPRISE-SERVICE-1218',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1218',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1218.'
    },
    1219: {
        'service_name': 'ENTERPRISE-SERVICE-1219',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1219',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1219.'
    },
    1220: {
        'service_name': 'ENTERPRISE-SERVICE-1220',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1220',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1220.'
    },
    1221: {
        'service_name': 'ENTERPRISE-SERVICE-1221',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1221',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1221.'
    },
    1222: {
        'service_name': 'ENTERPRISE-SERVICE-1222',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1222',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1222.'
    },
    1223: {
        'service_name': 'ENTERPRISE-SERVICE-1223',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1223',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1223.'
    },
    1224: {
        'service_name': 'ENTERPRISE-SERVICE-1224',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1224',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1224.'
    },
    1225: {
        'service_name': 'ENTERPRISE-SERVICE-1225',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1225',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1225.'
    },
    1226: {
        'service_name': 'ENTERPRISE-SERVICE-1226',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1226',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1226.'
    },
    1227: {
        'service_name': 'ENTERPRISE-SERVICE-1227',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1227',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1227.'
    },
    1228: {
        'service_name': 'ENTERPRISE-SERVICE-1228',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1228',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1228.'
    },
    1229: {
        'service_name': 'ENTERPRISE-SERVICE-1229',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1229',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1229.'
    },
    1230: {
        'service_name': 'ENTERPRISE-SERVICE-1230',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1230',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1230.'
    },
    1231: {
        'service_name': 'ENTERPRISE-SERVICE-1231',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1231',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1231.'
    },
    1232: {
        'service_name': 'ENTERPRISE-SERVICE-1232',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1232',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1232.'
    },
    1233: {
        'service_name': 'ENTERPRISE-SERVICE-1233',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1233',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1233.'
    },
    1234: {
        'service_name': 'ENTERPRISE-SERVICE-1234',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1234',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1234.'
    },
    1235: {
        'service_name': 'ENTERPRISE-SERVICE-1235',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1235',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1235.'
    },
    1236: {
        'service_name': 'ENTERPRISE-SERVICE-1236',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1236',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1236.'
    },
    1237: {
        'service_name': 'ENTERPRISE-SERVICE-1237',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1237',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1237.'
    },
    1238: {
        'service_name': 'ENTERPRISE-SERVICE-1238',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1238',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1238.'
    },
    1239: {
        'service_name': 'ENTERPRISE-SERVICE-1239',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1239',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1239.'
    },
    1240: {
        'service_name': 'ENTERPRISE-SERVICE-1240',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1240',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1240.'
    },
    1241: {
        'service_name': 'ENTERPRISE-SERVICE-1241',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1241',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1241.'
    },
    1242: {
        'service_name': 'ENTERPRISE-SERVICE-1242',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1242',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1242.'
    },
    1243: {
        'service_name': 'ENTERPRISE-SERVICE-1243',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1243',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1243.'
    },
    1244: {
        'service_name': 'ENTERPRISE-SERVICE-1244',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1244',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1244.'
    },
    1245: {
        'service_name': 'ENTERPRISE-SERVICE-1245',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1245',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1245.'
    },
    1246: {
        'service_name': 'ENTERPRISE-SERVICE-1246',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1246',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1246.'
    },
    1247: {
        'service_name': 'ENTERPRISE-SERVICE-1247',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1247',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1247.'
    },
    1248: {
        'service_name': 'ENTERPRISE-SERVICE-1248',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1248',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1248.'
    },
    1249: {
        'service_name': 'ENTERPRISE-SERVICE-1249',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1249',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1249.'
    },
    1250: {
        'service_name': 'ENTERPRISE-SERVICE-1250',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1250',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1250.'
    },
    1251: {
        'service_name': 'ENTERPRISE-SERVICE-1251',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1251',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1251.'
    },
    1252: {
        'service_name': 'ENTERPRISE-SERVICE-1252',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1252',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1252.'
    },
    1253: {
        'service_name': 'ENTERPRISE-SERVICE-1253',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1253',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1253.'
    },
    1254: {
        'service_name': 'ENTERPRISE-SERVICE-1254',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1254',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1254.'
    },
    1255: {
        'service_name': 'ENTERPRISE-SERVICE-1255',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1255',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1255.'
    },
    1256: {
        'service_name': 'ENTERPRISE-SERVICE-1256',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1256',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1256.'
    },
    1257: {
        'service_name': 'ENTERPRISE-SERVICE-1257',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1257',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1257.'
    },
    1258: {
        'service_name': 'ENTERPRISE-SERVICE-1258',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1258',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1258.'
    },
    1259: {
        'service_name': 'ENTERPRISE-SERVICE-1259',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1259',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1259.'
    },
    1260: {
        'service_name': 'ENTERPRISE-SERVICE-1260',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1260',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1260.'
    },
    1261: {
        'service_name': 'ENTERPRISE-SERVICE-1261',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1261',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1261.'
    },
    1262: {
        'service_name': 'ENTERPRISE-SERVICE-1262',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1262',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1262.'
    },
    1263: {
        'service_name': 'ENTERPRISE-SERVICE-1263',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1263',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1263.'
    },
    1264: {
        'service_name': 'ENTERPRISE-SERVICE-1264',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1264',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1264.'
    },
    1265: {
        'service_name': 'ENTERPRISE-SERVICE-1265',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1265',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1265.'
    },
    1266: {
        'service_name': 'ENTERPRISE-SERVICE-1266',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1266',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1266.'
    },
    1267: {
        'service_name': 'ENTERPRISE-SERVICE-1267',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1267',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1267.'
    },
    1268: {
        'service_name': 'ENTERPRISE-SERVICE-1268',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1268',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1268.'
    },
    1269: {
        'service_name': 'ENTERPRISE-SERVICE-1269',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1269',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1269.'
    },
    1270: {
        'service_name': 'ENTERPRISE-SERVICE-1270',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1270',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1270.'
    },
    1271: {
        'service_name': 'ENTERPRISE-SERVICE-1271',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1271',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1271.'
    },
    1272: {
        'service_name': 'ENTERPRISE-SERVICE-1272',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1272',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1272.'
    },
    1273: {
        'service_name': 'ENTERPRISE-SERVICE-1273',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1273',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1273.'
    },
    1274: {
        'service_name': 'ENTERPRISE-SERVICE-1274',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1274',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1274.'
    },
    1275: {
        'service_name': 'ENTERPRISE-SERVICE-1275',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1275',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1275.'
    },
    1276: {
        'service_name': 'ENTERPRISE-SERVICE-1276',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1276',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1276.'
    },
    1277: {
        'service_name': 'ENTERPRISE-SERVICE-1277',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1277',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1277.'
    },
    1278: {
        'service_name': 'ENTERPRISE-SERVICE-1278',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1278',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1278.'
    },
    1279: {
        'service_name': 'ENTERPRISE-SERVICE-1279',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1279',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1279.'
    },
    1280: {
        'service_name': 'ENTERPRISE-SERVICE-1280',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1280',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1280.'
    },
    1281: {
        'service_name': 'ENTERPRISE-SERVICE-1281',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1281',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1281.'
    },
    1282: {
        'service_name': 'ENTERPRISE-SERVICE-1282',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1282',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1282.'
    },
    1283: {
        'service_name': 'ENTERPRISE-SERVICE-1283',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1283',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1283.'
    },
    1284: {
        'service_name': 'ENTERPRISE-SERVICE-1284',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1284',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1284.'
    },
    1285: {
        'service_name': 'ENTERPRISE-SERVICE-1285',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1285',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1285.'
    },
    1286: {
        'service_name': 'ENTERPRISE-SERVICE-1286',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1286',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1286.'
    },
    1287: {
        'service_name': 'ENTERPRISE-SERVICE-1287',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1287',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1287.'
    },
    1288: {
        'service_name': 'ENTERPRISE-SERVICE-1288',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1288',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1288.'
    },
    1289: {
        'service_name': 'ENTERPRISE-SERVICE-1289',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1289',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1289.'
    },
    1290: {
        'service_name': 'ENTERPRISE-SERVICE-1290',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1290',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1290.'
    },
    1291: {
        'service_name': 'ENTERPRISE-SERVICE-1291',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1291',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1291.'
    },
    1292: {
        'service_name': 'ENTERPRISE-SERVICE-1292',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1292',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1292.'
    },
    1293: {
        'service_name': 'ENTERPRISE-SERVICE-1293',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1293',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1293.'
    },
    1294: {
        'service_name': 'ENTERPRISE-SERVICE-1294',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1294',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1294.'
    },
    1295: {
        'service_name': 'ENTERPRISE-SERVICE-1295',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1295',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1295.'
    },
    1296: {
        'service_name': 'ENTERPRISE-SERVICE-1296',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1296',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1296.'
    },
    1297: {
        'service_name': 'ENTERPRISE-SERVICE-1297',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1297',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1297.'
    },
    1298: {
        'service_name': 'ENTERPRISE-SERVICE-1298',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1298',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1298.'
    },
    1299: {
        'service_name': 'ENTERPRISE-SERVICE-1299',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1299',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1299.'
    },
    1300: {
        'service_name': 'ENTERPRISE-SERVICE-1300',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1300',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1300.'
    },
    1301: {
        'service_name': 'ENTERPRISE-SERVICE-1301',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1301',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1301.'
    },
    1302: {
        'service_name': 'ENTERPRISE-SERVICE-1302',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1302',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1302.'
    },
    1303: {
        'service_name': 'ENTERPRISE-SERVICE-1303',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1303',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1303.'
    },
    1304: {
        'service_name': 'ENTERPRISE-SERVICE-1304',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1304',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1304.'
    },
    1305: {
        'service_name': 'ENTERPRISE-SERVICE-1305',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1305',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1305.'
    },
    1306: {
        'service_name': 'ENTERPRISE-SERVICE-1306',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1306',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1306.'
    },
    1307: {
        'service_name': 'ENTERPRISE-SERVICE-1307',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1307',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1307.'
    },
    1308: {
        'service_name': 'ENTERPRISE-SERVICE-1308',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1308',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1308.'
    },
    1309: {
        'service_name': 'ENTERPRISE-SERVICE-1309',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1309',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1309.'
    },
    1310: {
        'service_name': 'ENTERPRISE-SERVICE-1310',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1310',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1310.'
    },
    1311: {
        'service_name': 'ENTERPRISE-SERVICE-1311',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1311',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1311.'
    },
    1312: {
        'service_name': 'ENTERPRISE-SERVICE-1312',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1312',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1312.'
    },
    1313: {
        'service_name': 'ENTERPRISE-SERVICE-1313',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1313',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1313.'
    },
    1314: {
        'service_name': 'ENTERPRISE-SERVICE-1314',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1314',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1314.'
    },
    1315: {
        'service_name': 'ENTERPRISE-SERVICE-1315',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1315',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1315.'
    },
    1316: {
        'service_name': 'ENTERPRISE-SERVICE-1316',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1316',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1316.'
    },
    1317: {
        'service_name': 'ENTERPRISE-SERVICE-1317',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1317',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1317.'
    },
    1318: {
        'service_name': 'ENTERPRISE-SERVICE-1318',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1318',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1318.'
    },
    1319: {
        'service_name': 'ENTERPRISE-SERVICE-1319',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1319',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1319.'
    },
    1320: {
        'service_name': 'ENTERPRISE-SERVICE-1320',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1320',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1320.'
    },
    1321: {
        'service_name': 'ENTERPRISE-SERVICE-1321',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1321',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1321.'
    },
    1322: {
        'service_name': 'ENTERPRISE-SERVICE-1322',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1322',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1322.'
    },
    1323: {
        'service_name': 'ENTERPRISE-SERVICE-1323',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1323',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1323.'
    },
    1324: {
        'service_name': 'ENTERPRISE-SERVICE-1324',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1324',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1324.'
    },
    1325: {
        'service_name': 'ENTERPRISE-SERVICE-1325',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1325',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1325.'
    },
    1326: {
        'service_name': 'ENTERPRISE-SERVICE-1326',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1326',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1326.'
    },
    1327: {
        'service_name': 'ENTERPRISE-SERVICE-1327',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1327',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1327.'
    },
    1328: {
        'service_name': 'ENTERPRISE-SERVICE-1328',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1328',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1328.'
    },
    1329: {
        'service_name': 'ENTERPRISE-SERVICE-1329',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1329',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1329.'
    },
    1330: {
        'service_name': 'ENTERPRISE-SERVICE-1330',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1330',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1330.'
    },
    1331: {
        'service_name': 'ENTERPRISE-SERVICE-1331',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1331',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1331.'
    },
    1332: {
        'service_name': 'ENTERPRISE-SERVICE-1332',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1332',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1332.'
    },
    1333: {
        'service_name': 'ENTERPRISE-SERVICE-1333',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1333',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1333.'
    },
    1334: {
        'service_name': 'ENTERPRISE-SERVICE-1334',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1334',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1334.'
    },
    1335: {
        'service_name': 'ENTERPRISE-SERVICE-1335',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1335',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1335.'
    },
    1336: {
        'service_name': 'ENTERPRISE-SERVICE-1336',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1336',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1336.'
    },
    1337: {
        'service_name': 'ENTERPRISE-SERVICE-1337',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1337',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1337.'
    },
    1338: {
        'service_name': 'ENTERPRISE-SERVICE-1338',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1338',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1338.'
    },
    1339: {
        'service_name': 'ENTERPRISE-SERVICE-1339',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1339',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1339.'
    },
    1340: {
        'service_name': 'ENTERPRISE-SERVICE-1340',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1340',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1340.'
    },
    1341: {
        'service_name': 'ENTERPRISE-SERVICE-1341',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1341',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1341.'
    },
    1342: {
        'service_name': 'ENTERPRISE-SERVICE-1342',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1342',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1342.'
    },
    1343: {
        'service_name': 'ENTERPRISE-SERVICE-1343',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1343',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1343.'
    },
    1344: {
        'service_name': 'ENTERPRISE-SERVICE-1344',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1344',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1344.'
    },
    1345: {
        'service_name': 'ENTERPRISE-SERVICE-1345',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1345',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1345.'
    },
    1346: {
        'service_name': 'ENTERPRISE-SERVICE-1346',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1346',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1346.'
    },
    1347: {
        'service_name': 'ENTERPRISE-SERVICE-1347',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1347',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1347.'
    },
    1348: {
        'service_name': 'ENTERPRISE-SERVICE-1348',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1348',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1348.'
    },
    1349: {
        'service_name': 'ENTERPRISE-SERVICE-1349',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1349',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1349.'
    },
    1350: {
        'service_name': 'ENTERPRISE-SERVICE-1350',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1350',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1350.'
    },
    1351: {
        'service_name': 'ENTERPRISE-SERVICE-1351',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1351',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1351.'
    },
    1352: {
        'service_name': 'ENTERPRISE-SERVICE-1352',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1352',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1352.'
    },
    1353: {
        'service_name': 'ENTERPRISE-SERVICE-1353',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1353',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1353.'
    },
    1354: {
        'service_name': 'ENTERPRISE-SERVICE-1354',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1354',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1354.'
    },
    1355: {
        'service_name': 'ENTERPRISE-SERVICE-1355',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1355',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1355.'
    },
    1356: {
        'service_name': 'ENTERPRISE-SERVICE-1356',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1356',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1356.'
    },
    1357: {
        'service_name': 'ENTERPRISE-SERVICE-1357',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1357',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1357.'
    },
    1358: {
        'service_name': 'ENTERPRISE-SERVICE-1358',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1358',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1358.'
    },
    1359: {
        'service_name': 'ENTERPRISE-SERVICE-1359',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1359',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1359.'
    },
    1360: {
        'service_name': 'ENTERPRISE-SERVICE-1360',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1360',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1360.'
    },
    1361: {
        'service_name': 'ENTERPRISE-SERVICE-1361',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1361',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1361.'
    },
    1362: {
        'service_name': 'ENTERPRISE-SERVICE-1362',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1362',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1362.'
    },
    1363: {
        'service_name': 'ENTERPRISE-SERVICE-1363',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1363',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1363.'
    },
    1364: {
        'service_name': 'ENTERPRISE-SERVICE-1364',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1364',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1364.'
    },
    1365: {
        'service_name': 'ENTERPRISE-SERVICE-1365',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1365',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1365.'
    },
    1366: {
        'service_name': 'ENTERPRISE-SERVICE-1366',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1366',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1366.'
    },
    1367: {
        'service_name': 'ENTERPRISE-SERVICE-1367',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1367',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1367.'
    },
    1368: {
        'service_name': 'ENTERPRISE-SERVICE-1368',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1368',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1368.'
    },
    1369: {
        'service_name': 'ENTERPRISE-SERVICE-1369',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1369',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1369.'
    },
    1370: {
        'service_name': 'ENTERPRISE-SERVICE-1370',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1370',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1370.'
    },
    1371: {
        'service_name': 'ENTERPRISE-SERVICE-1371',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1371',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1371.'
    },
    1372: {
        'service_name': 'ENTERPRISE-SERVICE-1372',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1372',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1372.'
    },
    1373: {
        'service_name': 'ENTERPRISE-SERVICE-1373',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1373',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1373.'
    },
    1374: {
        'service_name': 'ENTERPRISE-SERVICE-1374',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1374',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1374.'
    },
    1375: {
        'service_name': 'ENTERPRISE-SERVICE-1375',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1375',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1375.'
    },
    1376: {
        'service_name': 'ENTERPRISE-SERVICE-1376',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1376',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1376.'
    },
    1377: {
        'service_name': 'ENTERPRISE-SERVICE-1377',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1377',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1377.'
    },
    1378: {
        'service_name': 'ENTERPRISE-SERVICE-1378',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1378',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1378.'
    },
    1379: {
        'service_name': 'ENTERPRISE-SERVICE-1379',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1379',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1379.'
    },
    1380: {
        'service_name': 'ENTERPRISE-SERVICE-1380',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1380',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1380.'
    },
    1381: {
        'service_name': 'ENTERPRISE-SERVICE-1381',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1381',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1381.'
    },
    1382: {
        'service_name': 'ENTERPRISE-SERVICE-1382',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1382',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1382.'
    },
    1383: {
        'service_name': 'ENTERPRISE-SERVICE-1383',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1383',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1383.'
    },
    1384: {
        'service_name': 'ENTERPRISE-SERVICE-1384',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1384',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1384.'
    },
    1385: {
        'service_name': 'ENTERPRISE-SERVICE-1385',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1385',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1385.'
    },
    1386: {
        'service_name': 'ENTERPRISE-SERVICE-1386',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1386',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1386.'
    },
    1387: {
        'service_name': 'ENTERPRISE-SERVICE-1387',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1387',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1387.'
    },
    1388: {
        'service_name': 'ENTERPRISE-SERVICE-1388',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1388',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1388.'
    },
    1389: {
        'service_name': 'ENTERPRISE-SERVICE-1389',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1389',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1389.'
    },
    1390: {
        'service_name': 'ENTERPRISE-SERVICE-1390',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1390',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1390.'
    },
    1391: {
        'service_name': 'ENTERPRISE-SERVICE-1391',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1391',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1391.'
    },
    1392: {
        'service_name': 'ENTERPRISE-SERVICE-1392',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1392',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1392.'
    },
    1393: {
        'service_name': 'ENTERPRISE-SERVICE-1393',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1393',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1393.'
    },
    1394: {
        'service_name': 'ENTERPRISE-SERVICE-1394',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1394',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1394.'
    },
    1395: {
        'service_name': 'ENTERPRISE-SERVICE-1395',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1395',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1395.'
    },
    1396: {
        'service_name': 'ENTERPRISE-SERVICE-1396',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1396',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1396.'
    },
    1397: {
        'service_name': 'ENTERPRISE-SERVICE-1397',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1397',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1397.'
    },
    1398: {
        'service_name': 'ENTERPRISE-SERVICE-1398',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1398',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1398.'
    },
    1399: {
        'service_name': 'ENTERPRISE-SERVICE-1399',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1399',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1399.'
    },
    1400: {
        'service_name': 'ENTERPRISE-SERVICE-1400',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1400',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1400.'
    },
    1401: {
        'service_name': 'ENTERPRISE-SERVICE-1401',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1401',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1401.'
    },
    1402: {
        'service_name': 'ENTERPRISE-SERVICE-1402',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1402',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1402.'
    },
    1403: {
        'service_name': 'ENTERPRISE-SERVICE-1403',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1403',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1403.'
    },
    1404: {
        'service_name': 'ENTERPRISE-SERVICE-1404',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1404',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1404.'
    },
    1405: {
        'service_name': 'ENTERPRISE-SERVICE-1405',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1405',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1405.'
    },
    1406: {
        'service_name': 'ENTERPRISE-SERVICE-1406',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1406',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1406.'
    },
    1407: {
        'service_name': 'ENTERPRISE-SERVICE-1407',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1407',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1407.'
    },
    1408: {
        'service_name': 'ENTERPRISE-SERVICE-1408',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1408',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1408.'
    },
    1409: {
        'service_name': 'ENTERPRISE-SERVICE-1409',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1409',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1409.'
    },
    1410: {
        'service_name': 'ENTERPRISE-SERVICE-1410',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1410',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1410.'
    },
    1411: {
        'service_name': 'ENTERPRISE-SERVICE-1411',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1411',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1411.'
    },
    1412: {
        'service_name': 'ENTERPRISE-SERVICE-1412',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1412',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1412.'
    },
    1413: {
        'service_name': 'ENTERPRISE-SERVICE-1413',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1413',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1413.'
    },
    1414: {
        'service_name': 'ENTERPRISE-SERVICE-1414',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1414',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1414.'
    },
    1415: {
        'service_name': 'ENTERPRISE-SERVICE-1415',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1415',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1415.'
    },
    1416: {
        'service_name': 'ENTERPRISE-SERVICE-1416',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1416',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1416.'
    },
    1417: {
        'service_name': 'ENTERPRISE-SERVICE-1417',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1417',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1417.'
    },
    1418: {
        'service_name': 'ENTERPRISE-SERVICE-1418',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1418',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1418.'
    },
    1419: {
        'service_name': 'ENTERPRISE-SERVICE-1419',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1419',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1419.'
    },
    1420: {
        'service_name': 'ENTERPRISE-SERVICE-1420',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1420',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1420.'
    },
    1421: {
        'service_name': 'ENTERPRISE-SERVICE-1421',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1421',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1421.'
    },
    1422: {
        'service_name': 'ENTERPRISE-SERVICE-1422',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1422',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1422.'
    },
    1423: {
        'service_name': 'ENTERPRISE-SERVICE-1423',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1423',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1423.'
    },
    1424: {
        'service_name': 'ENTERPRISE-SERVICE-1424',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1424',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1424.'
    },
    1425: {
        'service_name': 'ENTERPRISE-SERVICE-1425',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1425',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1425.'
    },
    1426: {
        'service_name': 'ENTERPRISE-SERVICE-1426',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1426',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1426.'
    },
    1427: {
        'service_name': 'ENTERPRISE-SERVICE-1427',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1427',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1427.'
    },
    1428: {
        'service_name': 'ENTERPRISE-SERVICE-1428',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1428',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1428.'
    },
    1429: {
        'service_name': 'ENTERPRISE-SERVICE-1429',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1429',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1429.'
    },
    1430: {
        'service_name': 'ENTERPRISE-SERVICE-1430',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1430',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1430.'
    },
    1431: {
        'service_name': 'ENTERPRISE-SERVICE-1431',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1431',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1431.'
    },
    1432: {
        'service_name': 'ENTERPRISE-SERVICE-1432',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1432',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1432.'
    },
    1434: {
        'service_name': 'ENTERPRISE-SERVICE-1434',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1434',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1434.'
    },
    1435: {
        'service_name': 'ENTERPRISE-SERVICE-1435',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1435',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1435.'
    },
    1436: {
        'service_name': 'ENTERPRISE-SERVICE-1436',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1436',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1436.'
    },
    1437: {
        'service_name': 'ENTERPRISE-SERVICE-1437',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1437',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1437.'
    },
    1438: {
        'service_name': 'ENTERPRISE-SERVICE-1438',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1438',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1438.'
    },
    1439: {
        'service_name': 'ENTERPRISE-SERVICE-1439',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1439',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1439.'
    },
    1440: {
        'service_name': 'ENTERPRISE-SERVICE-1440',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1440',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1440.'
    },
    1441: {
        'service_name': 'ENTERPRISE-SERVICE-1441',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1441',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1441.'
    },
    1442: {
        'service_name': 'ENTERPRISE-SERVICE-1442',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1442',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1442.'
    },
    1443: {
        'service_name': 'ENTERPRISE-SERVICE-1443',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1443',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1443.'
    },
    1444: {
        'service_name': 'ENTERPRISE-SERVICE-1444',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1444',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1444.'
    },
    1445: {
        'service_name': 'ENTERPRISE-SERVICE-1445',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1445',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1445.'
    },
    1446: {
        'service_name': 'ENTERPRISE-SERVICE-1446',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1446',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1446.'
    },
    1447: {
        'service_name': 'ENTERPRISE-SERVICE-1447',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1447',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1447.'
    },
    1448: {
        'service_name': 'ENTERPRISE-SERVICE-1448',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1448',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1448.'
    },
    1449: {
        'service_name': 'ENTERPRISE-SERVICE-1449',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1449',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1449.'
    },
    1450: {
        'service_name': 'ENTERPRISE-SERVICE-1450',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1450',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1450.'
    },
    1451: {
        'service_name': 'ENTERPRISE-SERVICE-1451',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1451',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1451.'
    },
    1452: {
        'service_name': 'ENTERPRISE-SERVICE-1452',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1452',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1452.'
    },
    1453: {
        'service_name': 'ENTERPRISE-SERVICE-1453',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1453',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1453.'
    },
    1454: {
        'service_name': 'ENTERPRISE-SERVICE-1454',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1454',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1454.'
    },
    1455: {
        'service_name': 'ENTERPRISE-SERVICE-1455',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1455',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1455.'
    },
    1456: {
        'service_name': 'ENTERPRISE-SERVICE-1456',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1456',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1456.'
    },
    1457: {
        'service_name': 'ENTERPRISE-SERVICE-1457',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1457',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1457.'
    },
    1458: {
        'service_name': 'ENTERPRISE-SERVICE-1458',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1458',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1458.'
    },
    1459: {
        'service_name': 'ENTERPRISE-SERVICE-1459',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1459',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1459.'
    },
    1460: {
        'service_name': 'ENTERPRISE-SERVICE-1460',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1460',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1460.'
    },
    1461: {
        'service_name': 'ENTERPRISE-SERVICE-1461',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1461',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1461.'
    },
    1462: {
        'service_name': 'ENTERPRISE-SERVICE-1462',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1462',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1462.'
    },
    1463: {
        'service_name': 'ENTERPRISE-SERVICE-1463',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1463',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1463.'
    },
    1464: {
        'service_name': 'ENTERPRISE-SERVICE-1464',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1464',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1464.'
    },
    1465: {
        'service_name': 'ENTERPRISE-SERVICE-1465',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1465',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1465.'
    },
    1466: {
        'service_name': 'ENTERPRISE-SERVICE-1466',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1466',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1466.'
    },
    1467: {
        'service_name': 'ENTERPRISE-SERVICE-1467',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1467',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1467.'
    },
    1468: {
        'service_name': 'ENTERPRISE-SERVICE-1468',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1468',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1468.'
    },
    1469: {
        'service_name': 'ENTERPRISE-SERVICE-1469',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1469',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1469.'
    },
    1470: {
        'service_name': 'ENTERPRISE-SERVICE-1470',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1470',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1470.'
    },
    1471: {
        'service_name': 'ENTERPRISE-SERVICE-1471',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1471',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1471.'
    },
    1472: {
        'service_name': 'ENTERPRISE-SERVICE-1472',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1472',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1472.'
    },
    1473: {
        'service_name': 'ENTERPRISE-SERVICE-1473',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1473',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1473.'
    },
    1474: {
        'service_name': 'ENTERPRISE-SERVICE-1474',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1474',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1474.'
    },
    1475: {
        'service_name': 'ENTERPRISE-SERVICE-1475',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1475',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1475.'
    },
    1476: {
        'service_name': 'ENTERPRISE-SERVICE-1476',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1476',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1476.'
    },
    1477: {
        'service_name': 'ENTERPRISE-SERVICE-1477',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1477',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1477.'
    },
    1478: {
        'service_name': 'ENTERPRISE-SERVICE-1478',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1478',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1478.'
    },
    1479: {
        'service_name': 'ENTERPRISE-SERVICE-1479',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1479',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1479.'
    },
    1480: {
        'service_name': 'ENTERPRISE-SERVICE-1480',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1480',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1480.'
    },
    1481: {
        'service_name': 'ENTERPRISE-SERVICE-1481',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1481',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1481.'
    },
    1482: {
        'service_name': 'ENTERPRISE-SERVICE-1482',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1482',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1482.'
    },
    1483: {
        'service_name': 'ENTERPRISE-SERVICE-1483',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1483',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1483.'
    },
    1484: {
        'service_name': 'ENTERPRISE-SERVICE-1484',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1484',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1484.'
    },
    1485: {
        'service_name': 'ENTERPRISE-SERVICE-1485',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1485',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1485.'
    },
    1486: {
        'service_name': 'ENTERPRISE-SERVICE-1486',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1486',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1486.'
    },
    1487: {
        'service_name': 'ENTERPRISE-SERVICE-1487',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1487',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1487.'
    },
    1488: {
        'service_name': 'ENTERPRISE-SERVICE-1488',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1488',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1488.'
    },
    1489: {
        'service_name': 'ENTERPRISE-SERVICE-1489',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1489',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1489.'
    },
    1490: {
        'service_name': 'ENTERPRISE-SERVICE-1490',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1490',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1490.'
    },
    1491: {
        'service_name': 'ENTERPRISE-SERVICE-1491',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1491',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1491.'
    },
    1492: {
        'service_name': 'ENTERPRISE-SERVICE-1492',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1492',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1492.'
    },
    1493: {
        'service_name': 'ENTERPRISE-SERVICE-1493',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1493',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1493.'
    },
    1494: {
        'service_name': 'ENTERPRISE-SERVICE-1494',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1494',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1494.'
    },
    1495: {
        'service_name': 'ENTERPRISE-SERVICE-1495',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1495',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1495.'
    },
    1496: {
        'service_name': 'ENTERPRISE-SERVICE-1496',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1496',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1496.'
    },
    1497: {
        'service_name': 'ENTERPRISE-SERVICE-1497',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1497',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1497.'
    },
    1498: {
        'service_name': 'ENTERPRISE-SERVICE-1498',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1498',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1498.'
    },
    1499: {
        'service_name': 'ENTERPRISE-SERVICE-1499',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1499',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1499.'
    },
    1500: {
        'service_name': 'ENTERPRISE-SERVICE-1500',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1500',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1500.'
    },
    1501: {
        'service_name': 'ENTERPRISE-SERVICE-1501',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1501',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1501.'
    },
    1502: {
        'service_name': 'ENTERPRISE-SERVICE-1502',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1502',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1502.'
    },
    1503: {
        'service_name': 'ENTERPRISE-SERVICE-1503',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1503',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1503.'
    },
    1504: {
        'service_name': 'ENTERPRISE-SERVICE-1504',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1504',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1504.'
    },
    1505: {
        'service_name': 'ENTERPRISE-SERVICE-1505',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1505',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1505.'
    },
    1506: {
        'service_name': 'ENTERPRISE-SERVICE-1506',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1506',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1506.'
    },
    1507: {
        'service_name': 'ENTERPRISE-SERVICE-1507',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1507',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1507.'
    },
    1508: {
        'service_name': 'ENTERPRISE-SERVICE-1508',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1508',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1508.'
    },
    1509: {
        'service_name': 'ENTERPRISE-SERVICE-1509',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1509',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1509.'
    },
    1510: {
        'service_name': 'ENTERPRISE-SERVICE-1510',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1510',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1510.'
    },
    1511: {
        'service_name': 'ENTERPRISE-SERVICE-1511',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1511',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1511.'
    },
    1512: {
        'service_name': 'ENTERPRISE-SERVICE-1512',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1512',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1512.'
    },
    1513: {
        'service_name': 'ENTERPRISE-SERVICE-1513',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1513',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1513.'
    },
    1514: {
        'service_name': 'ENTERPRISE-SERVICE-1514',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1514',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1514.'
    },
    1515: {
        'service_name': 'ENTERPRISE-SERVICE-1515',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1515',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1515.'
    },
    1516: {
        'service_name': 'ENTERPRISE-SERVICE-1516',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1516',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1516.'
    },
    1517: {
        'service_name': 'ENTERPRISE-SERVICE-1517',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1517',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1517.'
    },
    1518: {
        'service_name': 'ENTERPRISE-SERVICE-1518',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1518',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1518.'
    },
    1519: {
        'service_name': 'ENTERPRISE-SERVICE-1519',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1519',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1519.'
    },
    1520: {
        'service_name': 'ENTERPRISE-SERVICE-1520',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1520',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1520.'
    },
    1522: {
        'service_name': 'ENTERPRISE-SERVICE-1522',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1522',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1522.'
    },
    1523: {
        'service_name': 'ENTERPRISE-SERVICE-1523',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1523',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1523.'
    },
    1524: {
        'service_name': 'ENTERPRISE-SERVICE-1524',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1524',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1524.'
    },
    1525: {
        'service_name': 'ENTERPRISE-SERVICE-1525',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1525',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1525.'
    },
    1526: {
        'service_name': 'ENTERPRISE-SERVICE-1526',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1526',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1526.'
    },
    1527: {
        'service_name': 'ENTERPRISE-SERVICE-1527',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1527',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1527.'
    },
    1528: {
        'service_name': 'ENTERPRISE-SERVICE-1528',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1528',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1528.'
    },
    1529: {
        'service_name': 'ENTERPRISE-SERVICE-1529',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1529',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1529.'
    },
    1530: {
        'service_name': 'ENTERPRISE-SERVICE-1530',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1530',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1530.'
    },
    1531: {
        'service_name': 'ENTERPRISE-SERVICE-1531',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1531',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1531.'
    },
    1532: {
        'service_name': 'ENTERPRISE-SERVICE-1532',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1532',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1532.'
    },
    1533: {
        'service_name': 'ENTERPRISE-SERVICE-1533',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1533',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1533.'
    },
    1534: {
        'service_name': 'ENTERPRISE-SERVICE-1534',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1534',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1534.'
    },
    1535: {
        'service_name': 'ENTERPRISE-SERVICE-1535',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1535',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1535.'
    },
    1536: {
        'service_name': 'ENTERPRISE-SERVICE-1536',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1536',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1536.'
    },
    1537: {
        'service_name': 'ENTERPRISE-SERVICE-1537',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1537',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1537.'
    },
    1538: {
        'service_name': 'ENTERPRISE-SERVICE-1538',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1538',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1538.'
    },
    1539: {
        'service_name': 'ENTERPRISE-SERVICE-1539',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1539',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1539.'
    },
    1540: {
        'service_name': 'ENTERPRISE-SERVICE-1540',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1540',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1540.'
    },
    1541: {
        'service_name': 'ENTERPRISE-SERVICE-1541',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1541',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1541.'
    },
    1542: {
        'service_name': 'ENTERPRISE-SERVICE-1542',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1542',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1542.'
    },
    1543: {
        'service_name': 'ENTERPRISE-SERVICE-1543',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1543',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1543.'
    },
    1544: {
        'service_name': 'ENTERPRISE-SERVICE-1544',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1544',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1544.'
    },
    1545: {
        'service_name': 'ENTERPRISE-SERVICE-1545',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1545',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1545.'
    },
    1546: {
        'service_name': 'ENTERPRISE-SERVICE-1546',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1546',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1546.'
    },
    1547: {
        'service_name': 'ENTERPRISE-SERVICE-1547',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1547',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1547.'
    },
    1548: {
        'service_name': 'ENTERPRISE-SERVICE-1548',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1548',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1548.'
    },
    1549: {
        'service_name': 'ENTERPRISE-SERVICE-1549',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1549',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1549.'
    },
    1550: {
        'service_name': 'ENTERPRISE-SERVICE-1550',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1550',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1550.'
    },
    1551: {
        'service_name': 'ENTERPRISE-SERVICE-1551',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1551',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1551.'
    },
    1552: {
        'service_name': 'ENTERPRISE-SERVICE-1552',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1552',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1552.'
    },
    1553: {
        'service_name': 'ENTERPRISE-SERVICE-1553',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1553',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1553.'
    },
    1554: {
        'service_name': 'ENTERPRISE-SERVICE-1554',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1554',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1554.'
    },
    1555: {
        'service_name': 'ENTERPRISE-SERVICE-1555',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1555',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1555.'
    },
    1556: {
        'service_name': 'ENTERPRISE-SERVICE-1556',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1556',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1556.'
    },
    1557: {
        'service_name': 'ENTERPRISE-SERVICE-1557',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1557',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1557.'
    },
    1558: {
        'service_name': 'ENTERPRISE-SERVICE-1558',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1558',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1558.'
    },
    1559: {
        'service_name': 'ENTERPRISE-SERVICE-1559',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1559',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1559.'
    },
    1560: {
        'service_name': 'ENTERPRISE-SERVICE-1560',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1560',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1560.'
    },
    1561: {
        'service_name': 'ENTERPRISE-SERVICE-1561',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1561',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1561.'
    },
    1562: {
        'service_name': 'ENTERPRISE-SERVICE-1562',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1562',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1562.'
    },
    1563: {
        'service_name': 'ENTERPRISE-SERVICE-1563',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1563',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1563.'
    },
    1564: {
        'service_name': 'ENTERPRISE-SERVICE-1564',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1564',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1564.'
    },
    1565: {
        'service_name': 'ENTERPRISE-SERVICE-1565',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1565',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1565.'
    },
    1566: {
        'service_name': 'ENTERPRISE-SERVICE-1566',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1566',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1566.'
    },
    1567: {
        'service_name': 'ENTERPRISE-SERVICE-1567',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1567',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1567.'
    },
    1568: {
        'service_name': 'ENTERPRISE-SERVICE-1568',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1568',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1568.'
    },
    1569: {
        'service_name': 'ENTERPRISE-SERVICE-1569',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1569',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1569.'
    },
    1570: {
        'service_name': 'ENTERPRISE-SERVICE-1570',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1570',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1570.'
    },
    1571: {
        'service_name': 'ENTERPRISE-SERVICE-1571',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1571',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1571.'
    },
    1572: {
        'service_name': 'ENTERPRISE-SERVICE-1572',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1572',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1572.'
    },
    1573: {
        'service_name': 'ENTERPRISE-SERVICE-1573',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1573',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1573.'
    },
    1574: {
        'service_name': 'ENTERPRISE-SERVICE-1574',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1574',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1574.'
    },
    1575: {
        'service_name': 'ENTERPRISE-SERVICE-1575',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1575',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1575.'
    },
    1576: {
        'service_name': 'ENTERPRISE-SERVICE-1576',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1576',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1576.'
    },
    1577: {
        'service_name': 'ENTERPRISE-SERVICE-1577',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1577',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1577.'
    },
    1578: {
        'service_name': 'ENTERPRISE-SERVICE-1578',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1578',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1578.'
    },
    1579: {
        'service_name': 'ENTERPRISE-SERVICE-1579',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1579',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1579.'
    },
    1580: {
        'service_name': 'ENTERPRISE-SERVICE-1580',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1580',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1580.'
    },
    1581: {
        'service_name': 'ENTERPRISE-SERVICE-1581',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1581',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1581.'
    },
    1582: {
        'service_name': 'ENTERPRISE-SERVICE-1582',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1582',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1582.'
    },
    1583: {
        'service_name': 'ENTERPRISE-SERVICE-1583',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1583',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1583.'
    },
    1584: {
        'service_name': 'ENTERPRISE-SERVICE-1584',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1584',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1584.'
    },
    1585: {
        'service_name': 'ENTERPRISE-SERVICE-1585',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1585',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1585.'
    },
    1586: {
        'service_name': 'ENTERPRISE-SERVICE-1586',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1586',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1586.'
    },
    1587: {
        'service_name': 'ENTERPRISE-SERVICE-1587',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1587',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1587.'
    },
    1588: {
        'service_name': 'ENTERPRISE-SERVICE-1588',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1588',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1588.'
    },
    1589: {
        'service_name': 'ENTERPRISE-SERVICE-1589',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1589',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1589.'
    },
    1590: {
        'service_name': 'ENTERPRISE-SERVICE-1590',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1590',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1590.'
    },
    1591: {
        'service_name': 'ENTERPRISE-SERVICE-1591',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1591',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1591.'
    },
    1592: {
        'service_name': 'ENTERPRISE-SERVICE-1592',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1592',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1592.'
    },
    1593: {
        'service_name': 'ENTERPRISE-SERVICE-1593',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1593',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1593.'
    },
    1594: {
        'service_name': 'ENTERPRISE-SERVICE-1594',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1594',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1594.'
    },
    1595: {
        'service_name': 'ENTERPRISE-SERVICE-1595',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1595',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1595.'
    },
    1596: {
        'service_name': 'ENTERPRISE-SERVICE-1596',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1596',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1596.'
    },
    1597: {
        'service_name': 'ENTERPRISE-SERVICE-1597',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1597',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1597.'
    },
    1598: {
        'service_name': 'ENTERPRISE-SERVICE-1598',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1598',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1598.'
    },
    1599: {
        'service_name': 'ENTERPRISE-SERVICE-1599',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1599',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1599.'
    },
    1600: {
        'service_name': 'ENTERPRISE-SERVICE-1600',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1600',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1600.'
    },
    1601: {
        'service_name': 'ENTERPRISE-SERVICE-1601',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1601',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1601.'
    },
    1602: {
        'service_name': 'ENTERPRISE-SERVICE-1602',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1602',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1602.'
    },
    1603: {
        'service_name': 'ENTERPRISE-SERVICE-1603',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1603',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1603.'
    },
    1604: {
        'service_name': 'ENTERPRISE-SERVICE-1604',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1604',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1604.'
    },
    1605: {
        'service_name': 'ENTERPRISE-SERVICE-1605',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1605',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1605.'
    },
    1606: {
        'service_name': 'ENTERPRISE-SERVICE-1606',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1606',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1606.'
    },
    1607: {
        'service_name': 'ENTERPRISE-SERVICE-1607',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1607',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1607.'
    },
    1608: {
        'service_name': 'ENTERPRISE-SERVICE-1608',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1608',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1608.'
    },
    1609: {
        'service_name': 'ENTERPRISE-SERVICE-1609',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1609',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1609.'
    },
    1610: {
        'service_name': 'ENTERPRISE-SERVICE-1610',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1610',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1610.'
    },
    1611: {
        'service_name': 'ENTERPRISE-SERVICE-1611',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1611',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1611.'
    },
    1612: {
        'service_name': 'ENTERPRISE-SERVICE-1612',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1612',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1612.'
    },
    1613: {
        'service_name': 'ENTERPRISE-SERVICE-1613',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1613',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1613.'
    },
    1614: {
        'service_name': 'ENTERPRISE-SERVICE-1614',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1614',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1614.'
    },
    1615: {
        'service_name': 'ENTERPRISE-SERVICE-1615',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1615',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1615.'
    },
    1616: {
        'service_name': 'ENTERPRISE-SERVICE-1616',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1616',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1616.'
    },
    1617: {
        'service_name': 'ENTERPRISE-SERVICE-1617',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1617',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1617.'
    },
    1618: {
        'service_name': 'ENTERPRISE-SERVICE-1618',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1618',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1618.'
    },
    1619: {
        'service_name': 'ENTERPRISE-SERVICE-1619',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1619',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1619.'
    },
    1620: {
        'service_name': 'ENTERPRISE-SERVICE-1620',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1620',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1620.'
    },
    1621: {
        'service_name': 'ENTERPRISE-SERVICE-1621',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1621',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1621.'
    },
    1622: {
        'service_name': 'ENTERPRISE-SERVICE-1622',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1622',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1622.'
    },
    1623: {
        'service_name': 'ENTERPRISE-SERVICE-1623',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1623',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1623.'
    },
    1624: {
        'service_name': 'ENTERPRISE-SERVICE-1624',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1624',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1624.'
    },
    1625: {
        'service_name': 'ENTERPRISE-SERVICE-1625',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1625',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1625.'
    },
    1626: {
        'service_name': 'ENTERPRISE-SERVICE-1626',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1626',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1626.'
    },
    1627: {
        'service_name': 'ENTERPRISE-SERVICE-1627',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1627',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1627.'
    },
    1628: {
        'service_name': 'ENTERPRISE-SERVICE-1628',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1628',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1628.'
    },
    1629: {
        'service_name': 'ENTERPRISE-SERVICE-1629',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1629',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1629.'
    },
    1630: {
        'service_name': 'ENTERPRISE-SERVICE-1630',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1630',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1630.'
    },
    1631: {
        'service_name': 'ENTERPRISE-SERVICE-1631',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1631',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1631.'
    },
    1632: {
        'service_name': 'ENTERPRISE-SERVICE-1632',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1632',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1632.'
    },
    1633: {
        'service_name': 'ENTERPRISE-SERVICE-1633',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1633',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1633.'
    },
    1634: {
        'service_name': 'ENTERPRISE-SERVICE-1634',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1634',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1634.'
    },
    1635: {
        'service_name': 'ENTERPRISE-SERVICE-1635',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1635',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1635.'
    },
    1636: {
        'service_name': 'ENTERPRISE-SERVICE-1636',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1636',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1636.'
    },
    1637: {
        'service_name': 'ENTERPRISE-SERVICE-1637',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1637',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1637.'
    },
    1638: {
        'service_name': 'ENTERPRISE-SERVICE-1638',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1638',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1638.'
    },
    1639: {
        'service_name': 'ENTERPRISE-SERVICE-1639',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1639',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1639.'
    },
    1640: {
        'service_name': 'ENTERPRISE-SERVICE-1640',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1640',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1640.'
    },
    1641: {
        'service_name': 'ENTERPRISE-SERVICE-1641',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1641',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1641.'
    },
    1642: {
        'service_name': 'ENTERPRISE-SERVICE-1642',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1642',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1642.'
    },
    1643: {
        'service_name': 'ENTERPRISE-SERVICE-1643',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1643',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1643.'
    },
    1644: {
        'service_name': 'ENTERPRISE-SERVICE-1644',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1644',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1644.'
    },
    1645: {
        'service_name': 'ENTERPRISE-SERVICE-1645',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1645',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1645.'
    },
    1646: {
        'service_name': 'ENTERPRISE-SERVICE-1646',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1646',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1646.'
    },
    1647: {
        'service_name': 'ENTERPRISE-SERVICE-1647',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1647',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1647.'
    },
    1648: {
        'service_name': 'ENTERPRISE-SERVICE-1648',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1648',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1648.'
    },
    1649: {
        'service_name': 'ENTERPRISE-SERVICE-1649',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1649',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1649.'
    },
    1650: {
        'service_name': 'ENTERPRISE-SERVICE-1650',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1650',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1650.'
    },
    1651: {
        'service_name': 'ENTERPRISE-SERVICE-1651',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1651',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1651.'
    },
    1652: {
        'service_name': 'ENTERPRISE-SERVICE-1652',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1652',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1652.'
    },
    1653: {
        'service_name': 'ENTERPRISE-SERVICE-1653',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1653',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1653.'
    },
    1654: {
        'service_name': 'ENTERPRISE-SERVICE-1654',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1654',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1654.'
    },
    1655: {
        'service_name': 'ENTERPRISE-SERVICE-1655',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1655',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1655.'
    },
    1656: {
        'service_name': 'ENTERPRISE-SERVICE-1656',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1656',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1656.'
    },
    1657: {
        'service_name': 'ENTERPRISE-SERVICE-1657',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1657',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1657.'
    },
    1658: {
        'service_name': 'ENTERPRISE-SERVICE-1658',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1658',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1658.'
    },
    1659: {
        'service_name': 'ENTERPRISE-SERVICE-1659',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1659',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1659.'
    },
    1660: {
        'service_name': 'ENTERPRISE-SERVICE-1660',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1660',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1660.'
    },
    1661: {
        'service_name': 'ENTERPRISE-SERVICE-1661',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1661',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1661.'
    },
    1662: {
        'service_name': 'ENTERPRISE-SERVICE-1662',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1662',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1662.'
    },
    1663: {
        'service_name': 'ENTERPRISE-SERVICE-1663',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1663',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1663.'
    },
    1664: {
        'service_name': 'ENTERPRISE-SERVICE-1664',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1664',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1664.'
    },
    1665: {
        'service_name': 'ENTERPRISE-SERVICE-1665',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1665',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1665.'
    },
    1666: {
        'service_name': 'ENTERPRISE-SERVICE-1666',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1666',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1666.'
    },
    1667: {
        'service_name': 'ENTERPRISE-SERVICE-1667',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1667',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1667.'
    },
    1668: {
        'service_name': 'ENTERPRISE-SERVICE-1668',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1668',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1668.'
    },
    1669: {
        'service_name': 'ENTERPRISE-SERVICE-1669',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1669',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1669.'
    },
    1670: {
        'service_name': 'ENTERPRISE-SERVICE-1670',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1670',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1670.'
    },
    1671: {
        'service_name': 'ENTERPRISE-SERVICE-1671',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1671',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1671.'
    },
    1672: {
        'service_name': 'ENTERPRISE-SERVICE-1672',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1672',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1672.'
    },
    1673: {
        'service_name': 'ENTERPRISE-SERVICE-1673',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1673',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1673.'
    },
    1674: {
        'service_name': 'ENTERPRISE-SERVICE-1674',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1674',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1674.'
    },
    1675: {
        'service_name': 'ENTERPRISE-SERVICE-1675',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1675',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1675.'
    },
    1676: {
        'service_name': 'ENTERPRISE-SERVICE-1676',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1676',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1676.'
    },
    1677: {
        'service_name': 'ENTERPRISE-SERVICE-1677',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1677',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1677.'
    },
    1678: {
        'service_name': 'ENTERPRISE-SERVICE-1678',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1678',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1678.'
    },
    1679: {
        'service_name': 'ENTERPRISE-SERVICE-1679',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1679',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1679.'
    },
    1680: {
        'service_name': 'ENTERPRISE-SERVICE-1680',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1680',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1680.'
    },
    1681: {
        'service_name': 'ENTERPRISE-SERVICE-1681',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1681',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1681.'
    },
    1682: {
        'service_name': 'ENTERPRISE-SERVICE-1682',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1682',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1682.'
    },
    1683: {
        'service_name': 'ENTERPRISE-SERVICE-1683',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1683',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1683.'
    },
    1684: {
        'service_name': 'ENTERPRISE-SERVICE-1684',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1684',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1684.'
    },
    1685: {
        'service_name': 'ENTERPRISE-SERVICE-1685',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1685',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1685.'
    },
    1686: {
        'service_name': 'ENTERPRISE-SERVICE-1686',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1686',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1686.'
    },
    1687: {
        'service_name': 'ENTERPRISE-SERVICE-1687',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1687',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1687.'
    },
    1688: {
        'service_name': 'ENTERPRISE-SERVICE-1688',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1688',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1688.'
    },
    1689: {
        'service_name': 'ENTERPRISE-SERVICE-1689',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1689',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1689.'
    },
    1690: {
        'service_name': 'ENTERPRISE-SERVICE-1690',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1690',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1690.'
    },
    1691: {
        'service_name': 'ENTERPRISE-SERVICE-1691',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1691',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1691.'
    },
    1692: {
        'service_name': 'ENTERPRISE-SERVICE-1692',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1692',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1692.'
    },
    1693: {
        'service_name': 'ENTERPRISE-SERVICE-1693',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1693',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1693.'
    },
    1694: {
        'service_name': 'ENTERPRISE-SERVICE-1694',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1694',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1694.'
    },
    1695: {
        'service_name': 'ENTERPRISE-SERVICE-1695',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1695',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1695.'
    },
    1696: {
        'service_name': 'ENTERPRISE-SERVICE-1696',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1696',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1696.'
    },
    1697: {
        'service_name': 'ENTERPRISE-SERVICE-1697',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1697',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1697.'
    },
    1698: {
        'service_name': 'ENTERPRISE-SERVICE-1698',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1698',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1698.'
    },
    1699: {
        'service_name': 'ENTERPRISE-SERVICE-1699',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1699',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1699.'
    },
    1700: {
        'service_name': 'ENTERPRISE-SERVICE-1700',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1700',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1700.'
    },
    1701: {
        'service_name': 'ENTERPRISE-SERVICE-1701',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1701',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1701.'
    },
    1702: {
        'service_name': 'ENTERPRISE-SERVICE-1702',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1702',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1702.'
    },
    1703: {
        'service_name': 'ENTERPRISE-SERVICE-1703',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1703',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1703.'
    },
    1704: {
        'service_name': 'ENTERPRISE-SERVICE-1704',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1704',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1704.'
    },
    1705: {
        'service_name': 'ENTERPRISE-SERVICE-1705',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1705',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1705.'
    },
    1706: {
        'service_name': 'ENTERPRISE-SERVICE-1706',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1706',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1706.'
    },
    1707: {
        'service_name': 'ENTERPRISE-SERVICE-1707',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1707',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1707.'
    },
    1708: {
        'service_name': 'ENTERPRISE-SERVICE-1708',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1708',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1708.'
    },
    1709: {
        'service_name': 'ENTERPRISE-SERVICE-1709',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1709',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1709.'
    },
    1710: {
        'service_name': 'ENTERPRISE-SERVICE-1710',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1710',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1710.'
    },
    1711: {
        'service_name': 'ENTERPRISE-SERVICE-1711',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1711',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1711.'
    },
    1712: {
        'service_name': 'ENTERPRISE-SERVICE-1712',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1712',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1712.'
    },
    1713: {
        'service_name': 'ENTERPRISE-SERVICE-1713',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1713',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1713.'
    },
    1714: {
        'service_name': 'ENTERPRISE-SERVICE-1714',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1714',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1714.'
    },
    1715: {
        'service_name': 'ENTERPRISE-SERVICE-1715',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1715',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1715.'
    },
    1716: {
        'service_name': 'ENTERPRISE-SERVICE-1716',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1716',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1716.'
    },
    1717: {
        'service_name': 'ENTERPRISE-SERVICE-1717',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1717',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1717.'
    },
    1718: {
        'service_name': 'ENTERPRISE-SERVICE-1718',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1718',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1718.'
    },
    1719: {
        'service_name': 'ENTERPRISE-SERVICE-1719',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1719',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1719.'
    },
    1720: {
        'service_name': 'ENTERPRISE-SERVICE-1720',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1720',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1720.'
    },
    1721: {
        'service_name': 'ENTERPRISE-SERVICE-1721',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1721',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1721.'
    },
    1722: {
        'service_name': 'ENTERPRISE-SERVICE-1722',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1722',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1722.'
    },
    1723: {
        'service_name': 'ENTERPRISE-SERVICE-1723',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1723',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1723.'
    },
    1724: {
        'service_name': 'ENTERPRISE-SERVICE-1724',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1724',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1724.'
    },
    1725: {
        'service_name': 'ENTERPRISE-SERVICE-1725',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1725',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1725.'
    },
    1726: {
        'service_name': 'ENTERPRISE-SERVICE-1726',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1726',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1726.'
    },
    1727: {
        'service_name': 'ENTERPRISE-SERVICE-1727',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1727',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1727.'
    },
    1728: {
        'service_name': 'ENTERPRISE-SERVICE-1728',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1728',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1728.'
    },
    1729: {
        'service_name': 'ENTERPRISE-SERVICE-1729',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1729',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1729.'
    },
    1730: {
        'service_name': 'ENTERPRISE-SERVICE-1730',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1730',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1730.'
    },
    1731: {
        'service_name': 'ENTERPRISE-SERVICE-1731',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1731',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1731.'
    },
    1732: {
        'service_name': 'ENTERPRISE-SERVICE-1732',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1732',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1732.'
    },
    1733: {
        'service_name': 'ENTERPRISE-SERVICE-1733',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1733',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1733.'
    },
    1734: {
        'service_name': 'ENTERPRISE-SERVICE-1734',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1734',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1734.'
    },
    1735: {
        'service_name': 'ENTERPRISE-SERVICE-1735',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1735',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1735.'
    },
    1736: {
        'service_name': 'ENTERPRISE-SERVICE-1736',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1736',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1736.'
    },
    1737: {
        'service_name': 'ENTERPRISE-SERVICE-1737',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1737',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1737.'
    },
    1738: {
        'service_name': 'ENTERPRISE-SERVICE-1738',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1738',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1738.'
    },
    1739: {
        'service_name': 'ENTERPRISE-SERVICE-1739',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1739',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1739.'
    },
    1740: {
        'service_name': 'ENTERPRISE-SERVICE-1740',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1740',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1740.'
    },
    1741: {
        'service_name': 'ENTERPRISE-SERVICE-1741',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1741',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1741.'
    },
    1742: {
        'service_name': 'ENTERPRISE-SERVICE-1742',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1742',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1742.'
    },
    1743: {
        'service_name': 'ENTERPRISE-SERVICE-1743',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1743',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1743.'
    },
    1744: {
        'service_name': 'ENTERPRISE-SERVICE-1744',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1744',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1744.'
    },
    1745: {
        'service_name': 'ENTERPRISE-SERVICE-1745',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1745',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1745.'
    },
    1746: {
        'service_name': 'ENTERPRISE-SERVICE-1746',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1746',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1746.'
    },
    1747: {
        'service_name': 'ENTERPRISE-SERVICE-1747',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1747',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1747.'
    },
    1748: {
        'service_name': 'ENTERPRISE-SERVICE-1748',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1748',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1748.'
    },
    1749: {
        'service_name': 'ENTERPRISE-SERVICE-1749',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1749',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1749.'
    },
    1750: {
        'service_name': 'ENTERPRISE-SERVICE-1750',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1750',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1750.'
    },
    1751: {
        'service_name': 'ENTERPRISE-SERVICE-1751',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1751',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1751.'
    },
    1752: {
        'service_name': 'ENTERPRISE-SERVICE-1752',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1752',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1752.'
    },
    1753: {
        'service_name': 'ENTERPRISE-SERVICE-1753',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1753',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1753.'
    },
    1754: {
        'service_name': 'ENTERPRISE-SERVICE-1754',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1754',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1754.'
    },
    1755: {
        'service_name': 'ENTERPRISE-SERVICE-1755',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1755',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1755.'
    },
    1756: {
        'service_name': 'ENTERPRISE-SERVICE-1756',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1756',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1756.'
    },
    1757: {
        'service_name': 'ENTERPRISE-SERVICE-1757',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1757',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1757.'
    },
    1758: {
        'service_name': 'ENTERPRISE-SERVICE-1758',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1758',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1758.'
    },
    1759: {
        'service_name': 'ENTERPRISE-SERVICE-1759',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1759',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1759.'
    },
    1760: {
        'service_name': 'ENTERPRISE-SERVICE-1760',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1760',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1760.'
    },
    1761: {
        'service_name': 'ENTERPRISE-SERVICE-1761',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1761',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1761.'
    },
    1762: {
        'service_name': 'ENTERPRISE-SERVICE-1762',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1762',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1762.'
    },
    1763: {
        'service_name': 'ENTERPRISE-SERVICE-1763',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1763',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1763.'
    },
    1764: {
        'service_name': 'ENTERPRISE-SERVICE-1764',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1764',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1764.'
    },
    1765: {
        'service_name': 'ENTERPRISE-SERVICE-1765',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1765',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1765.'
    },
    1766: {
        'service_name': 'ENTERPRISE-SERVICE-1766',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1766',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1766.'
    },
    1767: {
        'service_name': 'ENTERPRISE-SERVICE-1767',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1767',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1767.'
    },
    1768: {
        'service_name': 'ENTERPRISE-SERVICE-1768',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1768',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1768.'
    },
    1769: {
        'service_name': 'ENTERPRISE-SERVICE-1769',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1769',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1769.'
    },
    1770: {
        'service_name': 'ENTERPRISE-SERVICE-1770',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1770',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1770.'
    },
    1771: {
        'service_name': 'ENTERPRISE-SERVICE-1771',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1771',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1771.'
    },
    1772: {
        'service_name': 'ENTERPRISE-SERVICE-1772',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1772',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1772.'
    },
    1773: {
        'service_name': 'ENTERPRISE-SERVICE-1773',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1773',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1773.'
    },
    1774: {
        'service_name': 'ENTERPRISE-SERVICE-1774',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1774',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1774.'
    },
    1775: {
        'service_name': 'ENTERPRISE-SERVICE-1775',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1775',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1775.'
    },
    1776: {
        'service_name': 'ENTERPRISE-SERVICE-1776',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1776',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1776.'
    },
    1777: {
        'service_name': 'ENTERPRISE-SERVICE-1777',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1777',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1777.'
    },
    1778: {
        'service_name': 'ENTERPRISE-SERVICE-1778',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1778',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1778.'
    },
    1779: {
        'service_name': 'ENTERPRISE-SERVICE-1779',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1779',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1779.'
    },
    1780: {
        'service_name': 'ENTERPRISE-SERVICE-1780',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1780',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1780.'
    },
    1781: {
        'service_name': 'ENTERPRISE-SERVICE-1781',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1781',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1781.'
    },
    1782: {
        'service_name': 'ENTERPRISE-SERVICE-1782',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1782',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1782.'
    },
    1783: {
        'service_name': 'ENTERPRISE-SERVICE-1783',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1783',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1783.'
    },
    1784: {
        'service_name': 'ENTERPRISE-SERVICE-1784',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1784',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1784.'
    },
    1785: {
        'service_name': 'ENTERPRISE-SERVICE-1785',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1785',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1785.'
    },
    1786: {
        'service_name': 'ENTERPRISE-SERVICE-1786',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1786',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1786.'
    },
    1787: {
        'service_name': 'ENTERPRISE-SERVICE-1787',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1787',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1787.'
    },
    1788: {
        'service_name': 'ENTERPRISE-SERVICE-1788',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1788',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1788.'
    },
    1789: {
        'service_name': 'ENTERPRISE-SERVICE-1789',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1789',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1789.'
    },
    1790: {
        'service_name': 'ENTERPRISE-SERVICE-1790',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1790',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1790.'
    },
    1791: {
        'service_name': 'ENTERPRISE-SERVICE-1791',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1791',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1791.'
    },
    1792: {
        'service_name': 'ENTERPRISE-SERVICE-1792',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1792',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1792.'
    },
    1793: {
        'service_name': 'ENTERPRISE-SERVICE-1793',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1793',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1793.'
    },
    1794: {
        'service_name': 'ENTERPRISE-SERVICE-1794',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1794',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1794.'
    },
    1795: {
        'service_name': 'ENTERPRISE-SERVICE-1795',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1795',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1795.'
    },
    1796: {
        'service_name': 'ENTERPRISE-SERVICE-1796',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1796',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1796.'
    },
    1797: {
        'service_name': 'ENTERPRISE-SERVICE-1797',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1797',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1797.'
    },
    1798: {
        'service_name': 'ENTERPRISE-SERVICE-1798',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1798',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1798.'
    },
    1799: {
        'service_name': 'ENTERPRISE-SERVICE-1799',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1799',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1799.'
    },
    1800: {
        'service_name': 'ENTERPRISE-SERVICE-1800',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1800',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1800.'
    },
    1801: {
        'service_name': 'ENTERPRISE-SERVICE-1801',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1801',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1801.'
    },
    1802: {
        'service_name': 'ENTERPRISE-SERVICE-1802',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1802',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1802.'
    },
    1803: {
        'service_name': 'ENTERPRISE-SERVICE-1803',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1803',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1803.'
    },
    1804: {
        'service_name': 'ENTERPRISE-SERVICE-1804',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1804',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1804.'
    },
    1805: {
        'service_name': 'ENTERPRISE-SERVICE-1805',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1805',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1805.'
    },
    1806: {
        'service_name': 'ENTERPRISE-SERVICE-1806',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1806',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1806.'
    },
    1807: {
        'service_name': 'ENTERPRISE-SERVICE-1807',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1807',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1807.'
    },
    1808: {
        'service_name': 'ENTERPRISE-SERVICE-1808',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1808',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1808.'
    },
    1809: {
        'service_name': 'ENTERPRISE-SERVICE-1809',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1809',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1809.'
    },
    1810: {
        'service_name': 'ENTERPRISE-SERVICE-1810',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1810',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1810.'
    },
    1811: {
        'service_name': 'ENTERPRISE-SERVICE-1811',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1811',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1811.'
    },
    1812: {
        'service_name': 'ENTERPRISE-SERVICE-1812',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1812',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1812.'
    },
    1813: {
        'service_name': 'ENTERPRISE-SERVICE-1813',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1813',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1813.'
    },
    1814: {
        'service_name': 'ENTERPRISE-SERVICE-1814',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1814',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1814.'
    },
    1815: {
        'service_name': 'ENTERPRISE-SERVICE-1815',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1815',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1815.'
    },
    1816: {
        'service_name': 'ENTERPRISE-SERVICE-1816',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1816',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1816.'
    },
    1817: {
        'service_name': 'ENTERPRISE-SERVICE-1817',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1817',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1817.'
    },
    1818: {
        'service_name': 'ENTERPRISE-SERVICE-1818',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1818',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1818.'
    },
    1819: {
        'service_name': 'ENTERPRISE-SERVICE-1819',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1819',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1819.'
    },
    1820: {
        'service_name': 'ENTERPRISE-SERVICE-1820',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1820',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1820.'
    },
    1821: {
        'service_name': 'ENTERPRISE-SERVICE-1821',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1821',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1821.'
    },
    1822: {
        'service_name': 'ENTERPRISE-SERVICE-1822',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1822',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1822.'
    },
    1823: {
        'service_name': 'ENTERPRISE-SERVICE-1823',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1823',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1823.'
    },
    1824: {
        'service_name': 'ENTERPRISE-SERVICE-1824',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1824',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1824.'
    },
    1825: {
        'service_name': 'ENTERPRISE-SERVICE-1825',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1825',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1825.'
    },
    1826: {
        'service_name': 'ENTERPRISE-SERVICE-1826',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1826',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1826.'
    },
    1827: {
        'service_name': 'ENTERPRISE-SERVICE-1827',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1827',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1827.'
    },
    1828: {
        'service_name': 'ENTERPRISE-SERVICE-1828',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1828',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1828.'
    },
    1829: {
        'service_name': 'ENTERPRISE-SERVICE-1829',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1829',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1829.'
    },
    1830: {
        'service_name': 'ENTERPRISE-SERVICE-1830',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1830',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1830.'
    },
    1831: {
        'service_name': 'ENTERPRISE-SERVICE-1831',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1831',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1831.'
    },
    1832: {
        'service_name': 'ENTERPRISE-SERVICE-1832',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1832',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1832.'
    },
    1833: {
        'service_name': 'ENTERPRISE-SERVICE-1833',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1833',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1833.'
    },
    1834: {
        'service_name': 'ENTERPRISE-SERVICE-1834',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1834',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1834.'
    },
    1835: {
        'service_name': 'ENTERPRISE-SERVICE-1835',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1835',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1835.'
    },
    1836: {
        'service_name': 'ENTERPRISE-SERVICE-1836',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1836',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1836.'
    },
    1837: {
        'service_name': 'ENTERPRISE-SERVICE-1837',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1837',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1837.'
    },
    1838: {
        'service_name': 'ENTERPRISE-SERVICE-1838',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1838',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1838.'
    },
    1839: {
        'service_name': 'ENTERPRISE-SERVICE-1839',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1839',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1839.'
    },
    1840: {
        'service_name': 'ENTERPRISE-SERVICE-1840',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1840',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1840.'
    },
    1841: {
        'service_name': 'ENTERPRISE-SERVICE-1841',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1841',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1841.'
    },
    1842: {
        'service_name': 'ENTERPRISE-SERVICE-1842',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1842',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1842.'
    },
    1843: {
        'service_name': 'ENTERPRISE-SERVICE-1843',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1843',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1843.'
    },
    1844: {
        'service_name': 'ENTERPRISE-SERVICE-1844',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1844',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1844.'
    },
    1845: {
        'service_name': 'ENTERPRISE-SERVICE-1845',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1845',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1845.'
    },
    1846: {
        'service_name': 'ENTERPRISE-SERVICE-1846',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1846',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1846.'
    },
    1847: {
        'service_name': 'ENTERPRISE-SERVICE-1847',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1847',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1847.'
    },
    1848: {
        'service_name': 'ENTERPRISE-SERVICE-1848',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1848',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1848.'
    },
    1849: {
        'service_name': 'ENTERPRISE-SERVICE-1849',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1849',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1849.'
    },
    1850: {
        'service_name': 'ENTERPRISE-SERVICE-1850',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1850',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1850.'
    },
    1851: {
        'service_name': 'ENTERPRISE-SERVICE-1851',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1851',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1851.'
    },
    1852: {
        'service_name': 'ENTERPRISE-SERVICE-1852',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1852',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1852.'
    },
    1853: {
        'service_name': 'ENTERPRISE-SERVICE-1853',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1853',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1853.'
    },
    1854: {
        'service_name': 'ENTERPRISE-SERVICE-1854',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1854',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1854.'
    },
    1855: {
        'service_name': 'ENTERPRISE-SERVICE-1855',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1855',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1855.'
    },
    1856: {
        'service_name': 'ENTERPRISE-SERVICE-1856',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1856',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1856.'
    },
    1857: {
        'service_name': 'ENTERPRISE-SERVICE-1857',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1857',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1857.'
    },
    1858: {
        'service_name': 'ENTERPRISE-SERVICE-1858',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1858',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1858.'
    },
    1859: {
        'service_name': 'ENTERPRISE-SERVICE-1859',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1859',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1859.'
    },
    1860: {
        'service_name': 'ENTERPRISE-SERVICE-1860',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1860',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1860.'
    },
    1861: {
        'service_name': 'ENTERPRISE-SERVICE-1861',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1861',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1861.'
    },
    1862: {
        'service_name': 'ENTERPRISE-SERVICE-1862',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1862',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1862.'
    },
    1863: {
        'service_name': 'ENTERPRISE-SERVICE-1863',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1863',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1863.'
    },
    1864: {
        'service_name': 'ENTERPRISE-SERVICE-1864',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1864',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1864.'
    },
    1865: {
        'service_name': 'ENTERPRISE-SERVICE-1865',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1865',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1865.'
    },
    1866: {
        'service_name': 'ENTERPRISE-SERVICE-1866',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1866',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1866.'
    },
    1867: {
        'service_name': 'ENTERPRISE-SERVICE-1867',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1867',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1867.'
    },
    1868: {
        'service_name': 'ENTERPRISE-SERVICE-1868',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1868',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1868.'
    },
    1869: {
        'service_name': 'ENTERPRISE-SERVICE-1869',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1869',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1869.'
    },
    1870: {
        'service_name': 'ENTERPRISE-SERVICE-1870',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1870',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1870.'
    },
    1871: {
        'service_name': 'ENTERPRISE-SERVICE-1871',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1871',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1871.'
    },
    1872: {
        'service_name': 'ENTERPRISE-SERVICE-1872',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1872',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1872.'
    },
    1873: {
        'service_name': 'ENTERPRISE-SERVICE-1873',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1873',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1873.'
    },
    1874: {
        'service_name': 'ENTERPRISE-SERVICE-1874',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1874',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1874.'
    },
    1875: {
        'service_name': 'ENTERPRISE-SERVICE-1875',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1875',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1875.'
    },
    1876: {
        'service_name': 'ENTERPRISE-SERVICE-1876',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1876',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1876.'
    },
    1877: {
        'service_name': 'ENTERPRISE-SERVICE-1877',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1877',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1877.'
    },
    1878: {
        'service_name': 'ENTERPRISE-SERVICE-1878',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1878',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1878.'
    },
    1879: {
        'service_name': 'ENTERPRISE-SERVICE-1879',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1879',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1879.'
    },
    1880: {
        'service_name': 'ENTERPRISE-SERVICE-1880',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1880',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1880.'
    },
    1881: {
        'service_name': 'ENTERPRISE-SERVICE-1881',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1881',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1881.'
    },
    1882: {
        'service_name': 'ENTERPRISE-SERVICE-1882',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1882',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1882.'
    },
    1883: {
        'service_name': 'ENTERPRISE-SERVICE-1883',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1883',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1883.'
    },
    1884: {
        'service_name': 'ENTERPRISE-SERVICE-1884',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1884',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1884.'
    },
    1885: {
        'service_name': 'ENTERPRISE-SERVICE-1885',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1885',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1885.'
    },
    1886: {
        'service_name': 'ENTERPRISE-SERVICE-1886',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1886',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1886.'
    },
    1887: {
        'service_name': 'ENTERPRISE-SERVICE-1887',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1887',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1887.'
    },
    1888: {
        'service_name': 'ENTERPRISE-SERVICE-1888',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1888',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1888.'
    },
    1889: {
        'service_name': 'ENTERPRISE-SERVICE-1889',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1889',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1889.'
    },
    1890: {
        'service_name': 'ENTERPRISE-SERVICE-1890',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1890',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1890.'
    },
    1891: {
        'service_name': 'ENTERPRISE-SERVICE-1891',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1891',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1891.'
    },
    1892: {
        'service_name': 'ENTERPRISE-SERVICE-1892',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1892',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1892.'
    },
    1893: {
        'service_name': 'ENTERPRISE-SERVICE-1893',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1893',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1893.'
    },
    1894: {
        'service_name': 'ENTERPRISE-SERVICE-1894',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1894',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1894.'
    },
    1895: {
        'service_name': 'ENTERPRISE-SERVICE-1895',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1895',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1895.'
    },
    1896: {
        'service_name': 'ENTERPRISE-SERVICE-1896',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1896',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1896.'
    },
    1897: {
        'service_name': 'ENTERPRISE-SERVICE-1897',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1897',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1897.'
    },
    1898: {
        'service_name': 'ENTERPRISE-SERVICE-1898',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1898',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1898.'
    },
    1899: {
        'service_name': 'ENTERPRISE-SERVICE-1899',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1899',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1899.'
    },
    1900: {
        'service_name': 'ENTERPRISE-SERVICE-1900',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1900',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1900.'
    },
    1901: {
        'service_name': 'ENTERPRISE-SERVICE-1901',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1901',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1901.'
    },
    1902: {
        'service_name': 'ENTERPRISE-SERVICE-1902',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1902',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1902.'
    },
    1903: {
        'service_name': 'ENTERPRISE-SERVICE-1903',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1903',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1903.'
    },
    1904: {
        'service_name': 'ENTERPRISE-SERVICE-1904',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1904',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1904.'
    },
    1905: {
        'service_name': 'ENTERPRISE-SERVICE-1905',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1905',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1905.'
    },
    1906: {
        'service_name': 'ENTERPRISE-SERVICE-1906',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1906',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1906.'
    },
    1907: {
        'service_name': 'ENTERPRISE-SERVICE-1907',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1907',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1907.'
    },
    1908: {
        'service_name': 'ENTERPRISE-SERVICE-1908',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1908',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1908.'
    },
    1909: {
        'service_name': 'ENTERPRISE-SERVICE-1909',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1909',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1909.'
    },
    1910: {
        'service_name': 'ENTERPRISE-SERVICE-1910',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1910',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1910.'
    },
    1911: {
        'service_name': 'ENTERPRISE-SERVICE-1911',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1911',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1911.'
    },
    1912: {
        'service_name': 'ENTERPRISE-SERVICE-1912',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1912',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1912.'
    },
    1913: {
        'service_name': 'ENTERPRISE-SERVICE-1913',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1913',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1913.'
    },
    1914: {
        'service_name': 'ENTERPRISE-SERVICE-1914',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1914',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1914.'
    },
    1915: {
        'service_name': 'ENTERPRISE-SERVICE-1915',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1915',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1915.'
    },
    1916: {
        'service_name': 'ENTERPRISE-SERVICE-1916',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1916',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1916.'
    },
    1917: {
        'service_name': 'ENTERPRISE-SERVICE-1917',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1917',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1917.'
    },
    1918: {
        'service_name': 'ENTERPRISE-SERVICE-1918',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1918',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1918.'
    },
    1919: {
        'service_name': 'ENTERPRISE-SERVICE-1919',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1919',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1919.'
    },
    1920: {
        'service_name': 'ENTERPRISE-SERVICE-1920',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1920',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1920.'
    },
    1921: {
        'service_name': 'ENTERPRISE-SERVICE-1921',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1921',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1921.'
    },
    1922: {
        'service_name': 'ENTERPRISE-SERVICE-1922',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1922',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1922.'
    },
    1923: {
        'service_name': 'ENTERPRISE-SERVICE-1923',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1923',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1923.'
    },
    1924: {
        'service_name': 'ENTERPRISE-SERVICE-1924',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1924',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1924.'
    },
    1925: {
        'service_name': 'ENTERPRISE-SERVICE-1925',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1925',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1925.'
    },
    1926: {
        'service_name': 'ENTERPRISE-SERVICE-1926',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1926',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1926.'
    },
    1927: {
        'service_name': 'ENTERPRISE-SERVICE-1927',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1927',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1927.'
    },
    1928: {
        'service_name': 'ENTERPRISE-SERVICE-1928',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1928',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1928.'
    },
    1929: {
        'service_name': 'ENTERPRISE-SERVICE-1929',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1929',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1929.'
    },
    1930: {
        'service_name': 'ENTERPRISE-SERVICE-1930',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1930',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1930.'
    },
    1931: {
        'service_name': 'ENTERPRISE-SERVICE-1931',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1931',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1931.'
    },
    1932: {
        'service_name': 'ENTERPRISE-SERVICE-1932',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1932',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1932.'
    },
    1933: {
        'service_name': 'ENTERPRISE-SERVICE-1933',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1933',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1933.'
    },
    1934: {
        'service_name': 'ENTERPRISE-SERVICE-1934',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1934',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1934.'
    },
    1935: {
        'service_name': 'ENTERPRISE-SERVICE-1935',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1935',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1935.'
    },
    1936: {
        'service_name': 'ENTERPRISE-SERVICE-1936',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1936',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1936.'
    },
    1937: {
        'service_name': 'ENTERPRISE-SERVICE-1937',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1937',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1937.'
    },
    1938: {
        'service_name': 'ENTERPRISE-SERVICE-1938',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1938',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1938.'
    },
    1939: {
        'service_name': 'ENTERPRISE-SERVICE-1939',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1939',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1939.'
    },
    1940: {
        'service_name': 'ENTERPRISE-SERVICE-1940',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1940',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1940.'
    },
    1941: {
        'service_name': 'ENTERPRISE-SERVICE-1941',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1941',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1941.'
    },
    1942: {
        'service_name': 'ENTERPRISE-SERVICE-1942',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1942',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1942.'
    },
    1943: {
        'service_name': 'ENTERPRISE-SERVICE-1943',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1943',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1943.'
    },
    1944: {
        'service_name': 'ENTERPRISE-SERVICE-1944',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1944',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1944.'
    },
    1945: {
        'service_name': 'ENTERPRISE-SERVICE-1945',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1945',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1945.'
    },
    1946: {
        'service_name': 'ENTERPRISE-SERVICE-1946',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1946',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1946.'
    },
    1947: {
        'service_name': 'ENTERPRISE-SERVICE-1947',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1947',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1947.'
    },
    1948: {
        'service_name': 'ENTERPRISE-SERVICE-1948',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1948',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1948.'
    },
    1949: {
        'service_name': 'ENTERPRISE-SERVICE-1949',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1949',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1949.'
    },
    1950: {
        'service_name': 'ENTERPRISE-SERVICE-1950',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1950',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1950.'
    },
    1951: {
        'service_name': 'ENTERPRISE-SERVICE-1951',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1951',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1951.'
    },
    1952: {
        'service_name': 'ENTERPRISE-SERVICE-1952',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1952',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1952.'
    },
    1953: {
        'service_name': 'ENTERPRISE-SERVICE-1953',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1953',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1953.'
    },
    1954: {
        'service_name': 'ENTERPRISE-SERVICE-1954',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1954',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1954.'
    },
    1955: {
        'service_name': 'ENTERPRISE-SERVICE-1955',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1955',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1955.'
    },
    1956: {
        'service_name': 'ENTERPRISE-SERVICE-1956',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1956',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1956.'
    },
    1957: {
        'service_name': 'ENTERPRISE-SERVICE-1957',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1957',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1957.'
    },
    1958: {
        'service_name': 'ENTERPRISE-SERVICE-1958',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1958',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1958.'
    },
    1959: {
        'service_name': 'ENTERPRISE-SERVICE-1959',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1959',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1959.'
    },
    1960: {
        'service_name': 'ENTERPRISE-SERVICE-1960',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1960',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1960.'
    },
    1961: {
        'service_name': 'ENTERPRISE-SERVICE-1961',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1961',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1961.'
    },
    1962: {
        'service_name': 'ENTERPRISE-SERVICE-1962',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1962',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1962.'
    },
    1963: {
        'service_name': 'ENTERPRISE-SERVICE-1963',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1963',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1963.'
    },
    1964: {
        'service_name': 'ENTERPRISE-SERVICE-1964',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1964',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1964.'
    },
    1965: {
        'service_name': 'ENTERPRISE-SERVICE-1965',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1965',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1965.'
    },
    1966: {
        'service_name': 'ENTERPRISE-SERVICE-1966',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1966',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1966.'
    },
    1967: {
        'service_name': 'ENTERPRISE-SERVICE-1967',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1967',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1967.'
    },
    1968: {
        'service_name': 'ENTERPRISE-SERVICE-1968',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1968',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1968.'
    },
    1969: {
        'service_name': 'ENTERPRISE-SERVICE-1969',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1969',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1969.'
    },
    1970: {
        'service_name': 'ENTERPRISE-SERVICE-1970',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1970',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1970.'
    },
    1971: {
        'service_name': 'ENTERPRISE-SERVICE-1971',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1971',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1971.'
    },
    1972: {
        'service_name': 'ENTERPRISE-SERVICE-1972',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1972',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1972.'
    },
    1973: {
        'service_name': 'ENTERPRISE-SERVICE-1973',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1973',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1973.'
    },
    1974: {
        'service_name': 'ENTERPRISE-SERVICE-1974',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1974',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1974.'
    },
    1975: {
        'service_name': 'ENTERPRISE-SERVICE-1975',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1975',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1975.'
    },
    1976: {
        'service_name': 'ENTERPRISE-SERVICE-1976',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1976',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1976.'
    },
    1977: {
        'service_name': 'ENTERPRISE-SERVICE-1977',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1977',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1977.'
    },
    1978: {
        'service_name': 'ENTERPRISE-SERVICE-1978',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1978',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1978.'
    },
    1979: {
        'service_name': 'ENTERPRISE-SERVICE-1979',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1979',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1979.'
    },
    1980: {
        'service_name': 'ENTERPRISE-SERVICE-1980',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1980',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1980.'
    },
    1981: {
        'service_name': 'ENTERPRISE-SERVICE-1981',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1981',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1981.'
    },
    1982: {
        'service_name': 'ENTERPRISE-SERVICE-1982',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1982',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1982.'
    },
    1983: {
        'service_name': 'ENTERPRISE-SERVICE-1983',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1983',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1983.'
    },
    1984: {
        'service_name': 'ENTERPRISE-SERVICE-1984',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1984',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1984.'
    },
    1985: {
        'service_name': 'ENTERPRISE-SERVICE-1985',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1985',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1985.'
    },
    1986: {
        'service_name': 'ENTERPRISE-SERVICE-1986',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1986',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1986.'
    },
    1987: {
        'service_name': 'ENTERPRISE-SERVICE-1987',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1987',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1987.'
    },
    1988: {
        'service_name': 'ENTERPRISE-SERVICE-1988',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1988',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1988.'
    },
    1989: {
        'service_name': 'ENTERPRISE-SERVICE-1989',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1989',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1989.'
    },
    1990: {
        'service_name': 'ENTERPRISE-SERVICE-1990',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1990',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1990.'
    },
    1991: {
        'service_name': 'ENTERPRISE-SERVICE-1991',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1991',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1991.'
    },
    1992: {
        'service_name': 'ENTERPRISE-SERVICE-1992',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1992',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1992.'
    },
    1993: {
        'service_name': 'ENTERPRISE-SERVICE-1993',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1993',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1993.'
    },
    1994: {
        'service_name': 'ENTERPRISE-SERVICE-1994',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1994',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1994.'
    },
    1995: {
        'service_name': 'ENTERPRISE-SERVICE-1995',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1995',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1995.'
    },
    1996: {
        'service_name': 'ENTERPRISE-SERVICE-1996',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1996',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1996.'
    },
    1997: {
        'service_name': 'ENTERPRISE-SERVICE-1997',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1997',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1997.'
    },
    1998: {
        'service_name': 'ENTERPRISE-SERVICE-1998',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1998',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1998.'
    },
    1999: {
        'service_name': 'ENTERPRISE-SERVICE-1999',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 1999',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 1999.'
    },
    2000: {
        'service_name': 'ENTERPRISE-SERVICE-2000',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2000',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2000.'
    },
    2001: {
        'service_name': 'ENTERPRISE-SERVICE-2001',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2001',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2001.'
    },
    2002: {
        'service_name': 'ENTERPRISE-SERVICE-2002',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2002',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2002.'
    },
    2003: {
        'service_name': 'ENTERPRISE-SERVICE-2003',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2003',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2003.'
    },
    2004: {
        'service_name': 'ENTERPRISE-SERVICE-2004',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2004',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2004.'
    },
    2005: {
        'service_name': 'ENTERPRISE-SERVICE-2005',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2005',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2005.'
    },
    2006: {
        'service_name': 'ENTERPRISE-SERVICE-2006',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2006',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2006.'
    },
    2007: {
        'service_name': 'ENTERPRISE-SERVICE-2007',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2007',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2007.'
    },
    2008: {
        'service_name': 'ENTERPRISE-SERVICE-2008',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2008',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2008.'
    },
    2009: {
        'service_name': 'ENTERPRISE-SERVICE-2009',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2009',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2009.'
    },
    2010: {
        'service_name': 'ENTERPRISE-SERVICE-2010',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2010',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2010.'
    },
    2011: {
        'service_name': 'ENTERPRISE-SERVICE-2011',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2011',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2011.'
    },
    2012: {
        'service_name': 'ENTERPRISE-SERVICE-2012',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2012',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2012.'
    },
    2013: {
        'service_name': 'ENTERPRISE-SERVICE-2013',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2013',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2013.'
    },
    2014: {
        'service_name': 'ENTERPRISE-SERVICE-2014',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2014',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2014.'
    },
    2015: {
        'service_name': 'ENTERPRISE-SERVICE-2015',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2015',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2015.'
    },
    2016: {
        'service_name': 'ENTERPRISE-SERVICE-2016',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2016',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2016.'
    },
    2017: {
        'service_name': 'ENTERPRISE-SERVICE-2017',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2017',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2017.'
    },
    2018: {
        'service_name': 'ENTERPRISE-SERVICE-2018',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2018',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2018.'
    },
    2019: {
        'service_name': 'ENTERPRISE-SERVICE-2019',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2019',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2019.'
    },
    2020: {
        'service_name': 'ENTERPRISE-SERVICE-2020',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2020',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2020.'
    },
    2021: {
        'service_name': 'ENTERPRISE-SERVICE-2021',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2021',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2021.'
    },
    2022: {
        'service_name': 'ENTERPRISE-SERVICE-2022',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2022',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2022.'
    },
    2023: {
        'service_name': 'ENTERPRISE-SERVICE-2023',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2023',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2023.'
    },
    2024: {
        'service_name': 'ENTERPRISE-SERVICE-2024',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2024',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2024.'
    },
    2025: {
        'service_name': 'ENTERPRISE-SERVICE-2025',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2025',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2025.'
    },
    2026: {
        'service_name': 'ENTERPRISE-SERVICE-2026',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2026',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2026.'
    },
    2027: {
        'service_name': 'ENTERPRISE-SERVICE-2027',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2027',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2027.'
    },
    2028: {
        'service_name': 'ENTERPRISE-SERVICE-2028',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2028',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2028.'
    },
    2029: {
        'service_name': 'ENTERPRISE-SERVICE-2029',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2029',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2029.'
    },
    2030: {
        'service_name': 'ENTERPRISE-SERVICE-2030',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2030',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2030.'
    },
    2031: {
        'service_name': 'ENTERPRISE-SERVICE-2031',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2031',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2031.'
    },
    2032: {
        'service_name': 'ENTERPRISE-SERVICE-2032',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2032',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2032.'
    },
    2033: {
        'service_name': 'ENTERPRISE-SERVICE-2033',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2033',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2033.'
    },
    2034: {
        'service_name': 'ENTERPRISE-SERVICE-2034',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2034',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2034.'
    },
    2035: {
        'service_name': 'ENTERPRISE-SERVICE-2035',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2035',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2035.'
    },
    2036: {
        'service_name': 'ENTERPRISE-SERVICE-2036',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2036',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2036.'
    },
    2037: {
        'service_name': 'ENTERPRISE-SERVICE-2037',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2037',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2037.'
    },
    2038: {
        'service_name': 'ENTERPRISE-SERVICE-2038',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2038',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2038.'
    },
    2039: {
        'service_name': 'ENTERPRISE-SERVICE-2039',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2039',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2039.'
    },
    2040: {
        'service_name': 'ENTERPRISE-SERVICE-2040',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2040',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2040.'
    },
    2041: {
        'service_name': 'ENTERPRISE-SERVICE-2041',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2041',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2041.'
    },
    2042: {
        'service_name': 'ENTERPRISE-SERVICE-2042',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2042',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2042.'
    },
    2043: {
        'service_name': 'ENTERPRISE-SERVICE-2043',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2043',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2043.'
    },
    2044: {
        'service_name': 'ENTERPRISE-SERVICE-2044',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2044',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2044.'
    },
    2045: {
        'service_name': 'ENTERPRISE-SERVICE-2045',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2045',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2045.'
    },
    2046: {
        'service_name': 'ENTERPRISE-SERVICE-2046',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2046',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2046.'
    },
    2047: {
        'service_name': 'ENTERPRISE-SERVICE-2047',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2047',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2047.'
    },
    2048: {
        'service_name': 'ENTERPRISE-SERVICE-2048',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2048',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2048.'
    },
    2049: {
        'service_name': 'ENTERPRISE-SERVICE-2049',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2049',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2049.'
    },
    2050: {
        'service_name': 'ENTERPRISE-SERVICE-2050',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2050',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2050.'
    },
    2051: {
        'service_name': 'ENTERPRISE-SERVICE-2051',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2051',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2051.'
    },
    2052: {
        'service_name': 'ENTERPRISE-SERVICE-2052',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2052',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2052.'
    },
    2053: {
        'service_name': 'ENTERPRISE-SERVICE-2053',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2053',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2053.'
    },
    2054: {
        'service_name': 'ENTERPRISE-SERVICE-2054',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2054',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2054.'
    },
    2055: {
        'service_name': 'ENTERPRISE-SERVICE-2055',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2055',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2055.'
    },
    2056: {
        'service_name': 'ENTERPRISE-SERVICE-2056',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2056',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2056.'
    },
    2057: {
        'service_name': 'ENTERPRISE-SERVICE-2057',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2057',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2057.'
    },
    2058: {
        'service_name': 'ENTERPRISE-SERVICE-2058',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2058',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2058.'
    },
    2059: {
        'service_name': 'ENTERPRISE-SERVICE-2059',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2059',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2059.'
    },
    2060: {
        'service_name': 'ENTERPRISE-SERVICE-2060',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2060',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2060.'
    },
    2061: {
        'service_name': 'ENTERPRISE-SERVICE-2061',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2061',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2061.'
    },
    2062: {
        'service_name': 'ENTERPRISE-SERVICE-2062',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2062',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2062.'
    },
    2063: {
        'service_name': 'ENTERPRISE-SERVICE-2063',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2063',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2063.'
    },
    2064: {
        'service_name': 'ENTERPRISE-SERVICE-2064',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2064',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2064.'
    },
    2065: {
        'service_name': 'ENTERPRISE-SERVICE-2065',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2065',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2065.'
    },
    2066: {
        'service_name': 'ENTERPRISE-SERVICE-2066',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2066',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2066.'
    },
    2067: {
        'service_name': 'ENTERPRISE-SERVICE-2067',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2067',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2067.'
    },
    2068: {
        'service_name': 'ENTERPRISE-SERVICE-2068',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2068',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2068.'
    },
    2069: {
        'service_name': 'ENTERPRISE-SERVICE-2069',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2069',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2069.'
    },
    2070: {
        'service_name': 'ENTERPRISE-SERVICE-2070',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2070',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2070.'
    },
    2071: {
        'service_name': 'ENTERPRISE-SERVICE-2071',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2071',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2071.'
    },
    2072: {
        'service_name': 'ENTERPRISE-SERVICE-2072',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2072',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2072.'
    },
    2073: {
        'service_name': 'ENTERPRISE-SERVICE-2073',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2073',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2073.'
    },
    2074: {
        'service_name': 'ENTERPRISE-SERVICE-2074',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2074',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2074.'
    },
    2075: {
        'service_name': 'ENTERPRISE-SERVICE-2075',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2075',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2075.'
    },
    2076: {
        'service_name': 'ENTERPRISE-SERVICE-2076',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2076',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2076.'
    },
    2077: {
        'service_name': 'ENTERPRISE-SERVICE-2077',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2077',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2077.'
    },
    2078: {
        'service_name': 'ENTERPRISE-SERVICE-2078',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2078',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2078.'
    },
    2079: {
        'service_name': 'ENTERPRISE-SERVICE-2079',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2079',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2079.'
    },
    2080: {
        'service_name': 'ENTERPRISE-SERVICE-2080',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2080',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2080.'
    },
    2081: {
        'service_name': 'ENTERPRISE-SERVICE-2081',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2081',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2081.'
    },
    2082: {
        'service_name': 'ENTERPRISE-SERVICE-2082',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2082',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2082.'
    },
    2083: {
        'service_name': 'ENTERPRISE-SERVICE-2083',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2083',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2083.'
    },
    2084: {
        'service_name': 'ENTERPRISE-SERVICE-2084',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2084',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2084.'
    },
    2085: {
        'service_name': 'ENTERPRISE-SERVICE-2085',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2085',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2085.'
    },
    2086: {
        'service_name': 'ENTERPRISE-SERVICE-2086',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2086',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2086.'
    },
    2087: {
        'service_name': 'ENTERPRISE-SERVICE-2087',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2087',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2087.'
    },
    2088: {
        'service_name': 'ENTERPRISE-SERVICE-2088',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2088',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2088.'
    },
    2089: {
        'service_name': 'ENTERPRISE-SERVICE-2089',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2089',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2089.'
    },
    2090: {
        'service_name': 'ENTERPRISE-SERVICE-2090',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2090',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2090.'
    },
    2091: {
        'service_name': 'ENTERPRISE-SERVICE-2091',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2091',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2091.'
    },
    2092: {
        'service_name': 'ENTERPRISE-SERVICE-2092',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2092',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2092.'
    },
    2093: {
        'service_name': 'ENTERPRISE-SERVICE-2093',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2093',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2093.'
    },
    2094: {
        'service_name': 'ENTERPRISE-SERVICE-2094',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2094',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2094.'
    },
    2095: {
        'service_name': 'ENTERPRISE-SERVICE-2095',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2095',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2095.'
    },
    2096: {
        'service_name': 'ENTERPRISE-SERVICE-2096',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2096',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2096.'
    },
    2097: {
        'service_name': 'ENTERPRISE-SERVICE-2097',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2097',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2097.'
    },
    2098: {
        'service_name': 'ENTERPRISE-SERVICE-2098',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2098',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2098.'
    },
    2099: {
        'service_name': 'ENTERPRISE-SERVICE-2099',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2099',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2099.'
    },
    2100: {
        'service_name': 'ENTERPRISE-SERVICE-2100',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2100',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2100.'
    },
    2101: {
        'service_name': 'ENTERPRISE-SERVICE-2101',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2101',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2101.'
    },
    2102: {
        'service_name': 'ENTERPRISE-SERVICE-2102',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2102',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2102.'
    },
    2103: {
        'service_name': 'ENTERPRISE-SERVICE-2103',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2103',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2103.'
    },
    2104: {
        'service_name': 'ENTERPRISE-SERVICE-2104',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2104',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2104.'
    },
    2105: {
        'service_name': 'ENTERPRISE-SERVICE-2105',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2105',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2105.'
    },
    2106: {
        'service_name': 'ENTERPRISE-SERVICE-2106',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2106',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2106.'
    },
    2107: {
        'service_name': 'ENTERPRISE-SERVICE-2107',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2107',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2107.'
    },
    2108: {
        'service_name': 'ENTERPRISE-SERVICE-2108',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2108',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2108.'
    },
    2109: {
        'service_name': 'ENTERPRISE-SERVICE-2109',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2109',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2109.'
    },
    2110: {
        'service_name': 'ENTERPRISE-SERVICE-2110',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2110',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2110.'
    },
    2111: {
        'service_name': 'ENTERPRISE-SERVICE-2111',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2111',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2111.'
    },
    2112: {
        'service_name': 'ENTERPRISE-SERVICE-2112',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2112',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2112.'
    },
    2113: {
        'service_name': 'ENTERPRISE-SERVICE-2113',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2113',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2113.'
    },
    2114: {
        'service_name': 'ENTERPRISE-SERVICE-2114',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2114',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2114.'
    },
    2115: {
        'service_name': 'ENTERPRISE-SERVICE-2115',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2115',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2115.'
    },
    2116: {
        'service_name': 'ENTERPRISE-SERVICE-2116',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2116',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2116.'
    },
    2117: {
        'service_name': 'ENTERPRISE-SERVICE-2117',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2117',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2117.'
    },
    2118: {
        'service_name': 'ENTERPRISE-SERVICE-2118',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2118',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2118.'
    },
    2119: {
        'service_name': 'ENTERPRISE-SERVICE-2119',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2119',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2119.'
    },
    2120: {
        'service_name': 'ENTERPRISE-SERVICE-2120',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2120',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2120.'
    },
    2121: {
        'service_name': 'ENTERPRISE-SERVICE-2121',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2121',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2121.'
    },
    2122: {
        'service_name': 'ENTERPRISE-SERVICE-2122',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2122',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2122.'
    },
    2123: {
        'service_name': 'ENTERPRISE-SERVICE-2123',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2123',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2123.'
    },
    2124: {
        'service_name': 'ENTERPRISE-SERVICE-2124',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2124',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2124.'
    },
    2125: {
        'service_name': 'ENTERPRISE-SERVICE-2125',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2125',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2125.'
    },
    2126: {
        'service_name': 'ENTERPRISE-SERVICE-2126',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2126',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2126.'
    },
    2127: {
        'service_name': 'ENTERPRISE-SERVICE-2127',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2127',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2127.'
    },
    2128: {
        'service_name': 'ENTERPRISE-SERVICE-2128',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2128',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2128.'
    },
    2129: {
        'service_name': 'ENTERPRISE-SERVICE-2129',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2129',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2129.'
    },
    2130: {
        'service_name': 'ENTERPRISE-SERVICE-2130',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2130',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2130.'
    },
    2131: {
        'service_name': 'ENTERPRISE-SERVICE-2131',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2131',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2131.'
    },
    2132: {
        'service_name': 'ENTERPRISE-SERVICE-2132',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2132',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2132.'
    },
    2133: {
        'service_name': 'ENTERPRISE-SERVICE-2133',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2133',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2133.'
    },
    2134: {
        'service_name': 'ENTERPRISE-SERVICE-2134',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2134',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2134.'
    },
    2135: {
        'service_name': 'ENTERPRISE-SERVICE-2135',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2135',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2135.'
    },
    2136: {
        'service_name': 'ENTERPRISE-SERVICE-2136',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2136',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2136.'
    },
    2137: {
        'service_name': 'ENTERPRISE-SERVICE-2137',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2137',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2137.'
    },
    2138: {
        'service_name': 'ENTERPRISE-SERVICE-2138',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2138',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2138.'
    },
    2139: {
        'service_name': 'ENTERPRISE-SERVICE-2139',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2139',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2139.'
    },
    2140: {
        'service_name': 'ENTERPRISE-SERVICE-2140',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2140',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2140.'
    },
    2141: {
        'service_name': 'ENTERPRISE-SERVICE-2141',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2141',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2141.'
    },
    2142: {
        'service_name': 'ENTERPRISE-SERVICE-2142',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2142',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2142.'
    },
    2143: {
        'service_name': 'ENTERPRISE-SERVICE-2143',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2143',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2143.'
    },
    2144: {
        'service_name': 'ENTERPRISE-SERVICE-2144',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2144',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2144.'
    },
    2145: {
        'service_name': 'ENTERPRISE-SERVICE-2145',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2145',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2145.'
    },
    2146: {
        'service_name': 'ENTERPRISE-SERVICE-2146',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2146',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2146.'
    },
    2147: {
        'service_name': 'ENTERPRISE-SERVICE-2147',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2147',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2147.'
    },
    2148: {
        'service_name': 'ENTERPRISE-SERVICE-2148',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2148',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2148.'
    },
    2149: {
        'service_name': 'ENTERPRISE-SERVICE-2149',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2149',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2149.'
    },
    2150: {
        'service_name': 'ENTERPRISE-SERVICE-2150',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2150',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2150.'
    },
    2151: {
        'service_name': 'ENTERPRISE-SERVICE-2151',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2151',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2151.'
    },
    2152: {
        'service_name': 'ENTERPRISE-SERVICE-2152',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2152',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2152.'
    },
    2153: {
        'service_name': 'ENTERPRISE-SERVICE-2153',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2153',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2153.'
    },
    2154: {
        'service_name': 'ENTERPRISE-SERVICE-2154',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2154',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2154.'
    },
    2155: {
        'service_name': 'ENTERPRISE-SERVICE-2155',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2155',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2155.'
    },
    2156: {
        'service_name': 'ENTERPRISE-SERVICE-2156',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2156',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2156.'
    },
    2157: {
        'service_name': 'ENTERPRISE-SERVICE-2157',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2157',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2157.'
    },
    2158: {
        'service_name': 'ENTERPRISE-SERVICE-2158',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2158',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2158.'
    },
    2159: {
        'service_name': 'ENTERPRISE-SERVICE-2159',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2159',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2159.'
    },
    2160: {
        'service_name': 'ENTERPRISE-SERVICE-2160',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2160',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2160.'
    },
    2161: {
        'service_name': 'ENTERPRISE-SERVICE-2161',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2161',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2161.'
    },
    2162: {
        'service_name': 'ENTERPRISE-SERVICE-2162',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2162',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2162.'
    },
    2163: {
        'service_name': 'ENTERPRISE-SERVICE-2163',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2163',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2163.'
    },
    2164: {
        'service_name': 'ENTERPRISE-SERVICE-2164',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2164',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2164.'
    },
    2165: {
        'service_name': 'ENTERPRISE-SERVICE-2165',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2165',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2165.'
    },
    2166: {
        'service_name': 'ENTERPRISE-SERVICE-2166',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2166',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2166.'
    },
    2167: {
        'service_name': 'ENTERPRISE-SERVICE-2167',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2167',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2167.'
    },
    2168: {
        'service_name': 'ENTERPRISE-SERVICE-2168',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2168',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2168.'
    },
    2169: {
        'service_name': 'ENTERPRISE-SERVICE-2169',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2169',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2169.'
    },
    2170: {
        'service_name': 'ENTERPRISE-SERVICE-2170',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2170',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2170.'
    },
    2171: {
        'service_name': 'ENTERPRISE-SERVICE-2171',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2171',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2171.'
    },
    2172: {
        'service_name': 'ENTERPRISE-SERVICE-2172',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2172',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2172.'
    },
    2173: {
        'service_name': 'ENTERPRISE-SERVICE-2173',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2173',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2173.'
    },
    2174: {
        'service_name': 'ENTERPRISE-SERVICE-2174',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2174',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2174.'
    },
    2175: {
        'service_name': 'ENTERPRISE-SERVICE-2175',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2175',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2175.'
    },
    2176: {
        'service_name': 'ENTERPRISE-SERVICE-2176',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2176',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2176.'
    },
    2177: {
        'service_name': 'ENTERPRISE-SERVICE-2177',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2177',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2177.'
    },
    2178: {
        'service_name': 'ENTERPRISE-SERVICE-2178',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2178',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2178.'
    },
    2179: {
        'service_name': 'ENTERPRISE-SERVICE-2179',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2179',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2179.'
    },
    2180: {
        'service_name': 'ENTERPRISE-SERVICE-2180',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2180',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2180.'
    },
    2181: {
        'service_name': 'ENTERPRISE-SERVICE-2181',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2181',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2181.'
    },
    2182: {
        'service_name': 'ENTERPRISE-SERVICE-2182',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2182',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2182.'
    },
    2183: {
        'service_name': 'ENTERPRISE-SERVICE-2183',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2183',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2183.'
    },
    2184: {
        'service_name': 'ENTERPRISE-SERVICE-2184',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2184',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2184.'
    },
    2185: {
        'service_name': 'ENTERPRISE-SERVICE-2185',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2185',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2185.'
    },
    2186: {
        'service_name': 'ENTERPRISE-SERVICE-2186',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2186',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2186.'
    },
    2187: {
        'service_name': 'ENTERPRISE-SERVICE-2187',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2187',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2187.'
    },
    2188: {
        'service_name': 'ENTERPRISE-SERVICE-2188',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2188',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2188.'
    },
    2189: {
        'service_name': 'ENTERPRISE-SERVICE-2189',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2189',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2189.'
    },
    2190: {
        'service_name': 'ENTERPRISE-SERVICE-2190',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2190',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2190.'
    },
    2191: {
        'service_name': 'ENTERPRISE-SERVICE-2191',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2191',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2191.'
    },
    2192: {
        'service_name': 'ENTERPRISE-SERVICE-2192',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2192',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2192.'
    },
    2193: {
        'service_name': 'ENTERPRISE-SERVICE-2193',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2193',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2193.'
    },
    2194: {
        'service_name': 'ENTERPRISE-SERVICE-2194',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2194',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2194.'
    },
    2195: {
        'service_name': 'ENTERPRISE-SERVICE-2195',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2195',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2195.'
    },
    2196: {
        'service_name': 'ENTERPRISE-SERVICE-2196',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2196',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2196.'
    },
    2197: {
        'service_name': 'ENTERPRISE-SERVICE-2197',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2197',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2197.'
    },
    2198: {
        'service_name': 'ENTERPRISE-SERVICE-2198',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2198',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2198.'
    },
    2199: {
        'service_name': 'ENTERPRISE-SERVICE-2199',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2199',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2199.'
    },
    2200: {
        'service_name': 'ENTERPRISE-SERVICE-2200',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2200',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2200.'
    },
    2201: {
        'service_name': 'ENTERPRISE-SERVICE-2201',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2201',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2201.'
    },
    2202: {
        'service_name': 'ENTERPRISE-SERVICE-2202',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2202',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2202.'
    },
    2203: {
        'service_name': 'ENTERPRISE-SERVICE-2203',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2203',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2203.'
    },
    2204: {
        'service_name': 'ENTERPRISE-SERVICE-2204',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2204',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2204.'
    },
    2205: {
        'service_name': 'ENTERPRISE-SERVICE-2205',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2205',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2205.'
    },
    2206: {
        'service_name': 'ENTERPRISE-SERVICE-2206',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2206',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2206.'
    },
    2207: {
        'service_name': 'ENTERPRISE-SERVICE-2207',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2207',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2207.'
    },
    2208: {
        'service_name': 'ENTERPRISE-SERVICE-2208',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2208',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2208.'
    },
    2209: {
        'service_name': 'ENTERPRISE-SERVICE-2209',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2209',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2209.'
    },
    2210: {
        'service_name': 'ENTERPRISE-SERVICE-2210',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2210',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2210.'
    },
    2211: {
        'service_name': 'ENTERPRISE-SERVICE-2211',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2211',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2211.'
    },
    2212: {
        'service_name': 'ENTERPRISE-SERVICE-2212',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2212',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2212.'
    },
    2213: {
        'service_name': 'ENTERPRISE-SERVICE-2213',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2213',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2213.'
    },
    2214: {
        'service_name': 'ENTERPRISE-SERVICE-2214',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2214',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2214.'
    },
    2215: {
        'service_name': 'ENTERPRISE-SERVICE-2215',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2215',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2215.'
    },
    2216: {
        'service_name': 'ENTERPRISE-SERVICE-2216',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2216',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2216.'
    },
    2217: {
        'service_name': 'ENTERPRISE-SERVICE-2217',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2217',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2217.'
    },
    2218: {
        'service_name': 'ENTERPRISE-SERVICE-2218',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2218',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2218.'
    },
    2219: {
        'service_name': 'ENTERPRISE-SERVICE-2219',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2219',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2219.'
    },
    2220: {
        'service_name': 'ENTERPRISE-SERVICE-2220',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2220',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2220.'
    },
    2221: {
        'service_name': 'ENTERPRISE-SERVICE-2221',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2221',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2221.'
    },
    2222: {
        'service_name': 'ENTERPRISE-SERVICE-2222',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2222',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2222.'
    },
    2223: {
        'service_name': 'ENTERPRISE-SERVICE-2223',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2223',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2223.'
    },
    2224: {
        'service_name': 'ENTERPRISE-SERVICE-2224',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2224',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2224.'
    },
    2225: {
        'service_name': 'ENTERPRISE-SERVICE-2225',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2225',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2225.'
    },
    2226: {
        'service_name': 'ENTERPRISE-SERVICE-2226',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2226',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2226.'
    },
    2227: {
        'service_name': 'ENTERPRISE-SERVICE-2227',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2227',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2227.'
    },
    2228: {
        'service_name': 'ENTERPRISE-SERVICE-2228',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2228',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2228.'
    },
    2229: {
        'service_name': 'ENTERPRISE-SERVICE-2229',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2229',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2229.'
    },
    2230: {
        'service_name': 'ENTERPRISE-SERVICE-2230',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2230',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2230.'
    },
    2231: {
        'service_name': 'ENTERPRISE-SERVICE-2231',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2231',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2231.'
    },
    2232: {
        'service_name': 'ENTERPRISE-SERVICE-2232',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2232',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2232.'
    },
    2233: {
        'service_name': 'ENTERPRISE-SERVICE-2233',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2233',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2233.'
    },
    2234: {
        'service_name': 'ENTERPRISE-SERVICE-2234',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2234',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2234.'
    },
    2235: {
        'service_name': 'ENTERPRISE-SERVICE-2235',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2235',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2235.'
    },
    2236: {
        'service_name': 'ENTERPRISE-SERVICE-2236',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2236',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2236.'
    },
    2237: {
        'service_name': 'ENTERPRISE-SERVICE-2237',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2237',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2237.'
    },
    2238: {
        'service_name': 'ENTERPRISE-SERVICE-2238',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2238',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2238.'
    },
    2239: {
        'service_name': 'ENTERPRISE-SERVICE-2239',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2239',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2239.'
    },
    2240: {
        'service_name': 'ENTERPRISE-SERVICE-2240',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2240',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2240.'
    },
    2241: {
        'service_name': 'ENTERPRISE-SERVICE-2241',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2241',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2241.'
    },
    2242: {
        'service_name': 'ENTERPRISE-SERVICE-2242',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2242',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2242.'
    },
    2243: {
        'service_name': 'ENTERPRISE-SERVICE-2243',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2243',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2243.'
    },
    2244: {
        'service_name': 'ENTERPRISE-SERVICE-2244',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2244',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2244.'
    },
    2245: {
        'service_name': 'ENTERPRISE-SERVICE-2245',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2245',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2245.'
    },
    2246: {
        'service_name': 'ENTERPRISE-SERVICE-2246',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2246',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2246.'
    },
    2247: {
        'service_name': 'ENTERPRISE-SERVICE-2247',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2247',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2247.'
    },
    2248: {
        'service_name': 'ENTERPRISE-SERVICE-2248',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2248',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2248.'
    },
    2249: {
        'service_name': 'ENTERPRISE-SERVICE-2249',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2249',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2249.'
    },
    2250: {
        'service_name': 'ENTERPRISE-SERVICE-2250',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2250',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2250.'
    },
    2251: {
        'service_name': 'ENTERPRISE-SERVICE-2251',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2251',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2251.'
    },
    2252: {
        'service_name': 'ENTERPRISE-SERVICE-2252',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2252',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2252.'
    },
    2253: {
        'service_name': 'ENTERPRISE-SERVICE-2253',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2253',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2253.'
    },
    2254: {
        'service_name': 'ENTERPRISE-SERVICE-2254',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2254',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2254.'
    },
    2255: {
        'service_name': 'ENTERPRISE-SERVICE-2255',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2255',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2255.'
    },
    2256: {
        'service_name': 'ENTERPRISE-SERVICE-2256',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2256',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2256.'
    },
    2257: {
        'service_name': 'ENTERPRISE-SERVICE-2257',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2257',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2257.'
    },
    2258: {
        'service_name': 'ENTERPRISE-SERVICE-2258',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2258',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2258.'
    },
    2259: {
        'service_name': 'ENTERPRISE-SERVICE-2259',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2259',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2259.'
    },
    2260: {
        'service_name': 'ENTERPRISE-SERVICE-2260',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2260',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2260.'
    },
    2261: {
        'service_name': 'ENTERPRISE-SERVICE-2261',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2261',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2261.'
    },
    2262: {
        'service_name': 'ENTERPRISE-SERVICE-2262',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2262',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2262.'
    },
    2263: {
        'service_name': 'ENTERPRISE-SERVICE-2263',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2263',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2263.'
    },
    2264: {
        'service_name': 'ENTERPRISE-SERVICE-2264',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2264',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2264.'
    },
    2265: {
        'service_name': 'ENTERPRISE-SERVICE-2265',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2265',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2265.'
    },
    2266: {
        'service_name': 'ENTERPRISE-SERVICE-2266',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2266',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2266.'
    },
    2267: {
        'service_name': 'ENTERPRISE-SERVICE-2267',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2267',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2267.'
    },
    2268: {
        'service_name': 'ENTERPRISE-SERVICE-2268',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2268',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2268.'
    },
    2269: {
        'service_name': 'ENTERPRISE-SERVICE-2269',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2269',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2269.'
    },
    2270: {
        'service_name': 'ENTERPRISE-SERVICE-2270',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2270',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2270.'
    },
    2271: {
        'service_name': 'ENTERPRISE-SERVICE-2271',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2271',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2271.'
    },
    2272: {
        'service_name': 'ENTERPRISE-SERVICE-2272',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2272',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2272.'
    },
    2273: {
        'service_name': 'ENTERPRISE-SERVICE-2273',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2273',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2273.'
    },
    2274: {
        'service_name': 'ENTERPRISE-SERVICE-2274',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2274',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2274.'
    },
    2275: {
        'service_name': 'ENTERPRISE-SERVICE-2275',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2275',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2275.'
    },
    2276: {
        'service_name': 'ENTERPRISE-SERVICE-2276',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2276',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2276.'
    },
    2277: {
        'service_name': 'ENTERPRISE-SERVICE-2277',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2277',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2277.'
    },
    2278: {
        'service_name': 'ENTERPRISE-SERVICE-2278',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2278',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2278.'
    },
    2279: {
        'service_name': 'ENTERPRISE-SERVICE-2279',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2279',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2279.'
    },
    2280: {
        'service_name': 'ENTERPRISE-SERVICE-2280',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2280',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2280.'
    },
    2281: {
        'service_name': 'ENTERPRISE-SERVICE-2281',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2281',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2281.'
    },
    2282: {
        'service_name': 'ENTERPRISE-SERVICE-2282',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2282',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2282.'
    },
    2283: {
        'service_name': 'ENTERPRISE-SERVICE-2283',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2283',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2283.'
    },
    2284: {
        'service_name': 'ENTERPRISE-SERVICE-2284',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2284',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2284.'
    },
    2285: {
        'service_name': 'ENTERPRISE-SERVICE-2285',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2285',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2285.'
    },
    2286: {
        'service_name': 'ENTERPRISE-SERVICE-2286',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2286',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2286.'
    },
    2287: {
        'service_name': 'ENTERPRISE-SERVICE-2287',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2287',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2287.'
    },
    2288: {
        'service_name': 'ENTERPRISE-SERVICE-2288',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2288',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2288.'
    },
    2289: {
        'service_name': 'ENTERPRISE-SERVICE-2289',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2289',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2289.'
    },
    2290: {
        'service_name': 'ENTERPRISE-SERVICE-2290',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2290',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2290.'
    },
    2291: {
        'service_name': 'ENTERPRISE-SERVICE-2291',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2291',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2291.'
    },
    2292: {
        'service_name': 'ENTERPRISE-SERVICE-2292',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2292',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2292.'
    },
    2293: {
        'service_name': 'ENTERPRISE-SERVICE-2293',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2293',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2293.'
    },
    2294: {
        'service_name': 'ENTERPRISE-SERVICE-2294',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2294',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2294.'
    },
    2295: {
        'service_name': 'ENTERPRISE-SERVICE-2295',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2295',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2295.'
    },
    2296: {
        'service_name': 'ENTERPRISE-SERVICE-2296',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2296',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2296.'
    },
    2297: {
        'service_name': 'ENTERPRISE-SERVICE-2297',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2297',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2297.'
    },
    2298: {
        'service_name': 'ENTERPRISE-SERVICE-2298',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2298',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2298.'
    },
    2299: {
        'service_name': 'ENTERPRISE-SERVICE-2299',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2299',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2299.'
    },
    2300: {
        'service_name': 'ENTERPRISE-SERVICE-2300',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2300',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2300.'
    },
    2301: {
        'service_name': 'ENTERPRISE-SERVICE-2301',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2301',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2301.'
    },
    2302: {
        'service_name': 'ENTERPRISE-SERVICE-2302',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2302',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2302.'
    },
    2303: {
        'service_name': 'ENTERPRISE-SERVICE-2303',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2303',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2303.'
    },
    2304: {
        'service_name': 'ENTERPRISE-SERVICE-2304',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2304',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2304.'
    },
    2305: {
        'service_name': 'ENTERPRISE-SERVICE-2305',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2305',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2305.'
    },
    2306: {
        'service_name': 'ENTERPRISE-SERVICE-2306',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2306',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2306.'
    },
    2307: {
        'service_name': 'ENTERPRISE-SERVICE-2307',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2307',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2307.'
    },
    2308: {
        'service_name': 'ENTERPRISE-SERVICE-2308',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2308',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2308.'
    },
    2309: {
        'service_name': 'ENTERPRISE-SERVICE-2309',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2309',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2309.'
    },
    2310: {
        'service_name': 'ENTERPRISE-SERVICE-2310',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2310',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2310.'
    },
    2311: {
        'service_name': 'ENTERPRISE-SERVICE-2311',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2311',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2311.'
    },
    2312: {
        'service_name': 'ENTERPRISE-SERVICE-2312',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2312',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2312.'
    },
    2313: {
        'service_name': 'ENTERPRISE-SERVICE-2313',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2313',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2313.'
    },
    2314: {
        'service_name': 'ENTERPRISE-SERVICE-2314',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2314',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2314.'
    },
    2315: {
        'service_name': 'ENTERPRISE-SERVICE-2315',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2315',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2315.'
    },
    2316: {
        'service_name': 'ENTERPRISE-SERVICE-2316',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2316',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2316.'
    },
    2317: {
        'service_name': 'ENTERPRISE-SERVICE-2317',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2317',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2317.'
    },
    2318: {
        'service_name': 'ENTERPRISE-SERVICE-2318',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2318',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2318.'
    },
    2319: {
        'service_name': 'ENTERPRISE-SERVICE-2319',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2319',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2319.'
    },
    2320: {
        'service_name': 'ENTERPRISE-SERVICE-2320',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2320',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2320.'
    },
    2321: {
        'service_name': 'ENTERPRISE-SERVICE-2321',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2321',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2321.'
    },
    2322: {
        'service_name': 'ENTERPRISE-SERVICE-2322',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2322',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2322.'
    },
    2323: {
        'service_name': 'ENTERPRISE-SERVICE-2323',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2323',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2323.'
    },
    2324: {
        'service_name': 'ENTERPRISE-SERVICE-2324',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2324',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2324.'
    },
    2325: {
        'service_name': 'ENTERPRISE-SERVICE-2325',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2325',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2325.'
    },
    2326: {
        'service_name': 'ENTERPRISE-SERVICE-2326',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2326',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2326.'
    },
    2327: {
        'service_name': 'ENTERPRISE-SERVICE-2327',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2327',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2327.'
    },
    2328: {
        'service_name': 'ENTERPRISE-SERVICE-2328',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2328',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2328.'
    },
    2329: {
        'service_name': 'ENTERPRISE-SERVICE-2329',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2329',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2329.'
    },
    2330: {
        'service_name': 'ENTERPRISE-SERVICE-2330',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2330',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2330.'
    },
    2331: {
        'service_name': 'ENTERPRISE-SERVICE-2331',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2331',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2331.'
    },
    2332: {
        'service_name': 'ENTERPRISE-SERVICE-2332',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2332',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2332.'
    },
    2333: {
        'service_name': 'ENTERPRISE-SERVICE-2333',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2333',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2333.'
    },
    2334: {
        'service_name': 'ENTERPRISE-SERVICE-2334',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2334',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2334.'
    },
    2335: {
        'service_name': 'ENTERPRISE-SERVICE-2335',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2335',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2335.'
    },
    2336: {
        'service_name': 'ENTERPRISE-SERVICE-2336',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2336',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2336.'
    },
    2337: {
        'service_name': 'ENTERPRISE-SERVICE-2337',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2337',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2337.'
    },
    2338: {
        'service_name': 'ENTERPRISE-SERVICE-2338',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2338',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2338.'
    },
    2339: {
        'service_name': 'ENTERPRISE-SERVICE-2339',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2339',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2339.'
    },
    2340: {
        'service_name': 'ENTERPRISE-SERVICE-2340',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2340',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2340.'
    },
    2341: {
        'service_name': 'ENTERPRISE-SERVICE-2341',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2341',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2341.'
    },
    2342: {
        'service_name': 'ENTERPRISE-SERVICE-2342',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2342',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2342.'
    },
    2343: {
        'service_name': 'ENTERPRISE-SERVICE-2343',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2343',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2343.'
    },
    2344: {
        'service_name': 'ENTERPRISE-SERVICE-2344',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2344',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2344.'
    },
    2345: {
        'service_name': 'ENTERPRISE-SERVICE-2345',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2345',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2345.'
    },
    2346: {
        'service_name': 'ENTERPRISE-SERVICE-2346',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2346',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2346.'
    },
    2347: {
        'service_name': 'ENTERPRISE-SERVICE-2347',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2347',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2347.'
    },
    2348: {
        'service_name': 'ENTERPRISE-SERVICE-2348',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2348',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2348.'
    },
    2349: {
        'service_name': 'ENTERPRISE-SERVICE-2349',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2349',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2349.'
    },
    2350: {
        'service_name': 'ENTERPRISE-SERVICE-2350',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2350',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2350.'
    },
    2351: {
        'service_name': 'ENTERPRISE-SERVICE-2351',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2351',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2351.'
    },
    2352: {
        'service_name': 'ENTERPRISE-SERVICE-2352',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2352',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2352.'
    },
    2353: {
        'service_name': 'ENTERPRISE-SERVICE-2353',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2353',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2353.'
    },
    2354: {
        'service_name': 'ENTERPRISE-SERVICE-2354',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2354',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2354.'
    },
    2355: {
        'service_name': 'ENTERPRISE-SERVICE-2355',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2355',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2355.'
    },
    2356: {
        'service_name': 'ENTERPRISE-SERVICE-2356',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2356',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2356.'
    },
    2357: {
        'service_name': 'ENTERPRISE-SERVICE-2357',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2357',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2357.'
    },
    2358: {
        'service_name': 'ENTERPRISE-SERVICE-2358',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2358',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2358.'
    },
    2359: {
        'service_name': 'ENTERPRISE-SERVICE-2359',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2359',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2359.'
    },
    2360: {
        'service_name': 'ENTERPRISE-SERVICE-2360',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2360',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2360.'
    },
    2361: {
        'service_name': 'ENTERPRISE-SERVICE-2361',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2361',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2361.'
    },
    2362: {
        'service_name': 'ENTERPRISE-SERVICE-2362',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2362',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2362.'
    },
    2363: {
        'service_name': 'ENTERPRISE-SERVICE-2363',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2363',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2363.'
    },
    2364: {
        'service_name': 'ENTERPRISE-SERVICE-2364',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2364',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2364.'
    },
    2365: {
        'service_name': 'ENTERPRISE-SERVICE-2365',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2365',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2365.'
    },
    2366: {
        'service_name': 'ENTERPRISE-SERVICE-2366',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2366',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2366.'
    },
    2367: {
        'service_name': 'ENTERPRISE-SERVICE-2367',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2367',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2367.'
    },
    2368: {
        'service_name': 'ENTERPRISE-SERVICE-2368',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2368',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2368.'
    },
    2369: {
        'service_name': 'ENTERPRISE-SERVICE-2369',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2369',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2369.'
    },
    2370: {
        'service_name': 'ENTERPRISE-SERVICE-2370',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2370',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2370.'
    },
    2371: {
        'service_name': 'ENTERPRISE-SERVICE-2371',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2371',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2371.'
    },
    2372: {
        'service_name': 'ENTERPRISE-SERVICE-2372',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2372',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2372.'
    },
    2373: {
        'service_name': 'ENTERPRISE-SERVICE-2373',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2373',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2373.'
    },
    2374: {
        'service_name': 'ENTERPRISE-SERVICE-2374',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2374',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2374.'
    },
    2375: {
        'service_name': 'ENTERPRISE-SERVICE-2375',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2375',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2375.'
    },
    2376: {
        'service_name': 'ENTERPRISE-SERVICE-2376',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2376',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2376.'
    },
    2377: {
        'service_name': 'ENTERPRISE-SERVICE-2377',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2377',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2377.'
    },
    2378: {
        'service_name': 'ENTERPRISE-SERVICE-2378',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2378',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2378.'
    },
    2379: {
        'service_name': 'ENTERPRISE-SERVICE-2379',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2379',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2379.'
    },
    2380: {
        'service_name': 'ENTERPRISE-SERVICE-2380',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2380',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2380.'
    },
    2381: {
        'service_name': 'ENTERPRISE-SERVICE-2381',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2381',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2381.'
    },
    2382: {
        'service_name': 'ENTERPRISE-SERVICE-2382',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2382',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2382.'
    },
    2383: {
        'service_name': 'ENTERPRISE-SERVICE-2383',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2383',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2383.'
    },
    2384: {
        'service_name': 'ENTERPRISE-SERVICE-2384',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2384',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2384.'
    },
    2385: {
        'service_name': 'ENTERPRISE-SERVICE-2385',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2385',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2385.'
    },
    2386: {
        'service_name': 'ENTERPRISE-SERVICE-2386',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2386',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2386.'
    },
    2387: {
        'service_name': 'ENTERPRISE-SERVICE-2387',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2387',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2387.'
    },
    2388: {
        'service_name': 'ENTERPRISE-SERVICE-2388',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2388',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2388.'
    },
    2389: {
        'service_name': 'ENTERPRISE-SERVICE-2389',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2389',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2389.'
    },
    2390: {
        'service_name': 'ENTERPRISE-SERVICE-2390',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2390',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2390.'
    },
    2391: {
        'service_name': 'ENTERPRISE-SERVICE-2391',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2391',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2391.'
    },
    2392: {
        'service_name': 'ENTERPRISE-SERVICE-2392',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2392',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2392.'
    },
    2393: {
        'service_name': 'ENTERPRISE-SERVICE-2393',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2393',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2393.'
    },
    2394: {
        'service_name': 'ENTERPRISE-SERVICE-2394',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2394',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2394.'
    },
    2395: {
        'service_name': 'ENTERPRISE-SERVICE-2395',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2395',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2395.'
    },
    2396: {
        'service_name': 'ENTERPRISE-SERVICE-2396',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2396',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2396.'
    },
    2397: {
        'service_name': 'ENTERPRISE-SERVICE-2397',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2397',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2397.'
    },
    2398: {
        'service_name': 'ENTERPRISE-SERVICE-2398',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2398',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2398.'
    },
    2399: {
        'service_name': 'ENTERPRISE-SERVICE-2399',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2399',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2399.'
    },
    2400: {
        'service_name': 'ENTERPRISE-SERVICE-2400',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2400',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2400.'
    },
    2401: {
        'service_name': 'ENTERPRISE-SERVICE-2401',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2401',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2401.'
    },
    2402: {
        'service_name': 'ENTERPRISE-SERVICE-2402',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2402',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2402.'
    },
    2403: {
        'service_name': 'ENTERPRISE-SERVICE-2403',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2403',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2403.'
    },
    2404: {
        'service_name': 'ENTERPRISE-SERVICE-2404',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2404',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2404.'
    },
    2405: {
        'service_name': 'ENTERPRISE-SERVICE-2405',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2405',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2405.'
    },
    2406: {
        'service_name': 'ENTERPRISE-SERVICE-2406',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2406',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2406.'
    },
    2407: {
        'service_name': 'ENTERPRISE-SERVICE-2407',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2407',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2407.'
    },
    2408: {
        'service_name': 'ENTERPRISE-SERVICE-2408',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2408',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2408.'
    },
    2409: {
        'service_name': 'ENTERPRISE-SERVICE-2409',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2409',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2409.'
    },
    2410: {
        'service_name': 'ENTERPRISE-SERVICE-2410',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2410',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2410.'
    },
    2411: {
        'service_name': 'ENTERPRISE-SERVICE-2411',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2411',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2411.'
    },
    2412: {
        'service_name': 'ENTERPRISE-SERVICE-2412',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2412',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2412.'
    },
    2413: {
        'service_name': 'ENTERPRISE-SERVICE-2413',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2413',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2413.'
    },
    2414: {
        'service_name': 'ENTERPRISE-SERVICE-2414',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2414',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2414.'
    },
    2415: {
        'service_name': 'ENTERPRISE-SERVICE-2415',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2415',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2415.'
    },
    2416: {
        'service_name': 'ENTERPRISE-SERVICE-2416',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2416',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2416.'
    },
    2417: {
        'service_name': 'ENTERPRISE-SERVICE-2417',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2417',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2417.'
    },
    2418: {
        'service_name': 'ENTERPRISE-SERVICE-2418',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2418',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2418.'
    },
    2419: {
        'service_name': 'ENTERPRISE-SERVICE-2419',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2419',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2419.'
    },
    2420: {
        'service_name': 'ENTERPRISE-SERVICE-2420',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2420',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2420.'
    },
    2421: {
        'service_name': 'ENTERPRISE-SERVICE-2421',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2421',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2421.'
    },
    2422: {
        'service_name': 'ENTERPRISE-SERVICE-2422',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2422',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2422.'
    },
    2423: {
        'service_name': 'ENTERPRISE-SERVICE-2423',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2423',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2423.'
    },
    2424: {
        'service_name': 'ENTERPRISE-SERVICE-2424',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2424',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2424.'
    },
    2425: {
        'service_name': 'ENTERPRISE-SERVICE-2425',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2425',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2425.'
    },
    2426: {
        'service_name': 'ENTERPRISE-SERVICE-2426',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2426',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2426.'
    },
    2427: {
        'service_name': 'ENTERPRISE-SERVICE-2427',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2427',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2427.'
    },
    2428: {
        'service_name': 'ENTERPRISE-SERVICE-2428',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2428',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2428.'
    },
    2429: {
        'service_name': 'ENTERPRISE-SERVICE-2429',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2429',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2429.'
    },
    2430: {
        'service_name': 'ENTERPRISE-SERVICE-2430',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2430',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2430.'
    },
    2431: {
        'service_name': 'ENTERPRISE-SERVICE-2431',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2431',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2431.'
    },
    2432: {
        'service_name': 'ENTERPRISE-SERVICE-2432',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2432',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2432.'
    },
    2433: {
        'service_name': 'ENTERPRISE-SERVICE-2433',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2433',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2433.'
    },
    2434: {
        'service_name': 'ENTERPRISE-SERVICE-2434',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2434',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2434.'
    },
    2435: {
        'service_name': 'ENTERPRISE-SERVICE-2435',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2435',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2435.'
    },
    2436: {
        'service_name': 'ENTERPRISE-SERVICE-2436',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2436',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2436.'
    },
    2437: {
        'service_name': 'ENTERPRISE-SERVICE-2437',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2437',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2437.'
    },
    2438: {
        'service_name': 'ENTERPRISE-SERVICE-2438',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2438',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2438.'
    },
    2439: {
        'service_name': 'ENTERPRISE-SERVICE-2439',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2439',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2439.'
    },
    2440: {
        'service_name': 'ENTERPRISE-SERVICE-2440',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2440',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2440.'
    },
    2441: {
        'service_name': 'ENTERPRISE-SERVICE-2441',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2441',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2441.'
    },
    2442: {
        'service_name': 'ENTERPRISE-SERVICE-2442',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2442',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2442.'
    },
    2443: {
        'service_name': 'ENTERPRISE-SERVICE-2443',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2443',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2443.'
    },
    2444: {
        'service_name': 'ENTERPRISE-SERVICE-2444',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2444',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2444.'
    },
    2445: {
        'service_name': 'ENTERPRISE-SERVICE-2445',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2445',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2445.'
    },
    2446: {
        'service_name': 'ENTERPRISE-SERVICE-2446',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2446',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2446.'
    },
    2447: {
        'service_name': 'ENTERPRISE-SERVICE-2447',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2447',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2447.'
    },
    2448: {
        'service_name': 'ENTERPRISE-SERVICE-2448',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2448',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2448.'
    },
    2449: {
        'service_name': 'ENTERPRISE-SERVICE-2449',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2449',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2449.'
    },
    2450: {
        'service_name': 'ENTERPRISE-SERVICE-2450',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2450',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2450.'
    },
    2451: {
        'service_name': 'ENTERPRISE-SERVICE-2451',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2451',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2451.'
    },
    2452: {
        'service_name': 'ENTERPRISE-SERVICE-2452',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2452',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2452.'
    },
    2453: {
        'service_name': 'ENTERPRISE-SERVICE-2453',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2453',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2453.'
    },
    2454: {
        'service_name': 'ENTERPRISE-SERVICE-2454',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2454',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2454.'
    },
    2455: {
        'service_name': 'ENTERPRISE-SERVICE-2455',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2455',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2455.'
    },
    2456: {
        'service_name': 'ENTERPRISE-SERVICE-2456',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2456',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2456.'
    },
    2457: {
        'service_name': 'ENTERPRISE-SERVICE-2457',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2457',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2457.'
    },
    2458: {
        'service_name': 'ENTERPRISE-SERVICE-2458',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2458',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2458.'
    },
    2459: {
        'service_name': 'ENTERPRISE-SERVICE-2459',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2459',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2459.'
    },
    2460: {
        'service_name': 'ENTERPRISE-SERVICE-2460',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2460',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2460.'
    },
    2461: {
        'service_name': 'ENTERPRISE-SERVICE-2461',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2461',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2461.'
    },
    2462: {
        'service_name': 'ENTERPRISE-SERVICE-2462',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2462',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2462.'
    },
    2463: {
        'service_name': 'ENTERPRISE-SERVICE-2463',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2463',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2463.'
    },
    2464: {
        'service_name': 'ENTERPRISE-SERVICE-2464',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2464',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2464.'
    },
    2465: {
        'service_name': 'ENTERPRISE-SERVICE-2465',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2465',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2465.'
    },
    2466: {
        'service_name': 'ENTERPRISE-SERVICE-2466',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2466',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2466.'
    },
    2467: {
        'service_name': 'ENTERPRISE-SERVICE-2467',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2467',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2467.'
    },
    2468: {
        'service_name': 'ENTERPRISE-SERVICE-2468',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2468',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2468.'
    },
    2469: {
        'service_name': 'ENTERPRISE-SERVICE-2469',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2469',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2469.'
    },
    2470: {
        'service_name': 'ENTERPRISE-SERVICE-2470',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2470',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2470.'
    },
    2471: {
        'service_name': 'ENTERPRISE-SERVICE-2471',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2471',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2471.'
    },
    2472: {
        'service_name': 'ENTERPRISE-SERVICE-2472',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2472',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2472.'
    },
    2473: {
        'service_name': 'ENTERPRISE-SERVICE-2473',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2473',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2473.'
    },
    2474: {
        'service_name': 'ENTERPRISE-SERVICE-2474',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2474',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2474.'
    },
    2475: {
        'service_name': 'ENTERPRISE-SERVICE-2475',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2475',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2475.'
    },
    2476: {
        'service_name': 'ENTERPRISE-SERVICE-2476',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2476',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2476.'
    },
    2477: {
        'service_name': 'ENTERPRISE-SERVICE-2477',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2477',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2477.'
    },
    2478: {
        'service_name': 'ENTERPRISE-SERVICE-2478',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2478',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2478.'
    },
    2479: {
        'service_name': 'ENTERPRISE-SERVICE-2479',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2479',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2479.'
    },
    2480: {
        'service_name': 'ENTERPRISE-SERVICE-2480',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2480',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2480.'
    },
    2481: {
        'service_name': 'ENTERPRISE-SERVICE-2481',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2481',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2481.'
    },
    2482: {
        'service_name': 'ENTERPRISE-SERVICE-2482',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2482',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2482.'
    },
    2483: {
        'service_name': 'ENTERPRISE-SERVICE-2483',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2483',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2483.'
    },
    2484: {
        'service_name': 'ENTERPRISE-SERVICE-2484',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2484',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2484.'
    },
    2485: {
        'service_name': 'ENTERPRISE-SERVICE-2485',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2485',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2485.'
    },
    2486: {
        'service_name': 'ENTERPRISE-SERVICE-2486',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2486',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2486.'
    },
    2487: {
        'service_name': 'ENTERPRISE-SERVICE-2487',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2487',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2487.'
    },
    2488: {
        'service_name': 'ENTERPRISE-SERVICE-2488',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2488',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2488.'
    },
    2489: {
        'service_name': 'ENTERPRISE-SERVICE-2489',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2489',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2489.'
    },
    2490: {
        'service_name': 'ENTERPRISE-SERVICE-2490',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2490',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2490.'
    },
    2491: {
        'service_name': 'ENTERPRISE-SERVICE-2491',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2491',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2491.'
    },
    2492: {
        'service_name': 'ENTERPRISE-SERVICE-2492',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2492',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2492.'
    },
    2493: {
        'service_name': 'ENTERPRISE-SERVICE-2493',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2493',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2493.'
    },
    2494: {
        'service_name': 'ENTERPRISE-SERVICE-2494',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2494',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2494.'
    },
    2495: {
        'service_name': 'ENTERPRISE-SERVICE-2495',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2495',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2495.'
    },
    2496: {
        'service_name': 'ENTERPRISE-SERVICE-2496',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2496',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2496.'
    },
    2497: {
        'service_name': 'ENTERPRISE-SERVICE-2497',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2497',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2497.'
    },
    2498: {
        'service_name': 'ENTERPRISE-SERVICE-2498',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2498',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2498.'
    },
    2499: {
        'service_name': 'ENTERPRISE-SERVICE-2499',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2499',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2499.'
    },
    2500: {
        'service_name': 'ENTERPRISE-SERVICE-2500',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2500',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2500.'
    },
    2501: {
        'service_name': 'ENTERPRISE-SERVICE-2501',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2501',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2501.'
    },
    2502: {
        'service_name': 'ENTERPRISE-SERVICE-2502',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2502',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2502.'
    },
    2503: {
        'service_name': 'ENTERPRISE-SERVICE-2503',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2503',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2503.'
    },
    2504: {
        'service_name': 'ENTERPRISE-SERVICE-2504',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2504',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2504.'
    },
    2505: {
        'service_name': 'ENTERPRISE-SERVICE-2505',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2505',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2505.'
    },
    2506: {
        'service_name': 'ENTERPRISE-SERVICE-2506',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2506',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2506.'
    },
    2507: {
        'service_name': 'ENTERPRISE-SERVICE-2507',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2507',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2507.'
    },
    2508: {
        'service_name': 'ENTERPRISE-SERVICE-2508',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2508',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2508.'
    },
    2509: {
        'service_name': 'ENTERPRISE-SERVICE-2509',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2509',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2509.'
    },
    2510: {
        'service_name': 'ENTERPRISE-SERVICE-2510',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2510',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2510.'
    },
    2511: {
        'service_name': 'ENTERPRISE-SERVICE-2511',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2511',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2511.'
    },
    2512: {
        'service_name': 'ENTERPRISE-SERVICE-2512',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2512',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2512.'
    },
    2513: {
        'service_name': 'ENTERPRISE-SERVICE-2513',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2513',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2513.'
    },
    2514: {
        'service_name': 'ENTERPRISE-SERVICE-2514',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2514',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2514.'
    },
    2515: {
        'service_name': 'ENTERPRISE-SERVICE-2515',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2515',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2515.'
    },
    2516: {
        'service_name': 'ENTERPRISE-SERVICE-2516',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2516',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2516.'
    },
    2517: {
        'service_name': 'ENTERPRISE-SERVICE-2517',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2517',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2517.'
    },
    2518: {
        'service_name': 'ENTERPRISE-SERVICE-2518',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2518',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2518.'
    },
    2519: {
        'service_name': 'ENTERPRISE-SERVICE-2519',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2519',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2519.'
    },
    2520: {
        'service_name': 'ENTERPRISE-SERVICE-2520',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2520',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2520.'
    },
    2521: {
        'service_name': 'ENTERPRISE-SERVICE-2521',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2521',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2521.'
    },
    2522: {
        'service_name': 'ENTERPRISE-SERVICE-2522',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2522',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2522.'
    },
    2523: {
        'service_name': 'ENTERPRISE-SERVICE-2523',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2523',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2523.'
    },
    2524: {
        'service_name': 'ENTERPRISE-SERVICE-2524',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2524',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2524.'
    },
    2525: {
        'service_name': 'ENTERPRISE-SERVICE-2525',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2525',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2525.'
    },
    2526: {
        'service_name': 'ENTERPRISE-SERVICE-2526',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2526',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2526.'
    },
    2527: {
        'service_name': 'ENTERPRISE-SERVICE-2527',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2527',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2527.'
    },
    2528: {
        'service_name': 'ENTERPRISE-SERVICE-2528',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2528',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2528.'
    },
    2529: {
        'service_name': 'ENTERPRISE-SERVICE-2529',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2529',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2529.'
    },
    2530: {
        'service_name': 'ENTERPRISE-SERVICE-2530',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2530',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2530.'
    },
    2531: {
        'service_name': 'ENTERPRISE-SERVICE-2531',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2531',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2531.'
    },
    2532: {
        'service_name': 'ENTERPRISE-SERVICE-2532',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2532',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2532.'
    },
    2533: {
        'service_name': 'ENTERPRISE-SERVICE-2533',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2533',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2533.'
    },
    2534: {
        'service_name': 'ENTERPRISE-SERVICE-2534',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2534',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2534.'
    },
    2535: {
        'service_name': 'ENTERPRISE-SERVICE-2535',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2535',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2535.'
    },
    2536: {
        'service_name': 'ENTERPRISE-SERVICE-2536',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2536',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2536.'
    },
    2537: {
        'service_name': 'ENTERPRISE-SERVICE-2537',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2537',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2537.'
    },
    2538: {
        'service_name': 'ENTERPRISE-SERVICE-2538',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2538',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2538.'
    },
    2539: {
        'service_name': 'ENTERPRISE-SERVICE-2539',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2539',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2539.'
    },
    2540: {
        'service_name': 'ENTERPRISE-SERVICE-2540',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2540',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2540.'
    },
    2541: {
        'service_name': 'ENTERPRISE-SERVICE-2541',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2541',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2541.'
    },
    2542: {
        'service_name': 'ENTERPRISE-SERVICE-2542',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2542',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2542.'
    },
    2543: {
        'service_name': 'ENTERPRISE-SERVICE-2543',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2543',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2543.'
    },
    2544: {
        'service_name': 'ENTERPRISE-SERVICE-2544',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2544',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2544.'
    },
    2545: {
        'service_name': 'ENTERPRISE-SERVICE-2545',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2545',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2545.'
    },
    2546: {
        'service_name': 'ENTERPRISE-SERVICE-2546',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2546',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2546.'
    },
    2547: {
        'service_name': 'ENTERPRISE-SERVICE-2547',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2547',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2547.'
    },
    2548: {
        'service_name': 'ENTERPRISE-SERVICE-2548',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2548',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2548.'
    },
    2549: {
        'service_name': 'ENTERPRISE-SERVICE-2549',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2549',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2549.'
    },
    2550: {
        'service_name': 'ENTERPRISE-SERVICE-2550',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2550',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2550.'
    },
    2551: {
        'service_name': 'ENTERPRISE-SERVICE-2551',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2551',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2551.'
    },
    2552: {
        'service_name': 'ENTERPRISE-SERVICE-2552',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2552',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2552.'
    },
    2553: {
        'service_name': 'ENTERPRISE-SERVICE-2553',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2553',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2553.'
    },
    2554: {
        'service_name': 'ENTERPRISE-SERVICE-2554',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2554',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2554.'
    },
    2555: {
        'service_name': 'ENTERPRISE-SERVICE-2555',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2555',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2555.'
    },
    2556: {
        'service_name': 'ENTERPRISE-SERVICE-2556',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2556',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2556.'
    },
    2557: {
        'service_name': 'ENTERPRISE-SERVICE-2557',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2557',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2557.'
    },
    2558: {
        'service_name': 'ENTERPRISE-SERVICE-2558',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2558',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2558.'
    },
    2559: {
        'service_name': 'ENTERPRISE-SERVICE-2559',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2559',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2559.'
    },
    2560: {
        'service_name': 'ENTERPRISE-SERVICE-2560',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2560',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2560.'
    },
    2561: {
        'service_name': 'ENTERPRISE-SERVICE-2561',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2561',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2561.'
    },
    2562: {
        'service_name': 'ENTERPRISE-SERVICE-2562',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2562',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2562.'
    },
    2563: {
        'service_name': 'ENTERPRISE-SERVICE-2563',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2563',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2563.'
    },
    2564: {
        'service_name': 'ENTERPRISE-SERVICE-2564',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2564',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2564.'
    },
    2565: {
        'service_name': 'ENTERPRISE-SERVICE-2565',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2565',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2565.'
    },
    2566: {
        'service_name': 'ENTERPRISE-SERVICE-2566',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2566',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2566.'
    },
    2567: {
        'service_name': 'ENTERPRISE-SERVICE-2567',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2567',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2567.'
    },
    2568: {
        'service_name': 'ENTERPRISE-SERVICE-2568',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2568',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2568.'
    },
    2569: {
        'service_name': 'ENTERPRISE-SERVICE-2569',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2569',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2569.'
    },
    2570: {
        'service_name': 'ENTERPRISE-SERVICE-2570',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2570',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2570.'
    },
    2571: {
        'service_name': 'ENTERPRISE-SERVICE-2571',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2571',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2571.'
    },
    2572: {
        'service_name': 'ENTERPRISE-SERVICE-2572',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2572',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2572.'
    },
    2573: {
        'service_name': 'ENTERPRISE-SERVICE-2573',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2573',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2573.'
    },
    2574: {
        'service_name': 'ENTERPRISE-SERVICE-2574',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2574',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2574.'
    },
    2575: {
        'service_name': 'ENTERPRISE-SERVICE-2575',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2575',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2575.'
    },
    2576: {
        'service_name': 'ENTERPRISE-SERVICE-2576',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2576',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2576.'
    },
    2577: {
        'service_name': 'ENTERPRISE-SERVICE-2577',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2577',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2577.'
    },
    2578: {
        'service_name': 'ENTERPRISE-SERVICE-2578',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2578',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2578.'
    },
    2579: {
        'service_name': 'ENTERPRISE-SERVICE-2579',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2579',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2579.'
    },
    2580: {
        'service_name': 'ENTERPRISE-SERVICE-2580',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2580',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2580.'
    },
    2581: {
        'service_name': 'ENTERPRISE-SERVICE-2581',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2581',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2581.'
    },
    2582: {
        'service_name': 'ENTERPRISE-SERVICE-2582',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2582',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2582.'
    },
    2583: {
        'service_name': 'ENTERPRISE-SERVICE-2583',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2583',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2583.'
    },
    2584: {
        'service_name': 'ENTERPRISE-SERVICE-2584',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2584',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2584.'
    },
    2585: {
        'service_name': 'ENTERPRISE-SERVICE-2585',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2585',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2585.'
    },
    2586: {
        'service_name': 'ENTERPRISE-SERVICE-2586',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2586',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2586.'
    },
    2587: {
        'service_name': 'ENTERPRISE-SERVICE-2587',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2587',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2587.'
    },
    2588: {
        'service_name': 'ENTERPRISE-SERVICE-2588',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2588',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2588.'
    },
    2589: {
        'service_name': 'ENTERPRISE-SERVICE-2589',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2589',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2589.'
    },
    2590: {
        'service_name': 'ENTERPRISE-SERVICE-2590',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2590',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2590.'
    },
    2591: {
        'service_name': 'ENTERPRISE-SERVICE-2591',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2591',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2591.'
    },
    2592: {
        'service_name': 'ENTERPRISE-SERVICE-2592',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2592',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2592.'
    },
    2593: {
        'service_name': 'ENTERPRISE-SERVICE-2593',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2593',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2593.'
    },
    2594: {
        'service_name': 'ENTERPRISE-SERVICE-2594',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2594',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2594.'
    },
    2595: {
        'service_name': 'ENTERPRISE-SERVICE-2595',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2595',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2595.'
    },
    2596: {
        'service_name': 'ENTERPRISE-SERVICE-2596',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2596',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2596.'
    },
    2597: {
        'service_name': 'ENTERPRISE-SERVICE-2597',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2597',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2597.'
    },
    2598: {
        'service_name': 'ENTERPRISE-SERVICE-2598',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2598',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2598.'
    },
    2599: {
        'service_name': 'ENTERPRISE-SERVICE-2599',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2599',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2599.'
    },
    2600: {
        'service_name': 'ENTERPRISE-SERVICE-2600',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2600',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2600.'
    },
    2601: {
        'service_name': 'ENTERPRISE-SERVICE-2601',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2601',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2601.'
    },
    2602: {
        'service_name': 'ENTERPRISE-SERVICE-2602',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2602',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2602.'
    },
    2603: {
        'service_name': 'ENTERPRISE-SERVICE-2603',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2603',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2603.'
    },
    2604: {
        'service_name': 'ENTERPRISE-SERVICE-2604',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2604',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2604.'
    },
    2605: {
        'service_name': 'ENTERPRISE-SERVICE-2605',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2605',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2605.'
    },
    2606: {
        'service_name': 'ENTERPRISE-SERVICE-2606',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2606',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2606.'
    },
    2607: {
        'service_name': 'ENTERPRISE-SERVICE-2607',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2607',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2607.'
    },
    2608: {
        'service_name': 'ENTERPRISE-SERVICE-2608',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2608',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2608.'
    },
    2609: {
        'service_name': 'ENTERPRISE-SERVICE-2609',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2609',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2609.'
    },
    2610: {
        'service_name': 'ENTERPRISE-SERVICE-2610',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2610',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2610.'
    },
    2611: {
        'service_name': 'ENTERPRISE-SERVICE-2611',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2611',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2611.'
    },
    2612: {
        'service_name': 'ENTERPRISE-SERVICE-2612',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2612',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2612.'
    },
    2613: {
        'service_name': 'ENTERPRISE-SERVICE-2613',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2613',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2613.'
    },
    2614: {
        'service_name': 'ENTERPRISE-SERVICE-2614',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2614',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2614.'
    },
    2615: {
        'service_name': 'ENTERPRISE-SERVICE-2615',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2615',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2615.'
    },
    2616: {
        'service_name': 'ENTERPRISE-SERVICE-2616',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2616',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2616.'
    },
    2617: {
        'service_name': 'ENTERPRISE-SERVICE-2617',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2617',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2617.'
    },
    2618: {
        'service_name': 'ENTERPRISE-SERVICE-2618',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2618',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2618.'
    },
    2619: {
        'service_name': 'ENTERPRISE-SERVICE-2619',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2619',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2619.'
    },
    2620: {
        'service_name': 'ENTERPRISE-SERVICE-2620',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2620',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2620.'
    },
    2621: {
        'service_name': 'ENTERPRISE-SERVICE-2621',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2621',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2621.'
    },
    2622: {
        'service_name': 'ENTERPRISE-SERVICE-2622',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2622',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2622.'
    },
    2623: {
        'service_name': 'ENTERPRISE-SERVICE-2623',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2623',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2623.'
    },
    2624: {
        'service_name': 'ENTERPRISE-SERVICE-2624',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2624',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2624.'
    },
    2625: {
        'service_name': 'ENTERPRISE-SERVICE-2625',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2625',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2625.'
    },
    2626: {
        'service_name': 'ENTERPRISE-SERVICE-2626',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2626',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2626.'
    },
    2627: {
        'service_name': 'ENTERPRISE-SERVICE-2627',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2627',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2627.'
    },
    2628: {
        'service_name': 'ENTERPRISE-SERVICE-2628',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2628',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2628.'
    },
    2629: {
        'service_name': 'ENTERPRISE-SERVICE-2629',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2629',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2629.'
    },
    2630: {
        'service_name': 'ENTERPRISE-SERVICE-2630',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2630',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2630.'
    },
    2631: {
        'service_name': 'ENTERPRISE-SERVICE-2631',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2631',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2631.'
    },
    2632: {
        'service_name': 'ENTERPRISE-SERVICE-2632',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2632',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2632.'
    },
    2633: {
        'service_name': 'ENTERPRISE-SERVICE-2633',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2633',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2633.'
    },
    2634: {
        'service_name': 'ENTERPRISE-SERVICE-2634',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2634',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2634.'
    },
    2635: {
        'service_name': 'ENTERPRISE-SERVICE-2635',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2635',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2635.'
    },
    2636: {
        'service_name': 'ENTERPRISE-SERVICE-2636',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2636',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2636.'
    },
    2637: {
        'service_name': 'ENTERPRISE-SERVICE-2637',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2637',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2637.'
    },
    2638: {
        'service_name': 'ENTERPRISE-SERVICE-2638',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2638',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2638.'
    },
    2639: {
        'service_name': 'ENTERPRISE-SERVICE-2639',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2639',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2639.'
    },
    2640: {
        'service_name': 'ENTERPRISE-SERVICE-2640',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2640',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2640.'
    },
    2641: {
        'service_name': 'ENTERPRISE-SERVICE-2641',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2641',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2641.'
    },
    2642: {
        'service_name': 'ENTERPRISE-SERVICE-2642',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2642',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2642.'
    },
    2643: {
        'service_name': 'ENTERPRISE-SERVICE-2643',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2643',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2643.'
    },
    2644: {
        'service_name': 'ENTERPRISE-SERVICE-2644',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2644',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2644.'
    },
    2645: {
        'service_name': 'ENTERPRISE-SERVICE-2645',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2645',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2645.'
    },
    2646: {
        'service_name': 'ENTERPRISE-SERVICE-2646',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2646',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2646.'
    },
    2647: {
        'service_name': 'ENTERPRISE-SERVICE-2647',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2647',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2647.'
    },
    2648: {
        'service_name': 'ENTERPRISE-SERVICE-2648',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2648',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2648.'
    },
    2649: {
        'service_name': 'ENTERPRISE-SERVICE-2649',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2649',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2649.'
    },
    2650: {
        'service_name': 'ENTERPRISE-SERVICE-2650',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2650',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2650.'
    },
    2651: {
        'service_name': 'ENTERPRISE-SERVICE-2651',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2651',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2651.'
    },
    2652: {
        'service_name': 'ENTERPRISE-SERVICE-2652',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2652',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2652.'
    },
    2653: {
        'service_name': 'ENTERPRISE-SERVICE-2653',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2653',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2653.'
    },
    2654: {
        'service_name': 'ENTERPRISE-SERVICE-2654',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2654',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2654.'
    },
    2655: {
        'service_name': 'ENTERPRISE-SERVICE-2655',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2655',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2655.'
    },
    2656: {
        'service_name': 'ENTERPRISE-SERVICE-2656',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2656',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2656.'
    },
    2657: {
        'service_name': 'ENTERPRISE-SERVICE-2657',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2657',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2657.'
    },
    2658: {
        'service_name': 'ENTERPRISE-SERVICE-2658',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2658',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2658.'
    },
    2659: {
        'service_name': 'ENTERPRISE-SERVICE-2659',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2659',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2659.'
    },
    2660: {
        'service_name': 'ENTERPRISE-SERVICE-2660',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2660',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2660.'
    },
    2661: {
        'service_name': 'ENTERPRISE-SERVICE-2661',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2661',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2661.'
    },
    2662: {
        'service_name': 'ENTERPRISE-SERVICE-2662',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2662',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2662.'
    },
    2663: {
        'service_name': 'ENTERPRISE-SERVICE-2663',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2663',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2663.'
    },
    2664: {
        'service_name': 'ENTERPRISE-SERVICE-2664',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2664',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2664.'
    },
    2665: {
        'service_name': 'ENTERPRISE-SERVICE-2665',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2665',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2665.'
    },
    2666: {
        'service_name': 'ENTERPRISE-SERVICE-2666',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2666',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2666.'
    },
    2667: {
        'service_name': 'ENTERPRISE-SERVICE-2667',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2667',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2667.'
    },
    2668: {
        'service_name': 'ENTERPRISE-SERVICE-2668',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2668',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2668.'
    },
    2669: {
        'service_name': 'ENTERPRISE-SERVICE-2669',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2669',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2669.'
    },
    2670: {
        'service_name': 'ENTERPRISE-SERVICE-2670',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2670',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2670.'
    },
    2671: {
        'service_name': 'ENTERPRISE-SERVICE-2671',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2671',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2671.'
    },
    2672: {
        'service_name': 'ENTERPRISE-SERVICE-2672',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2672',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2672.'
    },
    2673: {
        'service_name': 'ENTERPRISE-SERVICE-2673',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2673',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2673.'
    },
    2674: {
        'service_name': 'ENTERPRISE-SERVICE-2674',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2674',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2674.'
    },
    2675: {
        'service_name': 'ENTERPRISE-SERVICE-2675',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2675',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2675.'
    },
    2676: {
        'service_name': 'ENTERPRISE-SERVICE-2676',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2676',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2676.'
    },
    2677: {
        'service_name': 'ENTERPRISE-SERVICE-2677',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2677',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2677.'
    },
    2678: {
        'service_name': 'ENTERPRISE-SERVICE-2678',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2678',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2678.'
    },
    2679: {
        'service_name': 'ENTERPRISE-SERVICE-2679',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2679',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2679.'
    },
    2680: {
        'service_name': 'ENTERPRISE-SERVICE-2680',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2680',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2680.'
    },
    2681: {
        'service_name': 'ENTERPRISE-SERVICE-2681',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2681',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2681.'
    },
    2682: {
        'service_name': 'ENTERPRISE-SERVICE-2682',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2682',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2682.'
    },
    2683: {
        'service_name': 'ENTERPRISE-SERVICE-2683',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2683',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2683.'
    },
    2684: {
        'service_name': 'ENTERPRISE-SERVICE-2684',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2684',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2684.'
    },
    2685: {
        'service_name': 'ENTERPRISE-SERVICE-2685',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2685',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2685.'
    },
    2686: {
        'service_name': 'ENTERPRISE-SERVICE-2686',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2686',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2686.'
    },
    2687: {
        'service_name': 'ENTERPRISE-SERVICE-2687',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2687',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2687.'
    },
    2688: {
        'service_name': 'ENTERPRISE-SERVICE-2688',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2688',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2688.'
    },
    2689: {
        'service_name': 'ENTERPRISE-SERVICE-2689',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2689',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2689.'
    },
    2690: {
        'service_name': 'ENTERPRISE-SERVICE-2690',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2690',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2690.'
    },
    2691: {
        'service_name': 'ENTERPRISE-SERVICE-2691',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2691',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2691.'
    },
    2692: {
        'service_name': 'ENTERPRISE-SERVICE-2692',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2692',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2692.'
    },
    2693: {
        'service_name': 'ENTERPRISE-SERVICE-2693',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2693',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2693.'
    },
    2694: {
        'service_name': 'ENTERPRISE-SERVICE-2694',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2694',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2694.'
    },
    2695: {
        'service_name': 'ENTERPRISE-SERVICE-2695',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2695',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2695.'
    },
    2696: {
        'service_name': 'ENTERPRISE-SERVICE-2696',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2696',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2696.'
    },
    2697: {
        'service_name': 'ENTERPRISE-SERVICE-2697',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2697',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2697.'
    },
    2698: {
        'service_name': 'ENTERPRISE-SERVICE-2698',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2698',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2698.'
    },
    2699: {
        'service_name': 'ENTERPRISE-SERVICE-2699',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2699',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2699.'
    },
    2700: {
        'service_name': 'ENTERPRISE-SERVICE-2700',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2700',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2700.'
    },
    2701: {
        'service_name': 'ENTERPRISE-SERVICE-2701',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2701',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2701.'
    },
    2702: {
        'service_name': 'ENTERPRISE-SERVICE-2702',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2702',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2702.'
    },
    2703: {
        'service_name': 'ENTERPRISE-SERVICE-2703',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2703',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2703.'
    },
    2704: {
        'service_name': 'ENTERPRISE-SERVICE-2704',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2704',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2704.'
    },
    2705: {
        'service_name': 'ENTERPRISE-SERVICE-2705',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2705',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2705.'
    },
    2706: {
        'service_name': 'ENTERPRISE-SERVICE-2706',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2706',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2706.'
    },
    2707: {
        'service_name': 'ENTERPRISE-SERVICE-2707',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2707',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2707.'
    },
    2708: {
        'service_name': 'ENTERPRISE-SERVICE-2708',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2708',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2708.'
    },
    2709: {
        'service_name': 'ENTERPRISE-SERVICE-2709',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2709',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2709.'
    },
    2710: {
        'service_name': 'ENTERPRISE-SERVICE-2710',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2710',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2710.'
    },
    2711: {
        'service_name': 'ENTERPRISE-SERVICE-2711',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2711',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2711.'
    },
    2712: {
        'service_name': 'ENTERPRISE-SERVICE-2712',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2712',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2712.'
    },
    2713: {
        'service_name': 'ENTERPRISE-SERVICE-2713',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2713',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2713.'
    },
    2714: {
        'service_name': 'ENTERPRISE-SERVICE-2714',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2714',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2714.'
    },
    2715: {
        'service_name': 'ENTERPRISE-SERVICE-2715',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2715',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2715.'
    },
    2716: {
        'service_name': 'ENTERPRISE-SERVICE-2716',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2716',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2716.'
    },
    2717: {
        'service_name': 'ENTERPRISE-SERVICE-2717',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2717',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2717.'
    },
    2718: {
        'service_name': 'ENTERPRISE-SERVICE-2718',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2718',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2718.'
    },
    2719: {
        'service_name': 'ENTERPRISE-SERVICE-2719',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2719',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2719.'
    },
    2720: {
        'service_name': 'ENTERPRISE-SERVICE-2720',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2720',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2720.'
    },
    2721: {
        'service_name': 'ENTERPRISE-SERVICE-2721',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2721',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2721.'
    },
    2722: {
        'service_name': 'ENTERPRISE-SERVICE-2722',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2722',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2722.'
    },
    2723: {
        'service_name': 'ENTERPRISE-SERVICE-2723',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2723',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2723.'
    },
    2724: {
        'service_name': 'ENTERPRISE-SERVICE-2724',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2724',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2724.'
    },
    2725: {
        'service_name': 'ENTERPRISE-SERVICE-2725',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2725',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2725.'
    },
    2726: {
        'service_name': 'ENTERPRISE-SERVICE-2726',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2726',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2726.'
    },
    2727: {
        'service_name': 'ENTERPRISE-SERVICE-2727',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2727',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2727.'
    },
    2728: {
        'service_name': 'ENTERPRISE-SERVICE-2728',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2728',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2728.'
    },
    2729: {
        'service_name': 'ENTERPRISE-SERVICE-2729',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2729',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2729.'
    },
    2730: {
        'service_name': 'ENTERPRISE-SERVICE-2730',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2730',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2730.'
    },
    2731: {
        'service_name': 'ENTERPRISE-SERVICE-2731',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2731',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2731.'
    },
    2732: {
        'service_name': 'ENTERPRISE-SERVICE-2732',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2732',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2732.'
    },
    2733: {
        'service_name': 'ENTERPRISE-SERVICE-2733',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2733',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2733.'
    },
    2734: {
        'service_name': 'ENTERPRISE-SERVICE-2734',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2734',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2734.'
    },
    2735: {
        'service_name': 'ENTERPRISE-SERVICE-2735',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2735',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2735.'
    },
    2736: {
        'service_name': 'ENTERPRISE-SERVICE-2736',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2736',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2736.'
    },
    2737: {
        'service_name': 'ENTERPRISE-SERVICE-2737',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2737',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2737.'
    },
    2738: {
        'service_name': 'ENTERPRISE-SERVICE-2738',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2738',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2738.'
    },
    2739: {
        'service_name': 'ENTERPRISE-SERVICE-2739',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2739',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2739.'
    },
    2740: {
        'service_name': 'ENTERPRISE-SERVICE-2740',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2740',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2740.'
    },
    2741: {
        'service_name': 'ENTERPRISE-SERVICE-2741',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2741',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2741.'
    },
    2742: {
        'service_name': 'ENTERPRISE-SERVICE-2742',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2742',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2742.'
    },
    2743: {
        'service_name': 'ENTERPRISE-SERVICE-2743',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2743',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2743.'
    },
    2744: {
        'service_name': 'ENTERPRISE-SERVICE-2744',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2744',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2744.'
    },
    2745: {
        'service_name': 'ENTERPRISE-SERVICE-2745',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2745',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2745.'
    },
    2746: {
        'service_name': 'ENTERPRISE-SERVICE-2746',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2746',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2746.'
    },
    2747: {
        'service_name': 'ENTERPRISE-SERVICE-2747',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2747',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2747.'
    },
    2748: {
        'service_name': 'ENTERPRISE-SERVICE-2748',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2748',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2748.'
    },
    2749: {
        'service_name': 'ENTERPRISE-SERVICE-2749',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2749',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2749.'
    },
    2750: {
        'service_name': 'ENTERPRISE-SERVICE-2750',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2750',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2750.'
    },
    2751: {
        'service_name': 'ENTERPRISE-SERVICE-2751',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2751',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2751.'
    },
    2752: {
        'service_name': 'ENTERPRISE-SERVICE-2752',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2752',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2752.'
    },
    2753: {
        'service_name': 'ENTERPRISE-SERVICE-2753',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2753',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2753.'
    },
    2754: {
        'service_name': 'ENTERPRISE-SERVICE-2754',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2754',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2754.'
    },
    2755: {
        'service_name': 'ENTERPRISE-SERVICE-2755',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2755',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2755.'
    },
    2756: {
        'service_name': 'ENTERPRISE-SERVICE-2756',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2756',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2756.'
    },
    2757: {
        'service_name': 'ENTERPRISE-SERVICE-2757',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2757',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2757.'
    },
    2758: {
        'service_name': 'ENTERPRISE-SERVICE-2758',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2758',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2758.'
    },
    2759: {
        'service_name': 'ENTERPRISE-SERVICE-2759',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2759',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2759.'
    },
    2760: {
        'service_name': 'ENTERPRISE-SERVICE-2760',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2760',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2760.'
    },
    2761: {
        'service_name': 'ENTERPRISE-SERVICE-2761',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2761',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2761.'
    },
    2762: {
        'service_name': 'ENTERPRISE-SERVICE-2762',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2762',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2762.'
    },
    2763: {
        'service_name': 'ENTERPRISE-SERVICE-2763',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2763',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2763.'
    },
    2764: {
        'service_name': 'ENTERPRISE-SERVICE-2764',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2764',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2764.'
    },
    2765: {
        'service_name': 'ENTERPRISE-SERVICE-2765',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2765',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2765.'
    },
    2766: {
        'service_name': 'ENTERPRISE-SERVICE-2766',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2766',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2766.'
    },
    2767: {
        'service_name': 'ENTERPRISE-SERVICE-2767',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2767',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2767.'
    },
    2768: {
        'service_name': 'ENTERPRISE-SERVICE-2768',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2768',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2768.'
    },
    2769: {
        'service_name': 'ENTERPRISE-SERVICE-2769',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2769',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2769.'
    },
    2770: {
        'service_name': 'ENTERPRISE-SERVICE-2770',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2770',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2770.'
    },
    2771: {
        'service_name': 'ENTERPRISE-SERVICE-2771',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2771',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2771.'
    },
    2772: {
        'service_name': 'ENTERPRISE-SERVICE-2772',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2772',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2772.'
    },
    2773: {
        'service_name': 'ENTERPRISE-SERVICE-2773',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2773',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2773.'
    },
    2774: {
        'service_name': 'ENTERPRISE-SERVICE-2774',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2774',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2774.'
    },
    2775: {
        'service_name': 'ENTERPRISE-SERVICE-2775',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2775',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2775.'
    },
    2776: {
        'service_name': 'ENTERPRISE-SERVICE-2776',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2776',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2776.'
    },
    2777: {
        'service_name': 'ENTERPRISE-SERVICE-2777',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2777',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2777.'
    },
    2778: {
        'service_name': 'ENTERPRISE-SERVICE-2778',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2778',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2778.'
    },
    2779: {
        'service_name': 'ENTERPRISE-SERVICE-2779',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2779',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2779.'
    },
    2780: {
        'service_name': 'ENTERPRISE-SERVICE-2780',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2780',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2780.'
    },
    2781: {
        'service_name': 'ENTERPRISE-SERVICE-2781',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2781',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2781.'
    },
    2782: {
        'service_name': 'ENTERPRISE-SERVICE-2782',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2782',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2782.'
    },
    2783: {
        'service_name': 'ENTERPRISE-SERVICE-2783',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2783',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2783.'
    },
    2784: {
        'service_name': 'ENTERPRISE-SERVICE-2784',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2784',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2784.'
    },
    2785: {
        'service_name': 'ENTERPRISE-SERVICE-2785',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2785',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2785.'
    },
    2786: {
        'service_name': 'ENTERPRISE-SERVICE-2786',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2786',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2786.'
    },
    2787: {
        'service_name': 'ENTERPRISE-SERVICE-2787',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2787',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2787.'
    },
    2788: {
        'service_name': 'ENTERPRISE-SERVICE-2788',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2788',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2788.'
    },
    2789: {
        'service_name': 'ENTERPRISE-SERVICE-2789',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2789',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2789.'
    },
    2790: {
        'service_name': 'ENTERPRISE-SERVICE-2790',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2790',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2790.'
    },
    2791: {
        'service_name': 'ENTERPRISE-SERVICE-2791',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2791',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2791.'
    },
    2792: {
        'service_name': 'ENTERPRISE-SERVICE-2792',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2792',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2792.'
    },
    2793: {
        'service_name': 'ENTERPRISE-SERVICE-2793',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2793',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2793.'
    },
    2794: {
        'service_name': 'ENTERPRISE-SERVICE-2794',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2794',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2794.'
    },
    2795: {
        'service_name': 'ENTERPRISE-SERVICE-2795',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2795',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2795.'
    },
    2796: {
        'service_name': 'ENTERPRISE-SERVICE-2796',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2796',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2796.'
    },
    2797: {
        'service_name': 'ENTERPRISE-SERVICE-2797',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2797',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2797.'
    },
    2798: {
        'service_name': 'ENTERPRISE-SERVICE-2798',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2798',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2798.'
    },
    2799: {
        'service_name': 'ENTERPRISE-SERVICE-2799',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2799',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2799.'
    },
    2800: {
        'service_name': 'ENTERPRISE-SERVICE-2800',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2800',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2800.'
    },
    2801: {
        'service_name': 'ENTERPRISE-SERVICE-2801',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2801',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2801.'
    },
    2802: {
        'service_name': 'ENTERPRISE-SERVICE-2802',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2802',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2802.'
    },
    2803: {
        'service_name': 'ENTERPRISE-SERVICE-2803',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2803',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2803.'
    },
    2804: {
        'service_name': 'ENTERPRISE-SERVICE-2804',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2804',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2804.'
    },
    2805: {
        'service_name': 'ENTERPRISE-SERVICE-2805',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2805',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2805.'
    },
    2806: {
        'service_name': 'ENTERPRISE-SERVICE-2806',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2806',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2806.'
    },
    2807: {
        'service_name': 'ENTERPRISE-SERVICE-2807',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2807',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2807.'
    },
    2808: {
        'service_name': 'ENTERPRISE-SERVICE-2808',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2808',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2808.'
    },
    2809: {
        'service_name': 'ENTERPRISE-SERVICE-2809',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2809',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2809.'
    },
    2810: {
        'service_name': 'ENTERPRISE-SERVICE-2810',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2810',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2810.'
    },
    2811: {
        'service_name': 'ENTERPRISE-SERVICE-2811',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2811',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2811.'
    },
    2812: {
        'service_name': 'ENTERPRISE-SERVICE-2812',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2812',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2812.'
    },
    2813: {
        'service_name': 'ENTERPRISE-SERVICE-2813',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2813',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2813.'
    },
    2814: {
        'service_name': 'ENTERPRISE-SERVICE-2814',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2814',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2814.'
    },
    2815: {
        'service_name': 'ENTERPRISE-SERVICE-2815',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2815',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2815.'
    },
    2816: {
        'service_name': 'ENTERPRISE-SERVICE-2816',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2816',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2816.'
    },
    2817: {
        'service_name': 'ENTERPRISE-SERVICE-2817',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2817',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2817.'
    },
    2818: {
        'service_name': 'ENTERPRISE-SERVICE-2818',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2818',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2818.'
    },
    2819: {
        'service_name': 'ENTERPRISE-SERVICE-2819',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2819',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2819.'
    },
    2820: {
        'service_name': 'ENTERPRISE-SERVICE-2820',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2820',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2820.'
    },
    2821: {
        'service_name': 'ENTERPRISE-SERVICE-2821',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2821',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2821.'
    },
    2822: {
        'service_name': 'ENTERPRISE-SERVICE-2822',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2822',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2822.'
    },
    2823: {
        'service_name': 'ENTERPRISE-SERVICE-2823',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2823',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2823.'
    },
    2824: {
        'service_name': 'ENTERPRISE-SERVICE-2824',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2824',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2824.'
    },
    2825: {
        'service_name': 'ENTERPRISE-SERVICE-2825',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2825',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2825.'
    },
    2826: {
        'service_name': 'ENTERPRISE-SERVICE-2826',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2826',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2826.'
    },
    2827: {
        'service_name': 'ENTERPRISE-SERVICE-2827',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2827',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2827.'
    },
    2828: {
        'service_name': 'ENTERPRISE-SERVICE-2828',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2828',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2828.'
    },
    2829: {
        'service_name': 'ENTERPRISE-SERVICE-2829',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2829',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2829.'
    },
    2830: {
        'service_name': 'ENTERPRISE-SERVICE-2830',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2830',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2830.'
    },
    2831: {
        'service_name': 'ENTERPRISE-SERVICE-2831',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2831',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2831.'
    },
    2832: {
        'service_name': 'ENTERPRISE-SERVICE-2832',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2832',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2832.'
    },
    2833: {
        'service_name': 'ENTERPRISE-SERVICE-2833',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2833',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2833.'
    },
    2834: {
        'service_name': 'ENTERPRISE-SERVICE-2834',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2834',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2834.'
    },
    2835: {
        'service_name': 'ENTERPRISE-SERVICE-2835',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2835',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2835.'
    },
    2836: {
        'service_name': 'ENTERPRISE-SERVICE-2836',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2836',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2836.'
    },
    2837: {
        'service_name': 'ENTERPRISE-SERVICE-2837',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2837',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2837.'
    },
    2838: {
        'service_name': 'ENTERPRISE-SERVICE-2838',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2838',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2838.'
    },
    2839: {
        'service_name': 'ENTERPRISE-SERVICE-2839',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2839',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2839.'
    },
    2840: {
        'service_name': 'ENTERPRISE-SERVICE-2840',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2840',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2840.'
    },
    2841: {
        'service_name': 'ENTERPRISE-SERVICE-2841',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2841',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2841.'
    },
    2842: {
        'service_name': 'ENTERPRISE-SERVICE-2842',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2842',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2842.'
    },
    2843: {
        'service_name': 'ENTERPRISE-SERVICE-2843',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2843',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2843.'
    },
    2844: {
        'service_name': 'ENTERPRISE-SERVICE-2844',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2844',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2844.'
    },
    2845: {
        'service_name': 'ENTERPRISE-SERVICE-2845',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2845',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2845.'
    },
    2846: {
        'service_name': 'ENTERPRISE-SERVICE-2846',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2846',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2846.'
    },
    2847: {
        'service_name': 'ENTERPRISE-SERVICE-2847',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2847',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2847.'
    },
    2848: {
        'service_name': 'ENTERPRISE-SERVICE-2848',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2848',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2848.'
    },
    2849: {
        'service_name': 'ENTERPRISE-SERVICE-2849',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2849',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2849.'
    },
    2850: {
        'service_name': 'ENTERPRISE-SERVICE-2850',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2850',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2850.'
    },
    2851: {
        'service_name': 'ENTERPRISE-SERVICE-2851',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2851',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2851.'
    },
    2852: {
        'service_name': 'ENTERPRISE-SERVICE-2852',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2852',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2852.'
    },
    2853: {
        'service_name': 'ENTERPRISE-SERVICE-2853',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2853',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2853.'
    },
    2854: {
        'service_name': 'ENTERPRISE-SERVICE-2854',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2854',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2854.'
    },
    2855: {
        'service_name': 'ENTERPRISE-SERVICE-2855',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2855',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2855.'
    },
    2856: {
        'service_name': 'ENTERPRISE-SERVICE-2856',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2856',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2856.'
    },
    2857: {
        'service_name': 'ENTERPRISE-SERVICE-2857',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2857',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2857.'
    },
    2858: {
        'service_name': 'ENTERPRISE-SERVICE-2858',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2858',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2858.'
    },
    2859: {
        'service_name': 'ENTERPRISE-SERVICE-2859',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2859',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2859.'
    },
    2860: {
        'service_name': 'ENTERPRISE-SERVICE-2860',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2860',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2860.'
    },
    2861: {
        'service_name': 'ENTERPRISE-SERVICE-2861',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2861',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2861.'
    },
    2862: {
        'service_name': 'ENTERPRISE-SERVICE-2862',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2862',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2862.'
    },
    2863: {
        'service_name': 'ENTERPRISE-SERVICE-2863',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2863',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2863.'
    },
    2864: {
        'service_name': 'ENTERPRISE-SERVICE-2864',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2864',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2864.'
    },
    2865: {
        'service_name': 'ENTERPRISE-SERVICE-2865',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2865',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2865.'
    },
    2866: {
        'service_name': 'ENTERPRISE-SERVICE-2866',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2866',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2866.'
    },
    2867: {
        'service_name': 'ENTERPRISE-SERVICE-2867',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2867',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2867.'
    },
    2868: {
        'service_name': 'ENTERPRISE-SERVICE-2868',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2868',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2868.'
    },
    2869: {
        'service_name': 'ENTERPRISE-SERVICE-2869',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2869',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2869.'
    },
    2870: {
        'service_name': 'ENTERPRISE-SERVICE-2870',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2870',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2870.'
    },
    2871: {
        'service_name': 'ENTERPRISE-SERVICE-2871',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2871',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2871.'
    },
    2872: {
        'service_name': 'ENTERPRISE-SERVICE-2872',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2872',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2872.'
    },
    2873: {
        'service_name': 'ENTERPRISE-SERVICE-2873',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2873',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2873.'
    },
    2874: {
        'service_name': 'ENTERPRISE-SERVICE-2874',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2874',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2874.'
    },
    2875: {
        'service_name': 'ENTERPRISE-SERVICE-2875',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2875',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2875.'
    },
    2876: {
        'service_name': 'ENTERPRISE-SERVICE-2876',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2876',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2876.'
    },
    2877: {
        'service_name': 'ENTERPRISE-SERVICE-2877',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2877',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2877.'
    },
    2878: {
        'service_name': 'ENTERPRISE-SERVICE-2878',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2878',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2878.'
    },
    2879: {
        'service_name': 'ENTERPRISE-SERVICE-2879',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2879',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2879.'
    },
    2880: {
        'service_name': 'ENTERPRISE-SERVICE-2880',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2880',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2880.'
    },
    2881: {
        'service_name': 'ENTERPRISE-SERVICE-2881',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2881',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2881.'
    },
    2882: {
        'service_name': 'ENTERPRISE-SERVICE-2882',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2882',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2882.'
    },
    2883: {
        'service_name': 'ENTERPRISE-SERVICE-2883',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2883',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2883.'
    },
    2884: {
        'service_name': 'ENTERPRISE-SERVICE-2884',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2884',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2884.'
    },
    2885: {
        'service_name': 'ENTERPRISE-SERVICE-2885',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2885',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2885.'
    },
    2886: {
        'service_name': 'ENTERPRISE-SERVICE-2886',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2886',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2886.'
    },
    2887: {
        'service_name': 'ENTERPRISE-SERVICE-2887',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2887',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2887.'
    },
    2888: {
        'service_name': 'ENTERPRISE-SERVICE-2888',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2888',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2888.'
    },
    2889: {
        'service_name': 'ENTERPRISE-SERVICE-2889',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2889',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2889.'
    },
    2890: {
        'service_name': 'ENTERPRISE-SERVICE-2890',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2890',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2890.'
    },
    2891: {
        'service_name': 'ENTERPRISE-SERVICE-2891',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2891',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2891.'
    },
    2892: {
        'service_name': 'ENTERPRISE-SERVICE-2892',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2892',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2892.'
    },
    2893: {
        'service_name': 'ENTERPRISE-SERVICE-2893',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2893',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2893.'
    },
    2894: {
        'service_name': 'ENTERPRISE-SERVICE-2894',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2894',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2894.'
    },
    2895: {
        'service_name': 'ENTERPRISE-SERVICE-2895',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2895',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2895.'
    },
    2896: {
        'service_name': 'ENTERPRISE-SERVICE-2896',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2896',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2896.'
    },
    2897: {
        'service_name': 'ENTERPRISE-SERVICE-2897',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2897',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2897.'
    },
    2898: {
        'service_name': 'ENTERPRISE-SERVICE-2898',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2898',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2898.'
    },
    2899: {
        'service_name': 'ENTERPRISE-SERVICE-2899',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2899',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2899.'
    },
    2900: {
        'service_name': 'ENTERPRISE-SERVICE-2900',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2900',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2900.'
    },
    2901: {
        'service_name': 'ENTERPRISE-SERVICE-2901',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2901',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2901.'
    },
    2902: {
        'service_name': 'ENTERPRISE-SERVICE-2902',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2902',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2902.'
    },
    2903: {
        'service_name': 'ENTERPRISE-SERVICE-2903',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2903',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2903.'
    },
    2904: {
        'service_name': 'ENTERPRISE-SERVICE-2904',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2904',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2904.'
    },
    2905: {
        'service_name': 'ENTERPRISE-SERVICE-2905',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2905',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2905.'
    },
    2906: {
        'service_name': 'ENTERPRISE-SERVICE-2906',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2906',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2906.'
    },
    2907: {
        'service_name': 'ENTERPRISE-SERVICE-2907',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2907',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2907.'
    },
    2908: {
        'service_name': 'ENTERPRISE-SERVICE-2908',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2908',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2908.'
    },
    2909: {
        'service_name': 'ENTERPRISE-SERVICE-2909',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2909',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2909.'
    },
    2910: {
        'service_name': 'ENTERPRISE-SERVICE-2910',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2910',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2910.'
    },
    2911: {
        'service_name': 'ENTERPRISE-SERVICE-2911',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2911',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2911.'
    },
    2912: {
        'service_name': 'ENTERPRISE-SERVICE-2912',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2912',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2912.'
    },
    2913: {
        'service_name': 'ENTERPRISE-SERVICE-2913',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2913',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2913.'
    },
    2914: {
        'service_name': 'ENTERPRISE-SERVICE-2914',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2914',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2914.'
    },
    2915: {
        'service_name': 'ENTERPRISE-SERVICE-2915',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2915',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2915.'
    },
    2916: {
        'service_name': 'ENTERPRISE-SERVICE-2916',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2916',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2916.'
    },
    2917: {
        'service_name': 'ENTERPRISE-SERVICE-2917',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2917',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2917.'
    },
    2918: {
        'service_name': 'ENTERPRISE-SERVICE-2918',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2918',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2918.'
    },
    2919: {
        'service_name': 'ENTERPRISE-SERVICE-2919',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2919',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2919.'
    },
    2920: {
        'service_name': 'ENTERPRISE-SERVICE-2920',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2920',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2920.'
    },
    2921: {
        'service_name': 'ENTERPRISE-SERVICE-2921',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2921',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2921.'
    },
    2922: {
        'service_name': 'ENTERPRISE-SERVICE-2922',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2922',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2922.'
    },
    2923: {
        'service_name': 'ENTERPRISE-SERVICE-2923',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2923',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2923.'
    },
    2924: {
        'service_name': 'ENTERPRISE-SERVICE-2924',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2924',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2924.'
    },
    2925: {
        'service_name': 'ENTERPRISE-SERVICE-2925',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2925',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2925.'
    },
    2926: {
        'service_name': 'ENTERPRISE-SERVICE-2926',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2926',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2926.'
    },
    2927: {
        'service_name': 'ENTERPRISE-SERVICE-2927',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2927',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2927.'
    },
    2928: {
        'service_name': 'ENTERPRISE-SERVICE-2928',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2928',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2928.'
    },
    2929: {
        'service_name': 'ENTERPRISE-SERVICE-2929',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2929',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2929.'
    },
    2930: {
        'service_name': 'ENTERPRISE-SERVICE-2930',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2930',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2930.'
    },
    2931: {
        'service_name': 'ENTERPRISE-SERVICE-2931',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2931',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2931.'
    },
    2932: {
        'service_name': 'ENTERPRISE-SERVICE-2932',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2932',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2932.'
    },
    2933: {
        'service_name': 'ENTERPRISE-SERVICE-2933',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2933',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2933.'
    },
    2934: {
        'service_name': 'ENTERPRISE-SERVICE-2934',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2934',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2934.'
    },
    2935: {
        'service_name': 'ENTERPRISE-SERVICE-2935',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2935',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2935.'
    },
    2936: {
        'service_name': 'ENTERPRISE-SERVICE-2936',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2936',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2936.'
    },
    2937: {
        'service_name': 'ENTERPRISE-SERVICE-2937',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2937',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2937.'
    },
    2938: {
        'service_name': 'ENTERPRISE-SERVICE-2938',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2938',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2938.'
    },
    2939: {
        'service_name': 'ENTERPRISE-SERVICE-2939',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2939',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2939.'
    },
    2940: {
        'service_name': 'ENTERPRISE-SERVICE-2940',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2940',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2940.'
    },
    2941: {
        'service_name': 'ENTERPRISE-SERVICE-2941',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2941',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2941.'
    },
    2942: {
        'service_name': 'ENTERPRISE-SERVICE-2942',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2942',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2942.'
    },
    2943: {
        'service_name': 'ENTERPRISE-SERVICE-2943',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2943',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2943.'
    },
    2944: {
        'service_name': 'ENTERPRISE-SERVICE-2944',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2944',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2944.'
    },
    2945: {
        'service_name': 'ENTERPRISE-SERVICE-2945',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2945',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2945.'
    },
    2946: {
        'service_name': 'ENTERPRISE-SERVICE-2946',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2946',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2946.'
    },
    2947: {
        'service_name': 'ENTERPRISE-SERVICE-2947',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2947',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2947.'
    },
    2948: {
        'service_name': 'ENTERPRISE-SERVICE-2948',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2948',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2948.'
    },
    2949: {
        'service_name': 'ENTERPRISE-SERVICE-2949',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2949',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2949.'
    },
    2950: {
        'service_name': 'ENTERPRISE-SERVICE-2950',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2950',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2950.'
    },
    2951: {
        'service_name': 'ENTERPRISE-SERVICE-2951',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2951',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2951.'
    },
    2952: {
        'service_name': 'ENTERPRISE-SERVICE-2952',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2952',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2952.'
    },
    2953: {
        'service_name': 'ENTERPRISE-SERVICE-2953',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2953',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2953.'
    },
    2954: {
        'service_name': 'ENTERPRISE-SERVICE-2954',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2954',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2954.'
    },
    2955: {
        'service_name': 'ENTERPRISE-SERVICE-2955',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2955',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2955.'
    },
    2956: {
        'service_name': 'ENTERPRISE-SERVICE-2956',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2956',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2956.'
    },
    2957: {
        'service_name': 'ENTERPRISE-SERVICE-2957',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2957',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2957.'
    },
    2958: {
        'service_name': 'ENTERPRISE-SERVICE-2958',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2958',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2958.'
    },
    2959: {
        'service_name': 'ENTERPRISE-SERVICE-2959',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2959',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2959.'
    },
    2960: {
        'service_name': 'ENTERPRISE-SERVICE-2960',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2960',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2960.'
    },
    2961: {
        'service_name': 'ENTERPRISE-SERVICE-2961',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2961',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2961.'
    },
    2962: {
        'service_name': 'ENTERPRISE-SERVICE-2962',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2962',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2962.'
    },
    2963: {
        'service_name': 'ENTERPRISE-SERVICE-2963',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2963',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2963.'
    },
    2964: {
        'service_name': 'ENTERPRISE-SERVICE-2964',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2964',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2964.'
    },
    2965: {
        'service_name': 'ENTERPRISE-SERVICE-2965',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2965',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2965.'
    },
    2966: {
        'service_name': 'ENTERPRISE-SERVICE-2966',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2966',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2966.'
    },
    2967: {
        'service_name': 'ENTERPRISE-SERVICE-2967',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2967',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2967.'
    },
    2968: {
        'service_name': 'ENTERPRISE-SERVICE-2968',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2968',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2968.'
    },
    2969: {
        'service_name': 'ENTERPRISE-SERVICE-2969',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2969',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2969.'
    },
    2970: {
        'service_name': 'ENTERPRISE-SERVICE-2970',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2970',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2970.'
    },
    2971: {
        'service_name': 'ENTERPRISE-SERVICE-2971',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2971',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2971.'
    },
    2972: {
        'service_name': 'ENTERPRISE-SERVICE-2972',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2972',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2972.'
    },
    2973: {
        'service_name': 'ENTERPRISE-SERVICE-2973',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2973',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2973.'
    },
    2974: {
        'service_name': 'ENTERPRISE-SERVICE-2974',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2974',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2974.'
    },
    2975: {
        'service_name': 'ENTERPRISE-SERVICE-2975',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2975',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2975.'
    },
    2976: {
        'service_name': 'ENTERPRISE-SERVICE-2976',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2976',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2976.'
    },
    2977: {
        'service_name': 'ENTERPRISE-SERVICE-2977',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2977',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2977.'
    },
    2978: {
        'service_name': 'ENTERPRISE-SERVICE-2978',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2978',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2978.'
    },
    2979: {
        'service_name': 'ENTERPRISE-SERVICE-2979',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2979',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2979.'
    },
    2980: {
        'service_name': 'ENTERPRISE-SERVICE-2980',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2980',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2980.'
    },
    2981: {
        'service_name': 'ENTERPRISE-SERVICE-2981',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2981',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2981.'
    },
    2982: {
        'service_name': 'ENTERPRISE-SERVICE-2982',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2982',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2982.'
    },
    2983: {
        'service_name': 'ENTERPRISE-SERVICE-2983',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2983',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2983.'
    },
    2984: {
        'service_name': 'ENTERPRISE-SERVICE-2984',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2984',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2984.'
    },
    2985: {
        'service_name': 'ENTERPRISE-SERVICE-2985',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2985',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2985.'
    },
    2986: {
        'service_name': 'ENTERPRISE-SERVICE-2986',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2986',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2986.'
    },
    2987: {
        'service_name': 'ENTERPRISE-SERVICE-2987',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2987',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2987.'
    },
    2988: {
        'service_name': 'ENTERPRISE-SERVICE-2988',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2988',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2988.'
    },
    2989: {
        'service_name': 'ENTERPRISE-SERVICE-2989',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2989',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2989.'
    },
    2990: {
        'service_name': 'ENTERPRISE-SERVICE-2990',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2990',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2990.'
    },
    2991: {
        'service_name': 'ENTERPRISE-SERVICE-2991',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2991',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2991.'
    },
    2992: {
        'service_name': 'ENTERPRISE-SERVICE-2992',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2992',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2992.'
    },
    2993: {
        'service_name': 'ENTERPRISE-SERVICE-2993',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2993',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2993.'
    },
    2994: {
        'service_name': 'ENTERPRISE-SERVICE-2994',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2994',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2994.'
    },
    2995: {
        'service_name': 'ENTERPRISE-SERVICE-2995',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2995',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2995.'
    },
    2996: {
        'service_name': 'ENTERPRISE-SERVICE-2996',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2996',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2996.'
    },
    2997: {
        'service_name': 'ENTERPRISE-SERVICE-2997',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2997',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2997.'
    },
    2998: {
        'service_name': 'ENTERPRISE-SERVICE-2998',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2998',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2998.'
    },
    2999: {
        'service_name': 'ENTERPRISE-SERVICE-2999',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 2999',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 2999.'
    },
    3000: {
        'service_name': 'ENTERPRISE-SERVICE-3000',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3000',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3000.'
    },
    3001: {
        'service_name': 'ENTERPRISE-SERVICE-3001',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3001',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3001.'
    },
    3002: {
        'service_name': 'ENTERPRISE-SERVICE-3002',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3002',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3002.'
    },
    3003: {
        'service_name': 'ENTERPRISE-SERVICE-3003',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3003',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3003.'
    },
    3004: {
        'service_name': 'ENTERPRISE-SERVICE-3004',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3004',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3004.'
    },
    3005: {
        'service_name': 'ENTERPRISE-SERVICE-3005',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3005',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3005.'
    },
    3006: {
        'service_name': 'ENTERPRISE-SERVICE-3006',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3006',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3006.'
    },
    3007: {
        'service_name': 'ENTERPRISE-SERVICE-3007',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3007',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3007.'
    },
    3008: {
        'service_name': 'ENTERPRISE-SERVICE-3008',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3008',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3008.'
    },
    3009: {
        'service_name': 'ENTERPRISE-SERVICE-3009',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3009',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3009.'
    },
    3010: {
        'service_name': 'ENTERPRISE-SERVICE-3010',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3010',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3010.'
    },
    3011: {
        'service_name': 'ENTERPRISE-SERVICE-3011',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3011',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3011.'
    },
    3012: {
        'service_name': 'ENTERPRISE-SERVICE-3012',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3012',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3012.'
    },
    3013: {
        'service_name': 'ENTERPRISE-SERVICE-3013',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3013',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3013.'
    },
    3014: {
        'service_name': 'ENTERPRISE-SERVICE-3014',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3014',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3014.'
    },
    3015: {
        'service_name': 'ENTERPRISE-SERVICE-3015',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3015',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3015.'
    },
    3016: {
        'service_name': 'ENTERPRISE-SERVICE-3016',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3016',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3016.'
    },
    3017: {
        'service_name': 'ENTERPRISE-SERVICE-3017',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3017',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3017.'
    },
    3018: {
        'service_name': 'ENTERPRISE-SERVICE-3018',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3018',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3018.'
    },
    3019: {
        'service_name': 'ENTERPRISE-SERVICE-3019',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3019',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3019.'
    },
    3020: {
        'service_name': 'ENTERPRISE-SERVICE-3020',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3020',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3020.'
    },
    3021: {
        'service_name': 'ENTERPRISE-SERVICE-3021',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3021',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3021.'
    },
    3022: {
        'service_name': 'ENTERPRISE-SERVICE-3022',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3022',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3022.'
    },
    3023: {
        'service_name': 'ENTERPRISE-SERVICE-3023',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3023',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3023.'
    },
    3024: {
        'service_name': 'ENTERPRISE-SERVICE-3024',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3024',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3024.'
    },
    3025: {
        'service_name': 'ENTERPRISE-SERVICE-3025',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3025',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3025.'
    },
    3026: {
        'service_name': 'ENTERPRISE-SERVICE-3026',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3026',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3026.'
    },
    3027: {
        'service_name': 'ENTERPRISE-SERVICE-3027',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3027',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3027.'
    },
    3028: {
        'service_name': 'ENTERPRISE-SERVICE-3028',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3028',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3028.'
    },
    3029: {
        'service_name': 'ENTERPRISE-SERVICE-3029',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3029',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3029.'
    },
    3030: {
        'service_name': 'ENTERPRISE-SERVICE-3030',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3030',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3030.'
    },
    3031: {
        'service_name': 'ENTERPRISE-SERVICE-3031',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3031',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3031.'
    },
    3032: {
        'service_name': 'ENTERPRISE-SERVICE-3032',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3032',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3032.'
    },
    3033: {
        'service_name': 'ENTERPRISE-SERVICE-3033',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3033',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3033.'
    },
    3034: {
        'service_name': 'ENTERPRISE-SERVICE-3034',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3034',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3034.'
    },
    3035: {
        'service_name': 'ENTERPRISE-SERVICE-3035',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3035',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3035.'
    },
    3036: {
        'service_name': 'ENTERPRISE-SERVICE-3036',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3036',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3036.'
    },
    3037: {
        'service_name': 'ENTERPRISE-SERVICE-3037',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3037',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3037.'
    },
    3038: {
        'service_name': 'ENTERPRISE-SERVICE-3038',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3038',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3038.'
    },
    3039: {
        'service_name': 'ENTERPRISE-SERVICE-3039',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3039',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3039.'
    },
    3040: {
        'service_name': 'ENTERPRISE-SERVICE-3040',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3040',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3040.'
    },
    3041: {
        'service_name': 'ENTERPRISE-SERVICE-3041',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3041',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3041.'
    },
    3042: {
        'service_name': 'ENTERPRISE-SERVICE-3042',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3042',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3042.'
    },
    3043: {
        'service_name': 'ENTERPRISE-SERVICE-3043',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3043',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3043.'
    },
    3044: {
        'service_name': 'ENTERPRISE-SERVICE-3044',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3044',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3044.'
    },
    3045: {
        'service_name': 'ENTERPRISE-SERVICE-3045',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3045',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3045.'
    },
    3046: {
        'service_name': 'ENTERPRISE-SERVICE-3046',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3046',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3046.'
    },
    3047: {
        'service_name': 'ENTERPRISE-SERVICE-3047',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3047',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3047.'
    },
    3048: {
        'service_name': 'ENTERPRISE-SERVICE-3048',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3048',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3048.'
    },
    3049: {
        'service_name': 'ENTERPRISE-SERVICE-3049',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3049',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3049.'
    },
    3050: {
        'service_name': 'ENTERPRISE-SERVICE-3050',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3050',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3050.'
    },
    3051: {
        'service_name': 'ENTERPRISE-SERVICE-3051',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3051',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3051.'
    },
    3052: {
        'service_name': 'ENTERPRISE-SERVICE-3052',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3052',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3052.'
    },
    3053: {
        'service_name': 'ENTERPRISE-SERVICE-3053',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3053',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3053.'
    },
    3054: {
        'service_name': 'ENTERPRISE-SERVICE-3054',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3054',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3054.'
    },
    3055: {
        'service_name': 'ENTERPRISE-SERVICE-3055',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3055',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3055.'
    },
    3056: {
        'service_name': 'ENTERPRISE-SERVICE-3056',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3056',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3056.'
    },
    3057: {
        'service_name': 'ENTERPRISE-SERVICE-3057',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3057',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3057.'
    },
    3058: {
        'service_name': 'ENTERPRISE-SERVICE-3058',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3058',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3058.'
    },
    3059: {
        'service_name': 'ENTERPRISE-SERVICE-3059',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3059',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3059.'
    },
    3060: {
        'service_name': 'ENTERPRISE-SERVICE-3060',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3060',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3060.'
    },
    3061: {
        'service_name': 'ENTERPRISE-SERVICE-3061',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3061',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3061.'
    },
    3062: {
        'service_name': 'ENTERPRISE-SERVICE-3062',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3062',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3062.'
    },
    3063: {
        'service_name': 'ENTERPRISE-SERVICE-3063',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3063',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3063.'
    },
    3064: {
        'service_name': 'ENTERPRISE-SERVICE-3064',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3064',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3064.'
    },
    3065: {
        'service_name': 'ENTERPRISE-SERVICE-3065',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3065',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3065.'
    },
    3066: {
        'service_name': 'ENTERPRISE-SERVICE-3066',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3066',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3066.'
    },
    3067: {
        'service_name': 'ENTERPRISE-SERVICE-3067',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3067',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3067.'
    },
    3068: {
        'service_name': 'ENTERPRISE-SERVICE-3068',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3068',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3068.'
    },
    3069: {
        'service_name': 'ENTERPRISE-SERVICE-3069',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3069',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3069.'
    },
    3070: {
        'service_name': 'ENTERPRISE-SERVICE-3070',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3070',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3070.'
    },
    3071: {
        'service_name': 'ENTERPRISE-SERVICE-3071',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3071',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3071.'
    },
    3072: {
        'service_name': 'ENTERPRISE-SERVICE-3072',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3072',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3072.'
    },
    3073: {
        'service_name': 'ENTERPRISE-SERVICE-3073',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3073',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3073.'
    },
    3074: {
        'service_name': 'ENTERPRISE-SERVICE-3074',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3074',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3074.'
    },
    3075: {
        'service_name': 'ENTERPRISE-SERVICE-3075',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3075',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3075.'
    },
    3076: {
        'service_name': 'ENTERPRISE-SERVICE-3076',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3076',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3076.'
    },
    3077: {
        'service_name': 'ENTERPRISE-SERVICE-3077',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3077',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3077.'
    },
    3078: {
        'service_name': 'ENTERPRISE-SERVICE-3078',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3078',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3078.'
    },
    3079: {
        'service_name': 'ENTERPRISE-SERVICE-3079',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3079',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3079.'
    },
    3080: {
        'service_name': 'ENTERPRISE-SERVICE-3080',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3080',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3080.'
    },
    3081: {
        'service_name': 'ENTERPRISE-SERVICE-3081',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3081',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3081.'
    },
    3082: {
        'service_name': 'ENTERPRISE-SERVICE-3082',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3082',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3082.'
    },
    3083: {
        'service_name': 'ENTERPRISE-SERVICE-3083',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3083',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3083.'
    },
    3084: {
        'service_name': 'ENTERPRISE-SERVICE-3084',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3084',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3084.'
    },
    3085: {
        'service_name': 'ENTERPRISE-SERVICE-3085',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3085',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3085.'
    },
    3086: {
        'service_name': 'ENTERPRISE-SERVICE-3086',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3086',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3086.'
    },
    3087: {
        'service_name': 'ENTERPRISE-SERVICE-3087',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3087',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3087.'
    },
    3088: {
        'service_name': 'ENTERPRISE-SERVICE-3088',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3088',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3088.'
    },
    3089: {
        'service_name': 'ENTERPRISE-SERVICE-3089',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3089',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3089.'
    },
    3090: {
        'service_name': 'ENTERPRISE-SERVICE-3090',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3090',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3090.'
    },
    3091: {
        'service_name': 'ENTERPRISE-SERVICE-3091',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3091',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3091.'
    },
    3092: {
        'service_name': 'ENTERPRISE-SERVICE-3092',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3092',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3092.'
    },
    3093: {
        'service_name': 'ENTERPRISE-SERVICE-3093',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3093',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3093.'
    },
    3094: {
        'service_name': 'ENTERPRISE-SERVICE-3094',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3094',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3094.'
    },
    3095: {
        'service_name': 'ENTERPRISE-SERVICE-3095',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3095',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3095.'
    },
    3096: {
        'service_name': 'ENTERPRISE-SERVICE-3096',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3096',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3096.'
    },
    3097: {
        'service_name': 'ENTERPRISE-SERVICE-3097',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3097',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3097.'
    },
    3098: {
        'service_name': 'ENTERPRISE-SERVICE-3098',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3098',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3098.'
    },
    3099: {
        'service_name': 'ENTERPRISE-SERVICE-3099',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3099',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3099.'
    },
    3100: {
        'service_name': 'ENTERPRISE-SERVICE-3100',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3100',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3100.'
    },
    3101: {
        'service_name': 'ENTERPRISE-SERVICE-3101',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3101',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3101.'
    },
    3102: {
        'service_name': 'ENTERPRISE-SERVICE-3102',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3102',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3102.'
    },
    3103: {
        'service_name': 'ENTERPRISE-SERVICE-3103',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3103',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3103.'
    },
    3104: {
        'service_name': 'ENTERPRISE-SERVICE-3104',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3104',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3104.'
    },
    3105: {
        'service_name': 'ENTERPRISE-SERVICE-3105',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3105',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3105.'
    },
    3106: {
        'service_name': 'ENTERPRISE-SERVICE-3106',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3106',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3106.'
    },
    3107: {
        'service_name': 'ENTERPRISE-SERVICE-3107',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3107',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3107.'
    },
    3108: {
        'service_name': 'ENTERPRISE-SERVICE-3108',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3108',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3108.'
    },
    3109: {
        'service_name': 'ENTERPRISE-SERVICE-3109',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3109',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3109.'
    },
    3110: {
        'service_name': 'ENTERPRISE-SERVICE-3110',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3110',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3110.'
    },
    3111: {
        'service_name': 'ENTERPRISE-SERVICE-3111',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3111',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3111.'
    },
    3112: {
        'service_name': 'ENTERPRISE-SERVICE-3112',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3112',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3112.'
    },
    3113: {
        'service_name': 'ENTERPRISE-SERVICE-3113',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3113',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3113.'
    },
    3114: {
        'service_name': 'ENTERPRISE-SERVICE-3114',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3114',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3114.'
    },
    3115: {
        'service_name': 'ENTERPRISE-SERVICE-3115',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3115',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3115.'
    },
    3116: {
        'service_name': 'ENTERPRISE-SERVICE-3116',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3116',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3116.'
    },
    3117: {
        'service_name': 'ENTERPRISE-SERVICE-3117',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3117',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3117.'
    },
    3118: {
        'service_name': 'ENTERPRISE-SERVICE-3118',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3118',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3118.'
    },
    3119: {
        'service_name': 'ENTERPRISE-SERVICE-3119',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3119',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3119.'
    },
    3120: {
        'service_name': 'ENTERPRISE-SERVICE-3120',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3120',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3120.'
    },
    3121: {
        'service_name': 'ENTERPRISE-SERVICE-3121',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3121',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3121.'
    },
    3122: {
        'service_name': 'ENTERPRISE-SERVICE-3122',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3122',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3122.'
    },
    3123: {
        'service_name': 'ENTERPRISE-SERVICE-3123',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3123',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3123.'
    },
    3124: {
        'service_name': 'ENTERPRISE-SERVICE-3124',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3124',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3124.'
    },
    3125: {
        'service_name': 'ENTERPRISE-SERVICE-3125',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3125',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3125.'
    },
    3126: {
        'service_name': 'ENTERPRISE-SERVICE-3126',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3126',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3126.'
    },
    3127: {
        'service_name': 'ENTERPRISE-SERVICE-3127',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3127',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3127.'
    },
    3128: {
        'service_name': 'ENTERPRISE-SERVICE-3128',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3128',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3128.'
    },
    3129: {
        'service_name': 'ENTERPRISE-SERVICE-3129',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3129',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3129.'
    },
    3130: {
        'service_name': 'ENTERPRISE-SERVICE-3130',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3130',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3130.'
    },
    3131: {
        'service_name': 'ENTERPRISE-SERVICE-3131',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3131',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3131.'
    },
    3132: {
        'service_name': 'ENTERPRISE-SERVICE-3132',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3132',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3132.'
    },
    3133: {
        'service_name': 'ENTERPRISE-SERVICE-3133',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3133',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3133.'
    },
    3134: {
        'service_name': 'ENTERPRISE-SERVICE-3134',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3134',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3134.'
    },
    3135: {
        'service_name': 'ENTERPRISE-SERVICE-3135',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3135',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3135.'
    },
    3136: {
        'service_name': 'ENTERPRISE-SERVICE-3136',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3136',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3136.'
    },
    3137: {
        'service_name': 'ENTERPRISE-SERVICE-3137',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3137',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3137.'
    },
    3138: {
        'service_name': 'ENTERPRISE-SERVICE-3138',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3138',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3138.'
    },
    3139: {
        'service_name': 'ENTERPRISE-SERVICE-3139',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3139',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3139.'
    },
    3140: {
        'service_name': 'ENTERPRISE-SERVICE-3140',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3140',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3140.'
    },
    3141: {
        'service_name': 'ENTERPRISE-SERVICE-3141',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3141',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3141.'
    },
    3142: {
        'service_name': 'ENTERPRISE-SERVICE-3142',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3142',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3142.'
    },
    3143: {
        'service_name': 'ENTERPRISE-SERVICE-3143',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3143',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3143.'
    },
    3144: {
        'service_name': 'ENTERPRISE-SERVICE-3144',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3144',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3144.'
    },
    3145: {
        'service_name': 'ENTERPRISE-SERVICE-3145',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3145',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3145.'
    },
    3146: {
        'service_name': 'ENTERPRISE-SERVICE-3146',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3146',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3146.'
    },
    3147: {
        'service_name': 'ENTERPRISE-SERVICE-3147',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3147',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3147.'
    },
    3148: {
        'service_name': 'ENTERPRISE-SERVICE-3148',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3148',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3148.'
    },
    3149: {
        'service_name': 'ENTERPRISE-SERVICE-3149',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3149',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3149.'
    },
    3150: {
        'service_name': 'ENTERPRISE-SERVICE-3150',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3150',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3150.'
    },
    3151: {
        'service_name': 'ENTERPRISE-SERVICE-3151',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3151',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3151.'
    },
    3152: {
        'service_name': 'ENTERPRISE-SERVICE-3152',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3152',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3152.'
    },
    3153: {
        'service_name': 'ENTERPRISE-SERVICE-3153',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3153',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3153.'
    },
    3154: {
        'service_name': 'ENTERPRISE-SERVICE-3154',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3154',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3154.'
    },
    3155: {
        'service_name': 'ENTERPRISE-SERVICE-3155',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3155',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3155.'
    },
    3156: {
        'service_name': 'ENTERPRISE-SERVICE-3156',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3156',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3156.'
    },
    3157: {
        'service_name': 'ENTERPRISE-SERVICE-3157',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3157',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3157.'
    },
    3158: {
        'service_name': 'ENTERPRISE-SERVICE-3158',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3158',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3158.'
    },
    3159: {
        'service_name': 'ENTERPRISE-SERVICE-3159',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3159',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3159.'
    },
    3160: {
        'service_name': 'ENTERPRISE-SERVICE-3160',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3160',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3160.'
    },
    3161: {
        'service_name': 'ENTERPRISE-SERVICE-3161',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3161',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3161.'
    },
    3162: {
        'service_name': 'ENTERPRISE-SERVICE-3162',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3162',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3162.'
    },
    3163: {
        'service_name': 'ENTERPRISE-SERVICE-3163',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3163',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3163.'
    },
    3164: {
        'service_name': 'ENTERPRISE-SERVICE-3164',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3164',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3164.'
    },
    3165: {
        'service_name': 'ENTERPRISE-SERVICE-3165',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3165',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3165.'
    },
    3166: {
        'service_name': 'ENTERPRISE-SERVICE-3166',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3166',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3166.'
    },
    3167: {
        'service_name': 'ENTERPRISE-SERVICE-3167',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3167',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3167.'
    },
    3168: {
        'service_name': 'ENTERPRISE-SERVICE-3168',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3168',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3168.'
    },
    3169: {
        'service_name': 'ENTERPRISE-SERVICE-3169',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3169',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3169.'
    },
    3170: {
        'service_name': 'ENTERPRISE-SERVICE-3170',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3170',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3170.'
    },
    3171: {
        'service_name': 'ENTERPRISE-SERVICE-3171',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3171',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3171.'
    },
    3172: {
        'service_name': 'ENTERPRISE-SERVICE-3172',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3172',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3172.'
    },
    3173: {
        'service_name': 'ENTERPRISE-SERVICE-3173',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3173',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3173.'
    },
    3174: {
        'service_name': 'ENTERPRISE-SERVICE-3174',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3174',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3174.'
    },
    3175: {
        'service_name': 'ENTERPRISE-SERVICE-3175',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3175',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3175.'
    },
    3176: {
        'service_name': 'ENTERPRISE-SERVICE-3176',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3176',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3176.'
    },
    3177: {
        'service_name': 'ENTERPRISE-SERVICE-3177',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3177',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3177.'
    },
    3178: {
        'service_name': 'ENTERPRISE-SERVICE-3178',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3178',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3178.'
    },
    3179: {
        'service_name': 'ENTERPRISE-SERVICE-3179',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3179',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3179.'
    },
    3180: {
        'service_name': 'ENTERPRISE-SERVICE-3180',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3180',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3180.'
    },
    3181: {
        'service_name': 'ENTERPRISE-SERVICE-3181',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3181',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3181.'
    },
    3182: {
        'service_name': 'ENTERPRISE-SERVICE-3182',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3182',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3182.'
    },
    3183: {
        'service_name': 'ENTERPRISE-SERVICE-3183',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3183',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3183.'
    },
    3184: {
        'service_name': 'ENTERPRISE-SERVICE-3184',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3184',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3184.'
    },
    3185: {
        'service_name': 'ENTERPRISE-SERVICE-3185',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3185',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3185.'
    },
    3186: {
        'service_name': 'ENTERPRISE-SERVICE-3186',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3186',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3186.'
    },
    3187: {
        'service_name': 'ENTERPRISE-SERVICE-3187',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3187',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3187.'
    },
    3188: {
        'service_name': 'ENTERPRISE-SERVICE-3188',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3188',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3188.'
    },
    3189: {
        'service_name': 'ENTERPRISE-SERVICE-3189',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3189',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3189.'
    },
    3190: {
        'service_name': 'ENTERPRISE-SERVICE-3190',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3190',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3190.'
    },
    3191: {
        'service_name': 'ENTERPRISE-SERVICE-3191',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3191',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3191.'
    },
    3192: {
        'service_name': 'ENTERPRISE-SERVICE-3192',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3192',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3192.'
    },
    3193: {
        'service_name': 'ENTERPRISE-SERVICE-3193',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3193',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3193.'
    },
    3194: {
        'service_name': 'ENTERPRISE-SERVICE-3194',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3194',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3194.'
    },
    3195: {
        'service_name': 'ENTERPRISE-SERVICE-3195',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3195',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3195.'
    },
    3196: {
        'service_name': 'ENTERPRISE-SERVICE-3196',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3196',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3196.'
    },
    3197: {
        'service_name': 'ENTERPRISE-SERVICE-3197',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3197',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3197.'
    },
    3198: {
        'service_name': 'ENTERPRISE-SERVICE-3198',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3198',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3198.'
    },
    3199: {
        'service_name': 'ENTERPRISE-SERVICE-3199',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3199',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3199.'
    },
    3200: {
        'service_name': 'ENTERPRISE-SERVICE-3200',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3200',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3200.'
    },
    3201: {
        'service_name': 'ENTERPRISE-SERVICE-3201',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3201',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3201.'
    },
    3202: {
        'service_name': 'ENTERPRISE-SERVICE-3202',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3202',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3202.'
    },
    3203: {
        'service_name': 'ENTERPRISE-SERVICE-3203',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3203',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3203.'
    },
    3204: {
        'service_name': 'ENTERPRISE-SERVICE-3204',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3204',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3204.'
    },
    3205: {
        'service_name': 'ENTERPRISE-SERVICE-3205',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3205',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3205.'
    },
    3206: {
        'service_name': 'ENTERPRISE-SERVICE-3206',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3206',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3206.'
    },
    3207: {
        'service_name': 'ENTERPRISE-SERVICE-3207',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3207',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3207.'
    },
    3208: {
        'service_name': 'ENTERPRISE-SERVICE-3208',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3208',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3208.'
    },
    3209: {
        'service_name': 'ENTERPRISE-SERVICE-3209',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3209',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3209.'
    },
    3210: {
        'service_name': 'ENTERPRISE-SERVICE-3210',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3210',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3210.'
    },
    3211: {
        'service_name': 'ENTERPRISE-SERVICE-3211',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3211',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3211.'
    },
    3212: {
        'service_name': 'ENTERPRISE-SERVICE-3212',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3212',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3212.'
    },
    3213: {
        'service_name': 'ENTERPRISE-SERVICE-3213',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3213',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3213.'
    },
    3214: {
        'service_name': 'ENTERPRISE-SERVICE-3214',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3214',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3214.'
    },
    3215: {
        'service_name': 'ENTERPRISE-SERVICE-3215',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3215',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3215.'
    },
    3216: {
        'service_name': 'ENTERPRISE-SERVICE-3216',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3216',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3216.'
    },
    3217: {
        'service_name': 'ENTERPRISE-SERVICE-3217',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3217',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3217.'
    },
    3218: {
        'service_name': 'ENTERPRISE-SERVICE-3218',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3218',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3218.'
    },
    3219: {
        'service_name': 'ENTERPRISE-SERVICE-3219',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3219',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3219.'
    },
    3220: {
        'service_name': 'ENTERPRISE-SERVICE-3220',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3220',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3220.'
    },
    3221: {
        'service_name': 'ENTERPRISE-SERVICE-3221',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3221',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3221.'
    },
    3222: {
        'service_name': 'ENTERPRISE-SERVICE-3222',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3222',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3222.'
    },
    3223: {
        'service_name': 'ENTERPRISE-SERVICE-3223',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3223',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3223.'
    },
    3224: {
        'service_name': 'ENTERPRISE-SERVICE-3224',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3224',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3224.'
    },
    3225: {
        'service_name': 'ENTERPRISE-SERVICE-3225',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3225',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3225.'
    },
    3226: {
        'service_name': 'ENTERPRISE-SERVICE-3226',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3226',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3226.'
    },
    3227: {
        'service_name': 'ENTERPRISE-SERVICE-3227',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3227',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3227.'
    },
    3228: {
        'service_name': 'ENTERPRISE-SERVICE-3228',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3228',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3228.'
    },
    3229: {
        'service_name': 'ENTERPRISE-SERVICE-3229',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3229',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3229.'
    },
    3230: {
        'service_name': 'ENTERPRISE-SERVICE-3230',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3230',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3230.'
    },
    3231: {
        'service_name': 'ENTERPRISE-SERVICE-3231',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3231',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3231.'
    },
    3232: {
        'service_name': 'ENTERPRISE-SERVICE-3232',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3232',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3232.'
    },
    3233: {
        'service_name': 'ENTERPRISE-SERVICE-3233',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3233',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3233.'
    },
    3234: {
        'service_name': 'ENTERPRISE-SERVICE-3234',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3234',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3234.'
    },
    3235: {
        'service_name': 'ENTERPRISE-SERVICE-3235',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3235',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3235.'
    },
    3236: {
        'service_name': 'ENTERPRISE-SERVICE-3236',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3236',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3236.'
    },
    3237: {
        'service_name': 'ENTERPRISE-SERVICE-3237',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3237',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3237.'
    },
    3238: {
        'service_name': 'ENTERPRISE-SERVICE-3238',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3238',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3238.'
    },
    3239: {
        'service_name': 'ENTERPRISE-SERVICE-3239',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3239',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3239.'
    },
    3240: {
        'service_name': 'ENTERPRISE-SERVICE-3240',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3240',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3240.'
    },
    3241: {
        'service_name': 'ENTERPRISE-SERVICE-3241',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3241',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3241.'
    },
    3242: {
        'service_name': 'ENTERPRISE-SERVICE-3242',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3242',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3242.'
    },
    3243: {
        'service_name': 'ENTERPRISE-SERVICE-3243',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3243',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3243.'
    },
    3244: {
        'service_name': 'ENTERPRISE-SERVICE-3244',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3244',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3244.'
    },
    3245: {
        'service_name': 'ENTERPRISE-SERVICE-3245',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3245',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3245.'
    },
    3246: {
        'service_name': 'ENTERPRISE-SERVICE-3246',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3246',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3246.'
    },
    3247: {
        'service_name': 'ENTERPRISE-SERVICE-3247',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3247',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3247.'
    },
    3248: {
        'service_name': 'ENTERPRISE-SERVICE-3248',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3248',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3248.'
    },
    3249: {
        'service_name': 'ENTERPRISE-SERVICE-3249',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3249',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3249.'
    },
    3250: {
        'service_name': 'ENTERPRISE-SERVICE-3250',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3250',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3250.'
    },
    3251: {
        'service_name': 'ENTERPRISE-SERVICE-3251',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3251',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3251.'
    },
    3252: {
        'service_name': 'ENTERPRISE-SERVICE-3252',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3252',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3252.'
    },
    3253: {
        'service_name': 'ENTERPRISE-SERVICE-3253',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3253',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3253.'
    },
    3254: {
        'service_name': 'ENTERPRISE-SERVICE-3254',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3254',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3254.'
    },
    3255: {
        'service_name': 'ENTERPRISE-SERVICE-3255',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3255',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3255.'
    },
    3256: {
        'service_name': 'ENTERPRISE-SERVICE-3256',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3256',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3256.'
    },
    3257: {
        'service_name': 'ENTERPRISE-SERVICE-3257',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3257',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3257.'
    },
    3258: {
        'service_name': 'ENTERPRISE-SERVICE-3258',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3258',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3258.'
    },
    3259: {
        'service_name': 'ENTERPRISE-SERVICE-3259',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3259',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3259.'
    },
    3260: {
        'service_name': 'ENTERPRISE-SERVICE-3260',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3260',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3260.'
    },
    3261: {
        'service_name': 'ENTERPRISE-SERVICE-3261',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3261',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3261.'
    },
    3262: {
        'service_name': 'ENTERPRISE-SERVICE-3262',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3262',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3262.'
    },
    3263: {
        'service_name': 'ENTERPRISE-SERVICE-3263',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3263',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3263.'
    },
    3264: {
        'service_name': 'ENTERPRISE-SERVICE-3264',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3264',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3264.'
    },
    3265: {
        'service_name': 'ENTERPRISE-SERVICE-3265',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3265',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3265.'
    },
    3266: {
        'service_name': 'ENTERPRISE-SERVICE-3266',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3266',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3266.'
    },
    3267: {
        'service_name': 'ENTERPRISE-SERVICE-3267',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3267',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3267.'
    },
    3268: {
        'service_name': 'ENTERPRISE-SERVICE-3268',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3268',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3268.'
    },
    3269: {
        'service_name': 'ENTERPRISE-SERVICE-3269',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3269',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3269.'
    },
    3270: {
        'service_name': 'ENTERPRISE-SERVICE-3270',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3270',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3270.'
    },
    3271: {
        'service_name': 'ENTERPRISE-SERVICE-3271',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3271',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3271.'
    },
    3272: {
        'service_name': 'ENTERPRISE-SERVICE-3272',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3272',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3272.'
    },
    3273: {
        'service_name': 'ENTERPRISE-SERVICE-3273',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3273',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3273.'
    },
    3274: {
        'service_name': 'ENTERPRISE-SERVICE-3274',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3274',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3274.'
    },
    3275: {
        'service_name': 'ENTERPRISE-SERVICE-3275',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3275',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3275.'
    },
    3276: {
        'service_name': 'ENTERPRISE-SERVICE-3276',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3276',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3276.'
    },
    3277: {
        'service_name': 'ENTERPRISE-SERVICE-3277',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3277',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3277.'
    },
    3278: {
        'service_name': 'ENTERPRISE-SERVICE-3278',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3278',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3278.'
    },
    3279: {
        'service_name': 'ENTERPRISE-SERVICE-3279',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3279',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3279.'
    },
    3280: {
        'service_name': 'ENTERPRISE-SERVICE-3280',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3280',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3280.'
    },
    3281: {
        'service_name': 'ENTERPRISE-SERVICE-3281',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3281',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3281.'
    },
    3282: {
        'service_name': 'ENTERPRISE-SERVICE-3282',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3282',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3282.'
    },
    3283: {
        'service_name': 'ENTERPRISE-SERVICE-3283',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3283',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3283.'
    },
    3284: {
        'service_name': 'ENTERPRISE-SERVICE-3284',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3284',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3284.'
    },
    3285: {
        'service_name': 'ENTERPRISE-SERVICE-3285',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3285',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3285.'
    },
    3286: {
        'service_name': 'ENTERPRISE-SERVICE-3286',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3286',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3286.'
    },
    3287: {
        'service_name': 'ENTERPRISE-SERVICE-3287',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3287',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3287.'
    },
    3288: {
        'service_name': 'ENTERPRISE-SERVICE-3288',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3288',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3288.'
    },
    3289: {
        'service_name': 'ENTERPRISE-SERVICE-3289',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3289',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3289.'
    },
    3290: {
        'service_name': 'ENTERPRISE-SERVICE-3290',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3290',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3290.'
    },
    3291: {
        'service_name': 'ENTERPRISE-SERVICE-3291',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3291',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3291.'
    },
    3292: {
        'service_name': 'ENTERPRISE-SERVICE-3292',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3292',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3292.'
    },
    3293: {
        'service_name': 'ENTERPRISE-SERVICE-3293',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3293',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3293.'
    },
    3294: {
        'service_name': 'ENTERPRISE-SERVICE-3294',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3294',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3294.'
    },
    3295: {
        'service_name': 'ENTERPRISE-SERVICE-3295',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3295',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3295.'
    },
    3296: {
        'service_name': 'ENTERPRISE-SERVICE-3296',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3296',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3296.'
    },
    3297: {
        'service_name': 'ENTERPRISE-SERVICE-3297',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3297',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3297.'
    },
    3298: {
        'service_name': 'ENTERPRISE-SERVICE-3298',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3298',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3298.'
    },
    3299: {
        'service_name': 'ENTERPRISE-SERVICE-3299',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3299',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3299.'
    },
    3300: {
        'service_name': 'ENTERPRISE-SERVICE-3300',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3300',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3300.'
    },
    3301: {
        'service_name': 'ENTERPRISE-SERVICE-3301',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3301',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3301.'
    },
    3302: {
        'service_name': 'ENTERPRISE-SERVICE-3302',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3302',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3302.'
    },
    3303: {
        'service_name': 'ENTERPRISE-SERVICE-3303',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3303',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3303.'
    },
    3304: {
        'service_name': 'ENTERPRISE-SERVICE-3304',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3304',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3304.'
    },
    3305: {
        'service_name': 'ENTERPRISE-SERVICE-3305',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3305',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3305.'
    },
    3307: {
        'service_name': 'ENTERPRISE-SERVICE-3307',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3307',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3307.'
    },
    3308: {
        'service_name': 'ENTERPRISE-SERVICE-3308',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3308',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3308.'
    },
    3309: {
        'service_name': 'ENTERPRISE-SERVICE-3309',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3309',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3309.'
    },
    3310: {
        'service_name': 'ENTERPRISE-SERVICE-3310',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3310',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3310.'
    },
    3311: {
        'service_name': 'ENTERPRISE-SERVICE-3311',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3311',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3311.'
    },
    3312: {
        'service_name': 'ENTERPRISE-SERVICE-3312',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3312',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3312.'
    },
    3313: {
        'service_name': 'ENTERPRISE-SERVICE-3313',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3313',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3313.'
    },
    3314: {
        'service_name': 'ENTERPRISE-SERVICE-3314',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3314',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3314.'
    },
    3315: {
        'service_name': 'ENTERPRISE-SERVICE-3315',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3315',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3315.'
    },
    3316: {
        'service_name': 'ENTERPRISE-SERVICE-3316',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3316',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3316.'
    },
    3317: {
        'service_name': 'ENTERPRISE-SERVICE-3317',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3317',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3317.'
    },
    3318: {
        'service_name': 'ENTERPRISE-SERVICE-3318',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3318',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3318.'
    },
    3319: {
        'service_name': 'ENTERPRISE-SERVICE-3319',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3319',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3319.'
    },
    3320: {
        'service_name': 'ENTERPRISE-SERVICE-3320',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3320',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3320.'
    },
    3321: {
        'service_name': 'ENTERPRISE-SERVICE-3321',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3321',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3321.'
    },
    3322: {
        'service_name': 'ENTERPRISE-SERVICE-3322',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3322',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3322.'
    },
    3323: {
        'service_name': 'ENTERPRISE-SERVICE-3323',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3323',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3323.'
    },
    3324: {
        'service_name': 'ENTERPRISE-SERVICE-3324',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3324',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3324.'
    },
    3325: {
        'service_name': 'ENTERPRISE-SERVICE-3325',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3325',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3325.'
    },
    3326: {
        'service_name': 'ENTERPRISE-SERVICE-3326',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3326',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3326.'
    },
    3327: {
        'service_name': 'ENTERPRISE-SERVICE-3327',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3327',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3327.'
    },
    3328: {
        'service_name': 'ENTERPRISE-SERVICE-3328',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3328',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3328.'
    },
    3329: {
        'service_name': 'ENTERPRISE-SERVICE-3329',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3329',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3329.'
    },
    3330: {
        'service_name': 'ENTERPRISE-SERVICE-3330',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3330',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3330.'
    },
    3331: {
        'service_name': 'ENTERPRISE-SERVICE-3331',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3331',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3331.'
    },
    3332: {
        'service_name': 'ENTERPRISE-SERVICE-3332',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3332',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3332.'
    },
    3333: {
        'service_name': 'ENTERPRISE-SERVICE-3333',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3333',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3333.'
    },
    3334: {
        'service_name': 'ENTERPRISE-SERVICE-3334',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3334',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3334.'
    },
    3335: {
        'service_name': 'ENTERPRISE-SERVICE-3335',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3335',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3335.'
    },
    3336: {
        'service_name': 'ENTERPRISE-SERVICE-3336',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3336',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3336.'
    },
    3337: {
        'service_name': 'ENTERPRISE-SERVICE-3337',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3337',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3337.'
    },
    3338: {
        'service_name': 'ENTERPRISE-SERVICE-3338',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3338',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3338.'
    },
    3339: {
        'service_name': 'ENTERPRISE-SERVICE-3339',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3339',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3339.'
    },
    3340: {
        'service_name': 'ENTERPRISE-SERVICE-3340',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3340',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3340.'
    },
    3341: {
        'service_name': 'ENTERPRISE-SERVICE-3341',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3341',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3341.'
    },
    3342: {
        'service_name': 'ENTERPRISE-SERVICE-3342',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3342',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3342.'
    },
    3343: {
        'service_name': 'ENTERPRISE-SERVICE-3343',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3343',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3343.'
    },
    3344: {
        'service_name': 'ENTERPRISE-SERVICE-3344',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3344',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3344.'
    },
    3345: {
        'service_name': 'ENTERPRISE-SERVICE-3345',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3345',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3345.'
    },
    3346: {
        'service_name': 'ENTERPRISE-SERVICE-3346',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3346',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3346.'
    },
    3347: {
        'service_name': 'ENTERPRISE-SERVICE-3347',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3347',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3347.'
    },
    3348: {
        'service_name': 'ENTERPRISE-SERVICE-3348',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3348',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3348.'
    },
    3349: {
        'service_name': 'ENTERPRISE-SERVICE-3349',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3349',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3349.'
    },
    3350: {
        'service_name': 'ENTERPRISE-SERVICE-3350',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3350',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3350.'
    },
    3351: {
        'service_name': 'ENTERPRISE-SERVICE-3351',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3351',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3351.'
    },
    3352: {
        'service_name': 'ENTERPRISE-SERVICE-3352',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3352',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3352.'
    },
    3353: {
        'service_name': 'ENTERPRISE-SERVICE-3353',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3353',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3353.'
    },
    3354: {
        'service_name': 'ENTERPRISE-SERVICE-3354',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3354',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3354.'
    },
    3355: {
        'service_name': 'ENTERPRISE-SERVICE-3355',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3355',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3355.'
    },
    3356: {
        'service_name': 'ENTERPRISE-SERVICE-3356',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3356',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3356.'
    },
    3357: {
        'service_name': 'ENTERPRISE-SERVICE-3357',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3357',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3357.'
    },
    3358: {
        'service_name': 'ENTERPRISE-SERVICE-3358',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3358',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3358.'
    },
    3359: {
        'service_name': 'ENTERPRISE-SERVICE-3359',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3359',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3359.'
    },
    3360: {
        'service_name': 'ENTERPRISE-SERVICE-3360',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3360',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3360.'
    },
    3361: {
        'service_name': 'ENTERPRISE-SERVICE-3361',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3361',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3361.'
    },
    3362: {
        'service_name': 'ENTERPRISE-SERVICE-3362',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3362',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3362.'
    },
    3363: {
        'service_name': 'ENTERPRISE-SERVICE-3363',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3363',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3363.'
    },
    3364: {
        'service_name': 'ENTERPRISE-SERVICE-3364',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3364',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3364.'
    },
    3365: {
        'service_name': 'ENTERPRISE-SERVICE-3365',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3365',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3365.'
    },
    3366: {
        'service_name': 'ENTERPRISE-SERVICE-3366',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3366',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3366.'
    },
    3367: {
        'service_name': 'ENTERPRISE-SERVICE-3367',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3367',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3367.'
    },
    3368: {
        'service_name': 'ENTERPRISE-SERVICE-3368',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3368',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3368.'
    },
    3369: {
        'service_name': 'ENTERPRISE-SERVICE-3369',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3369',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3369.'
    },
    3370: {
        'service_name': 'ENTERPRISE-SERVICE-3370',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3370',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3370.'
    },
    3371: {
        'service_name': 'ENTERPRISE-SERVICE-3371',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3371',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3371.'
    },
    3372: {
        'service_name': 'ENTERPRISE-SERVICE-3372',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3372',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3372.'
    },
    3373: {
        'service_name': 'ENTERPRISE-SERVICE-3373',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3373',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3373.'
    },
    3374: {
        'service_name': 'ENTERPRISE-SERVICE-3374',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3374',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3374.'
    },
    3375: {
        'service_name': 'ENTERPRISE-SERVICE-3375',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3375',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3375.'
    },
    3376: {
        'service_name': 'ENTERPRISE-SERVICE-3376',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3376',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3376.'
    },
    3377: {
        'service_name': 'ENTERPRISE-SERVICE-3377',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3377',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3377.'
    },
    3378: {
        'service_name': 'ENTERPRISE-SERVICE-3378',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3378',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3378.'
    },
    3379: {
        'service_name': 'ENTERPRISE-SERVICE-3379',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3379',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3379.'
    },
    3380: {
        'service_name': 'ENTERPRISE-SERVICE-3380',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3380',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3380.'
    },
    3381: {
        'service_name': 'ENTERPRISE-SERVICE-3381',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3381',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3381.'
    },
    3382: {
        'service_name': 'ENTERPRISE-SERVICE-3382',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3382',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3382.'
    },
    3383: {
        'service_name': 'ENTERPRISE-SERVICE-3383',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3383',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3383.'
    },
    3384: {
        'service_name': 'ENTERPRISE-SERVICE-3384',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3384',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3384.'
    },
    3385: {
        'service_name': 'ENTERPRISE-SERVICE-3385',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3385',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3385.'
    },
    3386: {
        'service_name': 'ENTERPRISE-SERVICE-3386',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3386',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3386.'
    },
    3387: {
        'service_name': 'ENTERPRISE-SERVICE-3387',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3387',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3387.'
    },
    3388: {
        'service_name': 'ENTERPRISE-SERVICE-3388',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3388',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3388.'
    },
    3390: {
        'service_name': 'ENTERPRISE-SERVICE-3390',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3390',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3390.'
    },
    3391: {
        'service_name': 'ENTERPRISE-SERVICE-3391',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3391',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3391.'
    },
    3392: {
        'service_name': 'ENTERPRISE-SERVICE-3392',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3392',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3392.'
    },
    3393: {
        'service_name': 'ENTERPRISE-SERVICE-3393',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3393',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3393.'
    },
    3394: {
        'service_name': 'ENTERPRISE-SERVICE-3394',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3394',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3394.'
    },
    3395: {
        'service_name': 'ENTERPRISE-SERVICE-3395',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3395',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3395.'
    },
    3396: {
        'service_name': 'ENTERPRISE-SERVICE-3396',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3396',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3396.'
    },
    3397: {
        'service_name': 'ENTERPRISE-SERVICE-3397',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3397',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3397.'
    },
    3398: {
        'service_name': 'ENTERPRISE-SERVICE-3398',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3398',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3398.'
    },
    3399: {
        'service_name': 'ENTERPRISE-SERVICE-3399',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3399',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3399.'
    },
    3400: {
        'service_name': 'ENTERPRISE-SERVICE-3400',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3400',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3400.'
    },
    3401: {
        'service_name': 'ENTERPRISE-SERVICE-3401',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3401',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3401.'
    },
    3402: {
        'service_name': 'ENTERPRISE-SERVICE-3402',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3402',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3402.'
    },
    3403: {
        'service_name': 'ENTERPRISE-SERVICE-3403',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3403',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3403.'
    },
    3404: {
        'service_name': 'ENTERPRISE-SERVICE-3404',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3404',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3404.'
    },
    3405: {
        'service_name': 'ENTERPRISE-SERVICE-3405',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3405',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3405.'
    },
    3406: {
        'service_name': 'ENTERPRISE-SERVICE-3406',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3406',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3406.'
    },
    3407: {
        'service_name': 'ENTERPRISE-SERVICE-3407',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3407',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3407.'
    },
    3408: {
        'service_name': 'ENTERPRISE-SERVICE-3408',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3408',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3408.'
    },
    3409: {
        'service_name': 'ENTERPRISE-SERVICE-3409',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3409',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3409.'
    },
    3410: {
        'service_name': 'ENTERPRISE-SERVICE-3410',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3410',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3410.'
    },
    3411: {
        'service_name': 'ENTERPRISE-SERVICE-3411',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3411',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3411.'
    },
    3412: {
        'service_name': 'ENTERPRISE-SERVICE-3412',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3412',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3412.'
    },
    3413: {
        'service_name': 'ENTERPRISE-SERVICE-3413',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3413',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3413.'
    },
    3414: {
        'service_name': 'ENTERPRISE-SERVICE-3414',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3414',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3414.'
    },
    3415: {
        'service_name': 'ENTERPRISE-SERVICE-3415',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3415',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3415.'
    },
    3416: {
        'service_name': 'ENTERPRISE-SERVICE-3416',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3416',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3416.'
    },
    3417: {
        'service_name': 'ENTERPRISE-SERVICE-3417',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3417',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3417.'
    },
    3418: {
        'service_name': 'ENTERPRISE-SERVICE-3418',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3418',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3418.'
    },
    3419: {
        'service_name': 'ENTERPRISE-SERVICE-3419',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3419',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3419.'
    },
    3420: {
        'service_name': 'ENTERPRISE-SERVICE-3420',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3420',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3420.'
    },
    3421: {
        'service_name': 'ENTERPRISE-SERVICE-3421',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3421',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3421.'
    },
    3422: {
        'service_name': 'ENTERPRISE-SERVICE-3422',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3422',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3422.'
    },
    3423: {
        'service_name': 'ENTERPRISE-SERVICE-3423',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3423',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3423.'
    },
    3424: {
        'service_name': 'ENTERPRISE-SERVICE-3424',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3424',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3424.'
    },
    3425: {
        'service_name': 'ENTERPRISE-SERVICE-3425',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3425',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3425.'
    },
    3426: {
        'service_name': 'ENTERPRISE-SERVICE-3426',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3426',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3426.'
    },
    3427: {
        'service_name': 'ENTERPRISE-SERVICE-3427',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3427',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3427.'
    },
    3428: {
        'service_name': 'ENTERPRISE-SERVICE-3428',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3428',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3428.'
    },
    3429: {
        'service_name': 'ENTERPRISE-SERVICE-3429',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3429',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3429.'
    },
    3430: {
        'service_name': 'ENTERPRISE-SERVICE-3430',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3430',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3430.'
    },
    3431: {
        'service_name': 'ENTERPRISE-SERVICE-3431',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3431',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3431.'
    },
    3432: {
        'service_name': 'ENTERPRISE-SERVICE-3432',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3432',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3432.'
    },
    3433: {
        'service_name': 'ENTERPRISE-SERVICE-3433',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3433',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3433.'
    },
    3434: {
        'service_name': 'ENTERPRISE-SERVICE-3434',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3434',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3434.'
    },
    3435: {
        'service_name': 'ENTERPRISE-SERVICE-3435',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3435',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3435.'
    },
    3436: {
        'service_name': 'ENTERPRISE-SERVICE-3436',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3436',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3436.'
    },
    3437: {
        'service_name': 'ENTERPRISE-SERVICE-3437',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3437',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3437.'
    },
    3438: {
        'service_name': 'ENTERPRISE-SERVICE-3438',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3438',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3438.'
    },
    3439: {
        'service_name': 'ENTERPRISE-SERVICE-3439',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3439',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3439.'
    },
    3440: {
        'service_name': 'ENTERPRISE-SERVICE-3440',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3440',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3440.'
    },
    3441: {
        'service_name': 'ENTERPRISE-SERVICE-3441',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3441',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3441.'
    },
    3442: {
        'service_name': 'ENTERPRISE-SERVICE-3442',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3442',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3442.'
    },
    3443: {
        'service_name': 'ENTERPRISE-SERVICE-3443',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3443',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3443.'
    },
    3444: {
        'service_name': 'ENTERPRISE-SERVICE-3444',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3444',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3444.'
    },
    3445: {
        'service_name': 'ENTERPRISE-SERVICE-3445',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3445',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3445.'
    },
    3446: {
        'service_name': 'ENTERPRISE-SERVICE-3446',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3446',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3446.'
    },
    3447: {
        'service_name': 'ENTERPRISE-SERVICE-3447',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3447',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3447.'
    },
    3448: {
        'service_name': 'ENTERPRISE-SERVICE-3448',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3448',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3448.'
    },
    3449: {
        'service_name': 'ENTERPRISE-SERVICE-3449',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3449',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3449.'
    },
    3450: {
        'service_name': 'ENTERPRISE-SERVICE-3450',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3450',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3450.'
    },
    3451: {
        'service_name': 'ENTERPRISE-SERVICE-3451',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3451',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3451.'
    },
    3452: {
        'service_name': 'ENTERPRISE-SERVICE-3452',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3452',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3452.'
    },
    3453: {
        'service_name': 'ENTERPRISE-SERVICE-3453',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3453',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3453.'
    },
    3454: {
        'service_name': 'ENTERPRISE-SERVICE-3454',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3454',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3454.'
    },
    3455: {
        'service_name': 'ENTERPRISE-SERVICE-3455',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3455',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3455.'
    },
    3456: {
        'service_name': 'ENTERPRISE-SERVICE-3456',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3456',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3456.'
    },
    3457: {
        'service_name': 'ENTERPRISE-SERVICE-3457',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3457',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3457.'
    },
    3458: {
        'service_name': 'ENTERPRISE-SERVICE-3458',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3458',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3458.'
    },
    3459: {
        'service_name': 'ENTERPRISE-SERVICE-3459',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3459',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3459.'
    },
    3460: {
        'service_name': 'ENTERPRISE-SERVICE-3460',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3460',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3460.'
    },
    3461: {
        'service_name': 'ENTERPRISE-SERVICE-3461',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3461',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3461.'
    },
    3462: {
        'service_name': 'ENTERPRISE-SERVICE-3462',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3462',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3462.'
    },
    3463: {
        'service_name': 'ENTERPRISE-SERVICE-3463',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3463',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3463.'
    },
    3464: {
        'service_name': 'ENTERPRISE-SERVICE-3464',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3464',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3464.'
    },
    3465: {
        'service_name': 'ENTERPRISE-SERVICE-3465',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3465',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3465.'
    },
    3466: {
        'service_name': 'ENTERPRISE-SERVICE-3466',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3466',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3466.'
    },
    3467: {
        'service_name': 'ENTERPRISE-SERVICE-3467',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3467',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3467.'
    },
    3468: {
        'service_name': 'ENTERPRISE-SERVICE-3468',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3468',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3468.'
    },
    3469: {
        'service_name': 'ENTERPRISE-SERVICE-3469',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3469',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3469.'
    },
    3470: {
        'service_name': 'ENTERPRISE-SERVICE-3470',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3470',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3470.'
    },
    3471: {
        'service_name': 'ENTERPRISE-SERVICE-3471',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3471',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3471.'
    },
    3472: {
        'service_name': 'ENTERPRISE-SERVICE-3472',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3472',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3472.'
    },
    3473: {
        'service_name': 'ENTERPRISE-SERVICE-3473',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3473',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3473.'
    },
    3474: {
        'service_name': 'ENTERPRISE-SERVICE-3474',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3474',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3474.'
    },
    3475: {
        'service_name': 'ENTERPRISE-SERVICE-3475',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3475',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3475.'
    },
    3476: {
        'service_name': 'ENTERPRISE-SERVICE-3476',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3476',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3476.'
    },
    3477: {
        'service_name': 'ENTERPRISE-SERVICE-3477',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3477',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3477.'
    },
    3478: {
        'service_name': 'ENTERPRISE-SERVICE-3478',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3478',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3478.'
    },
    3479: {
        'service_name': 'ENTERPRISE-SERVICE-3479',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3479',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3479.'
    },
    3480: {
        'service_name': 'ENTERPRISE-SERVICE-3480',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3480',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3480.'
    },
    3481: {
        'service_name': 'ENTERPRISE-SERVICE-3481',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3481',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3481.'
    },
    3482: {
        'service_name': 'ENTERPRISE-SERVICE-3482',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3482',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3482.'
    },
    3483: {
        'service_name': 'ENTERPRISE-SERVICE-3483',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3483',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3483.'
    },
    3484: {
        'service_name': 'ENTERPRISE-SERVICE-3484',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3484',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3484.'
    },
    3485: {
        'service_name': 'ENTERPRISE-SERVICE-3485',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3485',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3485.'
    },
    3486: {
        'service_name': 'ENTERPRISE-SERVICE-3486',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3486',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3486.'
    },
    3487: {
        'service_name': 'ENTERPRISE-SERVICE-3487',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3487',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3487.'
    },
    3488: {
        'service_name': 'ENTERPRISE-SERVICE-3488',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3488',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3488.'
    },
    3489: {
        'service_name': 'ENTERPRISE-SERVICE-3489',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3489',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3489.'
    },
    3490: {
        'service_name': 'ENTERPRISE-SERVICE-3490',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3490',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3490.'
    },
    3491: {
        'service_name': 'ENTERPRISE-SERVICE-3491',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3491',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3491.'
    },
    3492: {
        'service_name': 'ENTERPRISE-SERVICE-3492',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3492',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3492.'
    },
    3493: {
        'service_name': 'ENTERPRISE-SERVICE-3493',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3493',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3493.'
    },
    3494: {
        'service_name': 'ENTERPRISE-SERVICE-3494',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3494',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3494.'
    },
    3495: {
        'service_name': 'ENTERPRISE-SERVICE-3495',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3495',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3495.'
    },
    3496: {
        'service_name': 'ENTERPRISE-SERVICE-3496',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3496',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3496.'
    },
    3497: {
        'service_name': 'ENTERPRISE-SERVICE-3497',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3497',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3497.'
    },
    3498: {
        'service_name': 'ENTERPRISE-SERVICE-3498',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3498',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3498.'
    },
    3499: {
        'service_name': 'ENTERPRISE-SERVICE-3499',
        'transport': 'TCP',
        'full_name': 'Internal Microservice Port 3499',
        'description': 'Dynamic RPC or microservice endpoint allocated on port 3499.'
    },
}

def lookup_port_service(port: int):
    """Looks up registered network service by port number."""
    return IANA_PROTOCOL_REGISTRY.get(port, {
        'service_name': f'EPHEMERAL-{port}',
        'transport': 'TCP/UDP',
        'full_name': f'Ephemeral Dynamic Port {port}',
        'description': 'Dynamic high-range client socket port.'
    })
