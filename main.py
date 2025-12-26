from playwright.sync_api import sync_playwright
from locators.locator import Login ,Inventory, Checkout, Logout

import time
from test.conftest import timeit

@timeit
def login():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.fill(Login.LoginUsername , "standard_user")
    page.fill(Login.LoginPassword , "secret_sauce")
    page.click(Login.LoginButton)
    # time.sleep(3)

    page.click(Inventory.Inventory)
    page.click(Inventory.Basket)
    page.click(Inventory.Cehckout)
    # time.sleep(3)

    page.fill(Checkout.FirstName , "Геворг")
    page.fill(Checkout.LastName , "Григорян")
    page.fill(Checkout.ZipCode , "1488")
    page.click(Checkout.Continue)
    page.click(Checkout.Finish)

    page.click(Logout.BurgerMenu)
    page.click(Logout.Logout)

    # time.sleep(3)
    browser.close()
    playwright.stop()


login()