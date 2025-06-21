


def test_playwrightBasics(playwright):
    playwright.chromium.launch(headless=False).new_page().goto("https://www.google.com")