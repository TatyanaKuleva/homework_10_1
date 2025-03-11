from unittest.mock import patch, Mock, mock_open
import unittest
import pandas as pd
import json
from src. func_get_data_csv_excel import read_excel_file, read_csv_file


@patch('pandas.read_csv')
def test_read_csv_valid_data(mock_read_csv):
    mock_data = pd.DataFrame({'id': [1], 'amount': [100]})
    mock_read_csv.return_value = mock_data
    assert read_csv_file("test.csv") == [{'id': 1, 'amount': 100}]

@patch('pandas.read_excel')
def test_read_excel_valid_data(mock_read_excel):
    mock_data = pd.DataFrame({'id': [1], 'amount': [100]})
    mock_read_excel.return_value = mock_data
    assert read_excel_file("test.excel") == [{'id': 1, 'amount': 100}]




@patch('pandas.read_excel')
def test_get_data_from_excel(mock_read_excel):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Name": ["Sarah", "Mark", "John"]})
    mock_read_excel.return_value = mock_data

    result = read_excel_file("fake")
    expected = [
        {"id": "1", "Name": "Sarah"},
        {"id": "2", "Name": "Mark"},
        {"id": "3", "Name": "John"},
    ]
    assert result == expected