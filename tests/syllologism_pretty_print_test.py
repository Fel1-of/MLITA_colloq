import pytest
from app.terms import Arrow, Var, Not
from app.bfs import bfs
from app.syllologism_pretty_print import pretty

A = Var('a')
B = Var('b')
C = Var('c')


def test_pretty(axioms):
    target = Arrow(Var('A'), Var('A'))
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, arrowed)
    pretty_result = pretty(bfs_result)
    print()
    print(pretty_result)
    assert pretty_result == ''


@pytest.fixture()
def axioms():
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    B3 = Arrow(Arrow(A, B), Arrow(Arrow(A, Not(B)), Not(A)))  # noqa: F841
    F4 = Arrow(Not(Not(A)), A)  # noqa: F841
    TT = Arrow(Not(A), Arrow(A, B))  # noqa: F841
    GA = Arrow(Arrow(Arrow(A, B), Arrow(B, C)), Arrow(A, C))  # noqa: F841
    return [A1, A2, A3]
