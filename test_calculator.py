import pytest 
from calculator import add,sub

def test_add():
    assert add(4,5)==9
    assert add(1,2)==3

def test_sub():
    assert sub(4,2)==2
    assert sub(1,1)==0