import pytest
from src.calc import Calculator

calc = Calculator()

@pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (-4, 4**2, 12),
            (1/3, -2**4, -15.666666666666666 )
        ]
)
def test_addition(a, b, expected ):
    assert calc.sum(a,b) == expected

@pytest.mark.parametrize(
        "c, s, expected",
        [
            (2, 5, -3),
            (-9, 7**7, -823552),
            (1/2, 9.5, -9.0)
        ]

) 
def test_sub(c, s, expected):
    assert calc.subtract(c,s) == expected
    

@pytest.mark.parametrize(
        "d, k, expected",
        [
            (3, 6, 18 ),
            (-5, 5., -25.0),
            (6/3, 3**4, 162.0)
        ]
)

def test_mult(d, k, expected):
    assert calc.multiply(d,k) == expected

@pytest.mark.parametrize(
        "o, m, expected",
        [
            (4, 4, 1),
            (2.2, -6/2, -0.7333333333333334),
            (5.3**3, -91, -1.6360109890109888)
        ]
)


def test_div(o,m,expected):
    assert calc.divide(o,m) == expected
    
