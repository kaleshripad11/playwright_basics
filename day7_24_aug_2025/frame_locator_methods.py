from playwright.sync_api import sync_playwright, expect
import re

def frame_locator_methods():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=250)
        page = browser.new_page()
        page.goto("https://practice-automation.com/iframes/")
        
        frame = page.frame_locator("#iframe-1")
        frame.get_by_alt_text("Playwright logo").click()
        expect(frame.get_by_alt_text("Playwright logo")).to_be_visible()
        browser.close()

frame_locator_methods()