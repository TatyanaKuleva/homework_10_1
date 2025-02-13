def filter_by_currency(list_transction, type_currence):
    "Фильтрует список транзакций в указаной валюте"
    if len(list_transction) == 0:
        raise ValueError("Нет данных для фильтрации")
    else:
        for transaction in list_transction:
            if transaction["operationAmount"]["currency"]["name"] == type_currence:
                yield transaction


def transaction_descriptions(list_transction):
    "принимает список транзакций и возвращает описание каждой операции"
    if len(list_transction) == 0:
        raise ValueError("Нет данных для вывода либо список транзакций пуст")
    else:
        for transaction in list_transction:
            yield transaction["description"]


def card_number_generator(start, stop):
    "Генерирует номера карт в заданном диапазоне"
    if start < 1 or stop > 9999999999999999:
        raise ValueError("Вы ввели неверные данные для формирования номера")
    else:
        for i in range(start, stop + 1):
            card_number = f"{i:016}"
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
