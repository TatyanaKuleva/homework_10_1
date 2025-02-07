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

@pytest.fixture
def status_canceled():
    return 'CANCELED'

@pytest.fixture
def status_executed():
    return 'EXECUTED'

@pytest.fixture
def get_data_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def result_data_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def get_data_dict_no_status():
    return [{'id': 41428829,  'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def list_dict_sorted_by_descending():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def get_list_dict_same_dates():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def result_list_dict_same_dates():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def get_list_dict_mis_date():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '02:08:58.425572'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
