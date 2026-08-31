import time
import random
import sys
from datetime import datetime, timezone

sys.path.insert(0, '.')
from app import create_app
from app.models.base import db
from app.models.device import Device
from app.models.telemetry import NetworkFlowMetric, DNSQueryLog
from app.utils.datetime_utils import utc_now

app = create_app('development')

def stream_telemetry_batch():
    with app.app_context():
        devices = Device.query.filter_by(is_deleted=False).limit(20).all()
        if not devices:
            print('[!] No devices found in database.')
            return

        now = utc_now()
        domains = ['github.com', 'slack.com', 'aws.amazon.com', 'docs.python.org', 'notion.so', 'google.com', 'zoom.us']

        for d in devices:
            # 1. Ingest Flow
            flow = NetworkFlowMetric(
                device_id=d.id,
                subnet_id=d.subnet_id,
                source_ip=d.ip_address,
                destination_ip=f'142.250.190.{random.randint(1, 254)}',
                source_port=random.randint(1024, 65535),
                destination_port=443,
                protocol='TCP',
                bytes_in=random.randint(50_000, 2_000_000),
                bytes_out=random.randint(20_000, 800_000),
                packets_in=random.randint(50, 1500),
                packets_out=random.randint(30, 900),
                latency_ms=round(random.uniform(8.0, 25.0), 1),
                packet_loss_percent=round(random.uniform(0.0, 0.02), 3),
                jitter_ms=round(random.uniform(0.5, 2.0), 2),
                is_office_hours=True,
                timestamp=now
            )
            db.session.add(flow)

            # 2. Ingest DNS Query
            q = DNSQueryLog(
                device_id=d.id,
                domain_name=random.choice(domains),
                query_type='A',
                response_code='NOERROR',
                response_time_ms=round(random.uniform(4.0, 22.0), 1),
                category='Development',
                is_office_hours=True,
                is_blocked=False,
                timestamp=now
            )
            db.session.add(q)

        db.session.commit()
        print(f'[+] Ingested live telemetry batch for {len(devices)} devices at {now.isoformat()}')

if __name__ == '__main__':
    print('[*] Running single live telemetry stream iteration...')
    stream_telemetry_batch()
