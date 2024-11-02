from ..terms.abstract import Term, UnaryOperator
from ..terms.variable import Var


def is_var_or_unary_operator(term: Term) -> bool:
    return isinstance(term, Var) or isinstance(term, UnaryOperator)
