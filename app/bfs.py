from typing import Optional
from sortedcontainers import SortedSet
from app.utils.syllogism_result import SyllogismResult
from app.utils.modus_ponens import modus_ponens
from app.terms import Term


def _sorting_heuristics_key(term: Term) -> int:
    return len(str(term))


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
    old_terms: SortedSet[Term],
    last_terms: SortedSet[Term],
    target_term: Term,
    result_list: list[SyllogismResult],
) -> None:
    new_terms = SortedSet(key=_sorting_heuristics_key)
    old_terms.update(last_terms)
    for old_term in old_terms:
        for last_term in last_terms:
            syllogism_result = (
                modus_ponens(old_term, last_term) or modus_ponens(last_term, old_term)
            )
            if syllogism_result is None:
                continue
            new_term = syllogism_result.output_term
            length_before = len(new_terms)
            new_terms.add(new_term)
            length_after = len(new_terms)
            if length_before == length_after:
                continue
            result_list.append(syllogism_result)
            some_target = _is_target(new_term, target_term)
            if some_target is not None:
                result_list.append(some_target)
                return
    new_terms.difference_update(old_terms)
    if new_terms:
        _bfs(old_terms, new_terms, target_term, result_list)
    else:
        if len(old_terms) == 6:
            raise ValueError('DOUBLE CRINGE')
        if target_term not in old_terms.union(new_terms):
            raise ValueError(f'CRINGE {len(old_terms)}')


def _find_history_of_term(
    term: Term, result_list: list[SyllogismResult], history: list[SyllogismResult],
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
    input_terms = SortedSet(input_terms, key=_sorting_heuristics_key)
    _bfs(input_terms, input_terms, target_term, result_list)
    return result_list
    # history = []
    # _find_history_of_term(target_term, reversed(result_list), history)
    # history = reversed(history)
    # return history
