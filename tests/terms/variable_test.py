from app.terms import Var
import pytest
from copy import copy, deepcopy


def test_initialization():
    v = Var('A')
    assert v.name == 'A'


def test_immutability():
    v = Var('A')
    with pytest.raises(AttributeError):
        v.name = 'B'


def test_equality():
    v1 = Var('A')
    v2 = Var('A')
    v3 = Var('B')
    assert v1 == v2
    assert v1 != v3
    assert (v1 == 'A') is False


def test_hash():
    v1 = Var('A')
    v2 = Var('A')
    v3 = Var('B')
    assert hash(v1) == hash(v2)
    assert hash(v1) != hash(v3)


def test_dict_usage():
    v1 = Var('A')
    v2 = Var('B')
    v3 = Var('A')

    d = {v1: 'Value A', v2: 'Value B'}
    assert d[v3] == 'Value A'
    assert d[v2] == 'Value B'


def test_copy():
    v = Var('A')
    v_copy = copy(v)
    v_deepcopy = deepcopy(v)
    assert v == v_copy
    assert v == v_deepcopy
    assert v is not v_copy
    assert v is not v_deepcopy


def test_str():
    v = Var('A')
    assert str(v) == 'A'


def test_humanize():
    v = Var('A')
    assert v.humanize() == 'A'


def test_substitute():
    v = Var('A')
    substitution = v.substitute(A=Var('B'), C=Var('D'))
    assert substitution == Var('B')

    no_substitution = v.substitute(C=Var('D'))
    assert no_substitution == v


def test_to_implication_view():
    v = Var('A')
    implication_view = v.to_implication_view()
    assert implication_view == v
    assert implication_view is not v
