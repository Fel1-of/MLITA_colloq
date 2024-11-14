from typing import Optional
from app.terms.abstract.term import Term
from app.terms.implication import Arrow
from .syllogism_result import SyllogismResult
from string import ascii_lowercase


SYLLOGISM_NAME = 'modus ponens'


def modus_ponens(implication: Arrow, premise: Term) -> Optional[SyllogismResult]:
    premise = premise.unify(ascii_lowercase)
    sub_map: Optional[dict[str, Term]]
    sub_map = implication.arg1.get_substitution_map(premise)

    if sub_map is None:
        return None

    output_term = implication.arg2.substitute(**sub_map)
    output_term = output_term.unify()
    syllogism_result = SyllogismResult(
        syllogism_name=SYLLOGISM_NAME,
        input_terms=[implication, premise],
        substitutions=[sub_map, {}],
        output_term=output_term,
    )
    return syllogism_result
