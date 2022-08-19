from HW_playwright.pay_page import *


class Cart_page:
    def __init__(self, page):
        self.page = page

    DB_container = {}

    def add_to_cart(self)->Pay_page:
        """
        function:Add a dress to cart
        :return: Pay_page
        """
        self.page.goto(self.min_price())
        return Pay_page(self.page)

    def min_price(self)->str:
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

    DB_container = {'"dress1"': ['//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]',
                                 '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[1]/span[1]'],
                    'dress2': ['//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]',
                               '//*[@id="center_column"]/ul/li[2]/div/div[2]/div[1]/span'],
                    'dress3': ['//*[@id="center_column"]/ul/li[3]/div/div[2]/div[2]/a[1]',
                               '//*[@id="center_column"]/ul/li[3]/div/div[2]/div[1]/span[1]'],
                    'dress4': ['//*[@id="center_column"]/ul/li[4]/div/div[2]/div[2]/a[1]',
                               '//*[@id="center_column"]/ul/li[4]/div/div[2]/div[1]/span']}

    def get_all_dresses(self)->dict:
        """
        Returns the url and price of all dresses
        :return: dict_dresses:dict
        """
        dict_dresses = dict()
        for dress in self.DB_container.items():
            price_drees = self.page.locator(dress[1][1]).text_content().replace("\t", "").replace("\n", "").replace("$", "")
            url_drees = self.page.locator(dress[1][0]).get_attribute("href")
            dict_dresses[float(price_drees)] = url_drees
        return dict_dresses
