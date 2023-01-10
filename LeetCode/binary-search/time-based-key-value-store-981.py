

class TimeMap:

    def __init__(self):
        self.hash_map = {}
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hash_map:
            return ""

        values = self.hash_map[key]

        left = 0
        right = len(values)-1
        result = ""
        while left <= right:
            mid = (left+right)//2

            if timestamp == values[mid][1]:
                return values[mid][0]
            elif timestamp > values[mid][1]:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar", 2)
obj.set("foo", "bar", 3)
print(obj.hash_map)
param_2 = obj.get("foo", 1)
