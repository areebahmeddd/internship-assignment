from core.libs.helpers import get_utc_now

def test_get_utc_now():
    now = get_utc_now()
    assert now is not None
