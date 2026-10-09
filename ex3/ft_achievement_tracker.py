import random

achievements: set[str] = {'Crafting Genius', 'World Savior',
                          'Survivor', 'Master Explorer',
                          'Treasure Hunter', 'Hidden Path Finder',
                          'First Steps', 'Collector Supreme',
                          'Sharp Mind', 'Unstoppable', 'Boss Slayer',
                          'Strategist', 'Speed Runner',
                          'Collector Supreme', 'Untouchable'}


class Player:
    def __init__(self, name: str, achieves: set[str]):
        self.name: str = name.capitalize()
        self.achieves: set[str] = achieves

    def show(self) -> None:
        print(f'Player {self.name}:', self.achieves)

    def show_unique(self, others_set: set[str]) -> None:
        print(f'Only {self.name} has:',
              self.achieves.difference(others_set))

    def show_missing(self) -> None:
        print(self.name, 'is missing:',
              achievements.difference(self.achieves))


def gen_player_achievements() -> set[str]:
    count: int = random.randrange(0, len(achievements))
    return set(random.choices(tuple(achievements), k=count))


def show_players(*players: Player) -> None:
    for player in players:
        player.show()


def show_missings(*players: Player) -> None:
    for player in players:
        player.show_missing()


def get_common_achievements(*players: Player) -> set[str]:
    common: set[str] = players[0].achieves
    for player in players:
        common = common.intersection(player.achieves)
    return common


def get_all_achievements(*players: Player) -> set[str]:
    all_set: set[str] = players[0].achieves
    for player in players:
        all_set = all_set.union(player.achieves)
    return all_set


if __name__ == '__main__':
    print('== Achievement Tracker System ===', end='\n\n')
    alice: Player = Player('Alice', gen_player_achievements())
    bob: Player = Player('Bob', gen_player_achievements())
    dylan: Player = Player('Dylan', gen_player_achievements())
    tom: Player = Player('Tom', gen_player_achievements())
    show_players(alice, bob, dylan, tom)
    print('\nAll distinct achievements: ', achievements)
    print('\nCommon achievements:',
          get_common_achievements(alice, bob, dylan, tom))
    print()
    alice.show_unique(get_all_achievements(bob, dylan, tom))
    bob.show_unique(get_all_achievements(alice, dylan, tom))
    dylan.show_unique(get_all_achievements(alice, bob, tom))
    tom.show_unique(get_all_achievements(alice, bob, dylan))
    print()
    show_missings(alice, bob, dylan, tom)
