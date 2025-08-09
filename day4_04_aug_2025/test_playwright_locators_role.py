from playwright.sync_api import Playwright, expect, sync_playwright

class Test_Playwright_Locators:
    def setup(self, p: Playwright):
        self.browser = p.webkit.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://the-internet.herokuapp.com/")
    
    def test_checkbox(self):
        self.page.get_by_text("checkboxes").click()
        # The method 'nth()' will be used to locate an element based on its nth occurrence on page
        # When element does not have any attribute and multiple elements of same type - this method is suitable
        chk1 = self.page.get_by_role("checkbox").nth(0)
        chk2 = self.page.get_by_role("checkbox").nth(1)
        chk1.check()
        chk2.is_checked()
        expect(chk1).to_be_checked()
        expect(chk2).to_be_checked()

with sync_playwright() as p:
    pw = Test_Playwright_Locators(p)
    pw.setup(p)
    pw.test_checkbox(p)