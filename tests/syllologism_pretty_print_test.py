from app.syllologism_pretty_print import pretty


def test_pretty_AA(AA_bfs_result):
    pretty_result = pretty(AA_bfs_result)
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


def test_pretty_A11(A11_bfs_result):
    pretty_result = pretty(A11_bfs_result)
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
