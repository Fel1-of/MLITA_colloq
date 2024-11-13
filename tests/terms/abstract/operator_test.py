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


def test_equal_with_equal_vars():
    v1 = Var('A')
    v2 = Var('B')
    assert Arrow(v1, v1) == Arrow(v1, v1)
    assert Arrow(v1, v1) != Arrow(v1, v2)


def test_equal_with_different_operators():
    v1 = Var('A')
    v2 = Var('B')
    assert Arrow(v1, v2) != Equal(v1, v2)
    assert Arrow(v1, v1) != Or(v1, v1)


def test_equal_with_equal_operators():
    v1 = Var('A')
    v2 = Var('B')
    v3 = Var('C')
    assert Arrow(v1, v2) == Arrow(v2, v3)
    assert Or(v1, v2) == Or(v1, v2)
    assert And(v1, v1) == And(v1, v1)


@pytest.fixture
def x():
    return Var('x')
