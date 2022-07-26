print(
"""
# MORE ON LISTS
def array_ops(myList):
    nums = [6,7,8,8]
    myList.append(9)
    print("Append 9 at end of list", myList)
    myList.extend(nums)
    print("Extend a list", myList)
    myList.insert(0, 8)
    print("Insert at index list", myList)
    myList.remove(8)
    print("Remove 8 from list", myList)
    myList.pop(0)
    print("Pop item at index 0", myList)
    print("Count of items in a list", myList.count(6))
    myList.reverse()
    print("Reverse list", myList)
    myList.sort()
    print("Sort list", myList)
    copiedList = myList.copy()
    print("Copy list list", copiedList)
    print("Length of list", len(copiedList))
    
a = [1,2,3,4,5,6]
array_ops(a)  

You might have noticed that methods like insert, remove or sort 
that only modify the list have no return value printed – they return 
the default None. 1 This is a design principle for all mutable data 
structures in Python.

# USING LIST AS STACK
def satck_ops(stack):
    stack.append(9)
    print("Append 9 at end of list", stack)
    stack.pop()
    print("Pop item at index 0", stack) 
    
a = [1,2,3,4,5,6]
satck_ops(a)

The list methods make it very easy to use a list as a stack, 
where the last element added is the first element retrieved (“last-in, first-out”)

# USING LISTS AS QUEUES
from collections import deque

def queue_ops():
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    print("Append to queue", queue)
    queue.popleft()
    print("Pop from left first in first out", queue)
queue_ops()

# LIST COMPREHENSIONS
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
compresion = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(compresion)

Common applications are to make new lists where each element is the result of some operations

# DEL STATEMENT #retrun value of NONE
# remove an item from a list given its index instead of its value
a = [1,2,3,4,5,6,7,8]
del a[2:4]
print(a)

# TUPLES AND SEQUENCES # Tuples are immutable, 
t = 12345, 54321, 'hello!'
t[0]
print(t)
# sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the tuple.
x, y, z = t
# a tuple with one item is constructed by following a value with a comma
singleton = 'hello',

# SETS denoted by Curly braces or the set() 
# An unordered collection with no duplicate elements
basket = {'apple', 'orange', 'apple'}
# set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}

# DICTIONARIES # set of key: value pairs indexed by unique keys,
# tuples can be used as keys if they contain only strings, numbers, or tuples
# lists are mutable hence cant be used as keys
t = {'a': '1', 'gender': 'b', 'age': 2, 'personality': 'Fake', 'userName': "King"}
del(t['a'])
print(list(t))
print(sorted(t))

# Looping through dicts
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# loop over a sequence in reverse,then call the reversed() function
for i in reversed(range(1, 10, 2)): # 2 is the minus factor
    print(i)

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using set() on a sequence eliminates duplicate elements
for f in sorted(set(basket)):
    print(f)

# More on conditions
The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. 
The operators is and is not compare whether two objects are really the same object
chained coparison For example, a < b == c  # a is less than b and moreover b equals c.
"""
)
