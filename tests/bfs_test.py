from app.terms import Var, Arrow, Not, And
from app.bfs import bfs


def test_example():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    target = Arrow(A, A)
    assert '\n'.join(map(str, bfs([A1, A2, A3], target))) != ''


def test_example2():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    target = Arrow(And(A, B), A)
    assert '\n'.join(map(str, bfs([A1, A2, A3], target))) != ''


def test_example3():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    A1 = Arrow(A, Arrow(B, A))
    A2 = Arrow(Arrow(A, Arrow(B, C)), Arrow(Arrow(A, B), Arrow(A, C)))
    A3 = Arrow(Arrow(Not(B), Not(A)), Arrow(Arrow(Not(B), A), B))
    target = Arrow(A, Arrow(B, And(A, B)))
    assert '\n'.join(map(str, bfs([A1, A2, A3], target))) != ''
