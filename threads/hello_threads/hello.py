import time
import threading


def main():
    threads = [
        threading.Thread(target=greeter, args=('Vlad', 10), daemon=True),
        threading.Thread(target=greeter, args=('Sarah', 5), daemon=True),
        threading.Thread(target=greeter, args=('Zoe', 11), daemon=True)
    ]

    [t.start() for t in threads]

    print(2 * 2)

    [t.join() for t in threads]
    print('Done.')


def greeter(name: str, times: int):
    for _ in range(0, times):
        print(f'Hello there {name}')
        time.sleep(1)


if __name__ == '__main__':
    main()
