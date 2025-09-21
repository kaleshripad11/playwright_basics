#
# In playwright to handle file upload we can use set_input_files() method from page class
# Below code will demonstrate the file upload using playwright
# #

from playwright.sync_api import sync_playwright, expect

def file_upload_demo():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice.expandtesting.com/upload")
        page.set_input_files("input#fileInput", files=".\\file_upload_demo.txt", timeout=10000)
        page.get_by_role("button", name="Upload").click()
        expect(page.get_by_role("heading", name="File Uploaded!")).to_be_visible()
        expect(page.get_by_text("file_upload_demo.txt")).to_be_visible()

file_upload_demo()