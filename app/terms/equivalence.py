from .abstract import BinaryOperator
from .implication import Arrow
from .negation import Not
from app.utils import is_var_or_unary_operator


class Equal(BinaryOperator):
    _symbol = '='

    def humanize(self) -> str:
        if is_var_or_unary_operator(self.arg1):
            left = str(self.arg1.humanize())
        else:
            left = f'({self.arg1.humanize()})'

        if is_var_or_unary_operator(self.arg2):
            right = str(self.arg2.humanize())
        else:
            right = f'({self.arg2.humanize()})'
        return f'{left} эквивалентно {right}'

    def to_implication_view(self):
        return Not(
            Arrow(
                Arrow(
                    self.arg1.to_implication_view(),
                    self.arg2.to_implication_view()
                ),
                Not(
                    Arrow(
                        self.arg2.to_implication_view(),
                        self.arg1.to_implication_view()
                    )
                )
            )
        )

