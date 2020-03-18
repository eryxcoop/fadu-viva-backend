import requests


class Requester:
    def call(self, url, query_params=None):
        response = requests.get(url, query_params)
        json_response = response.json()
        print(json_response)

