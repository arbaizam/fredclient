# fredclient

Python client for the [FRED API](https://fred.stlouisfed.org/) — built from the official OpenAPI schema. This client lets you easily query macroeconomic data from the Federal Reserve Bank of St. Louis.

---

## 📦 Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/arbaizam/fredclient.git
```

---

## 🔑 Authentication

To use the FRED API, you’ll need an API key.  
Sign up for a free key here: https://fred.stlouisfed.org/docs/api/api_key.html

Then use it in your code like this:

```python
from fredclient import FredAPI

fred = FredAPI(api_key="YOUR_API_KEY")
```

---

## 🧪 Basic Usage

### Get Observations for a Series
```python
data = fred.get_series_observations(series_id="GDP")
print(data)
```

### Search for Series by Keyword
```python
results = fred.get_series_search(search_text="unemployment rate")
for series in results["seriess"]:
    print(series["title"])
```

### Get Category Information
```python
category = fred.get_category(category_id=125)
print(category)
```

### Get Child Categories
```python
children = fred.get_category_children(category_id=125)
```

### Get List of Releases
```python
releases = fred.get_releases(limit=5)
```

---

## 📁 Project Structure

```
fredclient/
├── __init__.py           # Public client interface (FredAPI)
├── core/                 # (Planned) Internal utilities, data types
├── pyproject.toml        # Build metadata
├── README.md             # You're reading it
└── tests/                # Test suite (coming soon)
```

---

## 🚧 Planned Features

- Auto-generated endpoint coverage from OpenAPI
- Async support
- DataFrame helpers (e.g. `.to_df()`)
- Tag and source lookup functions
- CLI tool

---

## 🧪 Testing Locally

Clone the repo and run:

```bash
pip install -e .
```

---

## 🙌 Contributing

Pull requests and suggestions are welcome!  
If you find a bug or have feature ideas, [open an issue](https://github.com/arbaizam/fredclient/issues).

---

## 📄 License

MIT License — see `LICENSE` file for details.

---

## 👋 Author

Developed by [@arbaizam](https://github.com/arbaizam)
