import requests
import bs4
from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor


def main():
    urls = [
        'https://talkpython.fm',
        'https://pythonbytes.fm',
        'https://google.com',
        'https://realpython.com',
    ]

    work = []
    with PoolExecutor() as executor:
        for url in urls:
            f: Future = executor.submit(get_title, url)
            work.append(f)

        print('Waiting for downloads...', flush=True)

    print('Done', flush=True)

    for f in work:
        print('{}'.format(f.result()), flush=True)


def get_title(url: str) -> str:
    print('Getting title from {}'.format(url.replace('https://', '')), flush=True)
    resp = requests.get(url)
    resp.raise_for_status()

    html = resp.text
    soup = bs4.BeautifulSoup(html, features='html.parser')
    tag: bs4.Tag = soup.select_one('h1')

    if not tag:
        return 'None'
    if not tag.text:
        a = tag.select_one('a')
        if a and a.text:
            return a.text
        elif a and 'title' in a.attrs:
            return a.attrs['title']
        else:
            return 'None'
    return tag.get_text(strip=True)


if __name__ == '__main__':
    main()
