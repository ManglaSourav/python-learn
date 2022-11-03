# implement a data structure for LRU cache implementation, which supports operations at O(1) time.


class LRUCache:
    def __init__(self, cap=5):
        self.max_cap = cap  # capacity of the cache
        # key is the actual key and value contains the index number of queue which holds the actual key-value pair
        self.hash_table = {}
        self.queue = []  # to hold the actual key-value pair

    def insert(self, key, value):
        # insert new key-value pair
        if key not in self.hash_table and len(self.hash_table) <= self.max_cap:
            temp_queue = [{key: value}]
            self.queue = temp_queue + self.queue
            self.hash_table[key] = 0

        # update existing one
        if key in self.hash_table:
            temp_queue = [{key: value}]
            index_value = self.hash_table[key]
            # placing updating key-value pair at index 0 because it is most recent
            self.queue = [{key: value}] + \
                self.queue[0:index_value] + self.queue[index_value+1:]
            self.hash_table[key] = 0 # put address instead of index 

        # if capacity is full, remove one least used entry and insert new one

    def print_everything(self):
        print(self.hash_table)
        print(self.queue)


cache = LRUCache()
cache.insert(1, 1)
cache.insert(2, 2)
cache.insert(3, 3)
cache.insert(3, 3)
cache.insert(4, 4)
cache.print_everything()
