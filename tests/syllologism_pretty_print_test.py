import pytest
from app.terms import Arrow, Var, Not, Or
from app.bfs import bfs
from app.syllologism_pretty_print import pretty

A = Var('a')
B = Var('b')
C = Var('c')


def test_pretty_AA(axioms):
    target = Arrow(Var('A'), Var('A'))
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, arrowed)
    pretty_result = pretty(bfs_result)
    print()
    print(pretty_result)
    s = """\
0. axiom:\t(a > (b > c)) > ((a > b) > (a > c))
1. axiom:\ta > (b > a)
2. modus ponens:
\tполучено (A > B) > (A > A)
\tиз 1=[a > (b > a)], 2=[(a > (b > c)) > ((a > b) > (a > c))]
\tподстановкой во 2 a: (A), b: (B), c: (A)
\t1=[a > (b > a)], 2=[(A > (B > A)) > ((A > B) > (A > A))]
3. axiom:\ta > (b > a)
4. modus ponens:
\tполучено A > A
\tиз 1=[a > (b > a)], 2=[(A > B) > (A > A)]
\tподстановкой во 2 a: (A), b: (B > A)
\t1=[a > (b > a)], 2=[(A > B) > (A > A)]"""
    assert pretty_result == s


def test_pretty_A11(axioms):
    target = Or(A, Not(A))
    arrowed = target.to_implication_view().unify()
    bfs_result = bfs(axioms, arrowed)
    pretty_result = pretty(bfs_result)
    print()
    print(pretty_result)
    s = """\
0. axiom:\t(a > (b > c)) > ((a > b) > (a > c))
1. axiom:\ta > (b > a)
2. modus ponens:
\tполучено (A > B) > (A > A)
\tиз 1=[a > (b > a)], 2=[(a > (b > c)) > ((a > b) > (a > c))]
\tподстановкой во 2 a: (A), b: (B), c: (A)
\t1=[a > (b > a)], 2=[(A > (B > A)) > ((A > B) > (A > A))]
3. axiom:\ta > (b > a)
4. modus ponens:
\tполучено A > A
\tиз 1=[a > (b > a)], 2=[(A > B) > (A > A)]
\tподстановкой во 2 a: (A), b: (B > A)
\t1=[a > (b > a)], 2=[(A > B) > (A > A)]
5. substitute:
\tполучено !A > !A
\tиз 1=[A > A]
\tподстановкой во 1 A: (!A)
\t1=[!A > !A]"""
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
