import requests
from src.data import BASE_URL


class ApiClient:

    def __init__(self):
        self.base_url = BASE_URL

    def post(self, path, payload):
        response_raw = requests.post(url=self.base_url+path, data=payload)
        return response_raw

