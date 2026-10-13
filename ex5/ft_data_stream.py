import random
import typing

names: list[str] = ['Alice', 'Bob', 'Tom', 'Dylan', 'Mark', 'Jose']
actions: list[str] = ['sleep', 'walk', 'eat', 'run', 'move', 'climb', 'read',
                      'write', 'swim', 'grab', 'release', 'drink', 'talk']


def gen_event() -> typing.Generator[tuple[str, str]]:
    while True:
        yield (random.choice(names), random.choice(actions))


def show_event(event_num: int, event: tuple[str, str]) -> None:
    name: str = event[0]
    action: str = event[1]
    print(f"Event {event_num}: Player {name} did action {action}")


def consume_event(events: list[tuple[str, str]])\
                  -> typing.Generator[tuple[str, str]]:
    while events:
        elem: tuple[str, str] = random.choice(events)
        events.remove(elem)
        yield elem


if __name__ == '__main__':
    print('=== Game Data Stream Processor ===')
    gen: typing.Generator[tuple[str, str]] = gen_event()
    for i in range(1000):
        show_event(i, next(gen))
    events: list[tuple[str, str]] = [next(gen) for _ in range(10)]
    print('Built list of 10 events: ', events)
    for event in consume_event(events):
        print('Got event from list:', event)
        print('Remains in list:', events)
