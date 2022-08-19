from HW_playwright.search_page import Search_page


class Authntication_page:
    def __init__(self, page):
        self.page = page

    DB_container = {"valid_user": ("admin11111@gmail.com", "admin11111"),
                    "Invalid_user": ("Unverified_admin@gmail.com", "Unverified_admin"),
                    "email": 'input[id="email"]',
                    "passwd": 'input[id="passwd"]',
                    "SubmitLogin": 'button[id="SubmitLogin"]'
                    }

    def login(self, user: str)-> Search_page:
        """
        User authentication by valid or invalid
        :param user: str
        :return: Search_page
        """
        self.page.locator(self.DB_container["email"]).fill(self.DB_container[user][0])
        self.page.locator(self.DB_container["passwd"]).fill(self.DB_container[user][1])
        self.page.locator(self.DB_container["SubmitLogin"]).click()
        return Search_page(self.page)
