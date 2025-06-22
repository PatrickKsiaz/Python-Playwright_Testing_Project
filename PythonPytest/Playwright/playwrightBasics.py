from playwright.sync_api import Page


def test_playwrightBasics(playwright):
    playwright.chromium.launch(headless=False).new_page().goto("https://rahulshettyacademy.com")


#chromium engine in Headless mode, 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")
    

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahukshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.locator("#signInBtn").click()
    assert page.locator(".alert-success").is_visible()

    