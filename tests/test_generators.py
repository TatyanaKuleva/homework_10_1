import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_get_filter_by_currency_right_result(get_list_transaction, result_filtr_transaction):
    usd_transactions = filter_by_currency(get_list_transaction, "USD")
    assert next(usd_transactions) == result_filtr_transaction


def test_get_filter_by_currency_no_date_for_g(get_type_number_mis):
    with pytest.raises(ValueError) as mis_len_type_number:
        mask_account_card(get_type_number_mis)
