from array import *


class ArrayList:
    def __init__(self, cap=10):
        self.array = Array(cap)
        self.first = 0
        self.last = 0
        self.n = 0

    def resize(self, newCap):
        self.array.resize(newCap, self.first, self.n)
        self.first = 0
        self.last = self.n

    def add_last(self, num):
        if(self.n == self.array.length()):
            self.resize(2*self.n)
        self.array.set_val(self.last, num)
        self.last = self.increment(self.last)
        self.n += 1

    def increment(self, i):
        return (i+1) % self.array.length()

    def decrement(self, i, by):
        i = (i - by) % self.array.length()
        if i < 0:
            i += self.array.length()
        return i

    def add_first(self, num):
        if(self.n == self.array.length()):
            self.resize(2*self.n)
        self.first = self.decrement(self.first, 1)
        self.array.set_val(self.first, num)
        self.n += 1

    def get(self, i):
        if i < 0 or i > self.n - 1:
            return -99999
        i = (self.first + i) % self.array.length()
        return self.array.get_val(i)

    def index_of(self, num):
        i = self.first
        # print("first", i)
        while i != self.last:
            if(self.array.get_val(i) == num):
                # print("found position", i)
                return self.decrement(i, self.first)
            i = self.increment(i)
        return -1

    def contains(self, num):
        return self.index_of(num) != -1

    def is_empty(self):
        return self.n == 0

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list")

        num = self.array.get_val(self.first)
        self.first = self.increment(self.first)
        self.n -= 1
        if(self.n < self.array.length() / 4 and self.array.length() / 2 >= 10):
            self.resize(self.array.length() / 4)
        return num

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty List")
        self.last = self.decrement(self.last, 1)
        last = self.get(self.last)
        self.n -= 1
        if(self.n < self.array.length() / 4 and self.array.length() / 2 >= 10):
            self.resize(self.array.length() / 4)
        return last

    def shift_left(self, i, by):
        j = self.decrement(i, by)
        while i != self.last:
            self.array.set_val(j, self.array.get_val(i))
            i = self.increment(i)
            j = self.increment(j)
        return

    def remove_by_index(self, i):
        num = - 9999
        if self.is_empty():
            raise Exception("Empty list")
        elif i < 0 or i > self.n - 1:
            return num
        elif i == 0:
            return self.remove_first()
        elif i == self.n - 1:
            return self.remove_last()
        else:  # [2,0,0,11,12]
            i = (self.first+i) % self.array.length()
            num = self.get(i)
            self.shift_left(self.increment(i), 1)
        n -= 1
        if(self.n < self.array.length() / 4 and self.array.length() / 2 >= 10):
            self.resize(self.array.length() / 4)
        return num

    def remove_by_value(self, num):
        index = self.index_of(num)
        if index == -1:
            return False
        self.remove_by_index(index)
        return True

al1 = ArrayList(10)
al1.add_last(12)
al1.add_first(10)
al1.array.to_string()
print(al1.index_of(12))
print(al1.get(1))
print(al1.remove_first())
al1.add_first(11)
al1.add_first(11)
al1.add_last(111)
al1.array.to_string()
al1.remove_last()
al1.array.to_string()
