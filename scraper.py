from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url, save_dir="output"):
    os.makedirs(save_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"[📖] Navigating to: {url}")
        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")

        # Take screenshot
        screenshot_path = os.path.join(save_dir, "screenshot.png")
        page.screenshot(path=screenshot_path, full_page=True)

        # Save HTML
        html_path = os.path.join(save_dir, "chapter.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page.content())

        # Extract text content
        content = page.inner_text("body")[:10000]  # Limit for test
        text_path = os.path.join(save_dir, "chapter.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()

        print(f"[✅] Scraping complete.\n→ Text: {text_path}\n→ Screenshot: {screenshot_path}")

# Example usage
if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scrape_chapter(url)
