from playwright.sync_api import sync_playwright, Playwright

# In playwright a 'page' refers to a tab. 
# There can be multiple pages(tabs) in a browser window
# Page is a class in playwright - which provides methods to interact with browser tab
# A single browser might have multiple pages

# In below methods parameter => 'playwright' is like an variable of type 'Playwright'. Its similar to class-object
def pages_demo(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    # If page is not created nothing will be displayed on UI
    page = context.new_page()
    page.goto("https://www.playwright.dev/python")

with sync_playwright() as p:
    pages_demo(p)