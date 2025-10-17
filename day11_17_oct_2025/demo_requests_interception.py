##
# In playwright requests can be intercepted using page.route()
# With page.route() api's can be mocked for testing purpose's
# Below code demonstrates a basic example for request interception using page.route()
# #
from playwright.sync_api import sync_playwright

def demo_requests_interception_using_page_route():
    with sync_playwright() as p:
        driver = p.chromium.launch(headless=False, slow_mo=1500)
        page = driver.new_page()

        # Block requests which path contains png, jpg or jpeg content
        page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        page.goto("https://flipkart.com")
        driver.close()

demo_requests_interception_using_page_route()