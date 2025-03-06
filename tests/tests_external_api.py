from unittest.mock import patch, Mock
import requests
from src.external_api import convertion_currency, cache
from dotenv import load_dotenv
import  os
from cachetools import Cache



load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

def reset_cache():
    cache.clear()


def test_get_convertion_currency():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 89.340238}

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = convertion_currency("1.0","USD")
        assert result == 89.340238
        mock_get.assert_called_once_with("1.0","USD")



def test_convertion_currency_failed_request():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.return_value = False

    with patch('requests.get', return_value=mock_response):
        result = convertion_currency("1.0", "USD")
        assert result == False

def test_get_convertion_currency_cache():
    reset_cache()

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 89.340238}

    with patch('requests.get', return_value=mock_response) as mock_get:
        result = convertion_currency("1.0", "USD")
        assert result == 89.340238
        mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1.0", headers={"apikey": f"{API_KEY}"})

        result_cached = convertion_currency("1.0", "USD")
        assert result_cached == 89.340238
        mock_get.assert_called_once()




