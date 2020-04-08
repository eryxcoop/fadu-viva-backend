import requests


class Requester:
    def call(self, url, query_params=None):
        response = requests.get(url, query_params)
        return response.json()
