from src.pages.login_page import *
from src.pages.inventory_page import *
from src.pages.checkout_page import *

class AppPages:
    def __init__(self, page, context):
        self.page = page
        self.context = context

        self.login_page = LoginPageAsync(page)
        self.inventory_page = InventoryPageAsync(page)
        self.checkout_page = CheckoutPageAsync(page)

    async def close(self):
        await self.page.close()
        await self.context.close()