from playwright.sync_api import sync_playwright

def request_interception_ex1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Intercept requests to a specific URL
        def handle_route(route, request):
            print(f"Intercepted: {request.url}")
            route.continue_()  # or route.abort(), route.fulfill()

        page.route("**/api/data", handle_route)
        page.goto("https://flipkart.com")

        browser.close()

def request_interception_ex2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Mock API
        page.route("**/api/data", lambda route, request: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"mocked": true}'
        ))
        page.goto("https://flipkart.com")
        browser.close()


request_interception_ex1()
request_interception_ex2()