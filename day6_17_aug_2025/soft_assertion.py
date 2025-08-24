from playwright.sync_api import sync_playwright, expect

def soft_assert_demo():
    with sync_playwright() as p:
        driver = p.webkit.launch(headless=False, slow_mo=500)
        context = driver.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.in/")
        try:
            assert page.locator("#nav-logo-sprites").is_enabled() == False
            print("Amazonn logo check validation successful!!!")
        except AssertionError as e:
            print(f"Exception occured: {e.__cause__}")
        
        try:
            page.locator("#icp-nav-link-inner").is_visible() == False
            print("Navigation check validation successful!!!")
        except AssertionError as e:
            print(f"Exception occured: {e}")

soft_assert_demo()