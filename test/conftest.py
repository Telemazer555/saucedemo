import pytest_asyncio
import pytest
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from src.pages.session_page import *


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        executable_path='/Users/desertik/Library/Caches/ms-playwright/chromium-1179/chrome-mac/Chromium.app/Contents/MacOS/Chromium',
        headless=False, slow_mo=200)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture(scope="function")
def checkout_page(page):
    return CheckoutPage(page)


# Async ######################################################################


@pytest_asyncio.fixture
async def async_browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            executable_path='/Users/desertik/Library/Caches/ms-playwright/chromium-1179/chrome-mac/Chromium.app/Contents/MacOS/Chromium',
            headless=False,
            slow_mo=100
        )
        yield browser
        await browser.close()
        await playwright.stop()


@pytest_asyncio.fixture
async def app_factory(async_browser):
    apps = []
    async def _create():
        context = await async_browser.new_context()
        page = await context.new_page()
        app = AppPages(page, context)
        apps.append(app)
        return app
    yield _create
    for app in apps:
        await app.close()
