import allure
from selene import have, by
from selene.support.shared.jquery_style import s, ss


class SavedCardsFragment():

    def __init__(self):
        self.articles_body = ss(".card-body")[2]
        self.main_buttons = self.articles_body.ss("button.tree-main-button")
        self.advertisers = self.main_buttons.element_by(have.text("Advertisers"))
        self.top_level_clients = self.main_buttons.element_by(have.text("Top level clients"))
        self.publishers = self.main_buttons.element_by(have.text("Publishers"))

    @allure.step
    def check_sub_article_in_article(self, sub_article, article):
        if article == "Top level clients":
            self.top_level_clients.s("..").s(by.text(sub_article))
        if article == "Advertisers":
            self.advertisers.s("..").s(by.text(sub_article))
        if article == "Publishers":
            self.publishers.s("..").s(by.text(sub_article))
