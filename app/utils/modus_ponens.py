from typing import Optional, Callable
from functools import wraps
from ..terms.abstract import Term
from ..terms import Arrow


def _check_modus_ponens_arguments(modus_ponens: Callable[[Arrow, Term], Optional[Term]]):
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


@_check_modus_ponens_arguments
def modus_ponens(implication: Arrow, premise: Term) -> Optional[Term]:
    implication.ar1 == premise
    implication
    pass

