from typing import Optional
from app.terms.abstract.term import Term
from app.terms.implication import Arrow
from app.terms.negation import Not
from .syllogism_result import SyllogismResult
from string import ascii_lowercase


SYLLOGISM_NAME = 'modus tollens'


def modus_tollens(implication: Arrow, premise: Not) -> Optional[SyllogismResult]:
    if not isinstance(premise, Not):
        return None

    premise = premise.unify(ascii_lowercase)
    sub_map: Optional[dict[str, Term]]
    sub_map = implication.arg2.get_substitution_map(premise.arg)

    if sub_map is None:
        return None

    output_term = Not(implication.arg1.substitute(**sub_map))
    output_term = output_term.unify()
    syllogism_result = SyllogismResult(
        syllogism_name=SYLLOGISM_NAME,
        input_terms=[implication, premise],
        substitutions=[sub_map, {}],
        output_term=output_term,
    )
    return syllogism_result
