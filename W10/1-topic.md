# Data Structures outline

[Go Back](0-welcome.md)

## Stack

**Stack** is a data structure that store items in a Last-In/First-Out manner or LIFO. An item is added in one end and is removed from that end only.

If you were going hiking with your friends or family, you probably would see cairns or stacked rocks placed along the trail to signify that you are on the right track.

Sometimes you might even make your own. Each time you add onto the stack, we call this **push** operation. However, since we are going to implement stacks in Python, the rock is actually added to the **back**.

When we take a rock off the stack, we call this **pop** operation

![Cairn image from pixabay.com](cairn.jpg)

## Common Stack Operation:

* empty() - Returns if the stack is empty or length of stack is zero
* size() - Returns the size of the stack
* push(value) - Adds 'value' at the back of stack
* pop() - Deletes the back most item of the stack

## Time Complexity / Performance

The common stack operations above are in the **Constant Time** complexity. A constant time is an O(1). An algorithm is said to have a constant time when it is not dependent on the input data (n). No matter the size of the input data, the running time will always be the same.

## Example Code in Python

In Python, to *push* an item to the stack, we use the **append** function: `stack.append(value)`

To *pop* an item of the stack, we use the **pop** function: `stack.pop()`

To determine the *size*, we use the **len** function: `length = len(stack)`

```python
sustenance = []

# append function to push element in the stack
sustenance.append('sushi')
sustenance.append('lasagna')
sustenance.append('steak')

print("Elements in sustenance: ")
print(sustenance)
print('')

# pop function to pop element from stack in LIFO order
print('Elements popped from sustenance: ')
print(sustenance.pop())
print(sustenance.pop())
print(sustenance.pop())

print('')
print(sustenance)
```

## Problem to Solve

```python
# First Problem
stack = []
 
# add the append() function to 
# push element in the stack
stack.('a')
stack.('b')
stack.('c')
 
# print initial stack 
print('Initial stack')
print(stack)

# add the pop() function to 
# pop element from stack
print('\nElements popped from stack:')
print(stack.())
print(stack.())
print(stack.())
 
print('\nStack after elements are popped:')
print(stack)
```

Click here for [Solution](stack_problem1_solution.md)

```python
# Second Problem

class Stack():

    def __init__(self):
        self.stack = list()
        self.maxNum = 8
        self.back = 0

    #############
    # Problem 1 #
    #############
    def push(self, data):
        pass

    #############
    # Problem 2 #
    #############

    def pop(self):
        pass


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

Click here for [Solution](stack_problem2_solution.md)

[Go Back](0-welcome.md)