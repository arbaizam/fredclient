# FRED Client (`fredclient`)

A lightweight, Pythonic wrapper for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) provided by the Federal Reserve Bank of St. Louis. This package simplifies access to economic data by dynamically handling all endpoints via a single client class.

---

## 🔧 Installation

```bash
pip install -r requirements.txt
```

You will also need to install `python-dotenv` if you want to load your API key from a `.env` file:

```bash
pip install python-dotenv
```

---

## 📁 Project Structure

```
fredclient/
├── __init__.py
├── client.py          # FredClient class lives here
├── metadata.py        # Endpoint metadata
tests/
├── test_endpoints.py  # Full test suite for all endpoints
.env                    # (Optional) for secure API key management
README.md
```

---

## 🚀 Usage

### Step 1: Add your API key to a `.env` file

```
FRED_API_KEY=your_actual_fred_api_key_here
```

### Step 2: Use the `FredClient` class

```python
from fredclient.client import FredClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FRED_API_KEY")

client = FredClient(api_key=api_key)

# List available endpoints
print(client.get_all_endpoints())

# See description for an endpoint
print(client.describe_endpoint("get_series"))

# Example: Fetch series metadata
response = client.get_series(series_id="GNPCA")
print(response)
```

---

## 🧪 Running Tests

```bash
pytest
```

Ensure your `.env` file is present with a valid `FRED_API_KEY` or override in the test script.

---

## 🧠 Features

- ✅ All available FRED endpoints
- ✅ Automatically validates required and optional parameters
- ✅ Intelligent error handling for missing/invalid parameters
- ✅ Endpoint docstrings include parameter descriptions
- ✅ Programmatic interface for inspecting API structure

---

## 📄 License

MIT License © arbaizam
