import bs4
import requests
from api.common.constants import *

def scrape(url):
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'lxml')

    data = soup.find_all('tr', class_=Site.CLASSES)

    table = []
    for row in data:
        team = {
            'rank': int((row.find('td')).text.strip()),
            'name': (row.find('span', class_='widget-match-standings__team--full-name')).text.strip(),
            'points': int((row.find('td', class_='widget-match-standings__pts')).text.strip()),
            'goals': (row.find('td', class_='widget-match-standings__goals-diff')).text.strip(),
            'matches': int((row.find('td', class_='widget-match-standings__matches-played')).text.strip()),
            'logo': row.find('img', class_='widget-match-standings__crest')['src'].strip()
        }
        table.append(team)

    return {'table': table}
