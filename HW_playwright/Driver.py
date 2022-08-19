from playwright.sync_api import sync_playwright

from HW_playwright.main_page import *


class Driver:
    def __init__(self, playwright):
        self.page_Base = playwright.chromium.launch(headless=False).new_page()

    def start_driver(self)-> Main_page:
        """
        function: Open browser
        :return: Main_page
        """
        self.page_Base.goto('http://automationpractice.com/index.php')
        return Main_page(self.page_Base)
