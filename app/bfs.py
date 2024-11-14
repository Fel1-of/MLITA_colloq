from typing import Optional
from ordered_set import OrderedSet
from app.utils.syllogism_result import SyllogismResult
from app.utils.modus_ponens import modus_ponens
from app.terms import Term


def _is_target(term: Term, target_term: Term) -> Optional[SyllogismResult]:
    subs = term.get_substitution_map(target_term)
    if subs is None:
        return None
    return SyllogismResult(
        syllogism_name='substitute',
        input_terms=[term],
        substitutions=[subs],
        output_term=target_term
    )


def _bfs(
    input_terms: OrderedSet[Term], target_term: Term, result_list: list[SyllogismResult],
) -> None:
    new_input_terms = input_terms.copy()
    for term1 in input_terms:
        for term2 in input_terms:
            syllogism_result = modus_ponens(term1, term2)
            if syllogism_result is None:
                continue
            new_term = syllogism_result.output_term
            length_before = len(new_input_terms)
            new_input_terms.add(new_term)
            length_after = len(new_input_terms)
            if length_before == length_after:
                continue
            result_list.append(syllogism_result)
            some_target = _is_target(new_term, target_term)
            if some_target is not None:
                result_list.append(some_target)
                return
    new_input_terms = OrderedSet(sorted(new_input_terms, key=lambda term: len(str(term))))
    _bfs(new_input_terms, target_term, result_list)


def _find_history_of_term(
    term: Term, result_list: list[SyllogismResult], history: list[SyllogismResult]
):
    for syllogism_result in result_list:
        if term != syllogism_result.output_term:
            continue
        if syllogism_result in history:
            continue
        history.append(syllogism_result)
        for parent in syllogism_result.input_terms:
            _find_history_of_term(parent, result_list, history)


def bfs(
    input_terms: list[Term], target_term: Term,
) -> list[SyllogismResult]:
    target_term = target_term.to_implication_view()
    input_terms = input_terms.copy()
    result_list = []
    for term in input_terms:
        subs = term.get_substitution_map(target_term)
        if subs is None:
            continue
        result_list.append(
            SyllogismResult(
                syllogism_name='substitute',
                input_terms=[term],
                substitutions=[subs],
                output_term=target_term
            )
        )
        return result_list
    input_terms = OrderedSet(input_terms)
    _bfs(input_terms, target_term, result_list)
    history = []
    _find_history_of_term(target_term, reversed(result_list), history)
    history = reversed(history)
    return history
