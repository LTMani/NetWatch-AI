# NetWatch AI - Enterprise Automated Remediation & Diagnostic Playbooks Knowledgebase
# Standardized operating procedures for rapid incident response

DIAGNOSTIC_PLAYBOOKS = {
    'SLOW_GATEWAY_LATENCY': {
        'title': 'Gateway & WAN Uplink Latency Degradation',
        'description': 'Triggered when RTT to default gateway exceeds 45ms or WAN latency exceeds 85ms.',
        'steps': ['1. Inspect edge router CPU utilization and buffer memory queue depth.', '2. Verify shaping and CoS / QoS bandwidth rate-limiting policies.', '3. Check interface error counters (CRC, frame alignment, collisions) on physical trunk link.', '4. Perform MTR traceroute to detect specific autonomous system (AS) hop degradation.', '5. Engage ISP NOC if latency is isolated to provider peering gateway.']
    },
    'DNS_RESOLUTION_LATENCY': {
        'title': 'DNS Resolver Congestion & Failure',
        'description': 'Triggered when internal or upstream DNS resolution times exceed 35ms.',
        'steps': ['1. Verify recursive DNS caching daemon process health and query cache hit ratio.', '2. Check upstream authoritative DNS root forwarders and failover resolver list.', '3. Inspect for DNS query flood or amplification attacks originating from internal subnet.', '4. Flush local DNS resolver cache if record corruption is suspected.', '5. Re-route DNS queries to secondary enterprise Anycast resolver.']
    },
    'BANDWIDTH_SATURATION_SPIKE': {
        'title': 'Egress Interface Bandwidth Saturation',
        'description': 'Triggered when uplink link utilization exceeds 90% capacity for > 5 minutes.',
        'steps': ['1. Identify top 5 talkers via NetFlow IPFIX conversation matrix.', '2. Check domain categories for unapproved video streaming, large OS updates, or P2P.', '3. Apply temporary QoS rate-limiting on non-essential traffic queues.', '4. If legitimate business spike, initiate dynamic bandwidth burst allocation.', '5. Quarantine any rogue endpoints violating traffic policies.']
    },
    'PACKET_DROP_BURST': {
        'title': 'Interface Packet Drop & Jitter Clustering',
        'description': 'Triggered when packet drop rate exceeds 0.5% on core distribution links.',
        'steps': ['1. Check switch port buffer drop counters and microburst statistics.', '2. Verify MTU size parity across all trunk switches (1500 vs 9000 Jumbo Frames).', '3. Inspect physical fiber transceivers (SFP/QSFP) for optical power level attenuation.', '4. Verify Spanning Tree Protocol (STP) convergence stability to rule out topology recalculation loops.', '5. Swap patch cables if physical layer CRC drops continue to increment.']
    },
    'OFF_HOURS_DATA_EXFILTRATION': {
        'title': 'Potential Data Exfiltration / C2 Beaconing',
        'description': 'Triggered when high-volume outbound data transfer occurs during non-office hours.',
        'steps': ['1. Immediately isolate source host from enterprise network via automated VLAN quarantine.', '2. Capture NetFlow session records: source/destination IPs, ports, bytes, protocol.', '3. Query DNS logs for high-entropy domains or fast-flux resolution patterns.', '4. Cross-reference destination IP with threat intelligence reputation feeds.', '5. Open SEV-1 incident ticket and notify SOC incident response on-call team.']
    },
    'TROUBLESHOOT_PATTERN_001': {
        'title': 'Automated Diagnostic Procedure 1: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #1.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_002': {
        'title': 'Automated Diagnostic Procedure 2: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #2.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_003': {
        'title': 'Automated Diagnostic Procedure 3: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #3.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_004': {
        'title': 'Automated Diagnostic Procedure 4: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #4.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_005': {
        'title': 'Automated Diagnostic Procedure 5: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #5.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_006': {
        'title': 'Automated Diagnostic Procedure 6: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #6.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_007': {
        'title': 'Automated Diagnostic Procedure 7: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #7.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_008': {
        'title': 'Automated Diagnostic Procedure 8: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #8.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_009': {
        'title': 'Automated Diagnostic Procedure 9: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #9.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_010': {
        'title': 'Automated Diagnostic Procedure 10: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #10.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_011': {
        'title': 'Automated Diagnostic Procedure 11: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #11.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_012': {
        'title': 'Automated Diagnostic Procedure 12: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #12.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_013': {
        'title': 'Automated Diagnostic Procedure 13: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #13.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_014': {
        'title': 'Automated Diagnostic Procedure 14: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #14.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_015': {
        'title': 'Automated Diagnostic Procedure 15: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #15.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_016': {
        'title': 'Automated Diagnostic Procedure 16: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #16.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_017': {
        'title': 'Automated Diagnostic Procedure 17: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #17.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_018': {
        'title': 'Automated Diagnostic Procedure 18: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #18.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_019': {
        'title': 'Automated Diagnostic Procedure 19: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #19.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_020': {
        'title': 'Automated Diagnostic Procedure 20: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #20.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_021': {
        'title': 'Automated Diagnostic Procedure 21: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #21.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_022': {
        'title': 'Automated Diagnostic Procedure 22: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #22.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_023': {
        'title': 'Automated Diagnostic Procedure 23: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #23.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_024': {
        'title': 'Automated Diagnostic Procedure 24: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #24.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_025': {
        'title': 'Automated Diagnostic Procedure 25: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #25.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_026': {
        'title': 'Automated Diagnostic Procedure 26: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #26.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_027': {
        'title': 'Automated Diagnostic Procedure 27: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #27.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_028': {
        'title': 'Automated Diagnostic Procedure 28: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #28.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_029': {
        'title': 'Automated Diagnostic Procedure 29: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #29.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_030': {
        'title': 'Automated Diagnostic Procedure 30: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #30.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_031': {
        'title': 'Automated Diagnostic Procedure 31: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #31.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_032': {
        'title': 'Automated Diagnostic Procedure 32: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #32.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_033': {
        'title': 'Automated Diagnostic Procedure 33: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #33.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_034': {
        'title': 'Automated Diagnostic Procedure 34: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #34.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_035': {
        'title': 'Automated Diagnostic Procedure 35: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #35.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_036': {
        'title': 'Automated Diagnostic Procedure 36: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #36.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_037': {
        'title': 'Automated Diagnostic Procedure 37: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #37.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_038': {
        'title': 'Automated Diagnostic Procedure 38: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #38.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_039': {
        'title': 'Automated Diagnostic Procedure 39: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #39.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_040': {
        'title': 'Automated Diagnostic Procedure 40: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #40.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_041': {
        'title': 'Automated Diagnostic Procedure 41: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #41.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_042': {
        'title': 'Automated Diagnostic Procedure 42: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #42.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_043': {
        'title': 'Automated Diagnostic Procedure 43: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #43.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_044': {
        'title': 'Automated Diagnostic Procedure 44: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #44.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_045': {
        'title': 'Automated Diagnostic Procedure 45: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #45.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_046': {
        'title': 'Automated Diagnostic Procedure 46: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #46.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_047': {
        'title': 'Automated Diagnostic Procedure 47: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #47.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_048': {
        'title': 'Automated Diagnostic Procedure 48: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #48.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_049': {
        'title': 'Automated Diagnostic Procedure 49: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #49.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_050': {
        'title': 'Automated Diagnostic Procedure 50: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #50.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_051': {
        'title': 'Automated Diagnostic Procedure 51: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #51.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_052': {
        'title': 'Automated Diagnostic Procedure 52: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #52.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_053': {
        'title': 'Automated Diagnostic Procedure 53: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #53.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_054': {
        'title': 'Automated Diagnostic Procedure 54: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #54.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_055': {
        'title': 'Automated Diagnostic Procedure 55: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #55.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_056': {
        'title': 'Automated Diagnostic Procedure 56: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #56.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_057': {
        'title': 'Automated Diagnostic Procedure 57: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #57.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_058': {
        'title': 'Automated Diagnostic Procedure 58: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #58.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_059': {
        'title': 'Automated Diagnostic Procedure 59: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #59.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_060': {
        'title': 'Automated Diagnostic Procedure 60: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #60.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_061': {
        'title': 'Automated Diagnostic Procedure 61: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #61.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_062': {
        'title': 'Automated Diagnostic Procedure 62: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #62.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_063': {
        'title': 'Automated Diagnostic Procedure 63: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #63.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_064': {
        'title': 'Automated Diagnostic Procedure 64: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #64.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_065': {
        'title': 'Automated Diagnostic Procedure 65: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #65.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_066': {
        'title': 'Automated Diagnostic Procedure 66: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #66.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_067': {
        'title': 'Automated Diagnostic Procedure 67: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #67.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_068': {
        'title': 'Automated Diagnostic Procedure 68: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #68.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_069': {
        'title': 'Automated Diagnostic Procedure 69: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #69.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_070': {
        'title': 'Automated Diagnostic Procedure 70: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #70.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_071': {
        'title': 'Automated Diagnostic Procedure 71: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #71.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_072': {
        'title': 'Automated Diagnostic Procedure 72: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #72.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_073': {
        'title': 'Automated Diagnostic Procedure 73: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #73.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_074': {
        'title': 'Automated Diagnostic Procedure 74: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #74.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_075': {
        'title': 'Automated Diagnostic Procedure 75: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #75.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_076': {
        'title': 'Automated Diagnostic Procedure 76: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #76.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_077': {
        'title': 'Automated Diagnostic Procedure 77: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #77.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_078': {
        'title': 'Automated Diagnostic Procedure 78: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #78.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_079': {
        'title': 'Automated Diagnostic Procedure 79: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #79.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_080': {
        'title': 'Automated Diagnostic Procedure 80: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #80.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_081': {
        'title': 'Automated Diagnostic Procedure 81: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #81.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_082': {
        'title': 'Automated Diagnostic Procedure 82: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #82.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_083': {
        'title': 'Automated Diagnostic Procedure 83: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #83.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_084': {
        'title': 'Automated Diagnostic Procedure 84: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #84.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_085': {
        'title': 'Automated Diagnostic Procedure 85: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #85.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_086': {
        'title': 'Automated Diagnostic Procedure 86: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #86.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_087': {
        'title': 'Automated Diagnostic Procedure 87: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #87.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_088': {
        'title': 'Automated Diagnostic Procedure 88: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #88.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_089': {
        'title': 'Automated Diagnostic Procedure 89: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #89.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_090': {
        'title': 'Automated Diagnostic Procedure 90: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #90.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_091': {
        'title': 'Automated Diagnostic Procedure 91: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #91.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_092': {
        'title': 'Automated Diagnostic Procedure 92: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #92.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_093': {
        'title': 'Automated Diagnostic Procedure 93: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #93.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_094': {
        'title': 'Automated Diagnostic Procedure 94: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #94.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_095': {
        'title': 'Automated Diagnostic Procedure 95: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #95.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_096': {
        'title': 'Automated Diagnostic Procedure 96: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #96.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_097': {
        'title': 'Automated Diagnostic Procedure 97: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #97.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_098': {
        'title': 'Automated Diagnostic Procedure 98: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #98.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_099': {
        'title': 'Automated Diagnostic Procedure 99: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #99.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_100': {
        'title': 'Automated Diagnostic Procedure 100: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #100.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_101': {
        'title': 'Automated Diagnostic Procedure 101: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #101.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_102': {
        'title': 'Automated Diagnostic Procedure 102: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #102.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_103': {
        'title': 'Automated Diagnostic Procedure 103: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #103.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_104': {
        'title': 'Automated Diagnostic Procedure 104: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #104.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_105': {
        'title': 'Automated Diagnostic Procedure 105: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #105.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_106': {
        'title': 'Automated Diagnostic Procedure 106: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #106.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_107': {
        'title': 'Automated Diagnostic Procedure 107: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #107.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_108': {
        'title': 'Automated Diagnostic Procedure 108: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #108.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_109': {
        'title': 'Automated Diagnostic Procedure 109: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #109.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_110': {
        'title': 'Automated Diagnostic Procedure 110: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #110.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_111': {
        'title': 'Automated Diagnostic Procedure 111: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #111.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_112': {
        'title': 'Automated Diagnostic Procedure 112: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #112.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_113': {
        'title': 'Automated Diagnostic Procedure 113: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #113.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_114': {
        'title': 'Automated Diagnostic Procedure 114: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #114.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_115': {
        'title': 'Automated Diagnostic Procedure 115: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #115.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_116': {
        'title': 'Automated Diagnostic Procedure 116: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #116.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_117': {
        'title': 'Automated Diagnostic Procedure 117: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #117.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_118': {
        'title': 'Automated Diagnostic Procedure 118: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #118.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_119': {
        'title': 'Automated Diagnostic Procedure 119: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #119.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_120': {
        'title': 'Automated Diagnostic Procedure 120: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #120.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_121': {
        'title': 'Automated Diagnostic Procedure 121: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #121.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_122': {
        'title': 'Automated Diagnostic Procedure 122: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #122.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_123': {
        'title': 'Automated Diagnostic Procedure 123: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #123.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_124': {
        'title': 'Automated Diagnostic Procedure 124: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #124.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_125': {
        'title': 'Automated Diagnostic Procedure 125: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #125.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_126': {
        'title': 'Automated Diagnostic Procedure 126: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #126.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_127': {
        'title': 'Automated Diagnostic Procedure 127: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #127.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_128': {
        'title': 'Automated Diagnostic Procedure 128: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #128.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_129': {
        'title': 'Automated Diagnostic Procedure 129: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #129.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_130': {
        'title': 'Automated Diagnostic Procedure 130: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #130.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_131': {
        'title': 'Automated Diagnostic Procedure 131: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #131.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_132': {
        'title': 'Automated Diagnostic Procedure 132: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #132.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_133': {
        'title': 'Automated Diagnostic Procedure 133: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #133.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_134': {
        'title': 'Automated Diagnostic Procedure 134: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #134.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_135': {
        'title': 'Automated Diagnostic Procedure 135: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #135.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_136': {
        'title': 'Automated Diagnostic Procedure 136: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #136.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_137': {
        'title': 'Automated Diagnostic Procedure 137: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #137.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_138': {
        'title': 'Automated Diagnostic Procedure 138: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #138.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_139': {
        'title': 'Automated Diagnostic Procedure 139: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #139.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_140': {
        'title': 'Automated Diagnostic Procedure 140: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #140.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_141': {
        'title': 'Automated Diagnostic Procedure 141: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #141.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_142': {
        'title': 'Automated Diagnostic Procedure 142: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #142.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_143': {
        'title': 'Automated Diagnostic Procedure 143: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #143.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_144': {
        'title': 'Automated Diagnostic Procedure 144: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #144.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_145': {
        'title': 'Automated Diagnostic Procedure 145: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #145.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_146': {
        'title': 'Automated Diagnostic Procedure 146: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #146.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_147': {
        'title': 'Automated Diagnostic Procedure 147: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #147.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_148': {
        'title': 'Automated Diagnostic Procedure 148: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #148.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_149': {
        'title': 'Automated Diagnostic Procedure 149: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #149.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_150': {
        'title': 'Automated Diagnostic Procedure 150: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #150.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_151': {
        'title': 'Automated Diagnostic Procedure 151: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #151.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_152': {
        'title': 'Automated Diagnostic Procedure 152: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #152.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_153': {
        'title': 'Automated Diagnostic Procedure 153: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #153.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_154': {
        'title': 'Automated Diagnostic Procedure 154: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #154.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_155': {
        'title': 'Automated Diagnostic Procedure 155: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #155.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_156': {
        'title': 'Automated Diagnostic Procedure 156: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #156.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_157': {
        'title': 'Automated Diagnostic Procedure 157: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #157.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_158': {
        'title': 'Automated Diagnostic Procedure 158: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #158.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_159': {
        'title': 'Automated Diagnostic Procedure 159: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #159.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_160': {
        'title': 'Automated Diagnostic Procedure 160: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #160.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_161': {
        'title': 'Automated Diagnostic Procedure 161: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #161.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_162': {
        'title': 'Automated Diagnostic Procedure 162: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #162.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_163': {
        'title': 'Automated Diagnostic Procedure 163: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #163.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_164': {
        'title': 'Automated Diagnostic Procedure 164: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #164.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_165': {
        'title': 'Automated Diagnostic Procedure 165: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #165.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_166': {
        'title': 'Automated Diagnostic Procedure 166: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #166.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_167': {
        'title': 'Automated Diagnostic Procedure 167: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #167.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_168': {
        'title': 'Automated Diagnostic Procedure 168: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #168.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_169': {
        'title': 'Automated Diagnostic Procedure 169: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #169.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_170': {
        'title': 'Automated Diagnostic Procedure 170: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #170.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_171': {
        'title': 'Automated Diagnostic Procedure 171: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #171.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_172': {
        'title': 'Automated Diagnostic Procedure 172: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #172.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_173': {
        'title': 'Automated Diagnostic Procedure 173: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #173.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_174': {
        'title': 'Automated Diagnostic Procedure 174: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #174.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_175': {
        'title': 'Automated Diagnostic Procedure 175: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #175.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_176': {
        'title': 'Automated Diagnostic Procedure 176: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #176.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_177': {
        'title': 'Automated Diagnostic Procedure 177: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #177.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_178': {
        'title': 'Automated Diagnostic Procedure 178: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #178.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_179': {
        'title': 'Automated Diagnostic Procedure 179: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #179.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_180': {
        'title': 'Automated Diagnostic Procedure 180: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #180.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_181': {
        'title': 'Automated Diagnostic Procedure 181: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #181.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_182': {
        'title': 'Automated Diagnostic Procedure 182: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #182.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_183': {
        'title': 'Automated Diagnostic Procedure 183: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #183.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_184': {
        'title': 'Automated Diagnostic Procedure 184: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #184.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_185': {
        'title': 'Automated Diagnostic Procedure 185: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #185.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_186': {
        'title': 'Automated Diagnostic Procedure 186: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #186.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_187': {
        'title': 'Automated Diagnostic Procedure 187: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #187.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_188': {
        'title': 'Automated Diagnostic Procedure 188: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #188.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_189': {
        'title': 'Automated Diagnostic Procedure 189: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #189.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_190': {
        'title': 'Automated Diagnostic Procedure 190: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #190.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_191': {
        'title': 'Automated Diagnostic Procedure 191: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #191.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_192': {
        'title': 'Automated Diagnostic Procedure 192: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #192.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_193': {
        'title': 'Automated Diagnostic Procedure 193: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #193.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_194': {
        'title': 'Automated Diagnostic Procedure 194: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #194.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_195': {
        'title': 'Automated Diagnostic Procedure 195: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #195.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_196': {
        'title': 'Automated Diagnostic Procedure 196: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #196.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_197': {
        'title': 'Automated Diagnostic Procedure 197: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #197.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_198': {
        'title': 'Automated Diagnostic Procedure 198: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #198.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_199': {
        'title': 'Automated Diagnostic Procedure 199: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #199.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_200': {
        'title': 'Automated Diagnostic Procedure 200: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #200.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_201': {
        'title': 'Automated Diagnostic Procedure 201: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #201.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_202': {
        'title': 'Automated Diagnostic Procedure 202: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #202.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_203': {
        'title': 'Automated Diagnostic Procedure 203: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #203.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_204': {
        'title': 'Automated Diagnostic Procedure 204: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #204.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_205': {
        'title': 'Automated Diagnostic Procedure 205: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #205.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_206': {
        'title': 'Automated Diagnostic Procedure 206: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #206.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_207': {
        'title': 'Automated Diagnostic Procedure 207: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #207.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_208': {
        'title': 'Automated Diagnostic Procedure 208: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #208.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_209': {
        'title': 'Automated Diagnostic Procedure 209: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #209.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_210': {
        'title': 'Automated Diagnostic Procedure 210: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #210.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_211': {
        'title': 'Automated Diagnostic Procedure 211: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #211.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_212': {
        'title': 'Automated Diagnostic Procedure 212: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #212.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_213': {
        'title': 'Automated Diagnostic Procedure 213: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #213.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_214': {
        'title': 'Automated Diagnostic Procedure 214: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #214.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_215': {
        'title': 'Automated Diagnostic Procedure 215: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #215.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_216': {
        'title': 'Automated Diagnostic Procedure 216: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #216.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_217': {
        'title': 'Automated Diagnostic Procedure 217: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #217.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_218': {
        'title': 'Automated Diagnostic Procedure 218: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #218.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_219': {
        'title': 'Automated Diagnostic Procedure 219: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #219.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_220': {
        'title': 'Automated Diagnostic Procedure 220: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #220.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_221': {
        'title': 'Automated Diagnostic Procedure 221: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #221.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_222': {
        'title': 'Automated Diagnostic Procedure 222: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #222.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_223': {
        'title': 'Automated Diagnostic Procedure 223: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #223.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_224': {
        'title': 'Automated Diagnostic Procedure 224: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #224.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_225': {
        'title': 'Automated Diagnostic Procedure 225: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #225.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_226': {
        'title': 'Automated Diagnostic Procedure 226: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #226.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_227': {
        'title': 'Automated Diagnostic Procedure 227: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #227.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_228': {
        'title': 'Automated Diagnostic Procedure 228: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #228.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_229': {
        'title': 'Automated Diagnostic Procedure 229: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #229.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_230': {
        'title': 'Automated Diagnostic Procedure 230: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #230.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_231': {
        'title': 'Automated Diagnostic Procedure 231: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #231.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_232': {
        'title': 'Automated Diagnostic Procedure 232: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #232.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_233': {
        'title': 'Automated Diagnostic Procedure 233: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #233.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_234': {
        'title': 'Automated Diagnostic Procedure 234: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #234.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_235': {
        'title': 'Automated Diagnostic Procedure 235: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #235.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_236': {
        'title': 'Automated Diagnostic Procedure 236: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #236.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_237': {
        'title': 'Automated Diagnostic Procedure 237: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #237.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_238': {
        'title': 'Automated Diagnostic Procedure 238: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #238.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_239': {
        'title': 'Automated Diagnostic Procedure 239: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #239.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_240': {
        'title': 'Automated Diagnostic Procedure 240: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #240.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_241': {
        'title': 'Automated Diagnostic Procedure 241: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #241.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_242': {
        'title': 'Automated Diagnostic Procedure 242: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #242.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_243': {
        'title': 'Automated Diagnostic Procedure 243: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #243.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_244': {
        'title': 'Automated Diagnostic Procedure 244: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #244.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_245': {
        'title': 'Automated Diagnostic Procedure 245: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #245.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_246': {
        'title': 'Automated Diagnostic Procedure 246: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #246.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_247': {
        'title': 'Automated Diagnostic Procedure 247: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #247.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_248': {
        'title': 'Automated Diagnostic Procedure 248: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #248.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
    'TROUBLESHOOT_PATTERN_249': {
        'title': 'Automated Diagnostic Procedure 249: Interface Telemetry Scenario',
        'description': 'Standard operating procedure for resolving network anomaly pattern #249.',
        'steps': [
            '1. Gather real-time flow metrics for past 15-minute window.',
            '2. Run ping and jitter probe to verify baseline latency.',
            '3. Check interface status via SNMP/Telemetry query.',
            '4. Apply corrective traffic policy if threshold is exceeded.'
        ]
    },
}
