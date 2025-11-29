import pytest
from pages.PageLogin import LoginPage
from pages.PageDashboard import DashboardPage

@pytest.mark.parametrize("username,password", [
    ("Admin", "admin123"),   # Positive
    ("wrongUser", "wrongPass")  # Negative
])
def test_login(page, username, password):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    login_page.navigate("https://opensource-demo.orangehrmlive.com/")
    login_page.login(username, password)

    if "Dashboard" in dashboard_page.get_header_text():
        assert True
    else:
        assert page.locator(".oxd-alert-content").is_visible()