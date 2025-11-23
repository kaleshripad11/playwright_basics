# Demo - monitoring network events 
from playwright.sync_api import sync_playwright

def demo_monitor_network_events_responses():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        print("=> Code | Request URL | Response Message")
        # Monitor & log every single request on console
        page.on("response", lambda response: print(f"=> {response.status} | {response.url} | {response.text()}"))

        # Navigate to URL to capture/log the api's in network tab
        page.goto("https://jsonplaceholder.typicode.com/")
        page.evaluate("fetch('https://jsonplaceholder.typicode.com/posts/')")
        page.wait_for_timeout(5000)
        browser.close()

demo_monitor_network_events_responses()