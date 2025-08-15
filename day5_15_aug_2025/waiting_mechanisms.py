#
# Playwright provides many waiting mechanisms to handle asynchronous operations & dynamic web content in a web application
# In this code will be using some of the main methods which are available in playwright & can be used regularly #

from playwright.sync_api import sync_playwright, Page, expect

def demo_wait_for_selector(p: Page):
    # To run this method without pytest - will require page object to be passed as parameter
    p.goto("https://the-internet.herokuapp.com/dynamic_loading")
    p.locator("a", has_text="hidden").click()
    p.wait_for_load_state('domcontentloaded')
    p.locator("button", has_text="Start").click()
    expect(p.locator("h4", has_text="hidden")).to_be_visible()

def login_to_oragne_hrm(p: Page, username, password):
    p.goto("https://opensource-demo.orangehrmlive.com/")
    p.wait_for_selector("input[placeholder='Username']", timeout=2000)
    p.locator("input[placeholder='Username']").fill(username)
    p.wait_for_selector("input[placeholder='Username']", timeout=2000)
    p.locator("input[placeholder='Password']").fill(password)
    p.wait_for_selector("button[type='submit']", state="visible")
    p.locator("button[type='submit']").click()
    expect(p.locator("h6")).to_contain_text("Dashboard", timeout=1500)

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    #demo_wait_for_selector(page)
    login_to_oragne_hrm(page, "Admin", "admin123")