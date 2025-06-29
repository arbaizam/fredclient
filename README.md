# fredclient

A lightweight, user-friendly Python wrapper for the [FRED API](https://fred.stlouisfed.org/), with automatic support for all documented endpoints and a focus on flexibility, validation, and discoverability.

## Features

- Access all FRED API endpoints dynamically
- Validates required and optional parameters
- Automatically documents parameter types and endpoint descriptions
- Easy integration into any data workflow
- Simple error handling with Python-native exceptions
- Utility functions to explore API capabilities

---

## Installation

```bash
pip install fredclient
```

Or clone directly from GitHub:

```bash
git clone https://github.com/arbaizam/fredclient.git
cd fredclient
pip install -e .
```

---

## Usage

### Basic Example

```python
from fredclient import get_series_observations

data = get_series_observations(
    api_key="YOUR_API_KEY",
    series_id="GDP",
    file_type="json"
)

print(data)
```

---

### List All Available Endpoints

```python
from fredclient import get_all_endpoints

print(get_all_endpoints())
```

---

### Describe a Specific Endpoint

```python
from fredclient import describe_endpoint

print(describe_endpoint("get_series_observations"))
```

---

### Example Output for `describe_endpoint("get_series_observations")`

```
get_series_observations: Get observations for a series.

Required parameters:
  - api_key: str
  - series_id: str

Optional parameters:
  - file_type: str
  - realtime_start: str
  - realtime_end: str
  - limit: int
  - offset: int
  - sort_order: str
  - observation_start: str
  - observation_end: str
  - units: str
  - frequency: str
  - aggregation_method: str
```

---

## Testing

To run all tests:

```bash
pytest tests/
```

---

## Contributing

Feel free to submit issues or pull requests. Future enhancements will include:

- Full schema-based validation
- Pydantic model support for response parsing
- Support for async and batch queries

---

## License

MIT License.
