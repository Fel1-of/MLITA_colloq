import pytest
from app.terms import Var, Arrow, Not, And, Or
from app.bfs import bfs

A = Var('A')
B = Var('B')
C = Var('C')


def test_example(axioms):
    target = Arrow(A, A)
    assert str(bfs(axioms, target)[-1].output_term) == str(target)


def test_example2(axioms):
    target = Arrow(And(A, B), A).to_implication_view()
    assert target == ""
    assert str(bfs(axioms, target)[-1].output_term) == str(target)


def test_example3(axioms):
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    target = Arrow(A, Arrow(B, And(A, B)))
    assert '\n'.join(map(str, bfs([A1, A2, A3], target))) != ''


@pytest.mark.timeout(30)
@pytest.mark.parametrize(
    ('name', 'target'),
    [
        ('a>a', Arrow(A, A)),
        ('A4', Arrow(And(A, B), A)),  # A4
        ('A5', Arrow(And(A, B), B)),  # A5
        ('A6', Arrow(A, Arrow(B, And(A, B)))),  # A6
        ('A7', Arrow(A, Or(A, B))),  # A7
        ('A8', Arrow(B, Or(A, B))),  # A8
        ('A9', Arrow(Arrow(A, C), Arrow(Arrow(B, C), Arrow(Or(A, B), C)))),  # A9
        ('A10', Arrow(Not(A), Arrow(A, B))),  # A10
        ('A11', Or(A, Not(A))),  # A11
    ],
)
def test_modus_penis(name, target, axioms):
    assert str(bfs(axioms, target)[-1].output_term) == str(target)


@pytest.fixture()
def axioms():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    B3 = Arrow(Arrow(A, B), Arrow(Arrow(A, Not(B)), Not(A)))
    F4 = Arrow(Not(Not(A)), A)
    TT = Arrow(Not(A), Arrow(A, B))
    return [A1, A2, B3, TT]
