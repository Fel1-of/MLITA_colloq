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
    input_terms: list[Term] = field(default_factory=list)
    substitutions: list[dict[str, Term]] = field(default_factory=list)
    output_term: Optional[Term] = None

    def __str__(self):
        subs_strs = map(substitution_to_str, self.substitutions)
        inp = '\t' + ';\n\t'.join(
            term_with_subs(term, subs) for term, subs in zip(self.input_terms, subs_strs)
        )
        out = f'⊢ {self.output_term}'
        return '\n'.join([self.syllogism_name, inp, out])
