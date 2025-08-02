from playwright.sync_api import Page, expect

app_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_login_with_valid_user(page: Page):
    page.goto(app_url)
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")

def test_login_with_in_valid_user(page: Page):
    page.goto(app_url)
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("Admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_contain_text("Invalid credentials")

