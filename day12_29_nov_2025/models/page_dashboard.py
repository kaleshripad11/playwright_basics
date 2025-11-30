from playwright.sync_api import Page
from .page_base import PageBase

class PageDashboard(PageBase):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard_locator = ".content-header>h1"

    def is_dashboard_visible(self, text):
        assert super().get_text(self.dashboard_locator) == text, "Test failed"
           