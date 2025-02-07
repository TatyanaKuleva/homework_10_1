import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_right_result(standart_number_card, result_mask_number_card):
    assert get_mask_card_number(standart_number_card) == result_mask_number_card

@pytest.mark.parametrize('get_number_card', [('123'), ('111111111111111111111111111111111'), (''), ('123455954')])
def test_get_mask_card_number_right_len(get_number_card):
    with pytest.raises(ValueError) as mis_len_number:
        get_mask_card_number(get_number_card)

@pytest.mark.parametrize('get_number_card', [('7000792289FG6361'), ('asdkflfndls;dkfl')])
def test_get_mask_card_number_no_all_digit(get_number_card):
    with pytest.raises(ValueError) as no_digit_number:
        get_mask_card_number(get_number_card)


def test_get_mask_card_account_right_result(standart_number_account, result_mask_number_account):
    assert get_mask_account(standart_number_account) == result_mask_number_account


@pytest.mark.parametrize('get_number_account', [('123'), ('111111111111111111111111111111111'), (''), ('123455954')])
def test_get_mask_card_number_right_len(get_number_account):
    with pytest.raises(ValueError) as mis_len_account:
        get_mask_account(get_number_account)


@pytest.mark.parametrize('get_number_account', [('7365410843013584D05'), ('asdkflfndls;dkfl'), ('7365410843013584 05')])
def test_get_mask_card_number_no_all_digit(get_number_account):
    with pytest.raises(ValueError) as no_digit_account:
        get_mask_account(get_number_account)

