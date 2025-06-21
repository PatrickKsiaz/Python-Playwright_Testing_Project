from playwright.sync_api import Page


def test_playwrightBasics(playwright):
    playwright.chromium.launch(headless=False).new_page().goto("https://rahulshettyacademy.com")


#chromium engine in Headless mode, 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")
    
