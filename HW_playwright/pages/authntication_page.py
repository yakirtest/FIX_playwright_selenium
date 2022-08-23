from HW_playwright.pages.base_page import Base_page
from HW_playwright.pages.search_page import Search_page


class Authntication_page(Base_page):

    def login(self, user: str)-> Search_page:
        """
        User authentication by valid or invalid
        :param user: str
        :return: Search_page
        """
        user_name=self.jsondb.get_user_name()[user]
        login_locators=self.jsondb.get_aut_page_locators()["login_locators"]
        self.page.locator(login_locators["Sign in"]).click()
        self.page.locator(login_locators["email"]).fill(user_name["Name"])
        self.page.locator(login_locators["passwd"]).fill(user_name["passwd"])
        self.page.locator(login_locators["SubmitLogin"]).click()
        return Search_page(self.page,self.jsondb)
