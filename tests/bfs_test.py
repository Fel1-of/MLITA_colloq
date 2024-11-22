import pytest
from app.terms import Var, Arrow, Not, And, Or
from app.bfs import bfs

A = Var('a')
B = Var('b')
C = Var('c')


@pytest.mark.timeout(2, func_only=True)
@pytest.mark.parametrize(
    ('name', 'target'),
    [
        ('a>a', Arrow(A, A)),
        ('A11', Or(A, Not(A))),  # A11
        ('A4', Arrow(And(A, B), A)),  # A4
        ('A5', Arrow(And(A, B), B)),  # A5
        ('A6', Arrow(A, Arrow(B, And(A, B)))),  # A6
        ('A7', Arrow(A, Or(A, B))),  # A7
        ('A8', Arrow(B, Or(A, B))),  # A8
        ('A9', Arrow(Arrow(A, C), Arrow(Arrow(B, C), Arrow(Or(A, B), C)))),  # A9
        ('A10', Arrow(Not(A), Arrow(A, B))),  # A10
    ],
)
def test_modus_penis(name, target, axioms):
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, target)
    assert len(bfs_result) > 2
    assert str(bfs_result[-1].output_term.unify()) == str(arrowed)


@pytest.mark.timeout(2, func_only=True)
def test_example2(axioms):
    target = Arrow(And(A, B), A).to_implication_view().unify()
    assert str(bfs(axioms, target)[-1].output_term) == str(target)


@pytest.mark.timeout(2, func_only=True)
def test_example3(axioms):
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    target = Arrow(A, Arrow(B, And(A, B))).unify()
    assert '\n'.join(map(str, bfs([A1, A2, A3], target))) != ''


@pytest.fixture()
def axioms():
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))  # noqa: F841
    B3 = Arrow(Arrow(A, B), Arrow(Arrow(A, Not(B)), Not(A)))  # noqa: F841
    F4 = Arrow(Not(Not(A)), A)  # noqa: F841
    TT = Arrow(Not(A), Arrow(A, B))  # noqa: F841
    GA = Arrow(Arrow(Arrow(A, B), Arrow(B, C)), Arrow(A, C))  # noqa: F841
    return [A1, A2, A3]
