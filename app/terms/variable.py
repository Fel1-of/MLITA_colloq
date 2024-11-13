from .abstract.term import Term
from copy import copy, deepcopy
from ordered_set import OrderedSet
from string import ascii_uppercase


class Var(Term):
    """Boolean variable class"""

    def __init__(self, char: str):
        self._name = char

    @property
    def name(self) -> str:
        """Get name of the Var. The name is read-only."""
        return self._name

    def __copy__(self) -> 'Var':
        return self.__class__(self.name)

    def __deepcopy__(self, memo):
        return copy(self)

    def __str__(self):
        return self.name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Var):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def humanize(self):
        return str(self)

    def substitute(self, **kwargs: dict[str, Term]) -> Term:
        return deepcopy(kwargs.get(self.name, self))

    def to_implication_view(self):
        return copy(self)

    def vars(self) -> OrderedSet[str]:
        return OrderedSet(self.name)

    def unification(self):
        # AGAIN, SORRY. JUST SORRY.
        return self.__class__(ascii_uppercase[0])
