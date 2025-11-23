from playwright.sync_api import sync_playwright

def demo_log_api_response_body():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()

        # Method to log response body on console
        def log_requests_responses(response):
            # log responses only for POST requests
            if "posts" in response.url:
                print(f"=> Response from {response.url}:")
                print(f"=> Status: {response.status}")
                print(f"=> Body: {response.text()}")

        page.on("response", log_requests_responses)
        page.on("requestfailed", lambda request: print(f"❌ Failed: {request.url}"))

        page.goto("https://jsonplaceholder.typicode.com/")
        page.evaluate("fetch('https://jsonplaceholder.typicode.com/posts/1')")
        page.wait_for_timeout(5000)
        browser.close()

demo_log_api_response_body()