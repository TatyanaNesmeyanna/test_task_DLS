from helpers.user import User
import  pytest

def test_login(user):
    user = User("79044444444", "123123123", "password")
    status_code, user.token = user.login()
    assert status_code == 200
    currentUser = user.getCurrentUserData(user.token)
    assert (currentUser['username']==user.username)
    assert (currentUser['password']==user.username)

