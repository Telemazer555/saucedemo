import os
import faker

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
faker = faker.Faker()

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