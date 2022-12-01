from rest_framework.views import APIView
from rest_framework.response import Response
from api.common.scrape import *

class PremierLeague(APIView):
    def get(self, request):
        response = {}
        try:
            data = scrape(Url.PREMIER_LEAGUE, 1)
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception as e:
            response['status'] = 500
            response['message'] = f'Something went wrong: {e}'
            response['data'] = {}

        return Response(response)

class Championship(APIView):
    def get(self, request):
        response = {}
        try:
            data = scrape(Url.CHAMPIONSHIP, 2)
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception as e:
            response['status'] = 500
            response['message'] = f'Something went wrong: {e}'
            response['data'] = {}

        return Response(response)

class LaLiga(APIView):
    def get(self, request):
        response = {}
        try:
            data = scrape(Url.LA_LIGA, 3)
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception as e:
            response['status'] = 500
            response['message'] = f'Something went wrong: {e}'
            response['data'] = {}

        return Response(response)

class Bundesliga(APIView):
    def get(self, request):
        response = {}
        try:
            data = scrape(Url.BUNDESLIGA, 4)
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception as e:
            response['status'] = 500
            response['message'] = f'Something went wrong: {e}'
            response['data'] = {}

        return Response(response)

class League1(APIView):
    def get(self, request):
        response = {}
        try:
            data = scrape(Url.LEAGUE_1, 5)
            response['status'] = 200
            response['message'] = 'Successfully retrieved'
            response['data'] = data

        except Exception as e:
            response['status'] = 500
            response['message'] = f'Something went wrong: {e}'
            response['data'] = {}

        return Response(response)
