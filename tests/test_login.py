from selene import be

from src.pages.login_page import LoginPage


def test_login():
    LoginPage().open() \
        .login_with("test", "test"). \
        avatar.should(be.visible)
