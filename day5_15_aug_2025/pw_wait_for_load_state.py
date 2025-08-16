from playwright.sync_api import sync_playwright, Page, expect
import re

def demo_wait_for_load_state(p: Page):
    p.goto("https://testautomationcentral.com/demo/shadow_dom.html")
    expect(p.locator("p")).to_contain_text(re.compile("content inside"))

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=1500)
    page = browser.new_page()
    demo_wait_for_load_state(page)