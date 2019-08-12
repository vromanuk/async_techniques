import bs4
import requests
import threading
from colorama import Fore


def get_html(episode_number: int, text_html: list) -> str:
    print(Fore.YELLOW + f'Getting HTML for episode {episode_number}', flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    resp = requests.get(url)
    resp.raise_for_status()

    text_html.append((resp.text, episode_number))
    return 'Done'


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f'Getting TITLE for episode {episode_number}', flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'Missing header'
    return header.text.strip()


def main():
    get_title_range()
    print('Done')


def get_title_range():
    threads = []
    text_html = []

    for n in range(150, 160):
        threads.append(threading.Thread(target=get_html, args=(n, text_html), daemon=True))
    [t.start() for t in threads]
    [t.join() for t in threads]
    for html, episode in text_html:
        title = get_title(html, episode)
        print(Fore.WHITE + f'Title found: {title}', flush=True)


if __name__ == '__main__':
    main()
