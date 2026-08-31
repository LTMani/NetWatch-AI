import math
from typing import List, Union

def format_bytes(byte_count: Union[int, float]) -> str:
    if byte_count is None or byte_count < 0:
        return '0 B'
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    val = float(byte_count)
    idx = 0
    while val >= 1024.0 and idx < len(units) - 1:
        val /= 1024.0
        idx += 1
    if idx == 0:
        return f'{int(val)} B'
    return f'{val:.2f} {units[idx]}'

def format_bitrate(bps: Union[int, float]) -> str:
    if bps is None or bps < 0:
        return '0 bps'
    units = ['bps', 'Kbps', 'Mbps', 'Gbps', 'Tbps']
    val = float(bps)
    idx = 0
    while val >= 1000.0 and idx < len(units) - 1:
        val /= 1000.0
        idx += 1
    if idx == 0:
        return f'{int(val)} bps'
    return f'{val:.2f} {units[idx]}'

def calculate_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_stddev(values: List[float], mean: float = None) -> float:
    if not values or len(values) < 2:
        return 0.0
    if mean is None:
        mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

def calculate_z_score(value: float, mean: float, stddev: float) -> float:
    if stddev <= 1e-9:
        return 0.0
    return (value - mean) / stddev

def calculate_ewma(values: List[float], alpha: float = 0.2) -> List[float]:
    if not values:
        return []
    ewma_series = [values[0]]
    for v in values[1:]:
        new_ewma = (alpha * v) + ((1.0 - alpha) * ewma_series[-1])
        ewma_series.append(new_ewma)
    return ewma_series

def calculate_percentile(values: List[float], percentile: float) -> float:
    if not values:
        return 0.0
    sorted_v = sorted(values)
    k = (len(sorted_v) - 1) * (percentile / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_v[int(k)]
    d0 = sorted_v[int(f)] * (c - k)
    d1 = sorted_v[int(c)] * (k - f)
    return d0 + d1
