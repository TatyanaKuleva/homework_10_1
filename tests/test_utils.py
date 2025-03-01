from unittest.mock import patch, Mock, mock_open
import unittest
import json
from src.utils import get_data_transaction, sum_one_transction


@patch('builtins.open', new_callable=mock_open, read_data='[{"id":1, "amount": 100}]')
def test_test_get_data_transactio(mock_file):
    result = get_data_transaction("file.json")
    assert result == [{"id": 1, "amount": 100}]
    mock_file.assert_called_once_with('file.json', 'r', encoding='utf-8')


@patch('src.utils.sum_one_transction')
def test_sum_one_transction(mock_func):
    mock_func.return_value = 31957.58
    result = sum_one_transction({'operationAmount': {'amount': "31957.58", 'currency': {'code': "RUB"}}})
    assert result == 31957.58

