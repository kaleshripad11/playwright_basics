from playwright.sync_api import sync_playwright, expect
import random

# Note: parameter "quality" is not applicale to png formats

def demo_capture_screenshot():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://demoqa.com/upload-download", wait_until="domcontentloaded")
        # Capture screenshot of visible area of a page with jpeg format
        page.screenshot(full_page=False, path=f"..\\screenshots\\screenshot{str(random.randint(100,200))}.jpeg", type="jpeg", quality=100)

        # Capture screenshot of fullpage with jpeg format
        page.screenshot(full_page=False, path=f"..\\screenshots\\screenshot{str(random.randint(100,200))}.jpeg", type="jpeg", quality=100)

        # Capture screenshot of a image/logo/web element
        heading_locator = page.get_by_role("heading",name="Upload and Download")
        heading_locator.screenshot(path=f"..\\screenshots\\heading_screenshot_{str(random.randint(100,200))}.jpeg", type="jpeg", quality=100)
        browser.close()

demo_capture_screenshot()