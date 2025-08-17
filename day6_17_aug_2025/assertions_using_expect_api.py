from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/text-box")

    name_input = page.locator("#userName")
    name_input.fill("Shripad")

    expect(name_input).to_have_value("Shripad")  # Assertion with auto-wait

    page.click("#submit")

    output = page.locator("#name")
    expect(output).to_have_text("Name:Shripad")  # Assertion after submit

    browser.close()