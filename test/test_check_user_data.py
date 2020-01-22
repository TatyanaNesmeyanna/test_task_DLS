from helpers.user import User


def test_check_user_data(session):
    user = User()
    user.getCurrentUserData(session.token)
    assert (user.username == '79044444444')
    assert (user.password == '123123123')
    assert (user.email_is_valid)
    assert (user.phone_is_valid)


