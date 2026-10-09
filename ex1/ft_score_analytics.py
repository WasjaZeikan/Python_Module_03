import sys


def print_usage() -> None:
    print('No scores provided.',
          'Usage: python3 ft_score_analytics.py <score1> <score2> ...')


def print_invalid_arg(arg: str) -> None:
    print(f"Invalid parameter: '{arg}'")


def print_stats(scores: list[int]) -> None:
    count = len(scores)
    total = sum(scores)
    high = max(scores)
    low = min(scores)
    print('Scores processed:', scores)
    print('Total players:', count)
    print('Total score:', total)
    print('Average score:', total / count)
    print('High score:', high)
    print('Low score:', low)
    print('Score range:', high - low)


if __name__ == '__main__':
    print('=== Player Score Analytics ===')
    argv: list[str] = sys.argv
    scores: list[int] = []
    for i in range(1, len(argv)):
        try:
            score: int = int(argv[i])
            scores.append(score)
        except Exception:
            print_invalid_arg(argv[i])
    if len(scores) == 0:
        print_usage()
    else:
        print_stats(scores)
