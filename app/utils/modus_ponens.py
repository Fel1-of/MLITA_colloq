from .syllogism_result import ModusPonensResult
from app.terms import Arrow
from string import ascii_lowercase, ascii_uppercase

SYLLOGISM_NAME = 'modus ponens'


def modus_ponens(
    *args: ModusPonensResult,
) -> list[ModusPonensResult]:
    implication_modus_result = args[0]
    premise_modus_result = args[1]
    implication = implication_modus_result.output_term
    premise = premise_modus_result.output_term

    syllogism_results_list = []

    if not isinstance(implication, Arrow):
        return []

    premise = premise.unify(ascii_lowercase)
    implication = implication.unify(ascii_lowercase)

    premise_twin = premise.unify(ascii_uppercase)
    implication_twin = implication.unify(ascii_uppercase)

    sub_map1 = implication.arg1.get_substitution_map(premise_twin)

    if sub_map1 is not None:
        output_term = implication.arg2.substitute(**sub_map1)
        output_term = output_term.unify()

        syllogism_result1 = ModusPonensResult(
            premise=premise_modus_result,
            implication=implication_modus_result,
            substitution_impl=sub_map1,
            output_term=output_term,
        )
        syllogism_results_list.append(syllogism_result1)

    sub_map2 = premise.get_substitution_map(implication_twin.arg1)

    if sub_map2 is not None:
        output_term = implication.arg2
        output_term = output_term.unify()

        syllogism_result2 = ModusPonensResult(
            premise=premise_modus_result,
            implication=implication_modus_result,
            substitution_premise=sub_map2,
            output_term=output_term,
        )
        syllogism_results_list.append(syllogism_result2)

    return syllogism_results_list
