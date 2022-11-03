
class Array:
    def __init__(self, args):
        self.array = []
        self.access_count = 0

        if isinstance(args, str):
            with open(args, 'r') as file:
                content = file.readlines()[1:]
                self.array = [int(line.rstrip()) for line in content]
        elif isinstance(args, list):
            self.array = args
        else:
            self.array = [0] * args

    def to_string(self):
        print(self.array)

    def length(self):
        return len(self.array)

    def get_val(self, i):
        num = self.array[i]
        self.access_count += 1
        return num

    def set_val(self, i, num):
        self.array[i] = num
        self.access_count += 1

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp
        self.access_count += 4

    def get_acces_count(self):
        return self.access_count


# a1 = Array("array1.txt")
# print(a1.array)
# a2 = Array(10)
# print(a2.array)

# a2.set_val(1, 12)
# a2.to_string()
# print(a2.get_acces_count())
