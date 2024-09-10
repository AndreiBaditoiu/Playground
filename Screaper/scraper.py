import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)

        # Verificăm dacă există voturi pentru acest articol
        if idx < len(subtext):
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        else:
            # Tratează articolele fără voturi (de exemplu, poți decide să le ignori)
            print(f"Articolul '{title}' nu are voturi.")

    return sort_stories_by_votes(hn)


# Afișează articolele cu minim 100 de voturi
pprint.pprint(create_custom_hn(links, subtext))
