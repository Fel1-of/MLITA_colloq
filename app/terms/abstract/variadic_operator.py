from app.terms.abstract.term import Term
from .operator import Operator


class VariadicOperator(Operator):
    """Boolean functions with two or more arguments (all associative functions)
    example: conjunction, XOR)"""
    def __init__(self, *args: tuple[Term]) -> None:
        if len(args) < 2:
            raise TypeError('Variadic operator need at least 2 arguments')
        super().__init__(*args)
