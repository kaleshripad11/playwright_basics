from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio, time

start_time = 0
end_time = 0

def launch_browser():
    start_time = time.time()
    with sync_playwright() as p:
        firefox = p.firefox.launch(headless=False)
        playwright_page = firefox.new_page()
        playwright_page.goto("https://www.google.com")
        print(playwright_page.title())
        firefox.close()
    end_time = time.time()
    print(f"Total time for playwright sync api: {end_time-start_time}")

async def launch_browser_using_async_api():
    start_time = time.time()
    async with async_playwright() as ap:
        browser = await ap.webkit.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        print(await page.title())
        await browser.close()
    end_time = time.time()
    print(f"Total time for playwright async api: {end_time - start_time}")

if __name__ == "__main__":
    # Use asyncio.run() to call async functions as follows
    for i in range(0,5):
        launch_browser()
        asyncio.run(launch_browser_using_async_api())

# Output & time difference in sync & async execution
# Google
# Total time for playwright sync api: 7.618374824523926
# Google
# Total time for playwright async api: 3.0103344917297363
# Google
# Total time for playwright sync api: 7.164842844009399
# Google
# Total time for playwright async api: 3.168748617172241
# Google
# Total time for playwright sync api: 7.142671346664429
# Google
# Total time for playwright async api: 2.76275372505188
# Google
# Total time for playwright sync api: 7.597453594207764
# Google
# Total time for playwright async api: 2.8412084579467773
# Google
# Total time for playwright sync api: 7.254518032073975
# Google
# Total time for playwright async api: 2.7615227699279785   