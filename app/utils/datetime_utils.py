from datetime import datetime, time, timedelta, timezone

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def format_iso_utc(dt: datetime) -> str:
    if not dt:
        return ''
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()

def parse_iso_datetime(dt_str: str) -> datetime:
    if not dt_str:
        return utc_now()
    dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def is_within_office_hours(dt: datetime, start_time_str: str = '09:00', end_time_str: str = '18:00', work_days: list = None) -> bool:
    if work_days is None:
        work_days = [0, 1, 2, 3, 4]
    if dt.weekday() not in work_days:
        return False
    start_h, start_m = map(int, start_time_str.split(':'))
    end_h, end_m = map(int, end_time_str.split(':'))
    start_t = time(start_h, start_m)
    end_t = time(end_h, end_m)
    current_t = dt.time()
    return start_t <= current_t <= end_t

def format_relative_time(dt: datetime) -> str:
    if not dt:
        return 'never'
    now = utc_now()
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    diff = now - dt
    seconds = int(diff.total_seconds())
    if seconds < 0:
        return 'just now'
    if seconds < 60:
        return f'{seconds}s ago' if seconds > 5 else 'just now'
    minutes = seconds // 60
    if minutes < 60:
        return f'{minutes}m ago'
    hours = minutes // 60
    if hours < 24:
        return f'{hours}h ago'
    days = hours // 24
    if days < 30:
        return f'{days}d ago'
    months = days // 30
    if months < 12:
        return f'{months}mo ago'
    years = days // 365
    return f'{years}y ago'
