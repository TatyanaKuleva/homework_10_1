import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_get_filter_by_currency_right_result(get_list_transaction, result_filtr_transaction):
    usd_transactions = filter_by_currency(get_list_transaction, "USD")
    assert next(usd_transactions) == result_filtr_transaction


def test_get_filter_by_currency_no_date_for_filtr(get_list_transaction):
    filtr_transaction= filter_by_currency(get_list_transaction, "EURO")
    for _ in range(5):
        try:
            print(next(filtr_transaction))
        except:
            print("Нет данных по выбранной валюте")

def test_get_filter_by_empty_dict(get_empty_list):
    usd_transactions = filter_by_currency(get_empty_list, "USD")
    with pytest.raises(ValueError) as empty_list:
        assert next(usd_transactions)

def test_transaction_descriptions_right_result(get_list_transaction):
    descripton_res = transaction_descriptions(get_list_transaction)
    assert next(descripton_res) == "Перевод организации"
    assert next(descripton_res) == "Перевод со счета на счет"
    assert next(descripton_res) == "Перевод со счета на счет"
    assert next(descripton_res) == "Перевод с карты на карту"
    assert next(descripton_res) == "Перевод организации"

def test_transaction_descriptions_epmty_list(get_empty_list):
    descripton_res_empty = transaction_descriptions(get_empty_list)
    with pytest.raises(ValueError) as empty_list:
        assert next(descripton_res_empty)

@pytest.mark.parametrize(
    "start, stop, expected_result",
    [
        ("1", "3", "0000 0000 0000 0001 0000 0000 0000 0002 0000 0000 0000 0003")
    ],
)
def test_card_number_generator_right_result(start, stop, expected_result):
    gen = card_number_generator(start, stop)
    assert next(gen) == expected_result
