from HW_playwright.pages.cart_page import Cart_page


class Search_page:
    def __init__(self, page,jsondb):
        self.page = page
        self.jsondb = jsondb

    def search(self, search_word: str) -> Cart_page:
        """
        function: Search by search word
        :param search_word: str
        :return: Cart_page
        """
        search_locators=self.jsondb.get_search_page_locators()["search_locators"]
        self.page.locator(search_locators["input_search"]).fill(search_word)
        self.page.locator(search_locators["button_search"]).click()
        return Cart_page(self.page,self.jsondb)

    def get_user_name(self):
        user_name_locators=self.jsondb.get_search_page_locators()["get_user_name_locators"]
        user_name =self.page.locator(user_name_locators["span_get_user_name"]).text_content()
        return user_name

    def get_error_message_Invalid_user(self):
        error_message_locators=self.jsondb.get_search_page_locators()["get_error_message_Invalid_user_locators"]
        error_message = self.page.locator(error_message_locators["il_get_error_message"]).text_content()
        return error_message

