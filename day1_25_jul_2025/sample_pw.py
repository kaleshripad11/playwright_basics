from playwright.sync_api import Page

def test_demo_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="domcontentloaded", timeout=10000)
    page.locator("input[placeholder='Username']").clear()
    page.locator("input[placeholder='Username']").fill("Admin", timeout=50000)
    page.locator("input[placeholder='Password']").clear()
    page.locator("input[placeholder='Password']").fill("admin123", timeout=50000)
    page.locator("button[type='submit']").click()