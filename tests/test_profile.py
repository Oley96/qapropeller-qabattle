from selene import be, have

from src.pages.main_page import MainPage
from src.pages.profile_page import ProfilePage


def test_change_user_with_valid_data(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().change_user_to("Ivan", "Ivanov") \
        .alert_success.should(be.present)


def test_change_user_with_invalid_name(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().change_user_to("", "Ivanov") \
        .error_first_name().should(be.present) \
        .should(have.text("Please set your first name."))


def test_change_user_with_invalid_last_name(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().change_user_to("Ivan", "") \
        .error_last_name().should(be.present) \
        .should(have.text("Please set your last name."))


def test_change_user_with_invalid_firs_and_last_names(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().change_user_to("", "") \
        .error_message.should(have.size(2)) \
        .should(have.texts("Please set your last name", "Please set your first name."))


def test_user_can_change_payment_info(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().select_payment_info() \
        .set_cart_number("1234 5678 1234 5678") \
        .with_payment_system("Visa") \
        .with_day_of_payment(10) \
        .slider_value.should(have.text("10"))
    ProfilePage().save() \
        .payment_successful.should(be.present)


def test_should_be_error_message_if_user_not_select_payment_system(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().select_payment_info() \
        .set_cart_number("1234 5678 1234 5678") \
        .with_day_of_payment(10) \
        .slider_value.should(have.text("10"))
    ProfilePage().save() \
        .error_payment().should(be.present)


def test_should_be_error_message_if_user_not_set_card_number(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().select_payment_info() \
        .with_payment_system("Visa") \
        .with_day_of_payment(10) \
        .slider_value.should(have.text("10"))
    ProfilePage().save() \
        .error_card().should(be.present)
