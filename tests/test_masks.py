from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_card_number_right():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'