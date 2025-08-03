from playwright.sync_api import Page, expect

def test_login_with_valid_credentials(page: Page):
    # The 'page: Page' argument in the function signature indicates that this test is designed to be run with the pytest-playwright plugin, 
    # which automatically provides the page object and manages the browser session.
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.context.storage_state(path = "playwright\\.auth\\auth_state.json")
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")