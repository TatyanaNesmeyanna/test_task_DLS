from helpers.user import User

def test_check_user_data(token):
    user = User(token)
    user_data = user.getCurrentUserData(user.token)
    assert (user_data != "Access denied!")
    assert (user_data['username'] == '79044444444')
    assert (user_data['password'] == '123123123')


