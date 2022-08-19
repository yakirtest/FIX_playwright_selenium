import pytest
from playwright.sync_api import sync_playwright
from HW_playwright.Driver import Driver


@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        page = Driver(playwright).start_driver()
        yield page


def test_start_driver():
    with sync_playwright() as playwright:
        start_page = Driver(playwright).start_driver()
        categories = start_page.page.locator('//*[@id="block_top_menu"]/div').text_content()
    assert categories == "Categories"


def test_sign_in(page):
    page.sign_in()
    authentication = page.page.locator('//*[@id="center_column"]/h1').text_content()
    print(authentication)
    assert authentication == "Authentication"


def test_login_Valid(page):
    login_page = page.sign_in()
    login_page.login("valid_user")
    user_name = login_page.page.locator('//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text_content()
    assert user_name == "Admin admin"


def test_login_Invalid(page):
    login_page = page.sign_in()
    login_page.login("Invalid_user")
    error_message = login_page.page.locator('//*[@id="center_column"]/div[1]/ol/li').text_content()
    assert error_message == "Authentication failed."


def test_Search(page):
    search_page = page.sign_in().login("valid_user")
    search_page.search("summer")
    search = search_page.page.locator('//*[@id="center_column"]/h1/span[1]').text_content().replace(" ", "").replace(
        "\n", "")
    assert search == '"summer"'


def test_add_to_cart(page):
    add_to_cart_page = page.sign_in().login("valid_user").search("summer")
    add_to_cart_page.add_to_cart()
    price = add_to_cart_page.page.locator('//*[@id="product_price_7_34_731444"]/span[1]').text_content()
    assert price == "$16.40"


def test_pay(page):
    pay_page = page.sign_in().login("valid_user").search("summer").add_to_cart()
    finish_page = pay_page.pay()
    end_message = finish_page.locator('//*[@id="center_column"]/div/p/strong').text_content()
    assert end_message == "Your order on My Store is complete."
