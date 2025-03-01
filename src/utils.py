import json
from src.external_api import convertion_currency

def get_data_transaction(path: str) -> list:
    try:
        with open(path, 'r', encoding="utf-8") as data_file:
            data_transaction = json.load(data_file)
            return data_transaction
    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        return []

def sum_one_transction(transactrion: dict) -> float:
    """функция принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    if transactrion['operationAmount']['currency']['code'] == "RUB":
        amount_data = transactrion['operationAmount']['amount']
        return amount_data
    else:
        currency_code = transactrion["operationAmount"]["currency"]["code"]
        transactrion_amount = transactrion["operationAmount"]["amount"]
        convertion_sum = round(convertion_currency(transactrion_amount, currency_code),2)
        return convertion_sum




if __name__== '__main__':
    dict_data =[]
    for index in range(3):
        dict_data.append(get_data_transaction('../data/operations.json')[index])
    for item in dict_data:
        print(sum_one_transction(item))








