from app.terms import Arrow, Var, Not


def test_str():
    assert str(Arrow(Var('A'), Var('B'))) == 'A > B'


def test_str_with_not():
    assert str(Arrow(Var('A'), Not(Var('B')))) == 'A > !B'


def test_humanize():
    assert Arrow(Var('A'), Var('B')).humanize() == 'если A, то B'


def test_not_humanize():
    ar = Arrow(Not(Var('A')), Var('B'))
    assert ar.humanize() == 'если не A, то B'


def test_complex_humanize():
    ar = Arrow(Arrow(Var('A'), Var('B')), Arrow(Var('C'), Var('D')))
    assert ar.humanize() == 'если (если A, то B), то (если C, то D)'


def test_to_implication_view():
    assert str(Arrow(Var('A'), Var('B')).to_implication_view()) == 'A > B'
