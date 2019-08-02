from typing import List, Generator


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


def fib_gen() -> Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt

        yield current


if __name__ == '__main__':
    MAX_ELEMENTS = 1000
    print(fib(10))
    for _ in fib_gen():
        print(_)
        if _ > MAX_ELEMENTS:
            break
