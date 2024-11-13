from abc import ABC, abstractmethod
from ordered_set import OrderedSet


class Term(ABC):
    """Term interface (abstract class) for all logic expressions"""

    @abstractmethod
    def __str__(self) -> str:
        return ''

    @abstractmethod
    def __copy__(self) -> 'Term':
        pass

    @abstractmethod
    def __deepcopy__(self, memo) -> 'Term':
        pass

    @abstractmethod
    def humanize(self) -> str:
        """String in russian language"""
        return ''

    @abstractmethod
    def to_implication_view(self) -> 'Term':
        """Equivalent term using only implication and negation"""
        return self

    @abstractmethod
    def substitute(self, **kwargs: dict[str, 'Term']) -> 'Term':
        """Substitute an Term instead of a Var"""
        pass

    @abstractmethod
    def unify(self) -> 'Term':
        """unify of Term for hash and equal (rename Vars)"""
        pass

    @abstractmethod
    def vars(self) -> OrderedSet[str]:
        """Returns names of used Vars in Term"""
        pass
