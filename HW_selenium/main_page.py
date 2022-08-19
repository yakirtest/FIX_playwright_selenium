from HW_selenium.authntication_page import *


class Main_page():
    def __init__(self, driver):
        self._driver = driver

    def sign_in(self) -> Authntication_page:
        """
        function: Clicking on 'Sign in'
        :return: Authntication_page
        """
        self._driver.find_element(By.LINK_TEXT, 'Sign in').click()
        return Authntication_page(self._driver)
