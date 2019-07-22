from typing import List, Generator


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


print(fib(10))


def fib_gen() -> Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt

        yield current


for _ in fib_gen():
    print(_)
    if _ > 1000:
        break
