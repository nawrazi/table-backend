from rest_framework.views import APIView
from rest_framework.response import Response
import bs4
import requests

class FetchTable(APIView):
    def scrape(self):
        url = 'https://www.goal.com/en/premier-league/table/2kwbbcootiqqgmrzs6o5inle5'
        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, 'lxml')

        data = soup.find_all('tr', class_=(
            'widget-match-standings__row widget-match-standings__row-- widget-match-standings__row--rank-status widget-match-standings__row--rank-status-1',
            'widget-match-standings__row widget-match-standings__row--active widget-match-standings__row--rank-status widget-match-standings__row--rank-status-2',
            'widget-match-standings__row widget-match-standings__row-- widget-match-standings__row--rank-status widget-match-standings__row--rank-status-',
            'widget-match-standings__row widget-match-standings__row--active widget-match-standings__row--rank-status widget-match-standings__row--rank-status-',
            'widget-match-standings__row widget-match-standings__row-- widget-match-standings__row--rank-status widget-match-standings__row--rank-status-relegation'
        ))

        table = []
        for row in data:
            team = {
                'rank': (row.find('td')).text.strip(),
                'name': (row.find('span', class_='widget-match-standings__team--full-name')).text.strip(),
                'pts': (row.find('td', class_='widget-match-standings__pts')).text.strip(),
                'gd': (row.find('td', class_='widget-match-standings__goals-diff')).text.strip(),
                'mp': (row.find('td', class_='widget-match-standings__matches-played')).text.strip()
            }
            table.append(team)

        return {'table': table}

    def get(self, request):
        response = {}
        try:
            data = self.scrape()
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception:
            response['status'] = 500
            response['message'] = 'Something went wrong'
            response['data'] = {}

        return Response(response)
