from HW_playwright.authntication_page import *


class Main_page:
    def __init__(self, page):
        self.page = page

    def sign_in(self)-> Authntication_page:
        """
        function: Clicking on 'Sign in'
        :return: Authntication_page
        """
        self.page.locator('a[class="login"]').click()
        return Authntication_page(self.page)
