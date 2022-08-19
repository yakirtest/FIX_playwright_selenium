import pytest
from HW_selenium.Driver import *


@pytest.fixture()
def page():
    page = Driver().start_driver()
    yield page


def test_start_driver():
    start_page = Driver().start_driver()
    title_page = start_page._driver.title
    assert title_page == "My Store"


def test_sign_in(page):
    page.sign_in()
    authentication = page._driver.find_element(By.XPATH, '//*[@id="center_column"]/h1').text
    assert authentication == "AUTHENTICATION"


def test_login_Valid(page):
    login_page = page.sign_in()
    login_page.login("valid_user")
    user_name = login_page._driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
    assert user_name == "Admin admin"


def test_login_Invalid(page):
    login_page = page.sign_in()
    login_page.login("Invalid_user")
    error_message = login_page._driver.find_element(By.XPATH, '//*[@id="center_column"]/div[1]/ol/li').text
    assert error_message == "Authentication failed."


def test_Search(page):
    search_page = page.sign_in().login("valid_user")
    search_page.search("summer")
    search = search_page._driver.find_element(By.XPATH, '//*[@id="center_column"]/h1/span[1]').text
    assert search == '"summer"'.upper()


def test_add_to_cart(page):
    add_to_cart_page = page.sign_in().login("valid_user").search("summer")
    add_to_cart_page.add_to_cart()
    price = add_to_cart_page._driver.find_element(By.XPATH, '//*[@id="product_price_7_34_731444"]/span[1]').text
    assert price == "$16.40"


def test_pay(page):
    pay_page = page.sign_in().login("valid_user").search("summer").add_to_cart()
    finish_page = pay_page.pay()
    end_message = finish_page.find_element(By.XPATH, '//*[@id="center_column"]/div/p/strong').text
    assert end_message == "Your order on My Store is complete."
