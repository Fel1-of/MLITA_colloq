from typing import Callable, Optional

from string import ascii_lowercase
from functools import reduce
from terms import Term, And
from .syllogism_result import SyllogismResult


def construct_syllogism(
        rule_name: str, rule_input: list[Term], rule_output: Term
) -> Callable:
    if not rule_input:
        raise ValueError('Empty input list for syllogism')
    conjucted_rule_input = reduce(And, rule_input)
    alphabets = [
        [f'{i}.{j}' for j in range(len(ascii_lowercase))] for i in range(len(rule_input))
    ]

    def syllogism(input: list[SyllogismResult]) -> Optional[SyllogismResult]:
        if len(input) != len(rule_input):
            return None
        input_terms = [syllogism.output_term for syllogism in input]
        unified = [term.unify(alphabet) for term, alphabet in zip(input_terms, alphabets)]
        conjucted = reduce(And, unified)
        sub_map = conjucted_rule_input.get_substitution_map(conjucted)
        if not sub_map:
            return None
        output = rule_output.unify(ascii_lowercase)
        result = SyllogismResult(
            syllogism_name=rule_name,
            input_terms=input,
            substitutions=[{} for i in range(len())],
            output_term=output,
        )
        return result
    syllogism.n = len(rule_input)
    return syllogism