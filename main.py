from app.parser import parse
from app.bfs import bfs
from app.axioms import modus_ponens_axioms
from app.syllologism_pretty_print import pretty
from app.utils.stats import get_stats_str


def main():
    user_input = input('Введите выражение: ')
    target_expression = parse(user_input)
    bfs_result = bfs(modus_ponens_axioms, target_expression)
    pretty_str = pretty(bfs_result)
    stats_str = get_stats_str(bfs_result)
    print(pretty_str)
    print(stats_str)


if __name__ == '__main__':
    main()
