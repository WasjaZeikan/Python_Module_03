import random


if __name__ == '__main__':
    print('== Game Data Alchemist ===')
    players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                          'Gregory', 'john', 'kevin', 'Liam']
    all_capitalized: list[str] = [name.capitalize() for name in players]
    some_capitalized: list[str] = [n for n in players if n[0].isupper()]
    scores: dict[str, int] = {k: v for k, v in [(n, random.randint(0, 1000))
                                                for n in all_capitalized]}
    avg: int = round(sum(scores.values()) / len(scores))
    high_scores: dict[str, int] = {k: v for k, v in scores.items() if v > avg}
    print('Initial list of players:', players)
    print('New list with all names capitalized:', all_capitalized)
    print('New list of capitalized names only:', some_capitalized)
    print()
    print('Score dict:', scores)
    print('Score average is', avg)
    print('High scores:', high_scores)
