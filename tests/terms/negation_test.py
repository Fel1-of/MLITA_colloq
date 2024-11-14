from app.terms import Not, Var, Or


def test_str():
    assert str(Not(Var('A'))) == '!A'


def test_double_str():
    assert str(Not(Not(Var('A')))) == '!!A'


def test_complex_str():
    assert str(Not(Or(Var('A'), Var('B')))) == '!(A | B)'


def test_repr():
    assert repr(Not(Var('A'))) == "Not(Var('A'))"


def test_repr_double():
    assert repr(Not(Not(Var('A')))) == "Not(Not(Var('A')))"


def test_repr_complex():
    assert repr(Not(Or(Var('A'), Var('B')))) == "Not(Or(Var('A'), Var('B')))"


def test_humanize():
    assert Not(Var('A')).humanize() == 'не A'


def test_complex_humanize():
    assert Not(Not(Var('A'))).humanize() == 'не (не A)'


def test_complex_humanize_2():
    assert Not(Or(Var('A'), Var('B'))).humanize() == 'не (A или B)'


def test_to_implication_view():
    assert str(Not(Var('A')).to_implication_view()) == '!A'
