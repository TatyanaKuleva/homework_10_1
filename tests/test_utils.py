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
    mock_func.assert_not_called()

@patch("builtins.open", create=True)
def test_get_data_transaction(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = '[{"id": 441945886}]'
    assert get_data_transaction("../data/operations.json") == [{"id": 441945886}]
    mock_open.assert_called_once_with("../data/operations.json", 'r', encoding="utf-8")

@patch("builtins.open", create=True)
def test_get_data_transaction_failed(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = "None"
    assert get_data_transaction("../data/operations.json") == []
    mock_open.assert_called_once_with("../data/operations.json", 'r', encoding="utf-8")











