from .abstract import BinaryOperator


class Arrow(BinaryOperator):
    _symbol = '>'

    def humanize(self) -> str:
        return f'не ({self.arg.humanize()})'

    def to_implication_view(self) -> 'Arrow':
        return self.__class__(*self._args.to_implication_view())
