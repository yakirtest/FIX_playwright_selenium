from playwright.sync_api import sync_playwright
from HW_playwright.pages.authntication_page import Authntication_page
import time


if __name__ == '__main__':
    with sync_playwright() as playwright:
        mainpage = Authntication_page(playwright)
        search=mainpage.login("valid_user")
        # search = mainpage.login("Invalid_user")
        cart = search.search("summer")
        pay = cart.add_to_cart()
        finis = pay.pay()
        print(finis.get_end_message())
        time.sleep(30)
