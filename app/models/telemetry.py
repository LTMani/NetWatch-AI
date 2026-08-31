from datetime import datetime, timezone
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, db

class NetworkFlowMetric(BaseModel):
    """NetFlow / IPFIX metadata frame recording authorized connection statistics."""
    __tablename__ = 'nw_flow_metrics'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    
    source_ip = Column(String(45), nullable=False, index=True)
    source_port = Column(Integer, nullable=False)
    destination_ip = Column(String(45), nullable=False, index=True)
    destination_port = Column(Integer, nullable=False, index=True)
    
    protocol = Column(String(16), default='TCP', nullable=False, index=True)
    bytes_in = Column(BigInteger, default=0, nullable=False)
    bytes_out = Column(BigInteger, default=0, nullable=False)
    packets_in = Column(Integer, default=0, nullable=False)
    packets_out = Column(Integer, default=0, nullable=False)
    
    duration_ms = Column(Integer, default=0, nullable=False)
    latency_ms = Column(Float, default=0.0, nullable=False)
    jitter_ms = Column(Float, default=0.0, nullable=False)
    packet_loss_percent = Column(Float, default=0.0, nullable=False)
    tcp_flags = Column(String(16), nullable=True)
    
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    device = relationship('Device', back_populates='flow_metrics')

class DNSQueryLog(BaseModel):
    """Authorized domain-level resolution telemetry without payload inspection."""
    __tablename__ = 'nw_dns_queries'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    domain_name = Column(String(256), nullable=False, index=True)
    query_type = Column(String(8), default='A', nullable=False) # A, AAAA, CNAME, MX, TXT, PTR
    response_code = Column(String(16), default='NOERROR', nullable=False) # NOERROR, NXDOMAIN, SERVFAIL
    response_ip = Column(String(45), nullable=True)
    response_time_ms = Column(Float, default=0.0, nullable=False)
    
    category = Column(String(64), default='Unknown', nullable=False, index=True)
    is_blocked = Column(Boolean, default=False, nullable=False, index=True)
    block_reason = Column(String(128), nullable=True)
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)

    device = relationship('Device', back_populates='dns_queries')

class BandwidthTimeseries(BaseModel):
    """Aggregated hourly/5-min bandwidth time series for fast historical analytics."""
    __tablename__ = 'nw_bandwidth_timeseries'

    device_id = Column(String(36), ForeignKey('nw_devices.id', ondelete='CASCADE'), nullable=True, index=True)
    subnet_id = Column(String(36), ForeignKey('nw_subnets.id'), nullable=True, index=True)
    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    
    bytes_in = Column(BigInteger, default=0, nullable=False)
    bytes_out = Column(BigInteger, default=0, nullable=False)
    peak_bps_in = Column(Float, default=0.0, nullable=False)
    peak_bps_out = Column(Float, default=0.0, nullable=False)
    avg_latency_ms = Column(Float, default=0.0, nullable=False)
    avg_packet_loss = Column(Float, default=0.0, nullable=False)
    
    interval_start = Column(DateTime, nullable=False, index=True)
    interval_end = Column(DateTime, nullable=False)
    is_office_hours = Column(Boolean, default=True, nullable=False, index=True)

class PacketMetric(BaseModel):
    """Raw network interface error counters and link performance metrics."""
    __tablename__ = 'nw_packet_metrics'

    site_id = Column(String(36), ForeignKey('nw_network_sites.id'), nullable=True, index=True)
    interface_name = Column(String(64), nullable=False, index=True)
    rx_bytes = Column(BigInteger, default=0, nullable=False)
    tx_bytes = Column(BigInteger, default=0, nullable=False)
    rx_packets = Column(BigInteger, default=0, nullable=False)
    tx_packets = Column(BigInteger, default=0, nullable=False)
    rx_errors = Column(Integer, default=0, nullable=False)
    tx_errors = Column(Integer, default=0, nullable=False)
    rx_drops = Column(Integer, default=0, nullable=False)
    tx_drops = Column(Integer, default=0, nullable=False)
    link_flaps = Column(Integer, default=0, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False, index=True)
