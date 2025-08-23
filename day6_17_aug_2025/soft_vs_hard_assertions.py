from playwright.sync_api import sync_playwright, expect

def soft_assert_demo():
    with sync_playwright() as p:
        driver = p.webkit.launch(headless=False, slow_mo=500)
        context = driver.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.in/")
        expect(page.locator("#nav-logo-sprites")).to_be_visible()   # Hard assert - if this assertion fails no further statement will be executed
        expect(page.locator("#icp-nav-link-inner")).to_be_visible()

soft_assert_demo()