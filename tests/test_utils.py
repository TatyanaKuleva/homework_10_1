from unittest.mock import patch, Mock
import requests
from src.utils import get_data_transaction, sum_one_transction


# Пример теста
@patch('operations.json', new_callable=mock_open, read_data='{"operationAmount": {"amount": "31957.58","currency": "name": "руб.", "code": "RUB"}')
def test_test_get_data_transactio(mock_file):
    result = get_data_transaction('../data/operations.json')
    assert result == '{"operationAmount": {"amount": "31957.58","currency": "name": "руб.", "code": "RUB"}'
    mock_file.assert_called_once_with('../data/operations.json', 'r')