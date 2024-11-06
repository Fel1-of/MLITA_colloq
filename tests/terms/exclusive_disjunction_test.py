from app.terms import Xor, Var, Not


def test_str():
    assert str(Xor(Var('A'), Var('B'))) == 'A + B'


def test_str_with_not():
    assert str(Xor(Var('A'), Not(Var('B')))) == 'A + !B'


def test_humanize():
    assert Xor(Var('A'), Var('B')).humanize() == 'либо A, либо B'


def test_complex_humanize():
    ar = Xor(Xor(Var('A'), Var('B')), Xor(Var('C'), Var('D')))
    assert ar.humanize() == 'либо (либо A, либо B), либо (либо C, либо D)'


def test_not_humanize():
    ar = Xor(Not(Var('A')), Var('B'))
    assert ar.humanize() == 'либо не A, либо B'


def test_to_implication_view():
    assert (
        str(Xor(Var('A'), Var('B')).to_implication_view())
        == '!((!A > B) > !(A > !B))'
    )
