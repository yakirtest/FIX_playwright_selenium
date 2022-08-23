import pytest
from playwright.sync_api import sync_playwright
from HW_playwright.pages.authntication_page import Authntication_page


@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        page = Authntication_page(playwright)
        yield page


def test_login_Valid(page):
    login_page=page.login("valid_user")
    user_name=login_page.get_user_name()
    assert user_name == "Admin admin"


def test_login_Invalid(page):
    login_page = page.login("Invalid_user")
    error_message =login_page.get_error_message_Invalid_user()
    assert error_message == "Authentication failed."


def test_Search(page):
    search_page = page.login("valid_user").search("summer")
    search=search_page.get_search_word()
    assert search == '"summer"'


def test_add_to_cart(page):
    add_to_cart_page = page.login("valid_user").search("summer").add_to_cart()
    price = add_to_cart_page.get_price_product()
    assert price == "$16.40"


def test_pay(page):
    pay_page = page.login("valid_user").search("summer").add_to_cart().pay()
    end_message=pay_page.get_end_message()
    assert end_message == "Your order on My Store is complete."
