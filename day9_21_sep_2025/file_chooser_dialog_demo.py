# Playwright code to demo file chooser dialog

from playwright.sync_api import sync_playwright, expect

def demo_file_chooser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com/upload-download")

        # Wait for file chooser dialog to appear on button click
        with page.expect_file_chooser() as file_chooser:
            page.click("input#uploadFile")

        # Store file chooser dialog
        file_chooser_fc = file_chooser.value

        # Choose files using "set_files()" method
        file_chooser_fc.set_files("D:\\test.png")

        expect(page.locator("p#uploadedFilePath")).to_be_visible()

        browser.close()

demo_file_chooser()