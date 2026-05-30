from playwright.sync_api import sync_playwright


def test_launch_browser():
    """Simple test that launches a Chromium browser, opens a page, and prints the page title.

    This uses Playwright's synchronous API via `sync_playwright()` and demonstrates a
    minimal flow: start Playwright, launch the browser, create a new page, navigate,
    read the title, and close the browser.
    """

    # Start Playwright in a context manager to ensure proper cleanup.
    with sync_playwright() as p:
        # Launch a Chromium browser instance.
        # - headless=False: open a visible browser window (useful for debugging).
        # - slow_mo=1000: slow down operations by 1000ms to observe actions.
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # Create a new browser page (tab).
        page = browser.new_page()

        # Navigate to the given URL. Note: the URL here includes a query string
        # but no explicit path — in many cases you'd use a search path like
        # 'https://www.google.com/search?q=playwright'. This line attempts to
        # load the provided URL as-is.
        page.goto("https://www.google.com?q=playwright")

        # Print the current page title to stdout. In a real test you'd assert
        # expected values instead of printing.
        print(page.title())

        # Close the browser when done to free resources.
        browser.close()