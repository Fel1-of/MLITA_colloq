from app.terms import Term
from app.terms.implication import Arrow
from app.terms.variable import Var
from app.terms.disjunction import Or
from app.utils.modus_ponens import modus_ponens
from app.utils.syllogism_result import SyllogismResult


def create_axiom(axiom: Term):
    return SyllogismResult(
        syllogism_name='axiom',
        input_terms=[],
        output_term=axiom,
        substitutions=[],
    )


def test_modus_ponens_happy_path():
    A = Var('A')
    B = Var('B')
    implication = create_axiom(Arrow(Arrow(A, B), A))
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    premise = create_axiom(Arrow(Or(X, Y), Z))
    assert len(modus_ponens(implication, premise)) == 1
    assert modus_ponens(implication, premise)[0].output_term == Or(X, Y)


def test_modus_ponens_not_funny():
    A = Var('A')
    B = Var('B')
    implication = create_axiom(Arrow(Arrow(A, B), A))
    premise = create_axiom(B)
    modus_ponens_results = modus_ponens(implication, premise)
    assert len(modus_ponens_results) == 1
    assert (modus_ponens_results[0].output_term == Var('a'))


def test_two_arrows():
    A = Var('A')
    B = Var('B')
    impl1 = create_axiom(Arrow(A, B))
    impl2 = create_axiom(Arrow(B, Arrow(A, B)))
    res1 = modus_ponens(impl1, impl2)
    assert len(res1) == 1
    res1 = res1[0]
    res2 = modus_ponens(impl2, impl1)
    assert len(res2) == 1
    res2 = res2[0]
    assert str(res1.output_term) == 'a'
    assert str(res2.output_term) == 'a > (b > c)'
