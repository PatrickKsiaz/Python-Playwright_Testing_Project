import time
from playwright.sync_api import Page


def test_playwrightBasics(playwright):
    playwright.chromium.launch(headless=False).new_page().goto("https://rahulshettyacademy.com")


#chromium engine in Headless mode, 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")
    

# -- checking by ID selector #terms .text-info
def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahukshettyacademy")
    page.get_by_label("Password").fill("learn")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role(role:"link", name="terms and conditions").click()
    page.get_by_role(role:"button", name="Sign In").click()
   
    time.sleep(5)  # Wait for 5 seconds to observe the result

    #page.get_by_role("button", name="Sign In").click()
    


    