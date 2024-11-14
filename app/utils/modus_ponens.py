from typing import Optional, Callable
from functools import wraps
from app.terms.abstract.term import Term
from app.terms.implication import Arrow
from .syllogism_result import SyllogismResult
from string import ascii_lowercase


SYLLOGISM_NAME = 'modus ponens'


def _check_modus_ponens_arguments(
        modus_ponens: Callable[[Arrow, Term], Optional[SyllogismResult]]
) -> Callable[[Term, Term], Optional[SyllogismResult]]:
    @wraps(modus_ponens)
    def wrapper(term1: Term, term2: Term) -> Optional[Term]:
        if isinstance(term1, Arrow) and not isinstance(term2, Arrow):
            return modus_ponens(term1, term2)
        elif isinstance(term2, Arrow) and not isinstance(term1, Arrow):
            return modus_ponens(term2, term1)
        elif isinstance(term1, Arrow) and isinstance(term2, Arrow):
            return modus_ponens(term1, term2) or modus_ponens(term2, term1)
        else:
            return None
    return wrapper


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
