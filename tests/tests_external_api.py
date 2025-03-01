from unittest.mock import patch, Mock
import requests
from src.external_api import convertion_currency



def test_get_convertion_currency():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 89.340238}

    with patch('requests.get', return_value=mock_response):
        result = convertion_currency("1.0","USD")
        assert result == 89.340238

def test_convertion_currency_failed_request():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.return_value = False

    with patch('requests.get', return_value=mock_response):
        result = convertion_currency("1.0", "USD")
        assert result == False

