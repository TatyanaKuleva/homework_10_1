from typing import Union


def get_mask_card_number(card_number: str) -> Union[str, int]:
    """Запрашивает номер карты пользователя и возвращает его с маскированием части данных"""
    mask_card_number = "*"
    if len(card_number) != 16:
        raise ValueError(
            f"Вы ввели не верный номер карты. " f"Количество цифр в номере карты 16, " f"вы ввыели {len(card_number)}."
        )
    return f"{card_number[:4]} {card_number[4:6]}{mask_card_number * 2} {mask_card_number * 4} {card_number[12:]}"


def get_mask_account(account_number: str) -> Union[str, int]:
    """Запрашивает номер банковского счета пользователя и возвращает его с маскированием части данных"""
    if len(account_number) != 20:
        raise ValueError(
            f"Вы ввели не верный номер счета. "
            f"Количество цифр в номере счета 20, "
            f"вы ввыели {len(account_number)}."
        )
    return "**" + account_number[-4:]
