import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, timeout=60000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
