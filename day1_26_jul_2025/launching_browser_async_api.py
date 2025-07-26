from playwright.async_api import async_playwright
import asyncio

# When calling async api in a function, function also should be defined with 'async' as shown below
# In async api every playwright command starts with 'await'
async def launch_browser_using_async_api():
    async with async_playwright() as ap:
        browser = await ap.webkit.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        print(await page.title())
        await browser.close()

if __name__ == "__main__":
    # Use asyncio.run() to call async functions as follows
    asyncio.run(launch_browser_using_async_api())