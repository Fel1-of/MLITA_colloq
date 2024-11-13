from app.terms import Var, Not, Arrow, And


def test_get_sub_map_happy_path():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), A)
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    term2 = Arrow(Arrow(And(X, Y), Not(Z)), And(X, Y))
    assert str(term1.substitute(term1.get_substitution_map(term2))) == str(term2)


def test_get_sub_map_bad_path():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), A)
    term2 = Arrow(Arrow(A, B), B)
    assert term1.get_substitution_map(term2) is None


def test_get_sub_map_var_to_term():
    A = Var('A')
    B = Var('B')
    term1 = A
    term2 = Arrow(A, B)
    assert str(term1.substitute(term1.get_substitution_map(term2))) == str(term2)


def test_get_sub_map_var_to_var():
    A = Var('A')
    B = Var('B')
    assert str(A.substitute(A.get_substitution_map(B))) == str(B)


def test_get_sub_map_var_to_itself():
    A = Var('A')
    assert A.substitute(A) == {}


def test_get_sub_map_term_to_itself():
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    term1 = Arrow(Arrow(And(X, Y), Not(Z)), And(X, Y))
    assert term1.substitute(term1) == {}


def test_get_sub_map_term_to_var():
    X = Var('X')
    Y = Var('Y')
    term1 = Arrow(X, Y)
    assert term1.get_substitution_map(X) is None
