from typing import Iterable, Optional
from app.terms.abstract.term import Term
from app.terms.implication import Arrow
from .syllogism_result import SyllogismResult, ModusPonensResult
from string import ascii_lowercase


SYLLOGISM_NAME = 'modus ponens'


def modus_ponens(
    *args: Iterable[ModusPonensResult],
) -> Optional[ModusPonensResult]:
    implication_modus_result = args[0]
    premise_modus_result = args[1]
    implication = implication_modus_result.output_term
    premise = premise_modus_result.output_term

    premise = premise.unify(ascii_lowercase)
    sub_map: Optional[dict[str, Term]]
    sub_map = implication.arg1.get_substitution_map(premise)

    if sub_map is None:
        return None

    output_term = implication.arg2.substitute(**sub_map)
    output_term = output_term.unify()

    syllogism_result = ModusPonensResult(
        # syllogism_name=SYLLOGISM_NAME,
        # input_terms=[premise, implication],
        premise=premise_modus_result,
        implication=implication_modus_result,
        substitution=sub_map,
        output_term=output_term,
    )
    return syllogism_result
