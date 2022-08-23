from HW_selenium.pages.basic_page import *


class Pay_page:

    def __init__(self, driver,jsondb):
        self._driver = driver
        self.jsondb =jsondb


    def pay(self):
        """
        function: Buying the dress
        :return: self._driver
        """

        pay_locators = self.jsondb.get_pay_page_locators()["pay_locators"]
        self._driver.find_element(*pay_locators["a1_pay_locators"]).click()
        self._driver.find_element(*pay_locators["button1_pay_locators"]).click()
        self._driver.find_element(*pay_locators["input_pay_locators"]).click()
        self._driver.find_element(*pay_locators["button2_pay_locators"]).click()
        self._driver.find_element(*pay_locators["a2_pay_locators"]).click()
        self._driver.find_element(*pay_locators["button3_pay_locators"]).click()
        return Pay_page(self._driver,self.jsondb)

    def get_price_product(self):
        price_product_locators = self.jsondb.get_pay_page_locators()["get_price_product_locators"]
        price = self._driver.find_element(*price_product_locators["price_locators"]).text
        return price

    def get_end_message(self):
        end_message_locators=self.jsondb.get_pay_page_locators()["get_end_message_locators"]
        end_message = self._driver.find_element(*end_message_locators["end_message_locators"]).text
        return end_message



