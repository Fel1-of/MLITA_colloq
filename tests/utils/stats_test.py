from app.utils.stats import get_stats_str


def test_stats_AA(AA_bfs_result):
    stats_str = get_stats_str(AA_bfs_result)
    s = 'Нетривиальных силлогизмов: 2'
    assert stats_str == s


def test_stats_A11(A11_bfs_result):
    stats_str = get_stats_str(A11_bfs_result)
    s = 'Нетривиальных силлогизмов: 2'
    assert stats_str == s
