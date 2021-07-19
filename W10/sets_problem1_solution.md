```python
# Simple Test

# Put in 'YOUR' favorite food, these are my (instructor) favorite food, unless you like the same things I like

# Create an empty set
food = set()
print(f'Empty set: {food}')

# Create a set of three of your favorite food
food = {'Sushi', 'Steak', 'Pasta'}
print(f'Your favorite food are: {food}')

# Add another food to the set
food.add('Burgers')
print(f'After adding another food: {food}')

# Add a duplicate of any of your favorite food in the set
food.add('Sushi')
print(f'After adding a duplicate food: {food}')

# Create another set of three of your favorite drinks
drink = {'Milkshake', 'Smoothie', 'Mountain Dew'}
print(f'Your favorite drinks are: {drink}')

# Create an union of sets with the two
food_and_drink = food | drink
print(f'Sustenance: {food_and_drink}')

# Remove your least favorite food in the union of sets
# then create another union of sets with the new set
food.remove('Burgers')
food_and_drink = food | drink
print(f'Sustenance: {food_and_drink}')
```

Back to [Set](2-topic.md)