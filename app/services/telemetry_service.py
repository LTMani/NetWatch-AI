from typing import List, Dict, Any
from datetime import datetime, timezone
from app.repositories.telemetry_repository import TelemetryRepository
from app.repositories.device_repository import DeviceRepository
from app.services.domain_engine import DomainClassificationEngine
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.utils.datetime_utils import utc_now, is_within_office_hours
from app.errors.exceptions import PrivacyViolationError, TelemetryIngestionError

class TelemetryIngestionService:
    def __init__(self, telemetry_repo: TelemetryRepository = None, device_repo: DeviceRepository = None):
        self.telemetry_repo = telemetry_repo or TelemetryRepository()
        self.device_repo = device_repo or DeviceRepository()
        self.domain_engine = DomainClassificationEngine()

    def ingest_flow_batch(self, flows: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Ingests a batch of NetFlow / IPFIX flow records strictly enforcing enterprise privacy boundaries."""
        flow_objects = []
        now = utc_now()
        
        for item in flows:
            # Privacy boundary: ensure no packet payloads or private messages are present
            if any(forbidden in item for forbidden in ('payload', 'keystrokes', 'message_body', 'raw_packet')):
                raise PrivacyViolationError('Packet payload or private message capture violates enterprise privacy policy.')

            src_ip = item.get('source_ip')
            dst_ip = item.get('destination_ip')
            if not src_ip or not dst_ip:
                continue

            device = self.device_repo.get_by_ip(src_ip)
            device_id = device.id if device else None
            subnet_id = device.subnet_id if device else None

            # Calculate office hours status
            ts = now
            in_office = is_within_office_hours(ts)

            flow_obj = NetworkFlowMetric(
                device_id=device_id,
                subnet_id=subnet_id,
                source_ip=src_ip,
                source_port=int(item.get('source_port', 0)),
                destination_ip=dst_ip,
                destination_port=int(item.get('destination_port', 0)),
                protocol=item.get('protocol', 'TCP').upper(),
                bytes_in=int(item.get('bytes_in', 0)),
                bytes_out=int(item.get('bytes_out', 0)),
                packets_in=int(item.get('packets_in', 0)),
                packets_out=int(item.get('packets_out', 0)),
                duration_ms=int(item.get('duration_ms', 0)),
                latency_ms=float(item.get('latency_ms', 10.0)),
                jitter_ms=float(item.get('jitter_ms', 1.0)),
                packet_loss_percent=float(item.get('packet_loss_percent', 0.0)),
                tcp_flags=item.get('tcp_flags', 'ACK'),
                is_office_hours=in_office,
                timestamp=ts
            )
            flow_objects.append(flow_obj)

        if flow_objects:
            self.telemetry_repo.insert_flow_batch(flow_objects)

        return {
            'status': 'success',
            'ingested_count': len(flow_objects),
            'timestamp': now.isoformat()
        }

    def ingest_dns_query(self, device_ip: str, domain_name: str, query_type: str = 'A', response_code: str = 'NOERROR', response_time_ms: float = 12.0) -> DNSQueryLog:
        device = self.device_repo.get_by_ip(device_ip)
        device_id = device.id if device else None
        
        cat, score, is_mal, _ = self.domain_engine.classify_domain(domain_name)
        filter_res = self.domain_engine.evaluate_filter_rules(domain_name)
        is_blocked = filter_res['blocked'] if filter_res else is_mal
        block_reason = filter_res['reason'] if filter_res else ('Known malicious domain' if is_mal else None)

        now = utc_now()
        in_office = is_within_office_hours(now)

        dns_log = DNSQueryLog(
            device_id=device_id,
            domain_name=domain_name.lower().strip(),
            query_type=query_type,
            response_code=response_code,
            response_time_ms=response_time_ms,
            category=cat,
            is_blocked=is_blocked,
            block_reason=block_reason,
            is_office_hours=in_office,
            timestamp=now
        )
        from app.models.base import db
        db.session.add(dns_log)
        db.session.commit()
        return dns_log
