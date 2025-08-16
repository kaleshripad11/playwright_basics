from playwright.sync_api import sync_playwright

def scrape_amazon_products():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to Amazon
        page.goto("https://www.amazon.in/")

        #page.get_by_role("button", name="Continue shopping").click()

        page.get_by_placeholder("Search Amazon.in").fill("laptops")
        # page.press("button[placeholder='Continue shopping']",key="Enter")

        page.get_by_role("button", name="laptops under 50k+").click()
        
        # Wait for products to load (AJAX content)
        page.wait_for_selector("div[data-component-type='s-search-result']")
        
        # Wait for network to be idle
        page.wait_for_load_state("networkidle")
        
        # Extract product info
        products = page.query_selector_all("div[data-component-type='s-search-result']")
        print(f"Found {len(products)} products")
        
        for product in products[:5]:  # First 5 products
            title = product.query_selector("h2").inner_text().strip()
            price = product.query_selector(".a-price .a-offscreen").inner_text().strip()
            print(f"Product: {title}\nPrice: {price}\n")
        
        browser.close()

scrape_amazon_products()