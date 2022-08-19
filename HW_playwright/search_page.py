from HW_playwright.cart_page import Cart_page


class Search_page:
    def __init__(self, page):
        self.page = page

    DB_container = {}

    def search(self, search_word: str) -> Cart_page:
        """
        function: Search by search word
        :param search_word: str
        :return: Cart_page
        """
        self.page.locator('input[id="search_query_top"]').fill(search_word)
        self.page.locator('button[name="submit_search"]').click()
        return Cart_page(self.page)
