print{"""
# CONTROL FLOW
# IF statement
x=2
if x<0:
    print("X is -ve no")
elif x>1:
    print("X is +ve no)
else: 
    print("No num entered")

# FOR loop (can iterate through items in a sequence list/string)
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w)) 

# Using RANGE 
nums=["one", "two", "three", "four", "five", "six"]
for num in range(0, len(nums)):
    print(nums[num]) 

# Using ENUMERATE prints both index and value used with keyword ""list""
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# break and continue Statements
breaks out of the innermost enclosing for or while loop
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')
"""}