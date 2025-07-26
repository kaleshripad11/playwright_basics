from playwright.sync_api import sync_playwright

# Basic function to open browser using playwright sync api
def launch_browser():
    with sync_playwright() as p:
        firefox = p.firefox.launch(headless=False)
        playwright_page = firefox.new_page()
        playwright_page.goto("https://www.playwright.dev/python")
        print(playwright_page.title())
        firefox.close()

def launch_multiple_browser_windows():
    with sync_playwright() as p:
        # Create browser object & store it in variable
        browser = p.webkit.launch(headless=False)
        # Create new page in context(separate isolated browser session within a single browser instance) variable
        # Each page will open a separate isolated window for webkit browser 
        page1 = browser.new_page()      
        page2 = browser.new_page()
        page1.goto("https://google.com")
        page2.goto("https://playwright.dev/python/docs/library")
        print(f"Page1 title - {page1.title()}")
        print(f"Page2 title - {page2.title()}")
        # Will close browser instance(Indirectly will close all the open webkit browser sessions/windows)
        browser.close()
        # Navigate to app URL using 

if __name__ == "__main__":
    launch_multiple_browser_windows()
    launch_browser()
