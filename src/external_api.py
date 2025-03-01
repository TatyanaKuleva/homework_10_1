import os
import requests
from dotenv import load_dotenv


def convertion_currency(amount: str, currency: str):
    """функция конвертации валюты в рубли с помощью Exchange Rates Data API"""
    load_dotenv('.env')
    API_KEY = os.getenv('API_KEY')
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": f"{API_KEY}"}

    response = requests.get(url, headers=headers)


    if response.status_code != 200:
        return False

    result = response.json()
    rub_amount = float(result["result"])

    return rub_amount


if __name__== '__main__':
    print(convertion_currency("1.0", "USD"))



