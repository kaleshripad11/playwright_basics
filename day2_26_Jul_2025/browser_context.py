# Browser context provides a way to operate multiple independent browser sessions at a time
# Playwright allows creating isolated non-persistent browser contexts with browser.new_context() method. 
# Non-persistent browser contexts don't write any browsing data to disk.

# Create browser context 
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import asyncio

# Browser contexts with sync api
def sync_context_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=False)
        # Create browser context
        context = browser.new_context()
        # Create new page under browser context
        page1 = context.new_page()
        page2 = context.new_page()

        page1.goto("https://www.playwright.dev/python")     # Will be opened in first tab(main browser window) under context
        page2.goto("https://www.playwright.dev/java")       # Will be opened in another tab under same context

        print(page1.title())    # Tab1 title under same browser window
        print(page2.title())    # Tab2 title under same browser window

        # Close browser session
        context.close()

if __name__ == "__main__":
    sync_context_demo()    