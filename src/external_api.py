import requests

def convertion_currency(amount: float, currency: str) -> float:
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount}"

    headers = {
        "apikey": "zzZbE9mmkrkoa3MsaJPHZ4UprySc0MZB"
    }

    response = requests.get(url, headers=headers)

    result = response.json()['result']

    return result


if __name__== '__main__':
    print(convertion_currency(30.0, "USD"))



