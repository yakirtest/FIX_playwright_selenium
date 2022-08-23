import json

class Read_the_json_file_DB:
    def __init__(self):
        with open("C:\Git_sela\pythonProject2\HW_playwright\Handling_JSON\DB_container.json") as file:
            self.data = json.load(file)

    def get_user_name(self):
        return self.data["user_name"]

    def get_aut_page_locators(self):
        return self.data["Aut_page_locators"]

    def get_search_page_locators(self):
        return self.data['Search_page_locators']

    def get_cart_page_locators(self):
        return self.data['Cart_page_locators']

    def get_pay_page_locators(self):
        return self.data['Pay_page_locators']

if __name__ == '__main__':
    json=Read_the_json_file_DB()
    print(json.get_user_name())
    print(json.get_aut_page_locators())
    print(json.get_search_page_locators())
    print(json.get_cart_page_locators())
    print(json.get_pay_page_locators())


    # with open("C:\Git_sela\pythonProject2\HW_selenium\DB_container.json") as f:
    #     data = json.load(f)
    # print(data['user_name']["valid_user"])
    # print(data['Aut_page_locators']["login_locators"])
    # print(data['Search_page_locators'])
    # print(data['Cart_page_locators'])
    # print(data['Pay_page_locators'])
