from app.utils.syllogism_result import SyllogismResult


def count_non_trivial_syllogisms(syllogism_list: list[SyllogismResult]) -> int:
    all_syllogisms_count = len(syllogism_list)
    trivial_syllogisms = set(['axiom', 'substitute'])
    trivial_count = len(
        [s for s in syllogism_list if s.syllogism_name in trivial_syllogisms]
    )

    non_trivial_syllogisms_count = all_syllogisms_count - trivial_count
    return non_trivial_syllogisms_count


def get_stats_str(syllogism_list: list[SyllogismResult]) -> str:
    non_trivial_count = count_non_trivial_syllogisms(syllogism_list)

    return f'Не тривиальных силлогизмов: {non_trivial_count}'
