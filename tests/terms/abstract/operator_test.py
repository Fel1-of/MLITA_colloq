import pytest
from copy import copy
from app.terms import Or, And, Not, Equal, Arrow, Xor, Var


def test_copy_is_not_implemented_or(x):
    with pytest.raises(NotImplementedError):
        copy(Or(x, x))


def test_copy_is_not_implemented_and(x):
    with pytest.raises(NotImplementedError):
        copy(And(x, x))


def test_copy_is_not_implemented_not(x):
    with pytest.raises(NotImplementedError):
        copy(Not(x))


def test_copy_is_not_implemented_equal(x):
    with pytest.raises(NotImplementedError):
        copy(Equal(x, x))


def test_copy_is_not_implemented_arrow(x):
    with pytest.raises(NotImplementedError):
        copy(Arrow(x, x))


def test_copy_is_not_implemented_xor(x):
    with pytest.raises(NotImplementedError):
        copy(Xor(x, x))


@pytest.fixture
def x():
    return Var('x')
