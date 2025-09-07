from src.utils.decorators import safe

def test_safe_default_returned():
    @safe(default=0)
    def to_int(x: str) -> int:
        return int(x)
    assert to_int("10") == 10
    assert to_int("oops") == 0

def test_safe_reraise():
    @safe(default=None, reraise=True)
    def boom():
        raise RuntimeError("x")
    try:
        boom()
        raised = False
    except RuntimeError:
        raised = True
    assert raised is True
