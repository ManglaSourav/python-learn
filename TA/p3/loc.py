import sys


class Loc:
    def __init__(self, x, y, val):
        self.row = x
        self.col = y
        self.val = val
        self.in_queue_ = False
        self.visited_ = False
        self.dist_ = sys.maxsize
        self.prev_ = None
        self.pos_in_PQ = -1

    def get_val(self):
        return self.val

    def to_string(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"

    def pos_in_pq(self):
        return self.pos_in_PQ

    def set_pos_in_pq(self, i):
        self.pos_in_PQ = i

    def dist(self):
        return self.dist_

    def set_dist(self, dist):
        self.dist_ = dist

    def prev(self):
        return self.prev_

    def set_prev(self, prev):
        self.prev_ = prev

    def get_val(self):
        return self.val

    def get_int_val(self):
        return int(self.val)

    def visited(self):
        return self.visited_

    def in_queue(self):
        return self.in_queue_

    def visit(self):
        self.visited_ = True

    def put_in_queue(self):
        self.in_queue_ = True

    def reset_bfs(self):
        self.visited_ = False
        self.in_queue_ = False

    def reset_sp(self):
        self.visited_ = False
        self.dist_ = sys.maxsize
        self.prev_ = None
        self.pos_in_PQ = -1
