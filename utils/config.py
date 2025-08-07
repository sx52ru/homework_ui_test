# файл конфигурации
# переменные окружения

from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        pass

    BASE_URL = "https://www.demoblaze.com/"

    load_dotenv()
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    ORDER_NAME = os.getenv('ORDER_NAME')
    ORDER_COUNTRY = os.getenv('ORDER_COUNTRY')
    ORDER_CITY = os.getenv('ORDER_CITY')
    CREDIT_CARD = os.getenv('CREDIT_CARD')
    ORDER_MONTH = os.getenv('ORDER_MONTH')
    ORDER_YEAR = os.getenv('ORDER_YEAR')

