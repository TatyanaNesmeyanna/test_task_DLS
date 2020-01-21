import requests
import json

BASE_URL = "https://testmassproduct.d-l-s.ru/"

class User:
    def __init__(self, username, password, grantType):
        self.username = username
        self.password = password
        self.grantType = grantType

    def login(self):
        payload = {'username': self.username, 'password': self.password, "grantType": self.grantType}
        _response = requests.post(url=BASE_URL + 'api/Authorization', data=payload)
        status_code = _response.status_code
        self.token = _response.text
        return status_code, self.token

    def getCurrentUserData(self, token):
        payload = {'token': token}
        _response = requests.get(url=BASE_URL + 'api/v3/users/current', data=payload)
        currentUser = json.loads(_response.content.decode('utf-8'))
        return currentUser





