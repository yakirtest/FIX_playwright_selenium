from HW_playwright.Handling_JSON.read_json_DB_container import Read_the_json_file_DB


class Base_page(object):
    def __init__(self, playwright):
        self.jsondb = Read_the_json_file_DB()
        self.page = playwright.chromium.launch(headless=False).new_page()
        self.page.goto('http://automationpractice.com/index.php')

