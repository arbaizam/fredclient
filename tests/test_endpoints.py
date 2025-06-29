import pytest
from fredclient import (
    get_category,
    get_category_children,
    get_category_series,
    get_series,
    get_series_observations
)

DEMO_KEY = "YOUR_API_KEY"  # Replace with your FRED demo or personal key

def test_get_category():
    resp = get_category(api_key=DEMO_KEY, category_id=125)
    assert "categories" in resp

def test_get_category_children():
    resp = get_category_children(api_key=DEMO_KEY, category_id=125)
    assert "categories" in resp

def test_get_category_series():
    resp = get_category_series(api_key=DEMO_KEY, category_id=125, file_type="json")
    assert "seriess" in resp

def test_get_series():
    resp = get_series(api_key=DEMO_KEY, series_id="GDP", file_type="json")
    assert "seriess" in resp

def test_get_series_observations():
    resp = get_series_observations(
        api_key=DEMO_KEY,
        series_id="GDP",
        file_type="json",
        observation_start="2020-01-01",
        observation_end="2020-12-31"
    )
    assert "observations" in resp