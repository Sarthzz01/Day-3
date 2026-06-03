import pytest 
from calculator import add,sub

def test_add():
    assert add(4,5)==9
    assert add(1,2)==3

def test_sub():
    assert sub(4,2)==2
    assert sub(1,1)==0

def test_mul():
    assert mul(4,2)==8
    assert mul(1,1)==1

def test_div():
    assert div(4,2)==2
    assert div(1,1)==1