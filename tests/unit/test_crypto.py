import pytest
from app.utils.crypto import hash_password, verify_password, calculate_sha256, generate_api_key

def test_password_hashing():
    pwd = 'SecurePassword2026!'
    hashed = hash_password(pwd)
    assert hashed != pwd
    assert verify_password(pwd, hashed) is True
    assert verify_password('WrongPassword!', hashed) is False

def test_password_too_short():
    with pytest.raises(ValueError):
        hash_password('short')

def test_sha256_calculation():
    h = calculate_sha256('netwatch-ai')
    assert len(h) == 64

def test_api_key_generation():
    key = generate_api_key('nw_live_')
    assert key.startswith('nw_live_')
    assert len(key) > 30
