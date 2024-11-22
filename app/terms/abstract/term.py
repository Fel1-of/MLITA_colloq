from abc import ABC, abstractmethod
from typing import Optional, Sequence
from ordered_set import OrderedSet
from string import ascii_uppercase


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
    def __hash__(self):
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
    def get_substitution_map(self, other: 'Term') -> Optional[dict[str, 'Term']]:
        """
        Returns substitution map, that convert self to other.
        None if it is impossible
        """
        pass

    @abstractmethod
    def unify(self, alphabet: Sequence[str] = ascii_uppercase) -> 'Term':
        """Unify of Term for hash and equal (rename Vars)"""
        pass

    @abstractmethod
    def vars(self) -> OrderedSet[str]:
        """Returns names of used Vars in Term"""
        pass
