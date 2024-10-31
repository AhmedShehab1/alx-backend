#!/usr/bin/env python3
"""
0-basic_cache.py
"""
import importlib

BaseCaching = importlib.import_module("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """
    def put(self, key, item):
        """Add an item to the cache"""
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
