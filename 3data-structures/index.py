print("""
# DATA STRUCTURES

# 1 MORE ON LISTS
list.append(x) - an item to the end of the list
list.extend(iterable) - extend the list by appending all the items from the iterable
list.insert(i, x) - insert an item at a given position/index
list.remove(x) - Remove the first item from the list whose value is equal to x.
list.pop([i]) - Remove the item at the given position in the list, If no index is specified, a.pop() removes and returns the last item in the list
list.clear() - remove all items from the list
list.count(x)- return the number of times x appears in the list
list.index(x) - return index in the list of the first item whose value is equal to x

# 2 USING LIST AS STACK
# last element added is the first element retrieved (“last-in, first-out”)
stack = [3, 4, 5]
stack.append(6) 
stack.pop()

# 3 USING LISTS AS QUEUES
# first element added is the first element retrieved
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Graham")          # Graham arrives
queue.popleft() 
print(queue)

""")
