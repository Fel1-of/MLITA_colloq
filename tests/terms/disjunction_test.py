from app.terms import Or, Var, Not


def test_str():
    assert str(Or(Var('A'), Var('B'))) == 'A | B'


def test_str_with_not():
    assert str(Or(Var('A'), Not(Var('B')))) == 'A | !B'


def test_complex_str():
    assert str(Or(Or(Var('A'), Var('B')), Var('C'))) == '(A | B) | C'


def test_repr():
    assert repr(Or(Var('A'), Var('B'))) == "Or(Var('A'), Var('B'))"


def test_humanize():
    assert Or(Var('A'), Var('B')).humanize() == 'A или B'


def test_complex_humanize():
    a = Or(Or(Var('A'), Var('B')), Or(Var('C'), Var('D')))
    assert a.humanize() == '(A или B) или (C или D)'


def test_not_humanize():
    a = Or(Not(Var('A')), Var('B'))
    assert a.humanize() == 'не A или B'


def test_to_implication_view():
    assert str(Or(Var('A'), Var('B')).to_implication_view()) == '!A > B'
