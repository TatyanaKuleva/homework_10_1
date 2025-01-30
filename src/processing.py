from datetime import datetime

def filter_by_state(data_dict: list[dict], state='EXECUTED')->list[dict]:
    new_data_list = []
    for item in data_dict:
        if item['state'] == state:
            new_data_list.append(item)
    return new_data_list

def sort_by_date(data_dict: list[dict], sort_sequence: bool = True)-> list[dict]:
    new_date_list = []
    for item in data_dict:
        if 'date' in item.keys():
            new_date_list.append(item)

    sorted_of_date_list = sorted(
        new_date_list,
        key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=sort_sequence,
    )

    return sorted_of_date_list






