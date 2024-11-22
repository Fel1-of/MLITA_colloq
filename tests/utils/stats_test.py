import pytest
from app.terms import Arrow, Var, Not, Or
from app.bfs import bfs
from app.utils.stats import get_stats_str

A = Var('a')
B = Var('b')
C = Var('c')


def test_stats_AA(axioms):
    target = Arrow(Var('A'), Var('A'))
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, arrowed)
    pretty_result = get_stats_str(bfs_result)
    print()
    print(pretty_result)
    s = 'Не тривиальных силлогизмов: 2'
    assert pretty_result == s


def test_stats_A11(axioms):
    target = Or(A, Not(A))
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, arrowed)
    pretty_result = get_stats_str(bfs_result)
    print()
    print(pretty_result)
    s = 'Не тривиальных силлогизмов: 2'
    assert pretty_result == s


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
