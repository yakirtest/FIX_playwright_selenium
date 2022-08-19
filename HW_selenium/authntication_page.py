from HW_selenium.search_page import *


class Authntication_page:

    def __init__(self, driver):
        self._driver = driver

    DB_container = {"valid_user": ("admin11111@gmail.com", "admin11111"),
                    "Invalid_user": ("Unverified_admin@gmail.com", "Unverified_admin"),
                    "email": (By.ID, "email"),
                    "passwd": (By.ID, "passwd"),
                    "SubmitLogin": (By.NAME, 'SubmitLogin')
                    }

    def login(self, user: str) -> Search_page:
        """
        User authentication by valid or invalid
        :param user: str
        :return: Search_page
        """
        self._driver.find_element(*self.DB_container["email"]).send_keys(self.DB_container[user][0])
        self._driver.find_element(*self.DB_container["passwd"]).send_keys(self.DB_container[user][1])
        self._driver.find_element(*self.DB_container["SubmitLogin"]).click()
        return Search_page(self._driver)
