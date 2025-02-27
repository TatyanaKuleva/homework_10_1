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
    if transactrion['operationAmount']['currency']['code'] == "USD" or 'EUR':
        sum_trans = transactrion['operationAmount']['amount']
        convertion_sum = convertion_currency(sum_trans, transactrion['operationAmount']['currency']['code'])
        return convertion_sum
    sum_trans = transactrion['operationAmount']['amount']
    return sum_trans



if __name__== '__main__':
    data_trans = get_data_transaction('../data/operations.json')
    for data in data_trans:
        print(sum_one_transction(data))






