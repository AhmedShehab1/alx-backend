#!/usr/bin/env python3
"""
1-fifo_cache.py
"""
import importlib

BaseCaching = importlib.import_module("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache Classs
    Discards Items Based on FIFO Algorithm
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if item and key:
            self.cache_data[key] = item

        if len(self.cache_data) > FIFOCache.MAX_ITEMS:
            popped_key = list(self.cache_data.keys())[0]
            del self.cache_data[popped_key]
            print(f"DISCARD: {popped_key}")

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
