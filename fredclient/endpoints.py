# fredclient/endpoints.py

from typing import Any, Callable, Dict

# Define metadata for endpoints
ENDPOINTS = {
    "get_category": {
        "path": "/category",
        "required": {"api_key": "str", "category_id": "int"},
        "optional": {"file_type": "str"},
        "description": "Get a category by ID."
    },
    "get_category_children": {
        "path": "/category/children",
        "required": {"api_key": "str", "category_id": "int"},
        "optional": {"file_type": "str"},
        "description": "Get the child categories for a specified parent category."
    },
    "get_category_related": {
        "path": "/category/related",
        "required": {"api_key": "str", "category_id": "int"},
        "optional": {"file_type": "str"},
        "description": "Get related categories for a category."
    },
    "get_category_series": {
        "path": "/category/series",
        "required": {"api_key": "str", "category_id": "int"},
        "optional": {
            "file_type": "str", "realtime_start": "str", "realtime_end": "str", 
            "limit": "int", "offset": "int", "order_by": "str", 
            "sort_order": "str", "filter_variable": "str", "filter_value": "str"
        },
        "description": "Retrieve series within a specified category."
    },
    "get_category_tags": {
        "path": "/category/tags",
        "required": {"api_key": "str", "category_id": "int"},
        "optional": {
            "file_type": "str", "search_text": "str", "tag_group_id": "str", 
            "tag_names": "str", "limit": "int", "offset": "int", 
            "order_by": "str", "sort_order": "str"
        },
        "description": "Get the FRED tags for a category."
    },
    "get_category_related_tags": {
        "path": "/category/related_tags",
        "required": {"api_key": "str", "category_id": "int", "tag_names": "str"},
        "optional": {"file_type": "str", "tag_group_id": "str"},
        "description": "Get related tags for a category."
    },
    "get_series": {
        "path": "/series",
        "required": {"api_key": "str", "series_id": "str"},
        "optional": {"file_type": "str"},
        "description": "Get a series."
    },
    "get_series_categories": {
        "path": "/series/categories",
        "required": {"api_key": "str", "series_id": "str"},
        "optional": {"file_type": "str"},
        "description": "Get the categories for a series."
    },
    "get_series_observations": {
        "path": "/series/observations",
        "required": {"api_key": "str", "series_id": "str"},
        "optional": {
            "file_type": "str", "realtime_start": "str", "realtime_end": "str", 
            "limit": "int", "offset": "int", "sort_order": "str", 
            "observation_start": "str", "observation_end": "str", 
            "units": "str", "frequency": "str", "aggregation_method": "str"
        },
        "description": "Get observations for a series."
    },
    "get_series_search": {
        "path": "/series/search",
        "required": {"api_key": "str", "search_text": "str"},
        "optional": {
            "file_type": "str", "realtime_start": "str", "realtime_end": "str", 
            "limit": "int", "offset": "int", "order_by": "str", 
            "sort_order": "str", "filter_variable": "str", "filter_value": "str"
        },
        "description": "Search for FRED series."
    }
}

