"""
fredclient - A Python client for the Federal Reserve Economic Data (FRED) API.

Usage:
    from fredclient import get_series, get_category_series

    data = get_series(api_key="...", series_id="GDP")
"""

from .endpoints import *