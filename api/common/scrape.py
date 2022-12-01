import bs4
import requests
from api.common.constants import *

def scrape(url, league):
    html = requests.get(url).text
    soup = bs4.BeautifulSoup(html, 'lxml')
    data = soup.find_all('tr')

    table = []
    for row in data[1:]:
        cols = row.find_all('td')
        name = row.find('a', class_='team-name__long').text.strip()
        team = {
            'id': str(abs(hash(name))),
            'rank': int(row.find('td', class_='table-column--sub').text.strip()),
            'name': name,
            'points': int(row.find('b').text.strip()),
            'goals': cols[8].text.strip(),
            'matches': int(cols[2].text.strip()),
            'logo': row.find('img', class_='team-crest')['src'].strip(),
            'leagueId': league
        }
        table.append(team)

    return {'table': table}
