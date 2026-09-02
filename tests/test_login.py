from pages.login_page import LoginPage


def test_login(navigate_to_login):
    login_page = LoginPage(navigate_to_login)
    login_page.login_user("kushtrim_user", "wrongPassword123")
