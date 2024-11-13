from app.terms import Var, Not, Arrow, And, Or, Equal, Xor


def test_unification_complex():
    varX = Var('X')
    varY = Var('Y')
    varZ = Var('Z')
    term1 = And(Equal(varZ, Xor(Or(Not(varX), Arrow(varX, varY)), varZ)), Not(varY))
    varZ = Var('Z')
    varO = Var('O')
    varV = Var('V')
    term2 = And(Equal(varV, Xor(Or(Not(varZ), Arrow(varZ, varO)), varV)), Not(varO))
    assert str(term1) != str(term2)
    assert str(term1.unification()) == str(term2.unification())
    assert str(term1.unification()) == '(A = ((!B | (B > C)) + A)) * !C'
