from HW_selenium.pages.authntication_page import Authntication_page

if __name__ == '__main__':
    authntication= Authntication_page()
    # search = authntication.login("Invalid_user")
    # print(search.get_error_message_Invalid_user())
    search = authntication.login("valid_user")
    cart = search.search("summer")
    pay = cart.add_to_cart()
    finis = pay.pay()
    message=finis.get_end_message()
    # print(message)



