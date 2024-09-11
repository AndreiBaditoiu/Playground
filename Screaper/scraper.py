import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

print(res, res2)

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

super_links = links + links2
super_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)

        # Check if there are votes for the article
        if idx < len(subtext):
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        else:
            # Deal with articles without votes.
            print(f"Articolul '{title}' nu are voturi.")

    return sort_stories_by_votes(hn)


# Display articles that have at least 100 votes.
pprint.pprint(create_custom_hn(super_links, super_subtext))
