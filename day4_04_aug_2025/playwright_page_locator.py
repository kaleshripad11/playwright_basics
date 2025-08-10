# The page.locator() returns element locator which can be used for performing some action on that element present on page/frame
# Syntax: page.locator(selector) or page.locator(selector, **kwargs)
# This is commonly used with CSS Selector, XPaths

from playwright.sync_api import sync_playwright, expect
import re

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=500)
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page1.goto("https://playwright.dev/python")
    
    # Locate using HTML tag as selector & Text present on it
    with page1.expect_navigation():
        page1.locator("a", has_text="Docs").click()

    expect(page1).to_have_title("Installation | Playwright Python")
    page1.close()
    context1.close()

    page2 = context2.new_page()
    page2.goto("https://opensource-demo.orangehrmlive.com/")

    # Locate using partital text
    # Wait for navigation after clicking "Forgot your password?"
    with page2.expect_navigation():
        page2.locator("text=Forgot").click()
    expect(page2).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
    page2.locator("button:has-text('Cancel')").click()

    # Locate element using CSS Selector
    page2.locator("input[name='username']").fill("Admin")
    page2.locator("input[name='password']").fill("Admin")
    page2.locator("button[type='submit']").click()


    browser.close()