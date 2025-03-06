from typing import Union
import logging

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s -%(name)s - %(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> Union[str, int]:
    """Запрашивает номер карты пользователя и возвращает его с маскированием части данных"""
    masks_logger.info(f"получил у пользователя номер {card_number} для маскирования")
    mask_card_number = "*"
    masks_logger.info(f"проверка введенного номера {card_number} на соответсвие длине символов")
    if len(card_number) != 16:
        masks_logger.error(f"номер карты {len(card_number)} не соответствует необходимой длине 16")
        raise ValueError(
            f"Вы ввели не верный номер карты. " f"Количество цифр в номере карты 16, " f"вы ввыели {len(card_number)}."
        )
    masks_logger.info(f"проверка введенного номера {card_number} на наличие символов помимо цифр")
    if not card_number.isdigit():
        masks_logger.error(f"номер карты содержит не только цифры")
        raise ValueError(f"Вы ввели не верный номер карты. Номер должен содержать только цифры")
    masks_logger.info(f"успешный результат маскирования номера карта {card_number}")
    return f"{card_number[:4]} {card_number[4:6]}{mask_card_number * 2} {mask_card_number * 4} {card_number[12:]}"


def get_mask_account(account_number: str) -> Union[str, int]:
    """Запрашивает номер банковского счета пользователя и возвращает его с маскированием части данных"""
    masks_logger.info(f"получил у пользователя счета {account_number} для маскирования")
    masks_logger.info(f"проверка введенного номера счета {account_number} на соответсвие длине символов")
    if len(account_number) != 20:
        masks_logger.error(f"номер счета {len(account_number)} не соответствует необходимой длине 20")
        raise ValueError(
            f"Вы ввели не верный номер счета. "
            f"Количество цифр в номере счета 20, "
            f"вы ввыели {len(account_number)}."
        )
    masks_logger.info(f"проверка введенного номера {account_number} на наличие символов помимо цифр")
    if not account_number.isdigit():
        masks_logger.error(f"номер счета содержит не только цифры")
        raise ValueError(f"Вы ввели не верный номер счета. Номер должен содержать только цифры")
    return "**" + account_number[-4:]
