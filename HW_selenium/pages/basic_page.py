from selenium import webdriver
from selenium.webdriver.edge.service import Service
from HW_selenium.Handling_JSON.read_json_DB_container import Read_json_DB_container

service = Service('C:\Git_sela\pythonProject\Browsers\msedgedriver.exe')
driver = webdriver.Edge(service=service)


class Base_page(object):
    def __init__(self):
        driver.get_window_size()
        driver.get("http://automationpractice.com/index.php")
        self._driver = driver
        self.jsondb = Read_json_DB_container()





