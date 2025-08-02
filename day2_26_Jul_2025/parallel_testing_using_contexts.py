from playwright.sync_api import sync_playwright, Playwright
import time

def parallel_test_execution(p: Playwright):
    browser = p.webkit.launch(headless=False)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page2 = context2.new_page()
    page1.goto("https://www.demoblaze.com/prod.html?idp_=13")
    page2.goto("https://www.playwright.dev/python")

    print(f"{time.ctime()}: {page1.title()}")
    print(f"{time.ctime()}: {page2.title()}")

with sync_playwright() as p:
    parallel_test_execution(p)