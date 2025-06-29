# fredclient/endpoints.py

import requests
from typing import Any, Callable, Dict

BASE_URL = "https://api.stlouisfed.org/fred"

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

def generate_endpoint_function(name: str, meta: Dict[str, Any]) -> Callable:
    """
    Dynamically generates a function for making API requests to a specified FRED endpoint.

    Parameters:
    -----------
    name : str
        The name of the endpoint function to generate.
    meta : dict
        Metadata for the endpoint including path, required and optional parameters, and a description.

    Returns:
    --------
    Callable
        A function that accepts keyword arguments for each required/optional parameter,
        performs type checking, and sends a request to the corresponding FRED API endpoint.

    Raises:
    -------
    ValueError
        If a required parameter is missing.
    TypeError
        If any parameter does not match the expected type.
    """
    def func(**kwargs):
        for param, param_type in meta["required"].items():
            if param not in kwargs:
                raise ValueError(f"Missing required parameter: {param}")
            if not isinstance(kwargs[param], eval(param_type)):
                raise TypeError(f"Parameter '{param}' must be of type {param_type}")

        for param, param_type in meta.get("optional", {}).items():
            if param in kwargs and not isinstance(kwargs[param], eval(param_type)):
                raise TypeError(f"Optional parameter '{param}' must be of type {param_type}")

        url = f"{BASE_URL}{meta['path']}"
        response = requests.get(url, params={k: v for k, v in kwargs.items() if v is not None})
        response.raise_for_status()
        return response.json()

    func.__name__ = name
    func.__doc__ = f"""{meta['description']}

Required parameters:
{chr(10).join(f"- {k}: {v}" for k, v in meta['required'].items())}

Optional parameters:
{chr(10).join(f"- {k}: {v}" for k, v in meta.get('optional', {}).items())}"""
    return func

# Generate all endpoint functions dynamically
globals().update({
    name: generate_endpoint_function(name, meta)
    for name, meta in ENDPOINTS.items()
})

def get_all_endpoints() -> list[str]:
    """
    Returns a list of all available endpoint function names.
    """
    return list(ENDPOINTS.keys())

def describe_endpoint(name: str) -> str:
    """
    Returns a formatted description of a specific endpoint, including its required
    and optional parameters and their expected types.

    Parameters:
    ----------
    name : str
        The name of the endpoint (e.g., 'get_series_observations').

    Returns:
    -------
    str
        A detailed description of the endpoint’s purpose and parameters.

    Raises:
    ------
    KeyError
        If the endpoint name is not found in the registry.
    """
    if name not in ENDPOINTS:
        raise KeyError(f"No such endpoint: '{name}'")

    meta = ENDPOINTS[name]
    desc = [f"{name}: {meta['description']}\n"]
    desc.append("Required parameters:")
    for k, v in meta["required"].items():
        desc.append(f"  - {k}: {v}")
    if meta.get("optional"):
        desc.append("Optional parameters:")
        for k, v in meta["optional"].items():
            desc.append(f"  - {k}: {v}")
    return "\n".join(desc)
