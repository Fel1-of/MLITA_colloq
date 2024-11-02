from app.terms import Or, Var


def test_str():
    assert str(Or(Var("A"), Var("B"))) == "A | B"


def test_complex_str():
    assert str(Or(Or(Var("A"), Var("B")), Var("C"))) == "(A | B) | C"


def test_humanize():
    assert Or(Var("A"), Var("B")).humanize() == "A или B"


def test_complex_humanize():
    a = Or(Or(Var("A"), Var("B")), Or(Var("C"), Var("D")))
    assert a.humanize() == "(A или B) или (C или D)"


def test_to_implication_view():
    assert str(Or(Var("A"), Var("B")).to_implication_view()) == "!A > B"
