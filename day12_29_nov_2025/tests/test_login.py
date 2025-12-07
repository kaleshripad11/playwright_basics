from day12_29_nov_2025.models.page_login import PageLogin
from day12_29_nov_2025.models.page_dashboard import PageDashboard
from playwright.sync_api import Page, sync_playwright

class Test_Login:
    def test_verify_login_with_valid_username_and_password(self, page: Page):
        login = PageLogin(page)
        login.login("admin@yourstore.com", "admin")
        dashboard = PageDashboard(page)
        dashboard.is_dashboard_visible("Dashboard")
