import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('get_type_number, result_type_number', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                                 ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card_right_result(get_type_number, result_type_number):
    assert mask_account_card(get_type_number) == result_type_number

@pytest.mark.parametrize('get_data_type_number, result_data_type_number',[('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                                          ('Счет 64686473678894779589', 'Счет **9589'),
                                                                          ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                                                          ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                                          ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                                                          ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                                                          ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card_diff_data(get_data_type_number, result_data_type_number):
    assert mask_account_card(get_data_type_number) == result_data_type_number

@pytest.mark.parametrize('get_type_number_mis', [('Master 123'), ('111111111111111111111111111111111'), (''), ('123455954')])
def test_mask_account_card_len(get_type_number_mis):
    with pytest.raises(ValueError) as mis_len_type_number:
        mask_account_card(get_type_number_mis)

@pytest.mark.parametrize('get_data_mis', [('1596837868705199'), ('64686473678894779589'), ('Master Card'), ('Счет')])
def test_mask_account_card_len(get_data_mis):
    with pytest.raises(ValueError) as incomplete_data:
        mask_account_card(get_data_mis)


def test_get_date_right_result(get_str_date, result_str_date):
    assert get_date(get_str_date) == result_str_date

