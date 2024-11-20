from app.terms.implication import Arrow
from app.terms.variable import Var
from app.terms.disjunction import Or
from app.terms.negation import Not
from app.utils.modus_tollens import modus_tollens


def test_modus_tollens_happy_path():
    A = Var('A')
    B = Var('B')
    implication = Arrow(A, Arrow(A, B))
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    premise = Not(Arrow(Or(X, Y), Z))
    assert modus_tollens(implication, premise).output_term == Not(Or(X, Y))


def test_modus_tollens_not_funny():
    A = Var('A')
    B = Var('B')
    implication = Arrow(A, Arrow(A, B))
    premise = Not(B)
    assert modus_tollens(implication, premise) is None


def test_two_arrows():
    A = Var('A')
    B = Var('B')
    impl1 = Arrow(A, B)
    impl2 = Arrow(B, Arrow(A, B))
    assert str(modus_tollens(impl1, Not(impl2)).output_term) == '!A'
    assert str(modus_tollens(impl2, Not(impl1)).output_term) == '!A'
