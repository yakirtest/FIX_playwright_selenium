
from HW_playwright.pages.pay_page import *


class Cart_page:

    def __init__(self, page, jsondb):
        self.page = page
        self.jsondb = jsondb

    def add_to_cart(self) -> Pay_page:
        """
        function:Add a dress to cart
        :return: Pay_page
        """
        self.page.goto(self.min_price())
        return Pay_page(self.page, self.jsondb)

    def min_price(self) -> str:
        """
        function: Returns the URL of the cheapest dress
        :return: url:str
        """
        dresses = self.get_all_dresses()
        min_price = float(100)
        for price, url in dresses.items():
            if price < min_price:
                min_price = price
        return dresses[min_price]

    def get_all_dresses(self) -> dict:
        """
        Returns the url and price of all dresses
        :return: dict_dresses:dict
        """
        min_price_locators = self.jsondb.get_cart_page_locators()["min_price_locators"]
        dict_dresses = dict()
        for dress in min_price_locators.items():
            price_drees = self.page.locator(dress[1][1]).text_content().replace("\t", "").replace("\n", "").replace("$",
                                                                                                                    "")
            url_drees = self.page.locator(dress[1][0]).get_attribute("href")
            dict_dresses[float(price_drees)] = url_drees
        return dict_dresses

    def get_search_word(self):
        search_word_locators= self.jsondb.get_cart_page_locators()["get_search_word_locators"]
        search = self.page.locator(search_word_locators["span_get_search_word"]).text_content().replace(" ","").replace("\n", "")
        return search
