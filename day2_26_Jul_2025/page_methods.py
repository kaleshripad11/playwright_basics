from playwright.sync_api import sync_playwright

def pages_builtin_methods():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(viewport={'width':1920, 'height':1080}, screen={'width':1920, 'height':1080})
        page = context.new_page()
        # goto() method 
        page.goto("https://playwright.dev/python")

        # Log messages when specific event occures using once() method
        page.once("load", lambda: print("page loaded"))

        # content() => Get html content of a page
        print(page.content())

if __name__ == "__main__":
    pages_builtin_methods()
