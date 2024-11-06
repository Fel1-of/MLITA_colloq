from app.terms import And, Var, Not


def test_str():
    assert str(And(Var('A'), Var('B'))) == 'A * B'


def test_str_with_not():
    assert str(And(Var('A'), Not(Var('B')))) == 'A * !B'


def test_complex_str():
    assert str(And(And(Var('A'), Var('B')), Var('C'))) == '(A * B) * C'


def test_humanize():
    assert And(Var('A'), Var('B')).humanize() == 'A и B'


def test_complex_humanize():
    a = And(And(Var('A'), Var('B')), And(Var('C'), Var('D')))
    assert a.humanize() == '(A и B) и (C и D)'


def test_not_humanize():
    a = And(Not(Var('A')), Var('B'))
    assert a.humanize() == 'не A и B'


def test_to_implication_view():
    assert str(And(Var('A'), Var('B')).to_implication_view()) == '!(A > !B)'
