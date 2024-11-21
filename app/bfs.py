from collections import deque
from typing import Optional

# from sortedcontainers import SortedSet
from app.utils.syllogism_result import SyllogismResult, ModusPonensResult
from app.utils.modus_ponens import modus_ponens
from app.terms import Term


def _sorting_heuristics_key(term: Term) -> int:
    return len(str(term))


def _is_target(
    ponens_res: ModusPonensResult, target_term: Term
) -> Optional[SyllogismResult]:
    term = ponens_res.output_term
    subs = term.get_substitution_map(target_term)
    if subs is None:
        return None
    return SyllogismResult(
        syllogism_name='substitute',
        input_terms=[ponens_res],
        substitution=subs,
        output_term=target_term,
    )


def _bfs(
    curr_terms: dict[Term, ModusPonensResult],
    last_terms: dict[Term, ModusPonensResult],
    target_term: Term,
) -> ModusPonensResult | SyllogismResult:
    new_terms: dict[Term, ModusPonensResult] = {}
    for old_modus in curr_terms.values():
        for last_modus in last_terms.values():
            syllogism = modus_ponens(old_modus, last_modus)
            if syllogism is None:
                continue
            new = syllogism.output_term
            if new in curr_terms:
                continue

            if new == target_term:
                return syllogism
            if new in new_terms:
                continue
            sub_result = _is_target(syllogism, target_term)
            if sub_result is not None:
                return sub_result

            new_terms[new] = syllogism

    for old_modus in curr_terms.values():
        for last_modus in last_terms.values():
            syllogism = modus_ponens(last_modus, old_modus)
            if syllogism is None:
                continue
            new = syllogism.output_term
            if new in curr_terms:
                continue

            if new == target_term:
                return syllogism
            if new in new_terms:
                continue
            sub_result = _is_target(syllogism, target_term)
            if sub_result is not None:
                return sub_result

            new_terms[new] = syllogism

    curr_terms.update(last_terms)
    return _bfs(curr_terms, new_terms, target_term)


# def _find_history_of_term(
#     term: Term,
#     result_list: list[SyllogismResult],
#     history: list[SyllogismResult],
# ):
#     for syllogism_result in result_list:
#         if term != syllogism_result.output_term:
#             continue
#         if syllogism_result in history:
#             continue
#         history.append(syllogism_result)
#         for parent in syllogism_result.input_terms:
#             _find_history_of_term(parent, result_list, history)


def bfs(
    axioms: list[Term],
    target_term: Term,
) -> list[ModusPonensResult | SyllogismResult]:

    target_term = target_term.to_implication_view()
    axioms = axioms.copy()

    input_terms = {
        axiom: SyllogismResult(
            syllogism_name='axiom',
            input_terms=[],
            output_term=axiom,
            substitutions=[],
        )
        for axiom in axioms
    }

    syllogism = _bfs(input_terms, input_terms, target_term)

    queue = deque([syllogism])
    result_list = []
    while queue:
        s = queue.popleft()
        result_list.append(s)
        print(repr(s))
        match s:
            case SyllogismResult('axiom', _, _, _):
                pass
            case SyllogismResult('substitute', [ponens_res], _):
                queue.append(ponens_res)
            case ModusPonensResult(_, _, None, None, _):
                pass
            case ModusPonensResult(_, _, premise, implication, _):
                print(repr(premise))
                queue.append(premise)
                queue.append(implication)
            case _:
                raise ValueError('DOUBLE CRINGE', s)

    result_list.reverse()
    return result_list
    # history = []
    # _find_history_of_term(target_term, reversed(result_list), history)
    # history = reversed(history)
    # return history
