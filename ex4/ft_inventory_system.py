import sys


def add_arg(inv: dict[str, int], arg: str) -> None:
    name, _, quantity = arg.partition(':')
    quantity_int: int
    if not quantity:
        print(f"Invalid parameter: '{name}'")
        return
    try:
        quantity_int = int(quantity)
    except Exception as ex:
        print(f"Quantity error for '{name}':", ex)
        return
    if name in inv:
        print(f"Reduntant item '{name}' - discarding")
        return
    inv[name] = quantity_int


def print_abundants(inv: dict[str, int]) -> None:
    items: list[tuple[str, int]] = list(inv.items())
    max_quan: int = items[0][1]
    min_quan: int = items[0][1]
    max_name: str = items[0][0]
    min_name: str = items[0][0]
    for i in range(1, len(items)):
        val: int = items[i][1]
        if val > max_quan:
            max_quan = val
            max_name = items[i][0]
        if val < min_quan:
            min_quan = val
            min_name = items[i][0]
    print(f"Item most abundant: {max_name} with quantity {max_quan}")
    print(f"Item least abundant: {min_name} with quantity {min_quan}")


def to_percent(num: float) -> float:
    return round(num * 100.0, 1)


if __name__ == '__main__':
    print('=== Inventory System Analysis ===')
    inv: dict[str, int] = {}
    for i in range(1, len(sys.argv)):
        add_arg(inv, sys.argv[i])
    total: int = sum(inv.values())
    count: int = len(inv)
    items: list[str] = list(inv.keys())
    print('Got inventory:', inv)
    print('Item list:', items)
    print(f"Total quantity of the {count} items: {total}")
    for item in items:
        print('Item', item, 'represents', f'{to_percent(inv[item] / total)}%')
    print_abundants(inv)
    inv.update(dagger=5)
    print('Updated inventory:', inv)
