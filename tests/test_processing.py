import pytest
from src.processing import filter_by_state, sort_by_date
from tests.conftest import get_data_dict_no_status


# def test_get_filter_by_test_right_result(get_data_dict, result_data_dict):
#     assert filter_by_state(get_data_dict) == result_data_dict

# def test_get_filter_by_test_no_status_for_filtr(get_data_dict_no_status):
#     with pytest.raises(ValueError) as dict_no_status:
#         filter_by_state(get_data_dict_no_status)

