class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        if items:
                if len(items) > limit:
                    raise ValueError("Too many items for the stack limit.")
                self.items = items.copy()


    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return None
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if self.isEmpty():
              raise IndexError("Cannot peek from an empty stack")
        return self.items[-1]
    
    def size(self):
            return len(self.items)
    def full(self):
        return self.size() == self.limit
    
    def search(self, target):
        for i in range(len(self.items)-1, -1,-1):
             if self.items[i] == target:
                  return len(self.items)-1-i
        return -1
    


s = Stack([1,2,3,4,5], limit =5)
print(s.items)
print(s.limit)
print(s.size())
print(s.pop())
print(s.full())
print(s.search(4))