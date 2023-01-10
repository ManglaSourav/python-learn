
class Stack:
    def __init__(self, c = 10):
        self.stack = [0]*10
        self.top = -1
        self.cap = c
    
    def push(self, item):
        
        self.top += 1
        self.stack[self.top] = item
        
    def peek(self):
        if self.top == -1:
            return None 
        return self.stack[self.top]
    
    def pop(self):
        if self.top == -1:
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1.pop())
print(s1.pop())
print(s1.stack)
        