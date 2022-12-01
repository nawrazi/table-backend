import bs4
import requests
from api.common.constants import *

def scrape(url, league):
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'lxml')

    data = soup.find_all('tr', class_=Site.CLASSES)

    table = []
    for row in data:
        name = (row.find('span', class_='widget-match-standings__team--full-name')).text.strip()
        team = {
            'id': str(abs(hash(name))),
            'rank': int((row.find('td')).text.strip()),
            'name': name,
            'points': int((row.find('td', class_='widget-match-standings__pts')).text.strip()),
            'goals': (row.find('td', class_='widget-match-standings__goals-diff')).text.strip(),
            'matches': int((row.find('td', class_='widget-match-standings__matches-played')).text.strip()),
            'logo': row.find('img', class_='widget-match-standings__crest')['src'].strip(),
            'leagueId': league
        }
        table.append(team)

    return {'table': table}
