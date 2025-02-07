import pytest

@pytest.fixture
def standart_number_card():
    return '7000792289606361'

@pytest.fixture
def result_mask_number_card():
    return '7000 79** **** 6361'

@pytest.fixture
def standart_number_account():
    return '73654108430135874305'

@pytest.fixture
def result_mask_number_account():
    return '**4305'

@pytest.fixture
def get_str_date():
    return '2024-03-11T02:26:18.671407'

@pytest.fixture
def result_str_date():
    return '11.03.2024'
