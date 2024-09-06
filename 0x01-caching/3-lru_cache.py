#!/usr/bin/env python3
"""Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements LRUCache"""
    def __init__(self):
        """Initializes class instance"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Assigns items to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage.remove(key)

        dict_len = len(self.cache_data)

        if dict_len >= BaseCaching.MAX_ITEMS:
            indexToBeRemoved = 0
            keytopop = self.usage[indexToBeRemoved]
            self.cache_data.pop(keytopop)
            self.usage.remove(keytopop)
            print(f'DISCARD: {keytopop}')
        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """Returns value in cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.usage.remove(key)
        self.usage.append(key)
        return self.cache_data[key]
