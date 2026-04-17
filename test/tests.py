import pytest
import asyncio


class TestSync:

    def test_1product_and_logout(self, item_sync):
        item_sync.one_product_and_logout()

    def test_1_random_product_and_logout(self, item_sync):
        item_sync.one_random_product_and_logout()

    def test_4_random_product_and_logout(self, item_sync):
        item_sync.four_random_products_and_logout()


class TestAsync:

    @pytest.mark.asyncio
    async def test_parallel_all(self, item_async_factory):
        item1 = await item_async_factory()
        item2 = await item_async_factory()
        item3 = await item_async_factory()
        tasks = [
            item1.one_product_and_logout(),
            item2.one_random_product_and_logout(),
            item3.four_random_products_and_logout(),
        ]
        await asyncio.gather(*tasks)

    @pytest.mark.asyncio
    async def test_parallel_all(self, item_async_factory):
        items = [await item_async_factory() for _ in range(12)]
        tasks = [item.four_random_products_and_logout() for item in items]
        await asyncio.gather(*tasks)
