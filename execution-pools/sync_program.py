import requests
import bs4


def main():
    urls = [
        'https://talkpython.fm',
        'https://pythonbytes.fm',
        'https://google.com',
        'https://realpython.com',
    ]

    for url in urls:
        print('Getting title from {}'.format(url.replace('https', '')), end='... ', flush=True)
        title = get_title(url)
        print('{}'.format(title), flush=True)

    print('Done', flush=True)


def get_title(url: str) -> str:
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
