from HW_playwright.Driver import *
import time

if __name__ == '__main__':
    with sync_playwright() as playwright:
        mainpage = Driver(playwright).start_driver()
        time.sleep(10)
        authntication = mainpage.sign_in()
        search = authntication.login("valid_user")
        cart = search.search("summer")
        pay = cart.add_to_cart()
        finis = pay.pay()
        print(finis)
        time.sleep(30)
