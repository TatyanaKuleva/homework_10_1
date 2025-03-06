import json
import logging
from src.external_api import convertion_currency


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s -%(name)s - %(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_data_transaction(path: str) -> list:
    """функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакция"""
    try:
        utils_logger.info(f"сохранен в файл {path} список транзакций")
        with open(path, "r", encoding="utf-8") as data_file:
            data_transaction = json.load(data_file)
            return data_transaction
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as ex:
        utils_logger.error(f"произошла ошибка {ex}")
        return []


def sum_one_transction(transactrion: dict) -> float:
    """функция принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    utils_logger.info("получаем данные о транзакции и определяем валюту заданной транзакции")
    if transactrion["operationAmount"]["currency"]["code"] == "RUB":
        amount_data = transactrion["operationAmount"]["amount"]
        utils_logger.info("выводим сумму транзакции в рублях")
        return float(amount_data)
    else:
        utils_logger.info("конвертируем в рубли и выводим сумму транзакции")
        currency_code = transactrion["operationAmount"]["currency"]["code"]
        transactrion_amount = transactrion["operationAmount"]["amount"]
        convertion_sum = round(convertion_currency(transactrion_amount, currency_code), 2)
        return convertion_sum


if __name__ == "__main__":
    print(sum_one_transction({"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}))
