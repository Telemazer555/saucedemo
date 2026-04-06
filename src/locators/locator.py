import os
import faker
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
faker = faker.Faker()


class Login:
    LoginUsername = ('[id="user-name"]')
    LoginPassword = ('[id="password"]')
    LoginButton = ('[id="login-button"]')


class Inventory:
    Basket = '[id="shopping_cart_container"]'
    Basket_Count = '.shopping_cart_badge'
    Checkout = '[id="checkout"]'
    Inventory_Item = '[id="add-to-cart-sauce-labs-backpack"]'
    Add_Buttons = 'button.btn.btn_primary.btn_small.btn_inventory:has-text("Add to cart")'
    Continue_shopping = 'button.btn.btn_secondary.back.btn_medium:has-text("Continue Shopping")'
    Continue_shopping_text = 'button:has-text("Continue Shopping")'
    Shopping_text_content = '[data-test="inventory-item-price"]'


class Checkout:
    FirstName = ('[id="first-name"]')
    LastName = ('[id="last-name"]')
    ZipCode = ('[id="postal-code"]')
    Continue = ('[id="continue"]')
    Finish = ('[id="finish"]')
    Prise = (".summary_subtotal_label")
    Total_price = ('.summary_total_label')


class Logout:
    BurgerMenu = ('[id="react-burger-menu-btn"]')
    Logout = ('[id="logout_sidebar_link"]')


class Creds:
    # Сначала проверяем наличие .env файла
    if not Path('.env').exists():
        print("\n" + "=" * 190)
        print("❌ ОШИБКА: Файл .env не найден")
        print("=" * 190)
        print("🔧 Создайте файл .env с конфигурацией")
        print("📋 Инструкция в README.md")
        print("=" * 190 + "\n")
        raise FileNotFoundError("Необходимо создать файл .env с конфигурацией")

    # Загружаем переменные окружения из .env файла

    # Проверяем BASE_URL
    BASE_URL = os.environ.get('BASE_URL')
    if BASE_URL is None or BASE_URL.strip() == "":
        print("\n" + "=" * 190)
        print("❌ ОШИБКА: BASE_URL не найдена или пуста в .env файле")
        print("=" * 190)
        print("🔧 Добавьте BASE_URL в файл .env")
        print("\n📋 Пример:")
        print('  BASE_URL=https://www.saucedemo.com')
        print("=" * 190 + "\n")
        raise ValueError("Необходимо указать BASE_URL в .env файле")
    else:
        print(f"✓ BASE_URL загружен: {BASE_URL}")

    # Проверяем USERNAME (простая строка, не JSON)
    USERNAME = os.environ.get('USERNAME')
    if USERNAME is None or USERNAME.strip() == "":
        print("\n" + "=" * 190)
        print("❌ ОШИБКА: USERNAME не найдена или пуста в .env файле")
        print("=" * 190)
        print("🔧 Добавьте USERNAME в файл .env")
        print("\n📋 Пример:")
        print('  USERNAME=standard_user')
        print("=" * 190 + "\n")
        raise ValueError("Необходимо указать USERNAME в .env файле")
    else:
        print(f"✓ USERNAME загружен: {USERNAME}")

    # Проверяем PASSWORD (простая строка, не JSON)
    PASSWORD = os.environ.get('PASSWORD')
    if PASSWORD is None or PASSWORD.strip() == "":
        print("\n" + "=" * 190)
        print("❌ ОШИБКА: PASSWORD не найдена или пуста в .env файле")
        print("=" * 190)
        print("🔧 Добавьте PASSWORD в файл .env")
        print("\n📋 Пример:")
        print('  PASSWORD=secret_sauce')
        print("=" * 190 + "\n")
        raise ValueError("Необходимо указать PASSWORD в .env файле")
    else:
        print(f"✓ PASSWORD загружен")

    FIRST_NAME = faker.first_name()
    LAST_NAME = faker.last_name()
    ZIP_CODE = faker.zipcode()
