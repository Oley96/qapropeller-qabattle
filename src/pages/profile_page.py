import allure
from selene import by, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import ActionChains


class ProfilePage:

    def __init__(self):
        self.profile_settings = s('.card')
        self.user_profile = s(by.text("User Profile"))
        self.payment_info = s(by.text("Payment info"))

        self.form_container = s("#v-pills-home")
        self.first_name_field = self.form_container.s("#firstNameInput")
        self.last_name_field = self.form_container.s("#lastNameInput")
        self.error_message = self.form_container.ss(".invalid-feedback")
        self.save_button = self.form_container.s("button.btn")
        self.alert_success = self.form_container.s("#successUserInfoSaveInfo")

        self.payment_container = s("#v-pills-messages")
        self.card_number_field = self.payment_container.s("#cardNumberInput")
        self.save_payment_button = self.payment_container.s(".btn.btn-primary")
        self.slider = "#paymentRange"
        self.slider_value = s("h6")
        self.payment_successful = s("#successPaymentInfoSaveInfo")

    @allure.step
    def change_user_to(self, name, last_name):
        self.first_name_field.type(name)
        self.last_name_field.type(last_name)
        self.save_button.click()
        return self

    def error_first_name(self):
        return self.error_message.first

    def error_last_name(self):
        return self.error_message[1]

    @allure.step
    def select_payment_info(self):
        self.payment_info.click()
        return self

    @allure.step
    def set_cart_number(self, num):
        self.card_number_field.type(num)
        return self

    @allure.step
    def with_payment_system(self, payment_system):
        s(f"//select[@class='custom-select']/option[text()='{payment_system}']").click()
        return self

    @allure.step
    def with_day_of_payment(self, val):
        el = browser.driver.find_element_by_css_selector(self.slider)
        minval = float(el.get_attribute("min") or 1)
        maxval = float(el.get_attribute("max") or 31)
        v = max(0, min(1, (float(val + 0.5) - minval) / (maxval - minval)))
        width = el.size["width"]
        target = float(width) * v
        ac = ActionChains(browser.driver)
        ac.move_to_element_with_offset(el, target, 1)
        ac.click()
        ac.perform()
        return self

    @allure.step
    def save(self):
        self.save_payment_button.click()
        return self

    def error_card(self):
        return ss(".invalid-feedback").element_by(have.text("Please set your card number."))

    def error_payment(self):
        return ss(".invalid-feedback").element_by(have.text("Please select your payment system."))
