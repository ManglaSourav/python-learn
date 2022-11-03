
from collections import deque
from distutils.util import change_root


class Deque:

    def __init__(self, n=10):
        self.deque = [0] * n
        self.front = 0
        self.back = 0
        self.size = 0
        self.init_cap = n

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def change_index(self, inc, in_front):
        if inc and in_front:
            self.front = (self.front + 1) % len(self.deque)
        elif not inc and in_front:
            self.front = (self.front - 1) % len(self.deque)
            if self.front < 0:
                self.front += len(deque)
        elif inc and not in_front:
            self.back = (self.back + 1) % len(self.deque)
        else:
            self.back = (self.back - 1) % len(self.deque)
            if self.back < 0:
                self.back += len(deque)

    def resize(self, max):
        new_array = [0] * int(max)  # need to check
        for i in range(self.size):
            new_array[i] = self.deque[self.front]
            self.change_index(True, True)

        self.deque = new_array
        self.front = 0
        self.back = self.size

    def add_to_front(self, item):
        if self.is_empty():
            self.item[self.front] = item
            self.change_index(True, False)
            self.size += 1
            return
        elif self.size == len(self.deque):
            self.resize(2*len(self.deque))
        self.change_index(False, True)
        self.deque[self.front] = item
        self.size += 1

    def add_to_back(self, item):
        if self.size == len(self.deque):
            self.resize(2 * len(self.deque))
        self.deque[self.back] = item
        self.size += 1
        self.change_index(True, False)

    # Remove and return the front item from the Deque;
    def get_first(self):
        if self.size == 0:
            raise Exception("Empty deque")
        item = self.deque[self.front]
        self.size -= 1
        self.deque[self.front] = 0
        self.change_index(True, True)
        if self.size > len(self.deque)/4 and len(self.deque)/2 >= self.init_cap:
            self.resize(len(self.deque)/2)
        return item

    # Remove and return the back item from the Deque;
    def get_last(self):
        if self.size == 0:
            raise Exception("Empty deque")

        self.change_index(False, False)
        item = self.deque[self.back]
        self.size -= 1
        self.deque[self.back] = 0
        if self.size > len(self.deque)/4 and len(self.deque)/2 >= self.init_cap:
            self.resize(len(self.deque)/2)
        return item

    def peek_first(self):
        if self.size == 0:
            raise Exception("Empty deque")
        return self.deque[self.front]

    def peek_last(self):
        if self.size == 0:
            raise Exception("Empty deque")
        back = (self.back - 1) % len(self.deque)
        if back < 0:
            back += len(self.deque)
        return self.deque[back]

    def get_array(self):
        return self.de

    def print_array(self):
        for i in range(self.front, self.back, (i+1) % len(self.deque)):
            print(self.deque[i])
