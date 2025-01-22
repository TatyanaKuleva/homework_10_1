def mask_account_card(type_number: str) -> str:
    """Запрашивает тип и номер карты пользователя или счета и возвращает его с маскированием части данных"""
    part_type_number = type_number.split()
    masks_number = ""
    result_masks = []
    for part in part_type_number:
        if part.isdigit():
            if len(part) != 16 and len(part) != 20:
                raise ValueError(
                    f"Вы ввели не верный номер карты или счета. "
                    f"Количество цифр в номере карты 16, в номере счета 20, "
                    f"вы ввыели {len(part)}."
                )
            elif len(part) == 16:
                masks_number = f"{part[:4]} {part[4:6]}+{"*" * 2} {"*" * 4} {part[12:]}"
            elif len(part) == 20:
                masks_number = "**" + part[-4:]

        else:
            result_masks.append(part)

    return " ".join(result_masks) + " " + masks_number


def get_date(date_time_coordinate: str) -> str:
    """принимает на вход строку с датой и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    first_version_data = date_time_coordinate[0:10]
    second_version_data = first_version_data.split("-")
    result_data = ".".join(second_version_data[::-1])
    return result_data
