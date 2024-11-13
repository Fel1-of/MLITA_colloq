from app.terms import Var, Not, Arrow, And, Or, Equal, Xor


def test_unify_of_var():
    varX = Var('X')
    varY = Var('Y')
    varA = Var('A')
    assert varX.unify() == varY.unify()
    assert varX.unify() == varA


def test_unify_alphabet():
    term1 = Or(Var('A'), Var('B'))
    term2 = Or(Var('B'), Var('A'))
    assert str(term1.unify()) == 'A | B'
    assert str(term2.unify()) == 'A | B'


def test_unify_complex():
    varX = Var('X')
    varY = Var('Y')
    varZ = Var('Z')
    term1 = And(Equal(varZ, Xor(Or(Not(varX), Arrow(varX, varY)), varZ)), Not(varY))
    varZ = Var('Z')
    varO = Var('O')
    varV = Var('V')
    term2 = And(Equal(varV, Xor(Or(Not(varZ), Arrow(varZ, varO)), varV)), Not(varO))
    assert str(term1) != str(term2)
    assert str(term1.unify()) == str(term2.unify())
    assert str(term1.unify()) == '(A = ((!B | (B > C)) + A)) * !C'
