from playwright.sync_api import sync_playwright

app_url = "https://www.google.com"

def browser_context_cookies_func():
    with sync_playwright() as p:
        # Create browser variable to hold webkit browser object
        browser = p.webkit.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(app_url)
        # Use "context_obj.cookies(url)" function to retrive cookies, If no URL is provided to function it will retrive all cookies
        print(context.cookies([app_url]))
        print("Clearing cookies...")
        context.clear_cookies()
        # Empty cookie list will be return as its cleared by above clear_cookies()
        print(context.cookies())    
        context.close()

if __name__ == "__main__":
    browser_context_cookies_func()