from src.utils.locator import Locator
from src.utils.base_element import BaseElement
from src.pages.base_page import BasePage

class ExamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com"

    def search_input(self):
        return BaseElement(self.driver, Locator.NAME("q"))

    def search_button(self):
        return BaseElement(self.driver, Locator.NAME("btnK"))

    def results_stats(self):
        return BaseElement(self.driver, Locator.ID("result-stats"))

    def open(self):
        super().open(self.url)

    def search(self, query):
        self.search_input().send_keys(query)
        self.search_button().click()

    def get_results_stats(self):
        return self.results_stats().text()
