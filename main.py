from playwright.sync_api import sync_playwright
from src.locators.locator import Login ,Inventory, Checkout, Logout
import time
from test.conftest import timeit

@timeit
def login():
    playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False, slow_mo=100)
    browser = playwright.chromium.launch(executable_path='/Users/desertik/Library/Caches/ms-playwright/chromium-1179/chrome-mac/Chromium.app/Contents/MacOS/Chromium', headless=False, slow_mo=100)

    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.wait_for_selector(Login.LoginUsername)
    page.fill(Login.LoginUsername , "standard_user")
    page.fill(Login.LoginPassword , "secret_sauce")
    page.click(Login.LoginButton)
    # time.sleep(3)

    page.click(Inventory.Inventory_Item)
    page.click(Inventory.Basket)
    page.click(Inventory.Checkout)
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

class LoginPage:

    login_1 =('.login-button:has-text("Войти как сотрудник РОЛЬФ")')
    LoginUsername = ('[id="username"]')
    LoginPassword = ('[id="password"]')
    LogiGO = ('[id="kc-login"]')
    # AddAM = ('.or-button.or-button_color-pink.or-button_m.or-button_square.or-button_primary.or-button_slot_empty.add-button--mobile')
    # AddAM = (".or-icon or-button__icon_before")
    AddAM = ('.or-button__text t2')
    # Находим radio-button, который находится внутри элемента, содержащего нужный текст

@timeit
def loginPP():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(executable_path='/Users/desertik/Library/Caches/ms-playwright/chromium-1179/chrome-mac/Chromium.app/Contents/MacOS/Chromium', headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto('https://dev-basecp-frt.rolf.loc:8443/auth/login')
    page.click(LoginPage.login_1)
    page.fill(LoginPage.LoginUsername , "user_spbv1")
    page.fill(LoginPage.LoginPassword , "mPKOv8kXSf0h")
    page.click(LoginPage.LogiGO)
    page.click(LoginPage.AddAM)
    button = page.locator('.or-button__text', has_text="Добавить КП")
    button.click()

    time.sleep(3)
    browser.close()
    playwright.stop()



