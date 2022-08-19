from HW_selenium.cart_page import *


class Search_page:
    def __init__(self, driver):
        self._driver = driver

    DB_container = {"input_search": (By.XPATH, '//input[@id="search_query_top"]'),
                    "button_search": (By.XPATH, '//button[@name="submit_search"]'),
                    }

    def search(self, search_word: str)->Cart_page:
        """
        function: Search by search word
        :param search_word: str
        :return: Cart_page
        """
        self._driver.find_element(*self.DB_container["input_search"]).send_keys(search_word)
        self._driver.find_element(*self.DB_container["button_search"]).click()
        return Cart_page(self._driver)
