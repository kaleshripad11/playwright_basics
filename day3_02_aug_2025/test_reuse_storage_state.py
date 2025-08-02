from playwright.sync_api import sync_playwright, expect

def test_admin_page():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        # Reusing storage file captured in previous test
        context = browser.new_context(storage_state="playwright\\.auth\\auth_state.json")
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        page.get_by_role("link", name="Admin").click()
        expect(page.get_by_role("banner")).to_contain_text("Admin")