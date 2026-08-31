import pytest
from app.utils.network_math import calculate_mean, calculate_stddev, calculate_z_score, calculate_ewma, format_bytes, format_bitrate

def test_mean_and_stddev():
    vals = [10.0, 20.0, 30.0, 40.0, 50.0]
    assert calculate_mean(vals) == 30.0
    assert round(calculate_stddev(vals), 2) == 15.81

def test_z_score():
    z = calculate_z_score(50.0, 30.0, 10.0)
    assert z == 2.0

def test_byte_formatting():
    assert format_bytes(1024) == '1.00 KB'
    assert format_bytes(1048576) == '1.00 MB'
    assert format_bytes(1073741824) == '1.00 GB'

def test_bitrate_formatting():
    assert format_bitrate(1000) == '1.00 Kbps'
    assert format_bitrate(1000000) == '1.00 Mbps'
