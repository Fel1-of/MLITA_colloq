from .abstract import BinaryOperator
from .implication import Arrow
from .negation import Not
from app.utils import is_var_or_unary_operator


class Or(BinaryOperator):
    _symbol = '|'

    def humanize(self) -> str:
        if is_var_or_unary_operator(self.arg1):
            left = self.arg1.humanize()
        else:
            left = f'({self.arg1.humanize()})'

        if is_var_or_unary_operator(self.arg2):
            right = self.arg2.humanize()
        else:
            right = f'({self.arg2.humanize()})'

        return f'{left} или {right}'

    def to_implication_view(self) -> 'Arrow':
        return Arrow(
            Not(self.arg1.to_implication_view()),
            self.arg2.to_implication_view(),
        )
