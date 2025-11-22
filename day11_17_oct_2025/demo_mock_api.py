# Playwright script to mock register api
from playwright.sync_api import sync_playwright
import random
def test_mock_register_api():
    with sync_playwright() as p:
        # create objects for browser & page
        browser = p.chromium.launch(
            headless=False,
            args=[
                    '--no-sandbox',
                    '--disable-blink-features=AutomationControlled',
                    '--disable-dev-shm-usage',
                    '--disable-web-security',
                    '--disable-features=VizDisplayCompositor',
                    '--disable-background-timer-throttling',
                    '--disable-backgrounding-occluded-windows',
                    '--disable-renderer-backgrounding'
                ],
                slow_mo=1500
            )
        page = browser.new_page()

        # intercept register api for nop-commerce
        def mock_register_usewr(route):
            fake_response = {"status":"Not Found"}
            route.fulfill(
                status = 404,
                content_type = "application/x-www-form-urlencoded",
                body = str(fake_response)
            )

        page.route("/register", mock_register_usewr)

        # Visit nop-commerce demo site
        page.goto("https://demo.nopcommerce.com/register")
        page.click("#gender-male")
        page.fill("#FirstName", "Yujiro")
        page.fill("#LastName", "Hanma")
        page.fill("#Email", f"yujiro.hanma-{str(random.randrange(0000,9999))}@yh-anime.com")
        page.fill("#Company", "Anime")
        page.fill("#Password", "yhanma@anime123")
        page.fill("#ConfirmPassword", "yhanma@anime123")
        page.click("#register-button")

        # Assert results
        assert page.inner_text(".result") == "Your registration completed"

        browser.close()