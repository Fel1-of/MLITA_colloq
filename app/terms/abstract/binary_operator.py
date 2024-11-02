from app.terms.variable import Var
from .term import Term
from .operator import Operator


class BinaryOperator(Operator):
    _symbol: str

    def __init__(self, arg1: Term, arg2: Term) -> None:
        super().__init__(arg1, arg2)

    def __str__(self):
        l = str(self.arg1) if isinstance(self.arg1, Var) else f'({self.arg1})'
        r = str(self.arg2) if isinstance(self.arg2, Var) else f'({self.arg2})'
        return f'{l} {self._symbol} {r}'

    @property
    def arg1(self) -> Term:
        return self._args[0]

    @arg1.setter
    def arg1(self, value: Term) -> None:
        self._args[0] = value

    @property
    def arg2(self) -> Term:
        return self._args[1]

    @arg2.setter
    def arg2(self, value: Term) -> None:
        self._args[1] = value
