import pytest
import myfactorial

def test_tres():
    assert myfactorial.factorial(3) == 6

def test_cero():
    assert myfactorial.factorial(0) == 1

def test_uno():
    assert myfactorial.factorial(1) == 1

def test_cuatro():
    assert myfactorial.factorial(4) == 24
