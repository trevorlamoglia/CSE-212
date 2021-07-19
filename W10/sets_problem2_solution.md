```python
def intersection(bball, vball):
    e = set()
    for b in bball and vball:
        if b in bball and vball:
            e.add(b)
    return e

def union(bball, vball):
    i = set()
    for j in bball:
        i.add(j)
    for k in vball:
        i.add(k)
    return i

def duplicates(sport):
    duplicate = set()
    for x in sport:
        duplicate.add(x)
        match = len(sport) - len(duplicate)
    return match

bball = {'B', 'C', 'G', 'H', 'J', 'M', 'R', 'T', 'Z'} # {'J', 'H', 'C', 'R', 'T', 'M'}
vball = {'A', 'C', 'H', 'I', 'J', 'M', 'R', 'T'} #{'Z', 'I', 'J', 'H', 'G', 'C', 'R', 'T', 'M', 'A', 'B'}
print(intersection(bball, vball))
print(union(bball, vball))

sport = ['A', 'B', 'C', 'C', 'G', 'H', 'H', 'I', 'J', 'J', 'M', 'M', 'R', 'R', 'T', 'T', 'Z']
print(duplicates(sport)) # 6
```

Back to [Set](2-topic.md)