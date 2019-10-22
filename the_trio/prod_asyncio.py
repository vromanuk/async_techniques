import datetime
import colorama
import random
import asyncio


async def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + 'App started.', flush=True)

    data = asyncio.Queue()

    task1 = asyncio.create_task(generate_data(20, data))
    task2 = asyncio.create_task(generate_data(20, data))
    task3 = asyncio.create_task(process_data(40, data))
    await task1
    await task2
    await task3

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + 'App exiting, total time: {:,.2f} sec.'.format(dt.total_seconds()), flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now()))
        print(colorama.Fore.YELLOW + f'-- generated item {idx}', flush=True)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get()
        processed += 1
        value, t = item[0], item[1]

        dt = datetime.datetime.now() - t
        print(colorama.Fore.CYAN +
              '+++ Processed value {} after {:,.2f} sec'.format(
                  value, dt.total_seconds()), flush=True)
        await asyncio.sleep(.05)


if __name__ == '__main__':
    asyncio.run(main())
