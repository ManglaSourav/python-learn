

class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[] for i in range(length)]
        self.snap_id = 0        

    def set(self, index: int, val: int) -> None:
        # need to check snap id length and data length
        data = self.data[index]
        if (len(data) - self.snap_id) == 1 and len(data) != 0:
            data[-1] = val
        else:
            data.append(val)
                    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1 

    def get(self, index: int, snap_id: int) -> int:
        index_data = self.data[index]
        if len(index_data) <= snap_id:

            return index_data[-1] if len(index_data)>0 else 0
        else:
            return index_data[snap_id]  
        
    


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(1)
# obj.set(0,4)
# obj.set(0,16)
# obj.set(0,13)
# param_2 = obj.snap()
# param_3 = obj.get(0,0)
# print(param_3)
# print(obj.data)
# param_4 = obj.snap()
# print(param_4)
# print(obj.data, obj.snap_data)
# print(param_3)


obj = SnapshotArray(2)
obj.set(0, 12)
obj.snap()
obj.snap()
obj.get(1,0)
obj.get(1,0)
obj.snap()
obj.snap()


# ["SnapshotArray","snap","snap","get","set","snap","set"]
# [[4],[],[],[3,1],[2,4],[],[1,4]]