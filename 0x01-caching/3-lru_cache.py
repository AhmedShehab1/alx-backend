#!/usr/bin/env python3
"""
3-lru_cache.py
"""
import importlib

BaseCaching = importlib.import_module("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache Classs
    Discards Items Based on LRU Algorithm
    """
    def __init__(self) -> None:
        """Constructor
        """
        super().__init__()
        self.priority_list = []

    def put(self, key, item):
        """Add an item to the cache"""
        if item and key:
            self.cache_data[key] = item
            if key in self.priority_list:
                self.priority_list.remove(key)
                self.priority_list.append(key)
            else:
                self.priority_list.append(key)
        if len(self.cache_data) > LRUCache.MAX_ITEMS:
            popped_key = self.priority_list.pop(0)
            del self.cache_data[popped_key]
            print(f"DISCARD: {popped_key}")

    def get(self, key):
        """Get an item by key"""
        if key in self.priority_list:
            self.priority_list.remove(key)
            self.priority_list.append(key)

        return self.cache_data.get(key)

