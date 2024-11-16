from app.terms import Var, Not, Arrow, And, Or


def test_get_sub_map_happy_path():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), A)
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    term2 = Arrow(Arrow(And(X, Y), Not(Z)), And(X, Y))
    subs_dict = term1.get_substitution_map(term2)
    assert subs_dict == {'A': And(X, Y), 'B': Not(Z)}
    assert str(term1.substitute(**subs_dict)) == str(term2)


def test_get_sub_map_bad_path():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), A)
    term2 = Arrow(Arrow(A, B), B)
    assert term1.get_substitution_map(term2) is None


def test_get_sub_map_nested_bad():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), Arrow(Arrow(A, B), A))
    term2 = Arrow(Arrow(A, B), Arrow(Arrow(A, B), B))
    assert term1.get_substitution_map(term2) is None


def test_get_sub_map_different_nested_bad():
    A = Var('A')
    B = Var('B')
    term1 = Arrow(Arrow(A, B), Arrow(Arrow(A, B), A))
    term2 = Arrow(Arrow(A, B), Arrow(Or(A, B), A))
    assert term1.get_substitution_map(term2) is None


def test_get_sub_map_var_to_term():
    A = Var('A')
    B = Var('B')
    term1 = A
    term2 = Arrow(A, B)
    subs_dict = term1.get_substitution_map(term2)
    assert subs_dict == {'A': Arrow(A, B)}
    assert str(term1.substitute(**subs_dict)) == str(term2)


def test_get_sub_map_var_to_var():
    A = Var('A')
    B = Var('B')
    assert A.get_substitution_map(B) == {'A': B}


def test_get_sub_map_var_to_itself():
    A = Var('A')
    assert A.get_substitution_map(A) == {}


def test_get_sub_map_term_to_itself():
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    term1 = Arrow(Arrow(And(X, Y), Not(Z)), And(X, Y))
    assert term1.get_substitution_map(term1) == {}


def test_get_substitution_map_on_not():
    A = Var('A')
    B = Var('B')
    not_A = Not(A)
    not_B = Not(B)

    assert not_A.get_substitution_map(not_B) == {'A': B}


def test_get_substitution_map_on_arrow():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    D = Var('D')
    arrow1 = Arrow(A, B)
    arrow2 = Arrow(C, D)

    assert arrow1.get_substitution_map(arrow2) == {'A': C, 'B': D}


def test_get_substitution_map_on_complex_left():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    D = Var('D')
    arrow1 = Arrow(A, B)
    arrow2 = Arrow(Arrow(C, D), C)

    assert arrow1.get_substitution_map(arrow2) == {'A': Arrow(C, D), 'B': C}


def test_get_substitution_map_on_complex_right():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    D = Var('D')
    arrow1 = Arrow(A, B)
    arrow2 = Arrow(B, Arrow(C, D))

    assert arrow1.get_substitution_map(arrow2) == {'A': B, 'B': Arrow(C, D)}


def test_get_substitution_map_on_complex_both_side():
    A = Var('A')
    B = Var('B')
    C = Var('C')
    D = Var('D')
    arrow1 = Arrow(A, B)
    arrow2 = Arrow(Arrow(A, B), Arrow(C, D))

    assert arrow1.get_substitution_map(arrow2) == {
        'A': Arrow(A, B),
        'B': Arrow(C, D),
    }
