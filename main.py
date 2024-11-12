from app.terms import Not, Var, Or
from copy import deepcopy

if __name__ == '__main__':
    a = Var('A')
    n = Not(a)

    s = deepcopy(n)

    ar = Or(a, n)
    print(ar)
    print(ar.humanize())
    print(ar.to_implication_view().to_implication_view())
    print("Мама-ама криминал!")
