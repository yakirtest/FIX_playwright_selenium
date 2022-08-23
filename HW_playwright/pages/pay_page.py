class Pay_page:
    def __init__(self, page,jsondb):
        self.page = page
        self.jsondb = jsondb

    def pay(self):
        """
        function: Buying the dress
        :return: self._driver
        """
        pay_locators=self.jsondb.get_pay_page_locators()["pay_locators"]
        self.page.locator(pay_locators["a1_pay_locators"]).click()
        self.page.locator(pay_locators["button1_pay_locators"]).click()
        self.page.locator(pay_locators["input_pay_locators"]).click()
        self.page.locator(pay_locators["button2_pay_locators"]).click()
        self.page.locator(pay_locators["a2_pay_locators"]).click()
        self.page.locator(pay_locators["button3_pay_locators"]).click()
        return Pay_page(self.page,self.jsondb)

    def get_price_product(self):
        price_product_locators = self.jsondb.get_pay_page_locators()["get_price_product_locators"]
        price=self.page.locator(price_product_locators["price_locators"]).text_content()
        return price

    def get_end_message(self):
        end_message_locators=self.jsondb.get_pay_page_locators()["get_end_message_locators"]
        end_message = self.page.locator(end_message_locators["end_message_locators"]).text_content()
        return end_message

