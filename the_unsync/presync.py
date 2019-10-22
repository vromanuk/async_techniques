import asyncio
import datetime
import math
import aiohttp
import requests
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def main():
    t0 = datetime.datetime.now()
    tasks = [
        asyncio.create_task(compute_some()),
        asyncio.create_task(compute_some()),
        asyncio.create_task(compute_some()),
        asyncio.create_task(download_some()),
        asyncio.create_task(download_some()),
        asyncio.create_task(download_some()),
        asyncio.create_task(download_some_more()),
        asyncio.create_task(download_some_more()),
        asyncio.create_task(wait_some()),
        asyncio.create_task(wait_some()),
        asyncio.create_task(wait_some()),
        asyncio.create_task(wait_some())]

    await asyncio.gather(*tasks)
    dt = datetime.datetime.now() - t0
    print('Asynchronous version done in {:,.2f} seconds.'.format(dt.total_seconds()))


async def compute_some():
    print('Computing...')
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


async def download_some():
    print('Downloading...')
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            text = await resp.text()
            print('Downloaded (more) {:,} characters'.format(len(text)))


async def download_some_more():
    print('Downloading more...')
    url = 'https://pythonbytes.fm./episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()
    text = resp.text
    print('Downloaded (more) {:,} characters'.format(len(text)))


async def wait_some():
    print('Waiting...')
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


if __name__ == '__main__':
    asyncio.run(main())
