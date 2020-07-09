import allure
from selene import by
from selene.support.shared.jquery_style import s, ss

from src.pages.fragments.card_fragment import CardFragment


class MainPage:

    def __init__(self):
        self.avatar = s("#avatar")
        self.articles_body = s(".card-body")

        self.main_buttons = self.articles_body.ss("button.tree-main-button")

        self.advertisers_button = self.main_buttons.first
        self.publishers_button = self.main_buttons[1]
        self.top_level_clients_button = self.main_buttons[2]

        self.advertisers_sub = ss('//button[text()="Advertisers"]/../div//button')

    @allure.step
    def get_sub_article_from_advertisers(self, name):
        self.advertisers_button.click()
        self.articles_body.s(by.text(name)).click()
        return CardFragment()

    @allure.step
    def get_sub_article_from_publishers(self, name):
        self.publishers_button.click()
        self.articles_body.s(by.text(name)).click()
        return CardFragment()

    @allure.step
    def get_sub_article_from_top_level_clients(self, name):
        self.top_level_clients_button.click()
        self.articles_body.s(by.text(name)).click()
        return CardFragment()

    @allure.step
    def get_all_sub_articles_from(self, name):
        return ss(f'//button[text()="{name}"]/../div//button')
