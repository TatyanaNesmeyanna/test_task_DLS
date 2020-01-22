import requests
import json
import re

BASE_URL = "https://testmassproduct.d-l-s.ru/"

class User:
    def __init__(self, username=None, email=None, phone=None):
        self.username = username
        self.email = email
        self.phone = phone


    def login(self):
        _response = requests.post(url=BASE_URL + 'api/Authorization', data={'username': self.username, 'password': self.password, "grantType": self.grantType})
        status_code = _response.status_code
        self.token = _response.text
        return status_code, self.token

    def getCurrentUserData(self, token):
        _response = requests.get(url=BASE_URL + 'api/v3/users/current', data={'token': token})
        currentUser = json.loads(_response.content.decode('utf-8'))
        self.username = currentUser['username']
        self.email = currentUser['email']
        self.phone = currentUser['phone']

    def email_is_valid(self):
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        is_valid = pattern.match(self.email)
        return is_valid


    def phone_is_valid(self):
        pattern = compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
        is_valid = pattern.match(self.phone)
        return is_valid





