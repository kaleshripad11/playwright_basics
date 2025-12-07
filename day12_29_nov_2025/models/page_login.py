# Page class for Google Search

# URL - https://admin-demo.nopcommerce.com/
from .page_base import PageBase
from playwright.sync_api import Page

class PageLogin(PageBase):
    def __init__(self, page: Page):
        super().__init__(page)
        self.txt_email = "#Email"
        self.txt_password = "#Password"
        self.btn_login = ".login-button"
    

    def login(self, username, password):
        #self.page.wait_for_timeout(15000)
        self.page.goto("https://admin-demo.nopcommerce.com/")
        #self.page.wait_for_timeout(90000)
        self.enter_text(self.txt_email, username)
        self.enter_text(self.txt_password, password)
        self.click(self.btn_login)