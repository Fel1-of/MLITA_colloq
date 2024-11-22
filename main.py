from app.parser import parse
from app.bfs import bfs
from app.axioms import modus_ponens_axioms
from app.syllologism_pretty_print import pretty
from app.utils.stats import get_stats_str
import time


def main():
    user_input = input('Введите выражение: ')
    start_time = time.perf_counter()
    try:
        target_expression = parse(user_input)
    except Exception as e:
        print('Неправильное выражение:')
        print(e)
        return
    bfs_result = bfs(modus_ponens_axioms, target_expression)
    pretty_str = pretty(bfs_result)
    stats_str = get_stats_str(bfs_result)
    total_time = time.perf_counter() - start_time
    print(f'Время выполнения: {total_time:.6f} секунд')
    print(pretty_str)
    print(stats_str)


if __name__ == '__main__':
    main()
