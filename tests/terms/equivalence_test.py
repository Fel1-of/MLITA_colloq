from app.terms import Equal, Var


def test_str():
    assert str(Equal(Var('A'), Var('B'))) == 'A = B'


def test_humanize():
    assert Equal(Var('A'), Var('B')).humanize() == 'A эквивалентно B'


def test_complex_humanize():
    ar = Equal(Equal(Var('A'), Var('B')), Equal(Var('C'), Var('D')))
    assert ar.humanize() \
           == '(A эквивалентно B) эквивалентно (C эквивалентно D)'


def test_to_implication_view():
    assert str(Equal(Var('A'), Var('B')).to_implication_view()) \
           == '!((A > B) > !(B > A))'
