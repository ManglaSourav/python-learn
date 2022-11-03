
from contextlib import nullcontext
from grid import *
from deque import *
from loc import *


class Puzzle:

    def __init__(self, grid):
        self.grid = grid
        self.found = False
        self.queue = Deque()
        self.path = Deque()
        self.locs2ResetBFS = []

    def get_up(self, r, c):
        return self.grid.get_loc(r-1, c)

    def get_right(self, r, c):
        return self.grid.get_loc(r, c+1)

    def get_down(self, r, c):
        return self.grid.get_loc(r+1, c)

    def get_left(self, r, c):
        return self.grid.get_loc(r, c-1)

    # BFS

    def find_first(self, first_char):
        curr = None
        while not self.queue.is_empty():
            curr = self.queue.get_first()
            if curr.get_val() == first_char:
                return curr
            curr.visit()

            row = curr.row
            col = curr.col
            up = self.get_up(row, col)
            self.add_to_queue(up)
            right = self.get_right(row, col)
            self.add_to_queue(right)
            down = self.get_down(row, col)
            self.add_to_queue(down)
            left = self.get_left(row, col)
            self.add_to_queue(left)
        return

    def reset_locs(self):
        for loc in self.locs2ResetBFS:
            loc.reset_bfs()
        return

    def get_string_path(self):
        str = ""
        while self.path != None and not self.path.is_empty():
            str += self.path.get_first().to_string()
        return str

    def get_neighbors(self, s, x, y):
        ret = Deque()

        up = self.get_up(x, y)
        if(up != None and up.get_val() == s):
            ret.add_to_back(up)

        right = self.get_right(x, y)
        if(right != None and right.get_val() == s):
            ret.add_to_back(right)

        down = self.get_down(x, y)
        if(down != None and down.get_val() == s):
            ret.add_to_back(down)

        left = self.get_left(x, y)
        if(left != None and left.get_val() == s):
            ret.add_to_back(left)

        return ret

    # DFS
    def search(self, word, curr, i):
        self.path.add_to_back(curr)  # adding to path
        if i > len(word) - 1:
            return True
        match = word[i:i+1]
        print("match for ", match)
        neighbors = self.get_neighbors(match, curr.row, curr.col)
        next = None
        while not neighbors.is_empty():
            next = neighbors.get_first()

            if self.search(word, next, i + 1):
                return True
        self.path.get_last()  # if
        return False

    def find(self, word, row, col):
        first = self.grid.get_loc(row, col)
        self.add_to_queue(first)
        first_char = word[:1]
        while(not self.found):
            start = self.find_first(first_char)
            # print(start.to_string())
            if start == None:
                return None
            self.found = self.search(word, start, 1)

        self.found = False
        self.reset_locs()
        return self.get_string_path()

    def add_to_queue(self, loc):
        if loc != None and not loc.visited() and not loc.in_queue():
            self.queue.add_to_back(loc)
            loc.put_in_queue()
            self.locs2ResetBFS.append(loc)


puzzle = Puzzle(Grid("puzzle1_test.txt", True))
words = ["AFGHANISTAN"]  # , "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA"]
start = [11, 11, 0, 0, 5, 12, 7, 8, 14, 0]
for i in range(len(words)):
    print("searching puzzle for " + words[i])
    x = start[2 * i]
    y = start[2 * i + 1]
    print(puzzle.find(words[i], x, y))


'''
(12, 10)(11, 10)(10, 10)(9, 10)(9, 11)(10, 11)(10, 12)(9, 12)(8, 12)(7, 12)(7, 13)
101
(1, 1)(1, 2)(2, 2)(2, 3)(3, 3)(4, 3)(4, 2)
43
(0, 14)(1, 14)(2, 14)(2, 13)(1, 13)(0, 13)(0, 14)
278
(12, 2)(12, 1)(12, 0)(11, 0)(10, 0)(9, 0)(9, 1)
846
(6, 6)(5, 6)(5, 7)(4, 7)(3, 7)(3, 8)
440
'''
