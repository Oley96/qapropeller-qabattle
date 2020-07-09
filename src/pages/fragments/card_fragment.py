import allure
from selene import by, command, query, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import ActionChains

from src.pages.fragments.saved_cards_fragment import SavedCardsFragment


class CardFragment:

    def __init__(self):
        self.container = ss(".card-body")[1]
        self.download_button = self.container.s(by.text("Download info"))
        self.move_to_saved_button = self.container.s(by.text("Move to saved"))
        self.removed_from_saved_button = self.container.s(by.text("Removed from saved"))
        self.card_title = self.container.s(".card-title")
        self.field = self.container.s(".form-control")
        self.slider = self.container.s("div.ui-slider")
        self.image = self.container.s("#heroImage")

    @allure.step
    def scroll_to_bottom_in_description(self):
        self.field.click() \
            .execute_script("document.querySelector('.form-control').scrollTop=400000")
        return self

    @allure.step
    def move_slider(self, offset):
        self.slider.should(be.visible)
        element = browser.driver.find_element_by_css_selector("div.ui-slider") \
            .find_element_by_css_selector("span")
        ActionChains(browser.driver).click_and_hold(element) \
            .move_by_offset(offset, 0).perform()
        return self

    @allure.step
    def add_to_saved(self):
        self.scroll_to_bottom_in_description()
        self.move_to_saved_button.click()
        return SavedCardsFragment()
