```python
class Stack:
    
    def __init__(self):
        self.stack = list()
        self.maxNum = 8
        self.back = 0

    # Adds element to the Stack
    def push(self, data):
        if self.back >= self.maxNum:
            return ("Stack is Full!")
        self.stack.append(data)
        self.back += 1
        return True

    # Removes element from the stack
    def pop(self):
        if self.back <= 0:
            return ("Stack is Empty!")
        item = self.stack.pop()
        self.back -= 1
        return item

# Test Cases
new_stack = Stack()
print(new_stack.push(1)) # True
print(new_stack.push(2)) # True
print(new_stack.push(3)) # True
print(new_stack.push(4)) # True
print(new_stack.push(5)) # True
print(new_stack.push(6)) # True
print(new_stack.push(7)) # True
print(new_stack.push(8)) # True
print(new_stack.push(9)) # Stack is Full!

print(new_stack.pop()) # 8
print(new_stack.pop()) # 7
print(new_stack.pop()) # 6
print(new_stack.pop()) # 5
print(new_stack.pop()) # 4
print(new_stack.pop()) # 3
print(new_stack.pop()) # 2
print(new_stack.pop()) # 1
print(new_stack.pop()) # Stack is Empty!
```

Back to [Stack](1-topic.md)