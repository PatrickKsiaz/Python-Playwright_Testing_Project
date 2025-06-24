def test_UIvalidationDynamicScript(page= Page):
    #iphone X , Nokia Edge - verify 2 items are showing in the cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahukshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role(role="button", name="Sign In").click()
    page.locator("app-card").filter("has_text='Iphone X'").get_by_role("button", name="Add to Cart").click()
    page.locator("app-card").filter("has_text='Nokia Edge'").get_by_role("button", name="Add to Cart").click()
    


