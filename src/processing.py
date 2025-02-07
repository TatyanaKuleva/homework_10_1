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


# def sort_by_date(data_dict: list[dict], sort_sequence: bool = True) -> list[dict]:
#     """сортирует список словарей по дате транзакции в соответствии с выбранным вариантом сортировки"""
#     sorted_by_date_list = sorted(data_dict, key=lambda x: (x['date'], x['id']), reverse=sort_sequence)
#     return sorted_by_date_list
