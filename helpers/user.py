import requests
import json

BASE_URL = "https://testmassproduct.d-l-s.ru/"

class User:
    def __init__(self, token=None):
        self.token = token


    def login(self):
        _response = requests.post(url=BASE_URL + 'api/Authorization', data={'username': self.username, 'password': self.password, "grantType": self.grantType})
        status_code = _response.status_code
        self.token = _response.text
        return status_code, self.token

    def getCurrentUserData(self, token):
        _response = requests.get(url=BASE_URL + 'api/v3/users/current', data={'token': token})
        currentUser = json.loads(_response.content.decode('utf-8'))
        return currentUser





