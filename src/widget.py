import datetime
from datetime import datetime, date
from dateutil.parser import parse


def mask_account_card(type_number: str) -> str:
    """Запрашивает тип и номер карты пользователя или счета и возвращает его с маскированием части данных"""
    part_type_number = type_number.split()
    masks_number = ""
    result_masks = []
    if len(part_type_number) <= 1:
        raise ValueError (
            "Вы ввели не полные данные"
        )
    else:
        for part in part_type_number:
            if part.isdigit():
                if len(part) != 16 and len(part) != 20:
                    raise ValueError(
                        f"Вы ввели не верный номер карты или счета. "
                        f"Количество цифр в номере карты 16, в номере счета 20, "
                        f"вы ввыели {len(part)}."
                    )
                elif len(part) == 16:
                    masks_number = f"{part[:4]} {part[4:6]}{"*" * 2} {"*" * 4} {part[12:]}"
                elif len(part) == 20:
                    masks_number = "**" + part[-4:]
            else:
                result_masks.append(part)
        if masks_number == "":
            raise ValueError(
                "Вы не ввели номер карты или счета"
            )
        else:
            return " ".join(result_masks) + " " + masks_number


def get_date(date_time_coordinate: str) -> str:
    """принимает на вход строку с датой и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    if len(date_time_coordinate) < 10:
        raise ValueError(
            'Нет полных данных о дате транзакции'
        )
    else:
        date_object = parse(date_time_coordinate)
        dt = date_object.date()
        if dt >= date.today():
            raise ValueError(
                f"Отсутствую корректные данные о дате транзакции "
            )
        else:
            date_string = dt.strftime("%d.%m.%Y")
            return date_string


    # dt_string = dt.strftime("%d.%m.%Y")

    # dt = datetime.strptime(date_object, '%Y-%m-%d').date()
    # date_string = date_time_coordinate[0:10]
    # date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
    # dt_string = date_object.strftime("%d.%m.%Y")
    # return dt_string

    # first_version_data = date_time_coordinate[0:10]
    # second_version_data = first_version_data.split("-")
    # result_data = ".".join(second_version_data[::-1])
    # return result_data

if __name__ == "__main__":
    # print(parse('2024-03-11T02:26:18.671407'))
    # print(parse('2021/11/03T02:26:18.671407'))
    # print(parse('11 Mar 2003T02:26:18.671407'))
    print(parse('2024.03.11T02:26:18.671407'))
    print(parse('T02:26:18.671407'))
    print(get_date('2024.03.11T02:26:18.671407'))

