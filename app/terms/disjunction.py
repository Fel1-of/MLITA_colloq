from .abstract import BinaryOperator
from .variable import Var
from .implication import Arrow
from .negation import Not


class Or(BinaryOperator):
    _symbol = '|'

    def humanize(self) -> str:
        if isinstance(self.arg1, Var):
            left = self.arg1.humanize()
        else:
            left = f'({self.arg1.humanize()})'

        if isinstance(self.arg2, Var):
            right = self.arg2.humanize()
        else:
            right = f'({self.arg2.humanize()})'

        return f'{left} или {right}'

    def to_implication_view(self) -> 'Arrow':
        return Arrow(
            Not(self.arg1.to_implication_view()),
            self.arg2.to_implication_view()
        )
