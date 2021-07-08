# Data Structures outline

[Go Back](0-welcome.md)

## Sets

The python **set** data structure is a collection of items which order is not important, similar to mathematical sets. However, python sets have additional conditions:

* Elements in the set cannot be duplicates
* Elements in the set are immutable but the set as a whole can be mutable

Sets are useful for finding duplicates and summarizing data. It performs fast when adding, removing or finding elements.

## Common Linked List Operation

* add(value) - Adds 'value' to the set
* remove(value) - Removes 'value' from the set
* member(value) - Determines if 'value' is in the set
* size() - Returns number of items in the set

## Time Complexity / Performance

Similary to the previous topic, linked list operations are also in the **Constant Time** complexity. No matter the size of the input data, the running time will always be the same.

## Example Code in Python

### Creating sets

A set is created using the **set()** function or placing all elements within curly braces:
```python
Food = set(['Sushi', 'Lasagna', 'Steak', 'Burgers', 'Mashed Potatoes'])
# or
Drink = {'Chocolate', 'Milkshake', 'Tea', 'Juice', 'Water'}

print(Food)
print(Drink)
```
When the above code is executed, it produces the result:
```python
{'Sushi', 'Mashed Potatoes', 'Steak', 'Lasagna', 'Burgers'}
{'Water', 'Tea', 'Milkshake', 'Juice', 'Chocolate'}
```
The order of the elements has changed in the result.

### Accessing Sets
To access elements, we can only access all the elements together like the example above. However, we can list individual elements by looping through a set:
```python
Food = set(['Sushi', 'Lasagna', 'Steak', 'Burgers', 'Mashed Potatoes'])

for eat in Food:
    print(eat)
```
When the above code is executed, it produces the result:
```python
Steak
Lasagna
Mashed Potatoes
Sushi
Burgers
```

### Adding items to a Set
To add elements into a set, we use the **add()** method:
```python
Food = set(['Sushi', 'Lasagna', 'Steak', 'Burgers', 'Mashed Potatoes'])

Food.add('Chicken Nuggets')
print(Food)
```
When the above code is executed, it produces the result:
```python
{'Lasagna', 'Sushi', 'Mashed Potatoes', 'Burgers', 'Steak', 'Chicken Nuggets'}
```

### Removing items from a Set
To remove elements from a set, we use the **discard()** method:
```python
Food = set(['Sushi', 'Lasagna', 'Steak','Chicken Nuggets', 'Burgers', 'Mashed Potatoes'])

Food.discard('Chicken Nuggets')
print(Food)
```
When the above code is executed, it produces the result:
```python
{'Steak', 'Mashed Potatoes', 'Sushi', 'Lasagna', 'Burgers'}
```

Sets in python are typically used in mathematical operations, like union, intersection, difference, etc. This tutorial will display only the first two.

### Union of Sets
A **union** of *two sets* produces a *new set* containing elements from both the sets. A union uses **"|"** symbol to combine the two sets.
```python
Food = set(['Sushi', 'Lasagna', 'Steak', 'Burgers', 'Mashed Potatoes', 'Chocolate'])
Drink = set(['Chocolate', 'Milkshake', 'Tea', 'Juice', 'Water'])
Sustenance = Food | Drink
print(Sustenance)
```
When the above code is executed, it produces the result:
```python
{'Burgers', 'Mashed Potatoes', 'Milkshake', 'Chocolate', 'Lasagna', 'Water', 'Juice', 'Sushi', 'Tea', 'Steak'}
```

### Intersection of Sets
An **intersection** of *two sets* produces a *new set* containing **only** the common elements from both sets. An intersection uses **"&"** symbol to combine the two sets.
```python
Food = set(['Sushi', 'Lasagna', 'Steak', 'Burgers', 'Mashed Potatoes', 'Chocolate'])
Drink = set(['Chocolate', 'Milkshake', 'Tea', 'Juice', 'Water'])
Sustenance = Food & Drink
print(Sustenance)
```
When the above code is executed, it produces the result:
```python
{'Chocolate'}
```

## Problem to Solve
```python
# Simple Problem

# Put in 'YOUR' favorite food, these are my (instructor) favorite food, unless you like the same things I like

# Create an empty set
food = None
print(f'Empty set: {food}')

# Create a set of three of your favorite food
food = None
print(f'Your favorite food are: {food}')

# Add another food to the set

print(f'After adding another food: ')

# Add a duplicate of any of your favorite food in the set

print(f'After adding a duplicate food: ')

# Create another set of three of your favorite drinks
drink = None
print(f'Your favorite drinks are: {drink}')

# Create a union of sets with the two
food_and_drink = None
print(f'Sustenance: {food_and_drink}')

# Remove you least favorite food in the union of sets
# then create another union of sets with the new set


print(f'Sustenance: {}')
```

Click here for [Solution](sets_simple_solution.md)

```python
# A little more Complex Problem
'''
Without using any set operators (&, |) and Python built-in functions (intersect, union), perform an intersection between two sets.
'''
def intersection(bball, vball):
    pass


'''
Without using any set operators (&, |) and Python built-in functions (intersect, union), perform a union between two sets.
'''
def union(bball, vball):
    pass


'''
Find out how many duplicates are there in the list (both sets combined)
'''
def duplicates(bball, vball):
    pass

bball = {'B', 'C', 'G', 'H', 'J', 'M', 'R', 'T', 'Z'} # {'J', 'H', 'C', 'R', 'T', 'M'}
vball = {'A', 'C', 'H', 'I', 'J', 'M', 'R', 'T'} # {'Z', 'I', 'J', 'H', 'G', 'C', 'R', 'T', 'M', 'A', 'B'}
print(intersection(bball, vball))
print(union(bball, vball))

sport = ['A', 'B', 'C', 'C', 'G', 'H', 'H', 'I', 'J', 'J', 'M', 'M', 'R', 'R', 'T', 'T', 'Z']
print(duplicates(sport)) # 6
```
Click here for [Solution](sets_problem2_solution.md)

[Go Back](0-welcome.md)