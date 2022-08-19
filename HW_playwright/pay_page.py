class Pay_page:
    def __init__(self, page):
        self.page = page

    def pay(self):
        """
        function: Buying the dress
        :return: self._driver
        """
        self.page.locator('a[class="button btn btn-default standard-checkout button-medium"]').click()
        self.page.locator('button[name="processAddress"]').click()
        self.page.locator('div[class="checker"]').click()
        self.page.locator('button[name="processCarrier"]').click()
        self.page.locator('a[title="Pay by bank wire"]').click()
        self.page.locator('button[class="button btn btn-default button-medium"]').click()
        return self.page
