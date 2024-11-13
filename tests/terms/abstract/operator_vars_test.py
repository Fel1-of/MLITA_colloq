from ordered_set import OrderedSet
from app.terms import Var, Not, Arrow, And, Or, Equal, Xor


def test_vars_complex():
    varZ = Var('Z')
    varO = Var('O')
    varV = Var('V')
    term2 = And(Equal(varV, Xor(Or(Not(varZ), Arrow(varZ, varO)), varV)), Not(varO))
    assert term2.vars() == OrderedSet(['V', 'Z', 'O'])
