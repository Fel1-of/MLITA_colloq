import pytest
from app.utils.modus_ponens import modus_ponens
from app.terms import Var, Arrow, Or

MODUS_PONENS_EXAMPLE_RES = """modus ponens
\t(A > B) > A при подстановке A: (a | b), B: c;
\t(a | b) > c
⊢ A | B"""


@pytest.mark.skip(reason='Not implemented')
def test_syllogism_result_str_complex():
    A = Var('A')
    B = Var('B')
    implication = Arrow(Arrow(A, B), A)
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    premise = Arrow(Or(X, Y), Z)
    syllogism_res = [modus_ponens(implication, premise)][0]
    assert str(syllogism_res.output_term) == MODUS_PONENS_EXAMPLE_RES
