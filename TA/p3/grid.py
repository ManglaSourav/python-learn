
# import loc
from re import L
from loc import *


class Grid:
    def __init__(self, filename, is_string):
        self.access_count = 0
        self.grid = [[]]
        n = 0
        with open(filename) as f:
            Lines = f.readlines()
            flag = True
            i = 0
            for line in Lines:
                # count += 1
                if flag:
                    n = int(line.strip())
                    self.grid = [[0] * n] * n
                    flag = False
                    continue
                char_list = line.strip().split(" ")
                self.grid[i] = [Loc(i, index, val)
                                for index, val in enumerate(char_list)]
                i += 1

            # print(self.grid)

    def to_string(self):
        str = ""
        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                str += self.grid[x][y].get_val() + " "
            str += "\n"
        return str

    def size(self):
        return len(self.grid)

    def check_index(self, i):
        return i >= 0 and i < self.size()

    def get_loc(self, i, j):
        if self.check_index(i) and self.check_index(j):
            self.access_count += 1
            return self.grid[i][j]
        return None

    # // returns the String value at (i, j) or
        # // null if it is outside the grid
    def get_val(self, i, j):
        loc = self.get_loc(i, j)
        if loc != None:
            return loc.get_val()
        return None

    def get_int_val(self, i, j):
        str = self.get_val(i, j)
        if(str != None):
            return int(str)
        return -9999

    def get_access_count(self):
        return self.access_count

    def reset_access_count(self):
        self.access_count = 0


# grid = Grid("puzzle1_test.txt", True)
# print(grid.to_string())
# print(grid.get_val(1,2))
