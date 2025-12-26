from playwright.sync_api import sync_playwright
from locators.login import Login as loc
import time
from test.conftest import timeit

@timeit
def login():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.fill(loc.LoginUsername , "standard_user")
    page.fill(loc.LoginPassword , "secret_sauce")
    page.click(loc.LoginButton)
    time.sleep(3)
    browser.close()
    playwright.stop()


login()