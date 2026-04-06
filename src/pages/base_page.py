from playwright.sync_api import expect
from src.locators.locator import Creds
import random


class BasePage:
    __BASE_URL = Creds.BASE_URL

    def __init__(self, page):
        self.page = page
        self._endpoint = ""

    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self._endpoint}"

    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_locator(self, selector):
        self.page.wait_for_selector(selector)
        locator = self.page.locator(selector)
        return locator

    def wait_for_selector_and_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector, value, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)

    @staticmethod
    def generate_random_index_locators(length_a, length_b, locators):
        index = random.randint(length_a, length_b)
        random_index = locators.nth(index)
        return random_index
