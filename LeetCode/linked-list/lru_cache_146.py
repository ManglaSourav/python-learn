from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def print_all(self):
        print(self.cache)


lru_cache = LRUCache(2)
print(lru_cache.put(1, 1))  # cache is {1=1}
lru_cache.print_all()
print(lru_cache.put(2, 2))  # cache is {1=1, 2=2}
lru_cache.print_all()

print(lru_cache.get(1))  # return 1
lru_cache.print_all()

print(lru_cache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lru_cache.print_all()
print(lru_cache.get(2))  # returns -1 (not found)

lru_cache.print_all()
print(lru_cache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lru_cache.print_all()

print(lru_cache.get(1))  # return -1 (not found)
lru_cache.print_all()

print(lru_cache.get(3))  # return 3
lru_cache.print_all()

print(lru_cache.get(4))  # return 4
