import os
import pytest
from dotenv import load_dotenv
from fredclient.endpoints import FredClient

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("FRED_API_KEY")

@pytest.fixture(scope="module")
def fred():
    return FredClient(api_key=API_KEY)

def test_get_all_endpoints(fred):
    endpoints = fred.get_all_endpoints()
    assert isinstance(endpoints, list)
    assert "get_series" in endpoints

def test_describe_endpoint(fred):
    doc = fred.describe_endpoint("get_series")
    assert "Required parameters:" in doc
    assert "series_id" in doc

def test_get_series(fred):
    response = fred.get_series(series_id="GNPCA")
    assert isinstance(response, dict)
    assert "seriess" in response

def test_get_category_series(fred):
    response = fred.get_category_series(category_id=125)
    assert isinstance(response, dict)
    assert "seriess" in response

def test_get_series_search(fred):
    response = fred.get_series_search(search_text="unemployment")
    assert isinstance(response, dict)
    assert "seriess" in response

def test_get_series_observations(fred):
    response = fred.get_series_observations(series_id="GNPCA")
    assert isinstance(response, dict)
    assert "observations" in response

def test_invalid_param_type(fred):
    with pytest.raises(TypeError):
        fred.get_series(series_id=123)  # should be str

def test_missing_required_param(fred):
    with pytest.raises(ValueError):
        fred.get_series()  # missing series_id
