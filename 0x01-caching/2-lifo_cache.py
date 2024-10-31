#!/usr/bin/env python3
"""
2-lifo_cache.py
"""
import importlib

BaseCaching = importlib.import_module("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache Classs
    Discards Items Based on LIFO Algorithm
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if item and key:
            self.cache_data[key] = item

        if len(self.cache_data) > LIFOCache.MAX_ITEMS:
            popped_key = self.cache_data.popitem()[0]
            print(f"DISCARD: {popped_key}")

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)

