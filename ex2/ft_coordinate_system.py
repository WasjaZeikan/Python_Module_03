import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords_str: str = input("Enter new coordinates\
as floats in format 'x,y,z': ")
        coords: list[str | float] = coords_str.split(',')
        if len(coords) != 3:
            print('Invalid syntax')
            continue
        for i in range(len(coords)):
            try:
                coords[i] = float(coords[i].strip())
            except Exception:
                print(f"Error on parameter '{coords[i]}':",
                      f"could not convert string to float: '{coords[i]}'")
                continue
        return tuple(coords)


def calculate_distance(first: tuple[float, float, float],
                       second: tuple[float, float, float]) -> float:
    return math.sqrt((second[0]-first[0])**2
                     + (second[1]-first[1])**2
                     + (second[2]-first[2])**2)


if __name__ == '__main__':
    print('=== Game Coordinate System ===', end='\n\n')
    print('Get a first set of coordinates')
    first: tuple[float, float, float] = get_player_pos()
    print('Got a first tuple:', first)
    print(f'It includes: X={first[0]}, Y={first[1]}, Z={first[2]}')
    print('Distance to center:', calculate_distance(first, (0.0, 0.0, 0.0)))
    print('Get a second set of coordinates')
    second: tuple[float, float, float] = get_player_pos()
    print('Distance between the 2 sets of coordinates:',
          calculate_distance(first, second))
