from HW_selenium.pay_page import *


class Cart_page:
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self)->Pay_page:
        """
        function:Add a dress to cart
        :return: Pay_page
        """
        url = self.min_price()
        self._driver.get(url)
        return Pay_page(self._driver)

    def min_price(self):
        """
        function: Returns the URL of the cheapest dress
        :return: url:str
        """
        dresses = self._driver.find_elements(By.XPATH, '//div[@class="right-block"]')
        url = self._driver.find_elements(By.XPATH, '//a[@title="Add to cart"]')
        min_price = float(100)
        index = int(-1)
        for i in range(len(dresses)):
            price = float(dresses[i].text.split("\n")[1].split(" ")[0].replace("$", ""))
            if price < min_price:
                min_price = price
                index = i
        return url[index].get_attribute('href')
