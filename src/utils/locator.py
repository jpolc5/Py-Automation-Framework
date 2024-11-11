from selenium.webdriver.common.by import By

class Locator:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    @classmethod
    def ID(cls, value):
        return cls(By.ID, value)

    @classmethod
    def NAME(cls, value):
        return cls(By.NAME, value)

    @classmethod
    def XPATH(cls, value):
        return cls(By.XPATH, value)

    @classmethod
    def CSS_SELECTOR(cls, value):
        return cls(By.CSS_SELECTOR, value)


