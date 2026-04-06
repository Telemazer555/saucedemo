from playwright.async_api import expect, Page
from src.locators.locator import Creds
import random

class BasePageAsync:
    __BASE_URL = Creds.BASE_URL

    def __init__(self, page: Page):
        self.page = page
        self._endpoint = ""

    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self._endpoint}"

    async def navigate_to(self):
        """Асинхронная навигация на страницу"""
        full_url = self._get_full_url()
        await self.page.goto(full_url)
        await self.page.wait_for_load_state('load')
        await expect(self.page).to_have_url(full_url)

    async def wait_for_selector_and_locator(self, selector):
        """Асинхронное ожидание селектора и получение локатора"""
        await self.page.wait_for_selector(selector)
        locator = self.page.locator(selector)
        return locator

    async def wait_for_selector_and_click(self, selector):
        """Асинхронное ожидание селектора и клик"""
        await self.page.wait_for_selector(selector)
        await self.page.click(selector)

    async def wait_for_selector_and_fill(self, selector, value):
        """Асинхронное ожидание селектора и заполнение поля"""
        await self.page.wait_for_selector(selector)
        await self.page.fill(selector, value)

    async def wait_for_selector_and_type(self, selector, value, delay):
        """Асинхронное ожидание селектора и печать с задержкой"""
        await self.page.wait_for_selector(selector)
        await self.page.type(selector, value, delay=delay)

    async def assert_element_is_visible(self, selector):
        """Асинхронная проверка видимости элемента"""
        await expect(self.page.locator(selector)).to_be_visible()

    async def assert_text_present_on_page(self, text):
        """Асинхронная проверка наличия текста на странице"""
        await expect(self.page.locator("body")).to_contain_text(text)

    async def assert_text_in_element(self, selector, text):
        """Асинхронная проверка текста в элементе"""
        await expect(self.page.locator(selector)).to_have_text(text)

    async def assert_input_value(self, selector, expected_value):
        """Асинхронная проверка значения в поле ввода"""
        await expect(self.page.locator(selector)).to_have_value(expected_value)

    @staticmethod
    def generate_random_index_locators(length_a, length_b, locators):
        """Статический метод (синхронный, не требует await)"""
        index = random.randint(length_a, length_b)
        random_index = locators.nth(index)
        return random_index