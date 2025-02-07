import pytest
from src.processing import filter_by_state, sort_by_date
from tests.conftest import get_data_dict_no_status


def test_get_filter_by_test_right_result(get_data_dict, result_data_dict):
    assert filter_by_state(get_data_dict) == result_data_dict

def test_get_filter_by_test_no_status_for_filtr(result_data_dict, status_canceled):
    with pytest.raises(ValueError) as dict_no_status_for_filtr:
        filter_by_state(result_data_dict, status_canceled)

def test_get_filter_by_test_no_status(get_data_dict_no_status, status_executed):
    with pytest.raises(ValueError) as dict_no_status_for_filtr:
        filter_by_state(get_data_dict_no_status, status_executed)

def test_sort_by_date_right_result(get_data_dict, list_dict_sorted_by_descending):
    assert sort_by_date(get_data_dict) == list_dict_sorted_by_descending

def test_sort_by_date_same_dates(get_list_dict_same_dates, result_list_dict_same_dates):
    assert sort_by_date(get_list_dict_same_dates) == result_list_dict_same_dates

def test_sort_by_date_mis_date(get_list_dict_mis_date):
    with pytest.raises(ValueError) as dict_mis_date:
       sort_by_date(get_list_dict_mis_date)


