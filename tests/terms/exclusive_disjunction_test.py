from app.terms import Xor, Var


def test_str():
    assert str(Xor(Var('A'), Var('B'))) == 'A + B'


def test_humanize():
    assert Xor(Var('A'), Var('B')).humanize() == 'либо A, либо B'


def test_complex_humanize():
    ar = Xor(Xor(Var('A'), Var('B')), Xor(Var('C'), Var('D')))
    assert ar.humanize() \
           == 'либо (либо A, либо B), либо (либо C, либо D)'


def test_to_implication_view():
    assert str(Xor(Var('A'), Var('B')).to_implication_view()) \
           == '!((!A > B) > !(A > !B))'
