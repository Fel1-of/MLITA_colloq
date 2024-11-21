from app.terms import Not, Var, Or, And, Arrow
from copy import deepcopy
from string import ascii_lowercase
from functools import reduce

if __name__ == '__main__':
    a = Var('A')
    n = Not(a)

    s = deepcopy(n)

    ar = Or(a, n)
    print(ar)
    print(ar.humanize())
    print(ar.to_implication_view().to_implication_view())

    rule_input = [Var('A'), Arrow(Var('A'), Var('B'))]
    input_terms = [Var('A'), Arrow(Var('B'), Var('B'))]

    conjucted_rule_input = reduce(And, rule_input)
    alphabets = [
        [f'{i}.{j}' for j in range(len(ascii_lowercase))] for i in range(len(rule_input))
    ]
    unified = [term.unify(alphabet) for term, alphabet in zip(input_terms, alphabets)]
    print(unified)
    conjucted = reduce(And, unified)
    sub_map = conjucted_rule_input.get_substitution_map(conjucted)
    print(sub_map)
