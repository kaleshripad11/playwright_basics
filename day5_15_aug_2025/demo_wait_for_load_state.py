from playwright.sync_api import sync_playwright, expect
import re

def demo_wait_for_selector():
    with sync_playwright() as p:
        # Browser object 
        webkit = p.webkit.launch(headless=False, slow_mo=1500)

        # Context object
        context = webkit.new_context()

        # Page object
        page = context.new_page()

        # wait_for_locator()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading")
        page.locator("a", has_text="hidden").click()
        page.locator("button", has_text="Start").click()
        page.wait_for_selector("div#finish", state="visible")
        expect(page.locator("div#finish h4")).to_contain_text(re.compile("Hello World"))

        # navigate back to previous page
        page.go_back()
        page.locator("a", has_text="fact").click()
        page.locator("button", has_text="Start").click()
        page.wait_for_selector("div#finish", state="visible")
        expect(page.locator("div#finish h4")).to_contain_text(re.compile("Hello World"))

demo_wait_for_selector()