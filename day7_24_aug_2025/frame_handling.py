from playwright.sync_api import sync_playwright, expect

def frame_handling_demo():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=250)
        page = browser.new_page()
        page.goto("https://practice-automation.com/iframes/")

        # Locate frame using page.frame_locator(locator)
        frame = page.frame_locator("#iframe-1")

        # Access all chield elements of frame using frame variable
        frame.locator("a", has_text="Get Started").click()

        # Here used nth(index) function as there are more than one locators with expected text
        expect(frame.locator("span.breadcrumbs__link").nth(1)).to_have_text("Installation")
        browser.close()
        
frame_handling_demo()