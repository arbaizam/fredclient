import pytest
import os
from fredclient import endpoints

API_KEY = os.getenv("FRED_API_KEY", "YOUR_API_KEY")


@pytest.mark.parametrize("func_name, kwargs", [
    ("get_category", {"api_key": API_KEY, "category_id": 125}),
    ("get_category_children", {"api_key": API_KEY, "category_id": 125}),
    ("get_category_related", {"api_key": API_KEY, "category_id": 125}),
    ("get_category_series", {"api_key": API_KEY, "category_id": 125}),
    ("get_category_tags", {"api_key": API_KEY, "category_id": 125}),
    ("get_category_related_tags", {"api_key": API_KEY, "category_id": 125, "tag_names": "gdp"}),
    ("get_series", {"api_key": API_KEY, "series_id": "GDP"}),
    ("get_series_categories", {"api_key": API_KEY, "series_id": "GDP"}),
    ("get_series_observations", {
        "api_key": API_KEY,
        "series_id": "GDP",
        "file_type": "json",
        "observation_start": "2020-01-01",
        "observation_end": "2020-12-31"
    }),
    ("get_series_search", {"api_key": API_KEY, "search_text": "unemployment"})
])
def test_fred_endpoints_success(func_name, kwargs):
    func = getattr(endpoints, func_name)
    response = func(**kwargs)
    assert isinstance(response, dict), f"{func_name} did not return a dict"


def test_missing_required_param():
    with pytest.raises(ValueError):
        endpoints.get_category(category_id=125)  # Missing api_key


def test_invalid_param_type():
    with pytest.raises(TypeError):
        endpoints.get_series(api_key=API_KEY, series_id=1234)  # series_id should be str