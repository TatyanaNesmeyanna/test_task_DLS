import requests
import json
import re

BASE_URL = "https://testmassproduct.d-l-s.ru/"

class User:
    def __init__(self, login=None, firstname=None, lastname=None, patronymic=None, email=None, phone=None):
        self.login = login
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic
        self.email = email
        self.phone = phone


    def login_(self):
        response = requests.post(url=BASE_URL + 'api/Authorization', data={'username': self.username, 'password': self.password, "grantType": self.grantType})
        status_code = response.status_code
        self.token = response.text
        return status_code, self.token

    def get_current_user_data(self, token):
        response = requests.get(url=BASE_URL + 'api/v3/users/current', headers={'Authorization': 'Bearer ' + token})
        currentUser = json.loads(response.content.decode('utf-8'))
        self.login = currentUser['login']
        self.firstname = currentUser['firstName']
        self.lastname = currentUser['lastName']
        self.patronymic = currentUser['patronymic']
        self.email = currentUser['email']
        self.phone = currentUser['fullPhoneNumber']

    def email_is_valid(self):
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        is_valid = pattern.match(self.email)
        return is_valid

    def phone_is_valid(self):
        pattern = compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
        is_valid = pattern.match(self.phone)
        return is_valid





