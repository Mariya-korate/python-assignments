def test_string():
    assert "worlds" not in "hello world"

def test_str_concat():
    a = "hello"
    b = "world"
    assert a+b == "helloworld"

def test_float_multi():
    a = 0.5
    b = 0.5
    assert a*b == 0.25

def test_check_float():
    value = 0.5
    assert isinstance(value, float)

def test_bool_type():
    value = False
    assert isinstance(value, bool)

def test_id_operator():
    a = 5
    b = a
    assert id(b) == id(a)
