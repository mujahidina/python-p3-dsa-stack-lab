class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items[:limit]
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    

    def push(self, item):
        if not self.full():
           self.items.append(item) 
        else:
            print('Stack is full, limit reached')


    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print('stack is empty')  
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and self.size() == self.limit

    def search(self, target):
        if target:
            index = self.items.index(target)
            return len(self.items) - index
        else:
            return  -1



# class Stack:
#     def __init__(self, items=[], limit=100):
#         self.items = items[:limit]
#         self.limit = limit

#     def isEmpty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         if not self.full():
#             self.items.append(item)
#         else:
#             print("Stack is full. Cannot push item.")

#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop()
#         else:
#             print("Stack is empty. Cannot pop item.")

#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1]
#         else:
#             print("Stack is empty. Cannot peek.")

#     def size(self):
#         return len(self.items)

#     def full(self):
#         return self.limit is not None and self.size() == self.limit

#     def search(self, target):
#         try:
#             index = self.items.index(target)
#             return len(self.items) - index
#         except ValueError:
#             return -1  # If target is not found, return -1


# class Stack:
#     def __init__(self, items=[], limit=100):
#         self.items = items[:limit]
#         self.limit = limit

#     def isEmpty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         if not self.full():
#             self.items.append(item)
#         else:
#             print("Stack is full. Cannot push item.")

#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop()
#         else:
#             print("Stack is empty. Cannot pop item.")

#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1]
#         else:
#             print("Stack is empty. Cannot peek.")

#     def size(self):
#         return len(self.items)

#     def full(self):
#         return self.limit is not None and self.size() == self.limit

#     def search(self, target):
#         try:
#             index = self.items.index(target)
#             return self.size() - index
#         except ValueError:
#             return -1  # If target is not found, return -1
