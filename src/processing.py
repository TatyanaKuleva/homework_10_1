def filter_by_state(data_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрует список словарей в соответствии с выбранным статусом"""
    new_data_list = []
    for item in data_dict:
        if 'state' not in item.keys():
            raise ValueError (
                'Нет статуса для фильтрации'
            )
        else:
            if item['state'] == state:
                new_data_list.append(item)
        return new_data_list


def sort_by_date(data_dict: list[dict], sort_sequence: bool = True) -> list[dict]:
    """сортирует список словарей по дате транзакции в соответствии с выбранным вариантом сортировки"""
    sorted_by_date_list = sorted(data_dict, key=lambda x: x["date"], reverse=sort_sequence)
    return sorted_by_date_list

