from src.locators.locator import *
from src.pages.base_page import BasePage
from src.pages.base_page_async import BasePageAsync


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(Inventory.Inventory_Item)
        self.assert_element_is_visible(Inventory.Basket)
        self.wait_for_selector_and_click(Inventory.Basket)

    def add_multiple_random_item_to_cart(self):
        all_buttons = self.wait_for_selector_and_locator(Inventory.Add_Buttons)
        self.generate_random_index_locators(0, 5, all_buttons).click()
        self.generate_random_index_locators(0, 4, all_buttons).click()
        self.generate_random_index_locators(0, 3, all_buttons).click()
        self.generate_random_index_locators(0, 2, all_buttons).click()

        button_count = self.wait_for_selector_and_locator(Inventory.Basket_Count)
        Count = button_count.text_content()

        assert int(Count) == 4, f"В корзине должно быть 4 а у нас {int(Count)}"

        self.assert_element_is_visible(Inventory.Basket)
        self.wait_for_selector_and_click(Inventory.Basket)
        self.assert_element_is_visible(Inventory.Continue_shopping)

        all_prices = self.wait_for_selector_and_locator(Inventory.Continue_shopping_text).locator('../..').locator(
            Inventory.Shopping_text_content).all_text_contents()

        print(f"Все цены: {all_prices}")
        first_price = sum(float(price.replace('$', '')) for price in all_prices)
        first_sum = f"Item total: ${first_price}"
        return first_sum

    def add_one_random_item_to_cart(self):
        all_buttons = self.wait_for_selector_and_locator(Inventory.Add_Buttons)
        self.generate_random_index_locators(0, 5, all_buttons).click()

        button_count = self.wait_for_selector_and_locator(Inventory.Basket_Count)
        Count = button_count.text_content()

        assert int(Count) == 1, f"В корзине должно быть 1 а у нас {int(Count)}"

        self.assert_element_is_visible(Inventory.Basket)
        self.wait_for_selector_and_click(Inventory.Basket)
        self.assert_element_is_visible(Inventory.Continue_shopping)

        all_prices = self.wait_for_selector_and_locator(Inventory.Continue_shopping_text
                                                        ).locator('../..').locator(
            Inventory.Shopping_text_content).all_text_contents()

        print(f"Все цены: {all_prices}")
        first_price = sum(float(price.replace('$', '')) for price in all_prices)
        first_sum = f"Item total: ${first_price}"
        return first_sum


class InventoryPageAsync(BasePageAsync):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    async def as_add_first_item_to_cart(self):
        await self.wait_for_selector_and_click(Inventory.Inventory_Item)
        await self.assert_element_is_visible(Inventory.Basket)
        await self.wait_for_selector_and_click(Inventory.Basket)

    async def as_add_multiple_random_item_to_cart(self):
        all_buttons = await self.wait_for_selector_and_locator(Inventory.Add_Buttons)

        # Кликаем на случайные кнопки
        await self.generate_random_index_locators(0, 5, all_buttons).click()
        await self.generate_random_index_locators(0, 4, all_buttons).click()
        await self.generate_random_index_locators(0, 3, all_buttons).click()
        await self.generate_random_index_locators(0, 2, all_buttons).click()

        button_count = await self.wait_for_selector_and_locator(Inventory.Basket_Count)
        Count = await button_count.text_content()
        assert int(Count) == 4, f"В корзине должно быть 4 а у нас {int(Count)}"

        await self.assert_element_is_visible(Inventory.Basket)
        await self.wait_for_selector_and_click(Inventory.Basket)
        await self.assert_element_is_visible(Inventory.Continue_shopping)

        continue_button = await self.wait_for_selector_and_locator(Inventory.Continue_shopping_text)
        all_prices = await continue_button.locator('../..').locator(
            Inventory.Shopping_text_content).all_text_contents()

        first_price = sum(float(price.replace('$', '')) for price in all_prices)
        first_sum = f"Item total: ${first_price}"
        return first_sum

    async def as_add_one_random_item_to_cart(self):
        all_buttons = await self.wait_for_selector_and_locator(Inventory.Add_Buttons)
        await self.generate_random_index_locators(0, 5, all_buttons).click()

        button_count = await self.wait_for_selector_and_locator(Inventory.Basket_Count)
        Count = await button_count.text_content()

        assert int(Count) == 1, f"В корзине должно быть 1 а у нас {int(Count)}"

        await self.assert_element_is_visible(Inventory.Basket)
        await self.wait_for_selector_and_click(Inventory.Basket)
        await self.assert_element_is_visible(Inventory.Continue_shopping)

        continue_button = await self.wait_for_selector_and_locator(Inventory.Continue_shopping_text)
        all_prices = await continue_button.locator('../..').locator(
            Inventory.Shopping_text_content).all_text_contents()

        first_price = sum(float(price.replace('$', '')) for price in all_prices)
        first_sum = f"Item total: ${first_price}"
        return first_sum
