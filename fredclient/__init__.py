
"""
fredclient: Python client for the FRED API
"""

import requests
from typing import Dict, Any, Optional


class FredAPI:
    BASE_URL = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        params['file_type'] = 'json'
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_series_observations(self, series_id: str, **kwargs) -> Dict[str, Any]:
        """GET /series/observations"""
        return self._get("series/observations", {"series_id": series_id, **kwargs})

    def get_category(self, category_id: int) -> Dict[str, Any]:
        """GET /category"""
        return self._get("category", {"category_id": category_id})

    def get_category_children(self, category_id: int) -> Dict[str, Any]:
        """GET /category/children"""
        return self._get("category/children", {"category_id": category_id})

    def get_releases(self, **kwargs) -> Dict[str, Any]:
        """GET /releases"""
        return self._get("releases", kwargs)

    def get_series_search(self, search_text: str, **kwargs) -> Dict[str, Any]:
        """GET /series/search"""
        return self._get("series/search", {"search_text": search_text, **kwargs})
