from selenium.webdriver.common.by import By


class Pay_page:

    def __init__(self, driver):
        self._driver = driver

    def pay(self):
        """
        function: Buying the dress
        :return: self._driver
        """
        self._driver.find_element(By.XPATH,
                                  '//a[@class="button btn btn-default standard-checkout button-medium"]').click()
        self._driver.find_element(By.XPATH, '//button[@class="button btn btn-default button-medium"]').click()
        self._driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
        self._driver.find_element(By.XPATH, '//button[@name="processCarrier"]').click()
        self._driver.find_element(By.XPATH, '//a[@class="bankwire"]').click()
        self._driver.find_element(By.XPATH, '//button[@class="button btn btn-default button-medium"]').click()
        return self._driver
