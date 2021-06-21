"""
CSE212 
(c) BYU-Idaho
02-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

import timeit

def search_sorted_1(data, target):
    """
    Search for 'target' in the list 'data'
    When its found (or not found) the variable count
    which represents the work done in the function 
    is returned.
    """
    count = 0
    for item in data:
        count += 1
        if item == target:
            return count # Found it
    return count # Didn't find it

def search_sorted_2(data, target):
    """
    Search for 'target' in the list 'data'
    When its found (or not found) the variable count
    which represents the work done in the function 
    is returned.
    """
    count = 0
    start = 0
    end = len(data) - 1
    while start <= end:
        count += 1
        middle = ((end - start) // 2) + start
        if data[middle] == target:
            return count # Found it
        elif data[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return count # Didn't find it

# This code will analyze the the 2 sorting functions for different values of "n" (size of the data)
print("{:>15}{:>15}{:>15}{:>15}{:>15}".format("n","sort1-count","sort2-count","sort1-time","sort2-time"))
print("{:>15}{:>15}{:>15}{:>15}{:>15}".format("-"*10,"-"*10,"-"*10,"-"*10,"-"*10))
for n in range(0,2,1):
    test_data = [x for x in range(n)]
    count1 = search_sorted_1(test_data, n)
    count2 = search_sorted_2(test_data, n)
    time1 = timeit.timeit("search_sorted_1(test_data, n)", number=100, globals=globals()) / 100 * 1000
    time2 = timeit.timeit("search_sorted_2(test_data, n)", number=100, globals=globals()) / 100 * 1000
    print("{:>15}{:>15}{:>15}{:>15.5f}{:>15.5f}".format(n, count1, count2, time1, time2))
       

