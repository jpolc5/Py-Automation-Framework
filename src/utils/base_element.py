from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.locator.by, self.locator.value))
        )

    def click(self):
        self.find().click()

    def send_keys(self, text):
        self.find().send_keys(text)

    def text(self):
        return self.find().text

