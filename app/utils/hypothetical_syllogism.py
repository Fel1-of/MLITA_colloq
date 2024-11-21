from string import ascii_lowercase, ascii_uppercase

from app.terms.implication import Arrow
from .syllogism_result import SyllogismResult

SYLLOGISM_NAME = 'hypothetical syllogism'


def hypothetical_syllogism(
        implication_1: Arrow,
        implication_2: Arrow,
) -> list[SyllogismResult]:
    if not isinstance(implication_1, Arrow) or not isinstance(implication_2, Arrow):
        return []
    impl_1 = implication_1.unify(ascii_uppercase)
    impl_2 = implication_2.unify(ascii_uppercase)
    twin_impl_1 = implication_1.unify(ascii_lowercase)
    twin_impl_2 = implication_2.unify(ascii_lowercase)

    sub_map_2_to_1 = impl_2.arg1.get_substitution_map(twin_impl_1.arg2)
    sub_map_1_to_2 = impl_1.arg2.get_substitution_map(twin_impl_2.arg1)

    res = []
    if sub_map_2_to_1 is not None:
        output_term = Arrow(twin_impl_1.arg1, impl_2.arg2.substitute(**sub_map_2_to_1))
        output_term = output_term.unify()

        syllogism_result = SyllogismResult(
            syllogism_name=SYLLOGISM_NAME,
            input_terms=[implication_1, implication_2],
            substitutions=[{}, sub_map_2_to_1],
            output_term=output_term,
        )

        res.append(syllogism_result)

    if sub_map_1_to_2 is not None:
        output_term = Arrow(impl_1.arg1.substitute(**sub_map_1_to_2), twin_impl_2.arg2)
        output_term = output_term.unify()

        syllogism_result = SyllogismResult(
            syllogism_name=SYLLOGISM_NAME,
            input_terms=[implication_1, implication_2],
            substitutions=[{}, sub_map_1_to_2],
            output_term=output_term,
        )

        res.append(syllogism_result)

    return res
