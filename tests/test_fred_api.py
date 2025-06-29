import pytest
from fredclient.fred import FredAPI
import os

@pytest.fixture
def fred():
    api_key = os.getenv("FRED_API_KEY", "DUMMY_KEY")
    return FredAPI(api_key=api_key)

def test_series_observations(monkeypatch, fred):
    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"observations": [{"date": "2022-01-01", "value": "1.0"}]}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = fred.get_series_observations(series_id="GDP")
    assert "observations" in response
    assert isinstance(response["observations"], list)

def test_category(monkeypatch, fred):
    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {"categories": [{"id": 125, "name": "Money"}]}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = fred.get_category(category_id=125)
    assert "categories" in response
