"""
Defines all supported FRED API endpoints and the corresponding path and required params.
"""

from typing import Dict, List

ENDPOINTS: Dict[str, Dict[str, List[str]]] = {
    "category": {
        "path": "category",
        "required_params": ["category_id"],
    },
    "category_children": {
        "path": "category/children",
        "required_params": ["category_id"],
    },
    "category_related": {
        "path": "category/related",
        "required_params": ["category_id"],
    },
    "category_series": {
        "path": "category/series",
        "required_params": ["category_id"],
    },
    "series_observations": {
        "path": "series/observations",
        "required_params": ["series_id"],
    },
    "series_search": {
        "path": "series/search",
        "required_params": ["search_text"],
    },
    "releases": {
        "path": "releases",
        "required_params": [],
    },
    "release": {
        "path": "release",
        "required_params": ["release_id"],
    },
    "release_series": {
        "path": "release/series",
        "required_params": ["release_id"],
    },
    "sources": {
        "path": "sources",
        "required_params": [],
    },
    "source": {
        "path": "source",
        "required_params": ["source_id"],
    },
    "source_releases": {
        "path": "source/releases",
        "required_params": ["source_id"],
    },
    "tags": {
        "path": "tags",
        "required_params": [],
    },
    "related_tags": {
        "path": "related_tags",
        "required_params": ["tag_names"],
    },
    "series_tags": {
        "path": "series/tags",
        "required_params": ["series_id"],
    },
}