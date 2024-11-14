from app.terms.implication import Arrow
from app.terms.variable import Var
from app.terms.disjunction import Or
from app.utils.modus_ponens import modus_ponens


def test_modus_ponens_happy_path():
    A = Var('A')
    B = Var('B')
    implication = Arrow(Arrow(A, B), A)
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    premise = Arrow(Or(X, Y), Z)
    assert modus_ponens(implication, premise).output_term == Or(X, Y)


def test_modus_ponens_not_funny():
    A = Var('A')
    B = Var('B')
    implication = Arrow(Arrow(A, B), A)
    premise = B
    assert modus_ponens(implication, premise) is None


def test_two_arrows():
    A = Var('A')
    B = Var('B')
    impl1 = Arrow(A, B)
    impl2 = Arrow(B, Arrow(A, B))
    assert str(modus_ponens(impl1, impl2).output_term) == 'A'
    assert str(modus_ponens(impl2, impl1).output_term) == 'A > (B > C)'
