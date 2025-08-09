# The page.locator() returns element locator which can be used for performing some action on that element present on page/frame
# Syntax: page.locator(selector) or page.locator(selector, **kwargs)
# This is commonly used with CSS Selector, XPaths

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python", wait_until="domcontentloaded")
    page.locator("a", has_text="Docs").click()
    print(f"Page title: {page.title()}")
    expect(page).to_have_title("Installation | Playwright Python")