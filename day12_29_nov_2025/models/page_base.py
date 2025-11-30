# Base page class for all web page actions
from playwright.sync_api import Page, Locator, expect

class PageBase:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: Locator):
        self.page.locator(locator).click()

    def enter_text(self, locator: Locator, input_text: str):
        self.page.locator(locator).fill(input_text)

    def navigate_to_url(self, page_url: str):
        self.page.goto(page_url)

    def get_text(self, locator: Locator) -> str:
        return self.page.locator(locator).inner_text()