from collections import UserList
from copy import deepcopy
from ordered_set import OrderedSet
from string import ascii_uppercase
from typing import Optional, Sequence
from .term import Term
from app.terms.variable import Var


class TermList(UserList[Term]):
    def humanize(self) -> list[str]:
        """String in russian language"""
        return [term.humanize() for term in self.data]

    def to_implication_view(self) -> 'TermList':
        """Equivalent term using only implication and negation"""
        return TermList(term.to_implication_view() for term in self.data)

    def substitute(self, **kwargs: dict[str, 'Term']) -> 'TermList':
        return TermList(term.substitute(**kwargs) for term in self.data)

    def vars(self) -> OrderedSet[str]:
        union_of_ordered_sets = OrderedSet()
        for term in self.data:
            union_of_ordered_sets.update(term.vars())
        return union_of_ordered_sets


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

    def __deepcopy__(self, memo) -> Term:
        return self.__class__(*deepcopy(self._args))

    def __eq__(self, other) -> bool:
        return str(self.unify()) == str(other.unify())

    def __hash__(self):
        return hash(str(self.unify()))

    def substitute(self, **kwargs: dict[str, 'Term']) -> Term:
        return self.__class__(*self._args.substitute(**kwargs))

    def get_substitution_map(self, other: 'Term') -> Optional[dict[str, 'Term']]:
        if type(self) is not type(other):
            return None

        new_substitution_map: dict[str, 'Term'] = {}
        for term1, term2 in zip(self._args, other._args):
            if isinstance(term1, Var):
                if term1.name not in new_substitution_map:
                    if isinstance(term2, Var) and term1 == term2:
                        continue
                    new_substitution_map[term1.name] = term2
                    continue
                continue
            if type(term1) is type(term2):
                local_substitute_map = term1.get_substitution_map(term2)
                if local_substitute_map is None:
                    return None
                new_substitution_map.update(local_substitute_map)
                continue
            return None
        self_substituted = self.substitute(**new_substitution_map)
        if str(self_substituted) != str(other):
            return None
        return new_substitution_map

    def vars(self) -> OrderedSet[str]:
        return self._args.vars()

    def unify(self, alphabet: Sequence[str] = ascii_uppercase) -> Term:
        vars: OrderedSet[str] = self.vars()
        # I AM VERY SORRY FOR THIS CODE. PLEASE DONT KILL ME
        # I REALLY DONT WANT TO WRITE THIS PART THAT WAY
        # IT IS SO BAD
        min_len = min(len(vars), len(alphabet))
        substitute_dict = dict(zip(vars[:min_len], map(Var, alphabet[:min_len])))
        return self.substitute(**substitute_dict)
