""" Test division """
import pytest
from app.div import div

def test_div():
    """ Test division """
    assert div(vala=10, valb=2) == 5

def test_divide_zero_exception():
    """ Test division by zero exception """
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
