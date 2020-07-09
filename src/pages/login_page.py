import allure
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser
from selene import be
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.main_page import MainPage


class LoginPage:

    def __init__(self):
        self.login_field = s("#loginInput")
        self.password_field = s("#passwordInput")
        self.button = ss(".btn")[1]
        self.sign_in_button = s("[src='sign.png']")

    @allure.step
    def open(self):
        browser.open("/")
        return self

    @allure.step
    def login_with(self, login, password):
        ss(".form-group").first.double_click()
        self.login_field.type(login)

        ss(".form-group")[1].double_click()
        self.password_field.type(password)

        self.button.hover().should(be.absent)
        self.sign_in_button.should(be.existing).hover().click()

        self.confirm_alert()
        self.confirm_alert()

        return MainPage()

    @allure.step
    def confirm_alert(self):
        WebDriverWait(browser.driver, browser.config.timeout).until(EC.alert_is_present())
        browser.driver.switch_to.alert.accept()
