from helpers.user import User


def test_check_user_data(session):
    user = User()
    user.get_current_user_data(session.token)
    assert (user.login == '79044444444')
    assert (user.firstname == 'Евгений')
    assert (user.lastname == 'Николаев')
    assert (user.patronymic == 'Александрович')
    assert (user.email_is_valid)
    assert (user.phone_is_valid)


