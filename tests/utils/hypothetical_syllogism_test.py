from app.terms.conjunction import And
from app.terms.implication import Arrow
from app.terms.negation import Not
from app.terms.variable import Var
from app.utils.hypothetical_syllogism import hypothetical_syllogism


def test_hypothetical_syllogism_from_task():
    A = Var('A')
    B = Var('B')
    implication_1 = Arrow(A, B)
    C = Var('C')
    implication_2 = Arrow(B, C)
    outputs = hypothetical_syllogism(implication_1, implication_2)
    assert len(outputs) == 2
    assert outputs[0].output_term == Arrow(A, C)
    assert outputs[1].output_term == Arrow(A, C)


def test_hypothetical_syllogism_not_funny():
    A = Var('A')
    B = Var('B')
    implication_1 = Arrow(Not(A), Not(A))
    implication_2 = Arrow(A, Arrow(B, A))

    outputs = hypothetical_syllogism(implication_1, implication_2)
    assert len(outputs) == 1
    assert outputs[0].output_term == Arrow(Not(Var('A')), Arrow(Var('B'), Not(Var('A'))))


def test_hypothetical_syllogism_with_axioms():
    A = Var('A')
    B = Var('B')
    impl1 = Arrow(And(A, B), B)
    impl2 = Arrow(Not(A), Arrow(A, B))
    outputs = hypothetical_syllogism(impl1, impl2)
    assert len(outputs) == 1
    res = Arrow(And(Var('A'), Not(Var('B'))), Arrow(Var('B'), Var('C')))
    assert outputs[0].output_term == res
