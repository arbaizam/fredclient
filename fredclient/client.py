import requests
from typing import Any, Callable, Dict
import pandas as pd
from .endpoints import ENDPOINTS


class FredClient:
    """
    Client for interacting with the FRED (Federal Reserve Economic Data) API.

    This class dynamically generates methods for each endpoint based on metadata
    defined in `endpoints.py`. Each method handles required/optional parameter validation
    and performs the HTTP request.

    Example:
    --------
    >>> client = FredClient(api_key="your_api_key")
    >>> data = client.get_series(series_id="GNPCA")
    >>> print(data)

    Parameters
    ----------
    api_key : str
        Your FRED API key.
    base_url : str, optional
        Override the default FRED base API URL.
    """
    BASE_URL = "https://api.stlouisfed.org/fred"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._register_endpoints()

    def _register_endpoints(self):
        for name, meta in ENDPOINTS.items():
            func = self._generate_endpoint_function(meta)
            setattr(self, name, func)

    def _generate_endpoint_function(self, meta: Dict[str, Any]) -> Callable:
        def endpoint_method(**kwargs):
            kwargs["api_key"] = self.api_key

            # Ensure default response format is JSON unless overridden
            kwargs.setdefault("file_type", "json")

            # Validate required parameters
            for param, expected_type in meta["required"].items():
                if param not in kwargs:
                    raise ValueError(f"Missing required parameter: {param}")
                if not isinstance(kwargs[param], eval(expected_type)):
                    raise TypeError(f"Parameter '{param}' must be of type {expected_type}")

            # Validate optional parameters
            for param, expected_type in meta.get("optional", {}).items():
                if param in kwargs and not isinstance(kwargs[param], eval(expected_type)):
                    raise TypeError(f"Optional parameter '{param}' must be of type {expected_type}")

            url = f"{self.BASE_URL}{meta['path']}"
            params = {k: v for k, v in kwargs.items() if v is not None}
            response = requests.get(url, params=params)
            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                raise ValueError(f"Expected JSON, got non-JSON response:\n{response.text}")

        #dynamic binding of name and docstrings.
        endpoint_method.__name__ = meta["path"].replace("/", "_").strip("_")
        endpoint_method.__doc__ = self._format_doc(meta)

        return endpoint_method

    def _format_doc(self, meta: Dict[str, Any]) -> str:
        """
        Format a user-facing docstring based on endpoint metadata.
        """
        doc = f"{meta['description']}\n\nRequired parameters:\n"
        doc += "\n".join(f"- {k}: {v}" for k, v in meta["required"].items())
        if meta.get("optional"):
            doc += "\n\nOptional parameters:\n"
            doc += "\n".join(f"- {k}: {v}" for k, v in meta["optional"].items())
        return doc

    def get_all_endpoints(self) -> pd.DataFrame:
        """
        Returns a DataFrame of all available FRED API endpoints, including
        name, path, description, required and optional parameters.

        Returns
        -------
        pd.DataFrame
            A table with one row per endpoint.
        """
        records = []
        for name, meta in ENDPOINTS.items():
            records.append({
                "name": name,
                "path": meta["path"],
                "description": meta["description"]
            })

        df = pd.DataFrame(records)
        print(df.to_markdown(index=False))


    def describe_endpoint(self, name: str) -> str:
        """
        Returns a description and parameter list for a specific endpoint.

        Parameters
        ----------
        name : str
            The name of the endpoint method (e.g., 'get_series').

        Returns
        -------
        str
            Description, required parameters, and optional parameters.

        Raises
        ------
        KeyError
            If the endpoint is not recognized.
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