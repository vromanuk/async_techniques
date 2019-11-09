import math_core
import datetime
import threading
import multiprocessing


def main():
    math_core.do_math(1)

    # do_math(num=30000000)
    processor_count = multiprocessing.cpu_count()
    print('Doing math on {:,} processors.'.format(multiprocessing.cpu_count()))
    threads = []
    for n in range(1, processor_count + 1):
        threads.append(
            (threading.Thread(target=math_core.do_math, args=(300_000 * (n - 1) / processor_count,
                                                              300_000 * n / processor_count),
                              daemon=True))
        )
    t0 = datetime.datetime.now()

    [t.start() for t in threads]
    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print('Done in {:,.2f} sec.'.format(dt.total_seconds()))


# def do_math(start=0, num=10):
#     pos = start
#     k_sq = 1000 * 1000
#     while pos < num:
#         pos += 1
#         math.sqrt((pos - k_sq) * (pos - k_sq))


if __name__ == '__main__':
    main()
