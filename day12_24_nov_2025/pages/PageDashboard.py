from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator("h6.oxd-topbar-header-breadcrumb")

    def get_header_text(self):
        return self.header.inner_text(timeout=60000)
