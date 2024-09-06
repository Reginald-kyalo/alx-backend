#!/usr/bin/env python3
"""Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements FIFOCache"""
    def __init__(self):
        """Initializes class instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns items to cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            indexToBeRemoved = 0
            keytopop = list(self.cache_data.keys())[indexToBeRemoved]
            self.cache_data.pop(keytopop)
            print(f'DISCARD: {keytopop}')
        self.cache_data[key] = item

    def get(self, key):
        """Returns value in cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
