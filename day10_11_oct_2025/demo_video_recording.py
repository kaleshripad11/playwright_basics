# In playwright screens can be recording during test executions using context object
# Videos/screen recordings are saved to browser context closure at the end of the tests execution
# Hence its mandatory to call browser_context.close() to save recordings
# Below is the code to demonstrate - Playwright's built in video/screen recording feature

from playwright.sync_api import sync_playwright, expect

def demo_video_recording_using_playwright():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=1000)
        context = browser.new_context(
                viewport={'width':1920, 'height':1080}, 
                screen={'width':1920, 'height':1080},
                record_video_dir="..\\screenshots",    # Capture video recording
                record_video_size={"width":1920, "height":1080}         # Set video resolution/size
            )
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_role("textbox", name="Username").fill("Admin")
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_alt_text("client brand banner")).to_be_visible()
        print(page.video)       # Will print the page URL for which video is recorded
        context.close()
        browser.close()

demo_video_recording_using_playwright()