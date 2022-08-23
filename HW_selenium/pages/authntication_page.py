from HW_selenium.pages.basic_page import Base_page
from HW_selenium.pages.search_page import Search_page


class Authntication_page(Base_page):

    def login(self, user: str) -> Search_page:
        """
        function: Click on 'Sign in' and
        User authentication by valid or invalid
        :param user: str
        :return: Search_page
        """
        self.jsondb.get_cart_page_locators()
        login_locators=self.jsondb.get_aut_page_locators()["login_locators"]
        user_name=self.jsondb.get_user_name()[user]
        self._driver.find_element(*login_locators["Sign in"]).click()
        self._driver.find_element(*login_locators["email"]).send_keys(user_name["Name"])
        self._driver.find_element(*login_locators["passwd"]).send_keys(user_name["passwd"])
        self._driver.find_element(*login_locators["SubmitLogin"]).click()
        return Search_page(self._driver,self.jsondb)
