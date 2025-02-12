import datetime
from datetime import datetime, date
from dateutil.parser import parse


def mask_account_card(type_number: str) -> str:
    """Запрашивает тип и номер карты пользователя или счета и возвращает его с маскированием части данных"""
    part_type_number = type_number.split()
    masks_number = ""
    result_masks = []
    if len(part_type_number) <= 1:
        raise ValueError("Вы ввели не полные данные")
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
            raise ValueError("Вы не ввели номер карты или счета")
        else:
            return " ".join(result_masks) + " " + masks_number


def get_date(date_time_coordinate: str) -> str:
    """принимает на вход строку с датой и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    if date_time_coordinate[0] == "T" or "T" not in date_time_coordinate:
        raise ValueError("Нет полных данных о дате транзакции")
    else:
        date_object = parse(date_time_coordinate)
        dt = date_object.date()
        if dt >= date.today():
            raise ValueError(f"Отсутствуют корректные данные о дате транзакции ")
        else:
            date_string = dt.strftime("%d.%m.%Y")
            return date_string
