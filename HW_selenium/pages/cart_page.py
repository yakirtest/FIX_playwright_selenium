from HW_selenium.pages.pay_page import Pay_page
from HW_selenium.pages.basic_page import *


class Cart_page:
    def __init__(self, driver,jsondb):
        self._driver = driver
        self.jsondb =jsondb

    def add_to_cart(self)->Pay_page:
        """
        function:Add a dress to cart
        :return: Pay_page
        """
        url = self.min_price()
        self._driver.get(url)
        return Pay_page(self._driver,self.jsondb)

    def min_price(self):
        """
        function: Returns the URL of the cheapest dress
        :return: url:str
        """
        min_price_locators=self.jsondb.get_cart_page_locators()["min_price_locators"]
        dresses = self._driver.find_elements(*min_price_locators["dresses_min_price"])
        url = self._driver.find_elements(*min_price_locators["urls_min_price"])
        min_price = float(100)
        index = int(-1)
        for i in range(len(dresses)):
            price = float(dresses[i].text.split("\n")[1].split(" ")[0].replace("$", ""))
            if price < min_price:
                min_price = price
                index = i
        return url[index].get_attribute('href')

    def get_search_word(self):
        search_word_locators=self.jsondb.get_cart_page_locators()["get_search_word_locators"]
        search_word = self._driver.find_element(*search_word_locators["span_get_search_word"]).text
        return search_word
