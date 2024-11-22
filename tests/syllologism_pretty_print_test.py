from app.syllologism_pretty_print import pretty


def test_pretty_AA(AA_bfs_result):
    pretty_result = pretty(AA_bfs_result)
    s = """\
0. axiom:\t(a > (b > c)) > ((a > b) > (a > c))
1. axiom:\ta > (b > a)
2. modus ponens:
\tполучено (a > b) > (a > a)
\tиз 1=[a > (b > a)], 2=[(a > (b > c)) > ((a > b) > (a > c))]
\tподстановкой во 2 a: (a), b: (b), c: (a)
\t1=[a > (b > a)], 2=[(a > (b > a)) > ((a > b) > (a > a))]
3. axiom:\ta > (b > a)
4. modus ponens:
\tполучено a > a
\tиз 1=[a > (b > a)], 2=[(a > b) > (a > a)]
\tподстановкой во 2 a: (a), b: (b > a)
\t1=[a > (b > a)], 2=[(a > (b > a)) > (a > a)]"""
    assert pretty_result == s


def test_pretty_A11(A11_bfs_result):
    pretty_result = pretty(A11_bfs_result)
    s = """\
0. axiom:\t(a > (b > c)) > ((a > b) > (a > c))
1. axiom:\ta > (b > a)
2. modus ponens:
\tполучено (a > b) > (a > a)
\tиз 1=[a > (b > a)], 2=[(a > (b > c)) > ((a > b) > (a > c))]
\tподстановкой во 2 a: (a), b: (b), c: (a)
\t1=[a > (b > a)], 2=[(a > (b > a)) > ((a > b) > (a > a))]
3. axiom:\ta > (b > a)
4. modus ponens:
\tполучено a > a
\tиз 1=[a > (b > a)], 2=[(a > b) > (a > a)]
\tподстановкой во 2 a: (a), b: (b > a)
\t1=[a > (b > a)], 2=[(a > (b > a)) > (a > a)]
5. substitute:
\tполучено !a > !a
\tиз 1=[a > a]
\tподстановкой во 1 a: (!a)
\t1=[a > a]"""
    assert pretty_result == s
