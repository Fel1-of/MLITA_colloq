from .abstract import BinaryOperator
from app.utils.is_var_or_unary_operator import is_var_or_unary_operator

class Arrow(BinaryOperator):
    _symbol = '>'

    def humanize(self) -> str:
        if is_var_or_unary_operator(self.arg1):
            left = str(self.arg1.humanize())
        else:
            left = f'({self.arg1.humanize()})'
            
        if is_var_or_unary_operator(self.arg2):
            right = str(self.arg2.humanize())
        else:
            right = f'({self.arg2.humanize()})'
        
        return f'если {left}, то {right}'

    def to_implication_view(self) -> 'Arrow':
        return self.__class__(*self._args.to_implication_view())
