from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    
    def handle_dialog(dialog):
        print(f"Dialog type: {dialog.type}")
        print(f"Dialog message: {dialog.message}")
        
        if dialog.type == "alert":
            dialog.accept()
            print("Alert accepted")
        elif dialog.type == "confirm":
            dialog.accept()  # or dialog.dismiss()
            print("Confirm accepted")
        elif dialog.type == "prompt":
            dialog.accept("Hello World")  # Provide input
            print("Prompt accepted with input")
    
    page.on("dialog", handle_dialog)

    urls_list = [
        "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt",
        "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert",
        "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm"
    ]
    
    for url in urls_list:
        page.goto(url)
        result_frame = page.frame_locator("#iframeResult")
        result_frame.get_by_role("button", name="Try it").click()