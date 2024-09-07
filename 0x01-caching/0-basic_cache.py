#!/usr/bin/env python3
"""A Caching System"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements Basic Cache"""
    def __init__(self):
        """Initializes class instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns items to cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Returns value in cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
