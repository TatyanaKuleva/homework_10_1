import re
from collections import Counter

def filter_by_state(data_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрует список словарей в соответствии с выбранным статусом"""
    new_data_list = []
    for item in data_dict:
        if "state" in item.keys():
            if item["state"] == state:
                new_data_list.append(item)
            if len(new_data_list) == 0:
                raise ValueError("Нет данных для указанного типа статуса")
        else:
            raise ValueError("отсутствует статус для фильтрации")

    return new_data_list


def sort_by_date(data_dict: list[dict], sort_sequence: bool = True) -> list[dict]:
    """сортирует список словарей по дате транзакции в соответствии с выбранным вариантом сортировки"""
    for item in data_dict:
        if item["date"][0] == "T" or "T" not in item["date"]:
            raise ValueError("нет даты транзакции для сортировки")

    sorted_by_date_list = sorted(data_dict, key=lambda x: (x["date"], x["id"]), reverse=sort_sequence)
    return sorted_by_date_list

def filtr_by_data_in_string(data_dict: list[dict], search_string: str)->list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска, возвращает список
    словарей, у которых в описании есть данная строка."""
    result = []
    pattern = re.compile(search_string, flags=re.IGNORECASE)
    for item in data_dict:
        if pattern.findall(item['description']):
            result.append(item)
    return result

def filtr_by_category(data_dict: list[dict], category_list: list)->list[dict]:
    fitr_transction_list = []
    result_dict = dict()
    for item in data_dict:
        if item['description'] in category_list:
            fitr_transction_list.append(item['description'])
    counted_category_list = Counter(fitr_transction_list)
    for i in category_list:
        result_dict[i] = counted_category_list[i]
    return result_dict










