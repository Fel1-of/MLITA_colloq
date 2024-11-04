from .term import Term
from collections import UserList
from copy import deepcopy


class TermList(UserList[Term]):
    def humanize(self) -> list[str]:
        """String in russian language"""
        return [term.humanize() for term in self.data]

    def to_implication_view(self) -> 'TermList':
        """Equivalent term using only implication and negation"""
        return TermList(term.to_implication_view() for term in self.data)

    def substitute(self, **kwargs: dict[str, 'Term']) -> 'TermList':
        return TermList(term.substitute(**kwargs) for term in self.data)


class Operator(Term):
    """Boolean function abstract class"""

    _args: TermList

    def __init__(self, *args: tuple[Term]) -> None:
        self._args = TermList()
        for arg in args:
            if not isinstance(arg, Term):
                TypeError('Operator argument must be Term or str')
            self._args.append(arg)

    def __copy__(self):
        raise NotImplementedError(
            'Operator is not copyable. Use deepcopy instead'
        )

    def __deepcopy__(self, memo) -> 'Term':
        return self.__class__(*deepcopy(self._args))

    def substitute(self, **kwargs: dict[str, 'Term']) -> Term:
        return self.__class__(*self._args.substitute(**kwargs))
