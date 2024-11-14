from app.utils.modus_ponens import modus_ponens
from app.terms import Var, Arrow, Or

MODUS_PONENS_EXAMPLE_RES = """modus ponens
\t(A > B) > A при подстановке A: (a | b), B: c;
\t(a | b) > c
⊢ A | B"""


def test_syllogism_result_str_complex():
    A = Var('A')
    B = Var('B')
    implication = Arrow(Arrow(A, B), A)
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    premise = Arrow(Or(X, Y), Z)
    assert str(modus_ponens(implication, premise)) == MODUS_PONENS_EXAMPLE_RES
