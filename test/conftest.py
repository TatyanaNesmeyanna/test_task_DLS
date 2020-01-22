import json
import requests
import pytest
from helpers.session import Session


BASE_URL = "https://testmassproduct.d-l-s.ru/"

@pytest.fixture(scope='session')
def session():
    _response = requests.post(url=BASE_URL + 'api/Authorization', data={'username': '79044444444', 'password': '123123123', 'grantType': 'password'})
    assert _response.status_code == 200
    decoded_response = json.loads(_response.content.decode('utf-8'))
    # getting a refresh-token
    refresh_token = decoded_response['refresh_token']
    assert refresh_token is not None
    # getting a access-token
    access_token = decoded_response['access_token']
    assert access_token is not None
    _session = Session(access_token)
    return _session

