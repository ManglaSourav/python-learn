import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        for i in range(1,1001):
            heapq.heappush(self.heap, i)


    def popSmallest(self):
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        return 0

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)