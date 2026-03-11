import pytest


def price_with_gst(price: float, rate: float) -> float:
    if price < 0 or rate < 0:
        raise ValueError("Negative values not allowed")
    return round(price * (1 + rate), 2)

@pytest.mark.parametrize(
    "price, rate, expected",
    [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 1),
        (1, 1, 2),
        (12, 0.10, 13.2)
    ]
)
def test_price_with_gst(price: float, rate: float, expected) -> float:
    print(price, rate)
    assert price_with_gst(price, rate) == expected

@pytest.mark.parametrize(
    "price, rate",
    [
        (-1, 0),
        (0, -1),
        (1, -1),
    ]
)
def test_price_with_gst_negative(price: float, rate: float) -> float:
    print(price, rate)
    with pytest.raises(ValueError):
        price_with_gst(price, rate)
    # assert price_with_gst(price, rate)



