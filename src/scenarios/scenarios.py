from src.pages.login_page import *
from src.pages.inventory_page import *
from src.pages.checkout_page import *
from src.locators.locator import *


class ItemSync:
    """Сценарий сам создаёт page objects — принимает только page"""

    def __init__(self, page):
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.checkout_page = CheckoutPage(page)

    def one_product_and_logout(self):
        """Купить 1 товар и выйти"""
        self.login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        self.inventory_page.add_first_item_to_cart()
        self.checkout_page.start_checkout()
        self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        self.login_page.logout()

    def one_random_product_and_logout(self):
        """Купить 1 случайный товар и выйти"""
        self.login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        self.inventory_page.add_one_random_item_to_cart()
        self.checkout_page.start_checkout()
        self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        self.login_page.logout()

    def four_random_products_and_logout(self):
        """Купить 4 случайных товара и выйти"""
        self.login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        inventory_page_summ = self.inventory_page.add_multiple_random_item_to_cart()
        self.checkout_page.start_checkout()
        finished_summ = self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        assert inventory_page_summ != finished_summ
        self.login_page.logout()


class ItemAsync:
    """Асинхронный сценарий"""

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPageAsync(page)
        self.inventory_page = InventoryPageAsync(page)
        self.checkout_page = CheckoutPageAsync(page)

    async def one_product_and_logout(self):
        await self.login_page.async_login(username=Creds.USERNAME, password=Creds.PASSWORD)
        await self.inventory_page.as_add_first_item_to_cart()
        await self.checkout_page.start_checkout()
        await self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        await self.login_page.async_logout()

    async def one_random_product_and_logout(self):
        await self.login_page.async_login(username=Creds.USERNAME, password=Creds.PASSWORD)
        await self.inventory_page.as_add_one_random_item_to_cart()
        await self.checkout_page.start_checkout()
        await self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        await self.login_page.async_logout()

    async def four_random_products_and_logout(self):
        await self.login_page.async_login(username=Creds.USERNAME, password=Creds.PASSWORD)
        inventory_page_summ = await self.inventory_page.as_add_multiple_random_item_to_cart()
        await self.checkout_page.start_checkout()
        finished_summ = await self.checkout_page.fill_checkout_form(
            Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE
        )
        assert inventory_page_summ != finished_summ
        await self.login_page.async_logout()