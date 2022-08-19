from HW_selenium.Driver import *

if __name__ == '__main__':
    mainpage = Driver().start_driver()
    authntication = mainpage.sign_in()
    search = authntication.login("valid_user")
    cart = search.search("summer")
    pay = cart.add_to_cart()
    finis = pay.pay()
    print(finis)
