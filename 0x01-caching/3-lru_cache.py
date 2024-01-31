#!/usr/bin/env python3
"""fifo caching method"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class FIFOCache inherits from BaseCache
    """
    def __init__(self):
        super().__init__()
        self.order_cache = []

    def put(self, key, item):
        """add to cached data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.order_cache[0]
                self.order_cache.remove(discard_key)
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
            self.order_cache.append(key)

    def get(self, key):
        """get by key"""
        if key is not None and key in self.order_cache:
            self.order_cache.remove(key)
            self.order_cache.append(key)
            return self.cache_data.get(key)
        
        else:
            return None
