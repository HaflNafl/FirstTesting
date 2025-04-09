from src.calc import Calculator

calc = Calculator()

def test_addition():
    assert calc.sum(2,2) == 4
    assert calc.sum(2.1, 2.1) == 4.2
    assert calc.sum(2/1,2) == 4
    assert calc.sum(-2,-2) == -4
    assert calc.sum(8.9,2) == 10.9
    assert calc.sum(-2,2) == 0
    assert calc.sum(2**2,2) == 6
    assert calc.sum(2/9,2/3) == 0.8888888888888888
    
def test_sub():
    assert calc.subtract(2,2) == 0
    assert calc.subtract(2.1,2.1) == 0
    assert calc.subtract(2/1,2/1) == 0
    assert calc.subtract(2**3,2**3) == 0
    assert calc.subtract(1.2,1.2) == 0
    assert calc.subtract(0/9,0/9) == 0
    
def test_mult():
    assert calc.multiply(2,2) == 4
    assert calc.multiply(1/1,2) == 2.0
    assert calc.multiply(2**2, 45**1) == 180
    assert calc.multiply(-2, -1/2) == 1
    assert calc.multiply(-3**1,-2.4) == 7.199999999999999
    assert calc.multiply(7/1, -2.3**3) == -85.16899999999998

def test_div():
    assert calc.divide(2,2) == 1
    assert calc.divide(2.1,2/2) == 2.1
    assert calc.divide(-2,-1.2) == 1.6666666666666667
    assert calc.divide(5**2,-2) == -12.5
    assert calc.divide(2/2,2.0) == 0.5
    assert calc.divide(2**7,-9.4**3/6) == -0.9246506072835499
    
