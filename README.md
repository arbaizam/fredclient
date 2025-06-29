# 🔧 Utility Functions for `fredclient`

This document outlines the utility methods available in the `fredclient` module for inspecting the FRED API endpoints.

---

## `get_all_endpoints()`

Returns a list of all available FRED API endpoints that are wrapped in the client.

**Returns:**  
- `list[str]`: List of endpoint function names (e.g., `get_series`, `get_category_tags`, etc.)

**Example:**

```python
from fredclient import get_all_endpoints

print(get_all_endpoints())
# Output: ['get_category', 'get_category_children', 'get_category_related', ..., 'get_series_search']
```

---

## `describe_endpoint(name: str)`

Returns a detailed, formatted string describing an individual endpoint, including:
- Summary of what it does
- Required parameters and their types
- Optional parameters and their types

**Parameters:**  
- `name` (`str`): The name of the endpoint (e.g., `"get_series_observations"`)

**Returns:**  
- `str`: Formatted multi-line string describing the endpoint

**Raises:**  
- `KeyError`: If the provided name does not match any available endpoint

**Example:**

```python
from fredclient import describe_endpoint

print(describe_endpoint("get_category_series"))
```

**Output:**
```
get_category_series: Retrieve series within a specified category.

Required parameters:
  - api_key: str
  - category_id: int

Optional parameters:
  - file_type: str
  - realtime_start: str
  - realtime_end: str
  - limit: int
  - offset: int
  - order_by: str
  - sort_order: str
  - filter_variable: str
  - filter_value: str
```