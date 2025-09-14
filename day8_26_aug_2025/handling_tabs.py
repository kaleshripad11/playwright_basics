from playwright.sync_api import sync_playwright
import time

def launch_new_tab():
    #
    # In playwright every page represents a tab.
    # Create a context
    # Created multiple pages under context
    # Navigate through it
    # #
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000)
        context = browser.new_context()
        page1 = context.new_page()
        page1.goto("https://playwright.dev/python/docs/pages")
        #time.sleep(2000)
        page2 = context.new_page()
        page2.goto("https://playwright.dev/python/docs/api/class-browsercontext#browser-context-pages")
        page2.screenshot(type="jpeg", quality=100, path="test.jpeg")
        tab_url = context.pages
        for i in tab_url:
            print(i)
            '''
                <Page url='https://playwright.dev/python/docs/pages'>
                <Page url='https://github.com/kaleshripad11'>
            '''
        
launch_new_tab()