from ..terms.abstract import Term
from typing import Optional
from dataclasses import dataclass, field
from app.utils import is_var_or_unary_operator


def bracked_term(term: Term):
    if is_var_or_unary_operator(term):
        return str(term)
    return f'({term})'


def substitution_to_str(sub: dict) -> str:
    return ', '.join(f'{var}: {bracked_term(term)}' for var, term in sub.items())


def term_with_subs(term: Term, subs_str: str):
    if subs_str:
        return f'{term} при подстановке {subs_str}'
    else:
        return str(term)


@dataclass
class SyllogismResult:
    syllogism_name: str = ''
    input_terms: list['SyllogismResult'] = field(default_factory=list)
    substitutions: dict[str, Term] = field(default_factory=dict)
    output_term: Optional[Term] = None

    # def __str__(self):
    #     subs_strs = map(substitution_to_str, self.substitutions)
    #     inp = '\t' + ';\n\t'.join(
    #         term_with_subs(term, subs) for term, subs in zip(self.input_terms, subs_strs)
    #     )
    #     out = f'⊢ {self.output_term}'
    #     return '\n'.join([self.syllogism_name, inp, out])


@dataclass
class ModusPonensResult(SyllogismResult):
    def __init__(
        self,
        output_term: Term,
        premise: Optional['ModusPonensResult'],
        implication: Optional['ModusPonensResult'],
        substitution_impl: Optional[dict[str, Term]] = None,
        substitution_premise: Optional[dict[str, Term]] = None,
    ) -> None:
        syllogism_name: str = 'modus ponens'
        if substitution_impl is None:
            substitution_impl = {}
        if substitution_premise is None:
            substitution_premise = {}

        super().__init__(
            syllogism_name,
            [premise, implication],
            [substitution_premise, substitution_impl],
            output_term,
        )
        output_term: Term
        premise: Optional['ModusPonensResult'] = None
        implication: Optional['ModusPonensResult'] = None
        substitution_impl: dict[str, Term] = field(default_factory=dict)

    @property
    def premise(self) -> 'ModusPonensResult':
        return self.input_terms[0]

    @premise.setter
    def premise(self, value: 'ModusPonensResult') -> None:
        self.input_terms[0] = value

    @property
    def implication(self) -> 'ModusPonensResult':
        return self.input_terms[1]

    @implication.setter
    def implication(self, value: 'ModusPonensResult') -> None:
        self.input_terms[1] = value

    @property
    def substitution_premise(self) -> dict[str, Term]:
        return self.output_term[0]

    @substitution_premise.setter
    def substitution_premise(self, value: dict[str, Term]) -> None:
        self.output_term[0] = value

    @property
    def substitution_impl(self) -> dict[str, Term]:
        return self.output_term[1]

    @substitution_impl.setter
    def substitution_impl(self, value: dict[str, Term]) -> None:
        self.output_term[1] = value
