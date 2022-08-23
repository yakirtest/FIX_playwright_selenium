from HW_selenium.pages.cart_page import Cart_page
from HW_selenium.pages.basic_page import *


class Search_page:
    def __init__(self, driver,jsondb):
        self._driver = driver
        self.jsondb =jsondb

    def search(self, search_word: str)->Cart_page:
        """
        function: Search by search word
        :param search_word: str
        :return: Cart_page
        """

        search_locators=self.jsondb.get_search_page_locators()["search_locators"]
        self._driver.find_element(*search_locators["input_search"]).send_keys(search_word)
        self._driver.find_element(*search_locators["button_search"]).click()
        return Cart_page(self._driver,self.jsondb)

    def get_user_name(self):
        get_user_name_locators =self.jsondb.get_search_page_locators()["get_user_name_locators"]
        self._driver.find_element(*get_user_name_locators["div_get_user_name"])
        user_name=self._driver.find_element(*get_user_name_locators["span_get_user_name"]).text
        return user_name

    def get_error_message_Invalid_user(self):
        get_error_message_locators = self.jsondb.get_search_page_locators()["get_error_message_Invalid_user_locators"]
        error_message = self._driver.find_element(*get_error_message_locators["il_get_error_message"]).text
        return error_message