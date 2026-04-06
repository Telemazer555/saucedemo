from src.locators.locator import *
from src.pages.base_page import BasePage
from src.pages.base_page_async import BasePageAsync


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(Login.LoginUsername, username)
        self.wait_for_selector_and_fill(Login.LoginPassword, password)
        self.wait_for_selector_and_click(Login.LoginButton)
        self.assert_text_present_on_page("Products")

    def logout(self):
        self.wait_for_selector_and_click(Logout.BurgerMenu)
        self.wait_for_selector_and_click(Logout.Logout)

class LoginPageAsync(BasePageAsync):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    async def async_login(self, username, password):
        await self.navigate_to()
        await self.wait_for_selector_and_fill(Login.LoginUsername, username)
        await self.wait_for_selector_and_fill(Login.LoginPassword, password)
        await self.wait_for_selector_and_click(Login.LoginButton)
        await self.assert_text_present_on_page("Products")

    async def async_logout(self):
        await self.wait_for_selector_and_click(Logout.BurgerMenu)
        await self.wait_for_selector_and_click(Logout.Logout)