from selenium import webdriver
from selenium.webdriver.edge.service import Service
from HW_selenium.main_page import *


class Driver:
    def __init__(self):
        self.service = Service('C:\Git_sela\pythonProject\Browsers\msedgedriver.exe')
        self.driver_Base = webdriver.Edge(service=self.service)

    def start_driver(self) -> Main_page:
        """
        function: Open browser
        :return: Main_page
        """
        self.driver_Base.get_window_size()
        self.driver_Base.get("http://automationpractice.com/index.php")
        return Main_page(self.driver_Base)
