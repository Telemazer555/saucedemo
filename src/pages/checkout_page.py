from src.locators.locator import *
from src.pages.base_page import BasePage
from src.pages.base_page_async import BasePageAsync

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(Inventory.Checkout)
        self.assert_element_is_visible(Checkout.FirstName)


    def fill_checkout_form(self, first_name, last_name, postal_code):

        self.wait_for_selector_and_type(Checkout.FirstName,first_name,delay=1)
        self.wait_for_selector_and_type(Checkout.LastName,last_name,delay=1)
        self.wait_for_selector_and_type(Checkout.ZipCode,postal_code,delay=1)
        self.wait_for_selector_and_click(Checkout.Continue)

        prise = self.wait_for_selector_and_locator(Checkout.Prise)
        prise.text_content()
        prise_text = str(prise.text_content())
        total_price =self.wait_for_selector_and_locator(Checkout.Total_price)
        total_price.text_content()
        total_price_text = str(total_price.text_content())

        self.wait_for_selector_and_click(Checkout.Finish)
        return total_price_text


class CheckoutPageAsync(BasePageAsync):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-one.html'

    async def start_checkout(self):
        await self.wait_for_selector_and_click(Inventory.Checkout)
        await self.assert_element_is_visible(Checkout.FirstName)

    async def fill_checkout_form(self, first_name, last_name, postal_code):
        await self.wait_for_selector_and_type(Checkout.FirstName, first_name, delay=1)
        await self.wait_for_selector_and_type(Checkout.LastName, last_name, delay=1)
        await self.wait_for_selector_and_type(Checkout.ZipCode, postal_code, delay=1)
        await self.wait_for_selector_and_click(Checkout.Continue)

        # задумка к тесту
        # prise = await self.wait_for_selector_and_locator(Checkout.Prise)
        # prise_text = str(await prise.text_content())

        total_price = await self.wait_for_selector_and_locator(Checkout.Total_price)
        total_price_text = str(await total_price.text_content())

        await self.wait_for_selector_and_click(Checkout.Finish)
        return total_price_text