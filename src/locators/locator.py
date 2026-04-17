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
    # Проверка .env
    if not Path('.env').exists():
        raise FileNotFoundError("\n[ERROR] .env file not found. Create it with:\n""   BASE_URL, USERNAME, PASSWORD\n")
    BASE_URL = os.environ.get('BASE_URL', '').strip()
    USERNAME = os.environ.get('USERNAME', '').strip()
    PASSWORD = os.environ.get('PASSWORD', '').strip()
    # Собираем все ошибки
    missing = [k for k, v in {'BASE_URL': BASE_URL, 'USERNAME': USERNAME, 'PASSWORD': PASSWORD, }.items() if not v]
    if missing:
        raise ValueError(
            f"\n[ERROR] Missing env variables: {', '.join(missing)}\n" f"   Required: BASE_URL, USERNAME, PASSWORD\n")

    FIRST_NAME = faker.first_name()
    LAST_NAME = faker.last_name()
    ZIP_CODE = faker.zipcode()
