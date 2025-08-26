# Playwright handles alerts using event listeners
# 'dialog' event on the page can be listened - whenever a dialog is shown
# By default playwright dismiss the dialogs on its own 

from playwright.sync_api import sync_playwright, expect
import time

def alert_handling_demo():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True)
        page = browser.new_page()

        # Listen for the 'dialog' event and accept it
        page.on("dialog", lambda dialog: dialog.accept())

        # Navigate to a page that triggers an alert
        page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

        # Locate the iframe from where alert can be triggered
        result_frame = page.frame_locator("#iframeResult")
        result_frame.get_by_role("button", name="Try it").click()
        
        browser.close()

alert_handling_demo()