#
# This code demonstrates file download using playwright
# #

from playwright.sync_api import sync_playwright, expect


def download_file_demo():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice.expandtesting.com/download")
        page.get_by_test_id("1758463591211_file_upload_demo.txt").click()
        
        # Wait for the popup to appear & close it
        with page.expect_download() as download_info:
            # Handle the ad popup
            page.locator("iframe[name=\"aswift_5\"]").content_frame.locator("iframe[name=\"ad_iframe\"]").content_frame.get_by_role("button", name="Close ad").click()
        download = download_info.value

        # Wait for the download link to appear
        with page.expect_download() as download1_info:
            # Locate the download link/button & perform action on it
            page.get_by_test_id("1758463591211_file_upload_demo.txt").click()
        download1 = download1_info.value
        # Wait for download process to finish & save the downloaded file on given path
        download.save_as(".\\" + download.suggested_filename)

        # ---------------------
        context.close()
        browser.close()
            
        

download_file_demo()