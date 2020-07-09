import pytest
from selene import have, be

from src.pages.fragments.card_fragment import CardFragment
from src.pages.fragments.saved_cards_fragment import SavedCardsFragment
from src.pages.main_page import MainPage
from src.pages.profile_page import ProfilePage


def test_should_have_three_articles(login_by_cookie):
    MainPage().main_buttons \
        .should(have.size(3))


def test_verify_articles_name(login_by_cookie):
    MainPage().main_buttons \
        .should(have.exact_texts("Advertisers", "Publishers", "Top level clients"))


def test_articles_should_have_sub_articles(login_by_cookie):
    MainPage().advertisers_button.click()
    MainPage().get_all_sub_articles_from("Advertisers").should(have.size(2)) \
        .should(have.exact_texts("Test Advertiser", "Adidas"))

    MainPage().publishers_button.click()
    MainPage().get_all_sub_articles_from("Publishers").should(have.size(2)) \
        .should(have.exact_texts("Youtube", "Instagram"))

    MainPage().top_level_clients_button.click()
    MainPage().get_all_sub_articles_from("Top level clients").should(have.size(10)) \
        .should(have.exact_texts("Jon Snow", "Artur Fleck", "Tim Cook", "Bugs Bunny", "Sasha Grey", "You",
                                 "Leonel Messi", "Tony Stark", "Elon Musk", "Darth Vader"))


def test_sub_article_should_have_buttons(login_by_cookie):
    MainPage().get_sub_article_from_advertisers("Test Advertiser") \
        .download_button.should(be.visible)
    CardFragment().removed_from_saved_button.should(be.visible)
    CardFragment().move_to_saved_button.should(be.disabled).should(be.visible)


@pytest.mark.parametrize("name", ["Jon Snow", "Artur Fleck", "Bugs Bunny", "Sasha Grey", "You",
                                  "Leonel Messi", "Tony Stark", "Tim Cook", "Elon Musk", "Darth Vader"])
def test_all_blocks_from_clients_should_have_name(login_by_cookie, name):
    MainPage().get_sub_article_from_top_level_clients(name) \
        .card_title.should(have.exact_text(name))


def test_add_to_saved_button_enabled_after_scrolling_to_bottom(login_by_cookie):
    MainPage().get_sub_article_from_top_level_clients("Darth Vader") \
        .scroll_to_bottom_in_description()
    CardFragment().move_to_saved_button.should(be.enabled)


def test_change_image_size(login_by_cookie):
    MainPage().get_sub_article_from_top_level_clients("Darth Vader") \
        .move_slider(600) \
        .image.should(have._not_.attribute("style", "width: 300px; height: 300px;"))


def test_add_to_saved_articles(login_by_cookie):
    MainPage().get_sub_article_from_top_level_clients("Darth Vader") \
        .scroll_to_bottom_in_description() \
        .add_to_saved() \
        .articles_body.should(be.present)
    SavedCardsFragment().top_level_clients.should(be.present)
    SavedCardsFragment().check_sub_article_in_article("Darth Vader", "Top level clients")

    MainPage().get_sub_article_from_advertisers("Adidas") \
        .scroll_to_bottom_in_description() \
        .add_to_saved() \
        .articles_body.should(be.present)
    SavedCardsFragment().advertisers.should(be.present)
    SavedCardsFragment().check_sub_article_in_article("Adidas", "Advertisers")

    MainPage().get_sub_article_from_publishers("Instagram") \
        .scroll_to_bottom_in_description() \
        .add_to_saved() \
        .articles_body.should(be.present)
    SavedCardsFragment().publishers.should(be.present)
    SavedCardsFragment().check_sub_article_in_article("Instagram", "Publishers")


def test_avatar_should_open_profile_settings(login_by_cookie):
    MainPage().avatar.click()
    ProfilePage().profile_settings.should(be.present)
