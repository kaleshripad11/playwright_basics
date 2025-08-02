from playwright.sync_api import Page,expect
import re, time

def test_perform_search(page: Page):
    page.wait_for_timeout(1000)
    page.goto("https://www.google.com/ncr")
    time.sleep(5)

    try:
        page.get_by_role("button", name="Accept all").click(timeout=1000)
    except:
        print("No popup to accept")

    page.get_by_role("combobox", name="search").fill("Playwright python")
    page.keyboard.press("Enter")
    time.sleep(5)
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))