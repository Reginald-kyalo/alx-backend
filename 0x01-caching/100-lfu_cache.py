#!/usr/bin/env python3
"""A Caching System"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Implements LFUCache"""
    def __init__(self):
        """Initializes class instance"""
        super().__init__()
        self.usage_lfu = {}
        self.usage_lru = []
        self.count = 0

    def put(self, key, item):
        """Assigns items to cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_lfu[key] += 1
            if key in self.usage_lru:
                self.usage_lru.remove(key)
            self.usage_lru.append(key)
            return

        dict_len = len(self.cache_data)

        if dict_len >= BaseCaching.MAX_ITEMS:
            sorted_dict_desc = dict(sorted(
                self.cache_data.items(),
                key=lambda item: item[1],
                reverse=True
                ))
            indexToBeRemoved = 0
            keytopop = list(sorted_dict_desc.keys())[indexToBeRemoved]
            for key, value in sorted_dict_desc.items():
                if value == sorted_dict_desc[keytopop]:
                    if key == self.usage_lru[len(self.usage_lru) - 1]:
                        keytopop = key
                        break
            self.cache_data.pop(keytopop)
            self.usage_lfu.pop(keytopop)
            self.usage_lru.remove(keytopop)
            print(f'DISCARD: {keytopop}')
        self.cache_data[key] = item
        self.usage_lfu[key] = 1
        self.usage_lru.append(key)

    def get(self, key):
        """Returns value in cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.usage_lfu[key] += 1
        if key in self.usage_lru:
            self.usage_lru.remove(key)
        self.usage_lru.append(key)
        return self.cache_data[key]
