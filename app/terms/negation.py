from app.utils import is_var_or_unary_operator
from .abstract.unary_operator import UnaryOperator
from .variable import Var


class Not(UnaryOperator):
    def __str__(self) -> str:
        if is_var_or_unary_operator(self.arg):
            return f'!{self.arg}'
        return f'!({self.arg})'

    def humanize(self):
        if isinstance(self.arg, Var):
            return f'не {self.arg.humanize()}'
        return f'не ({self.arg.humanize()})'

    def to_implication_view(self) -> 'Not':
        return self.__class__(*self._args.to_implication_view())
