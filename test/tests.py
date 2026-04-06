from src.pages.login_page import *
from src.pages.checkout_page import *
from src.pages.inventory_page import *
import pytest
import asyncio


class TestSync:

    def test_1product_and_logout(self, login_page, inventory_page, checkout_page):
        login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        inventory_page.add_first_item_to_cart()
        checkout_page.start_checkout()
        checkout_page.fill_checkout_form(Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE)
        login_page.logout()

    def test_1_random_product_and_logout(self, login_page, inventory_page, checkout_page):
        login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        inventory_page.add_one_random_item_to_cart()
        checkout_page.start_checkout()
        checkout_page.fill_checkout_form(Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE)
        login_page.logout()

    def test_4_random_product_and_logout(self, login_page, inventory_page, checkout_page):
        login_page.login(username=Creds.USERNAME, password=Creds.PASSWORD)
        inventory_page_summ = inventory_page.add_multiple_random_item_to_cart()
        checkout_page.start_checkout()
        finished_summ = checkout_page.fill_checkout_form(Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE)
        assert inventory_page_summ != finished_summ
        login_page.logout()


class TestAsync:

    @pytest.mark.asyncio
    async def test_as_update_and_get_and_delete1(self, async_browser, app_factory):
        # Вариант 1 вынесения объявлений в отдельный блок
        async def login_task1(app):
            await app.login_page.async_login(Creds.USERNAME, Creds.PASSWORD)
            await app.inventory_page.as_add_first_item_to_cart()
            await app.checkout_page.start_checkout()
            await app.checkout_page.fill_checkout_form(Creds.FIRST_NAME, Creds.LAST_NAME, Creds.ZIP_CODE)
            await app.login_page.async_logout()

        app1 = await app_factory()
        app2 = await app_factory()

        tasks = [login_task1(app1), login_task1(app2), ]
        await asyncio.gather(*tasks)
        # С определением прямо в тесте
        async def login_task2():
            # Создаём НОВЫЙ КОНТЕКСТ для каждой задачи (изолированное окружение)
            context = await async_browser.new_context()
            page = await context.new_page()

            try:
                login_page = LoginPageAsync(page)
                async_checkout_page = CheckoutPageAsync(page)
                inventory_page = InventoryPageAsync(page)

                await login_page.async_login(username=Creds.USERNAME, password=Creds.PASSWORD)
                await inventory_page.as_add_multiple_random_item_to_cart()
                await async_checkout_page.start_checkout()
                await async_checkout_page.fill_checkout_form(
                    Creds.FIRST_NAME,
                    Creds.LAST_NAME,
                    Creds.ZIP_CODE
                )
                await login_page.async_logout()
            finally:
                await page.close()
                await context.close()

        async def login_task3():

            context = await async_browser.new_context()
            page = await context.new_page()
            try:
                login_page = LoginPageAsync(page)
                async_checkout_page = CheckoutPageAsync(page)
                inventory_page = InventoryPageAsync(page)

                await login_page.async_login(username=Creds.USERNAME, password=Creds.PASSWORD)
                await inventory_page.as_add_one_random_item_to_cart()
                await async_checkout_page.start_checkout()
                await async_checkout_page.fill_checkout_form(
                    Creds.FIRST_NAME,
                    Creds.LAST_NAME,
                    Creds.ZIP_CODE
                )
                await login_page.async_logout()
            finally:
                await page.close()
                await context.close()  # Закрываем контекст

        # Запускаем
        # tasks = [login_task3() for _ in range(2)]
        # tasks = [login_task2() for _ in range(2)]
        tasks = [login_task2(), login_task3(), login_task2(), login_task3()]
        await asyncio.gather(*tasks)
